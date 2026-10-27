"""
KrushiNudi 24/7 Keep-Alive & Auto-Wake Automation.
Author: Abhishek Hitabutti
Copyright: © 2026 Abhishek Hitabutti. All rights reserved.

Automated worker that visits https://krushinudi-mvp.streamlit.app on a regular schedule:
1. Detects if Streamlit Community Cloud has put the app to sleep ("Zzzz... This app has gone to sleep").
2. Automatically clicks "Yes, get this app back up!" to wake it up.
3. Resets the 12-hour inactivity timer so the app remains awake and responsive for all visitors 24/7.
"""

import os
import sys
import time

URL = os.environ.get("STREAMLIT_APP_URL", "https://krushinudi-mvp.streamlit.app")


def wake_with_playwright():
    from playwright.sync_api import sync_playwright

    print(f"[Keep-Alive] Navigating to {URL} with headless Chromium...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 720}
        )
        page = context.new_page()

        try:
            response = page.goto(URL, wait_until="networkidle", timeout=60000)
            status_code = response.status if response else "Unknown"
            print(f"[Keep-Alive] Page loaded with HTTP status: {status_code}")
        except Exception as e:
            print(f"[Keep-Alive] Navigation warning: {e}. Checking DOM...")

        page.wait_for_timeout(4000)

        # Inspect if sleep screen is displayed
        sleep_indicators = [
            'button:has-text("Yes, get this app back up")',
            'button:has-text("get this app back up")',
            'button:has-text("wake")',
            'button:has-text("Wake")'
        ]

        woken = False
        for selector in sleep_indicators:
            locator = page.locator(selector)
            if locator.count() > 0:
                print(f"[Keep-Alive] 😴 Sleep screen detected! Found button: '{selector}'. Clicking now...")
                locator.first.click()
                woken = True
                print("[Keep-Alive] Waiting for app container to boot...")
                page.wait_for_timeout(10000)
                print("[Keep-Alive] 🚀 'Yes, get this app back up!' clicked successfully!")
                break

        if not woken:
            print("[Keep-Alive] ✅ App is already awake and actively serving sessions. Inactivity timer reset!")

        browser.close()


def main():
    try:
        wake_with_playwright()
    except ImportError:
        print("[Keep-Alive] Playwright not found, executing HTTP ping fallback...")
        import urllib.request
        req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"[Keep-Alive] HTTP fallback ping successful: {resp.status}")


if __name__ == "__main__":
    main()

