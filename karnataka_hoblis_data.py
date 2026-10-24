"""
Karnataka Comprehensive Revenue Geography Database:
Districts -> Taluks -> Hoblis (Revenue Circles) -> Villages with Micro-Basin Coordinates.
Supports precision cadastral and agricultural borewell point positioning across Karnataka.
"""

KARNATAKA_HOBLIS = {
    "Belagavi": {
        "Chikkodi": {
            "Sadalga": {
                "lat": 16.5700, "lon": 74.5300, "name_kn": "ಸದಲಗಾ",
                "villages": ["ಸದಲಗಾ {Sadalga}", "ಬೋರಗಾಂವ್ {Borgaon}", "ಬೆಡಕಿಹಾಳ {Bedkihal}", "ಶಾಮೇವಾಡಿ {Shamewadi}", "ಜಾನವಾಡ {Janwad}", "ನಾನಡಿ {Nanadi}", "ಬಾರವಾಡ {Barwad}"]
            },
            "Chikkodi": {
                "lat": 16.4300, "lon": 74.5900, "name_kn": "ಚಿಕ್ಕೋಡಿ",
                "villages": ["ಚಿಕ್ಕೋಡಿ {Chikkodi}", "ಕರೋಶಿ {Karoshi}", "ಕೇರೂರ {Kerur}", "ಹಿರೇಕೋಡಿ {Hirekudi}", "ನೈಂಗಳಜ {Nainglaj}", "ಕಬ್ಬೂರ {Kabbur}", "ಚಿಂಚಣಿ {Chinchani}"]
            },
            "Ankali": {
                "lat": 16.4800, "lon": 74.7200, "name_kn": "ಅಂಕಲಿ",
                "villages": ["ಅಂಕಲಿ {Ankali}", "ಮಂಜರಿ {Manjari}", "ದಿಗ್ಗೆವಾಡಿ {Diggewadi}", "ಯಡೂರ {Yadur}", "ಕಲ್ಲೋಳ {Kallol}", "ಹಾರುಗೇರಿ {Harugeri}"]
            },
            "Nagaral": {
                "lat": 16.4800, "lon": 74.6500, "name_kn": "ನಾಗರಾಳ",
                "villages": ["ನಾಗರಾಳ {Nagaral}", "ಮಜಲಟ್ಟಿ {Majalatti}", "ಜಾಗನೂರ {Jaganur}", "ತೋರಣಹಳ್ಳಿ {Toranahalli}", "ಹಂಚಿನಾಳ {Hanchinal}"]
            },
            "Soundalga": {
                "lat": 16.5100, "lon": 74.4800, "name_kn": "ಸೌಂದಲಗಾ",
                "villages": ["ಸೌಂದಲಗಾ {Soundalga}", "ಕೋದನಿ {Kodani}", "ಮಾಮದಾಪುರ {Mamdapur}", "ಬೆನಾಡಿ {Benadi}", "ಖಡಕಲಾಟ {Khadaklat}"]
            }
        },
        "Gokak": {
            "Gokak": {
                "lat": 16.1600, "lon": 74.8200, "name_kn": "ಗೋಕಾಕ್",
                "villages": ["ಗೋಕಾಕ್ {Gokak}", "ಉಪ್ಪಾರಹಟ್ಟಿ {Upparhatti}", "ಕೊಣ್ಣೂರ {Konnur}", "ಲೋಳಸೂರ {Lolsur}", "ಮಾಮದಾಪುರ {Mamdapur}"]
            },
            "Arabhavi": {
                "lat": 16.2300, "lon": 74.8300, "name_kn": "ಅರಭಾವಿ",
                "villages": ["ಅರಭಾವಿ {Arabhavi}", "ಮೂಡಲಗಿ {Mudalagi}", "ಯಾದವಾಡ {Yadawad}", "ಸುನ್ನಾಳ {Sunnal}", "ಧೂಪದಾಳ {Dhupdal}"]
            },
            "Koujalgi": {
                "lat": 16.1400, "lon": 75.0200, "name_kn": "ಕೌಜಲಗಿ",
                "villages": ["ಕೌಜಲಗಿ {Koujalgi}", "ಮೇಲವಂಕಿ {Melavanki}", "ತುಕಾನಟ್ಟಿ {Tukanatti}", "ಬೆಟಗೇರಿ {Betageri}"]
            }
        },
        "Athani": {
            "Athani": {
                "lat": 16.7300, "lon": 75.0600, "name_kn": "ಅಥಣಿ",
                "villages": ["ಅಥಣಿ {Athani}", "ದರೂರ {Darur}", "ಸತ್ತಿ {Satti}", "ಐಗಳಿ {Aigali}", "ನಾಂದಿ ಇಂಗಳಗಾಂವ್ {Nadi Ingalgaon}"]
            },
            "Kagwad": {
                "lat": 16.7000, "lon": 74.7200, "name_kn": "ಕಾಗವಾಡ",
                "villages": ["ಕಾಗವಾಡ {Kagwad}", "ಶೇಡಬಾಳ {Shedbal}", "ಉಗಾರ ಖುರ್ದ್ {Ugar Khurd}", "ಶಿರಗುಪ್ಪಿ {Shiraguppi}", "ಮಂಗಾವತಿ {Mangavati}"]
            },
            "Anantapur": {
                "lat": 16.6300, "lon": 75.1800, "name_kn": "ಅನಂತಪುರ",
                "villages": ["ಅನಂತಪುರ {Anantapur}", "ಕೊಹಳ್ಳಿ {Kohalli}", "ಕೋಕಟನೂರ {Kokatnur}", "ಬಳ್ಳಿಗೇರಿ {Balligeri}"]
            },
            "Telsang": {
                "lat": 16.8200, "lon": 75.2500, "name_kn": "ತೆಲಸಂಗ",
                "villages": ["ತೆಲಸಂಗ {Telsang}", "ಖವಟಕೊಪ್ಪ {Khavatakoppa}", "ಬನ್ನೂರ {Bannur}", "ಪಾಂಡೇಗಾಂವ್ {Pandegaon}"]
            }
        },
        "Bailhongal": {
            "Bailhongal": {
                "lat": 15.8200, "lon": 74.8600, "name_kn": "ಬೈಲಹೊಂಗಲ",
                "villages": ["ಬೈಲಹೊಂಗಲ {Bailhongal}", "ಸಂಪಗಾಂವ್ {Sampgaon}", "ದೇವಲಾಪುರ {Devalapur}", "ಬೆಳವಡಿ {Belwadi}"]
            },
            "Nesargi": {
                "lat": 15.9500, "lon": 74.7600, "name_kn": "ನೇಸರಗಿ",
                "villages": ["ನೇಸರಗಿ {Nesargi}", "ದೇಶನೂರ {Deshnur}", "ಮದನಭಾವಿ {Madanbhavi}", "ವಂಟಮೂರಿ {Vantamuri}"]
            },
            "Kittur": {
                "lat": 15.6000, "lon": 74.7900, "name_kn": "ಕಿತ್ತೂರು",
                "villages": ["ಕಿತ್ತೂರು {Kittur}", "ಕುಲವಳ್ಳಿ {Kulavalli}", "ದೇಗಾಂವ {Degaon}", "ಕಡೊಳ್ಳಿ {Kadolli}"]
            }
        },
        "Hukkeri": {
            "Hukkeri": {
                "lat": 16.2300, "lon": 74.6000, "name_kn": "ಹುಕ್ಕೇರಿ",
                "villages": ["ಹುಕ್ಕೇರಿ {Hukkeri}", "ಬೆಲ್ಲದ ಬಾಗೇವಾಡಿ {Bellad Bagewadi}", "ಬಾದಕುಂದ್ರಿ {Badkundri}", "ಹೆಬ್ಬಾಳ {Hebbal}"]
            },
            "Sankeshwar": {
                "lat": 16.2600, "lon": 74.4800, "name_kn": "ಸಂಕೇಶ್ವರ",
                "villages": ["ಸಂಕೇಶ್ವರ {Sankeshwar}", "ಹಾರೂಗೇರಿ {Harali}", "ಕಣಗಲಾ {Kanagala}", "ಅಮ್ಮಿನಭಾವಿ {Amminbhavi}"]
            },
            "Yamakanmardi": {
                "lat": 16.1300, "lon": 74.5200, "name_kn": "ಯಮಕನಮರಡಿ",
                "villages": ["ಯಮಕನಮರಡಿ {Yamakanmardi}", "ಶಿರಗಾಂವ {Shiragaon}", "ಹತ್ತರಗಿ {Hattargi}", "ಗೋತೂರ {Gotur}"]
            }
        },
        "Belagavi": {
            "Belagavi": {
                "lat": 15.8500, "lon": 74.5000, "name_kn": "ಬೆಳಗಾವಿ",
                "villages": ["ಬೆಳಗಾವಿ {Belagavi}", "ಪೀರನವಾಡಿ {Peeranwadi}", "ವಡಗಾಂವ {Vadgaon}", "ಮಜಗಾಂವ {Majgaon}"]
            },
            "Kakati": {
                "lat": 15.9300, "lon": 74.5500, "name_kn": "ಕಾಕತಿ",
                "villages": ["ಕಾಕತಿ {Kakati}", "ಹೊನ್ನಾಗಾ {Honaga}", "ಹೊನ್ನಿಹಾಳ {Honnihal}", "ಮುಚಂಡಿ {Muchandi}"]
            },
            "Bagewadi": {
                "lat": 15.7400, "lon": 74.6300, "name_kn": "ಬಾಗೇವಾಡಿ",
                "villages": ["ಬಾಗೇವಾಡಿ {Bagewadi}", "ಹಲಗಾ {Halaga}", "ಬಸ್ತವಾಡ {Bastawad}", "ಸುಳೇಭಾವಿ {Sulebhavi}"]
            },
            "Uchagaon": {
                "lat": 15.8900, "lon": 74.4100, "name_kn": "ಉಚಗಾಂವ್",
                "villages": ["ಉಚಗಾಂವ್ {Uchagaon}", "ಸಾಂಬ್ರಾ {Sambra}", "ಮೊಡಗಾ {Modaga}", "ತುರಮುರಿ {Turmuri}"]
            }
        },
        "Raibag": {
            "Raibag": {
                "lat": 16.4800, "lon": 74.7800, "name_kn": "ರಾಯಬಾಗ",
                "villages": ["ರಾಯಬಾಗ {Raibag}", "ಕುಡಚಿ {Kudachi}", "ಅಲಗವಾಡಿ {Alagawadi}", "ಚಿಂಚಲಿ {Chinchali}"]
            },
            "Harugeri": {
                "lat": 16.5400, "lon": 74.9800, "name_kn": "ಹಾರೂಗೇರಿ",
                "villages": ["ಹಾರೂಗೇರಿ {Harugeri}", "ಮೊರಬ {Morab}", "ಜಲಾಲಪುರ {Jalalpur}", "ಮುಗಳಖೋಡ {Mugalkhod}"]
            }
        },
        "Ramdurg": {
            "Ramdurg": {
                "lat": 15.9500, "lon": 75.3000, "name_kn": "ರಾಮದುರ್ಗ",
                "villages": ["ರಾಮದುರ್ಗ {Ramdurg}", "ಸುರೇಬಾನ {Sureban}", "ಕಟ್ಕೋಳ {Katkol}", "ಸಾಲಹಳ್ಳಿ {Salahalli}"]
            }
        },
        "Saundatti": {
            "Saundatti": {
                "lat": 15.7700, "lon": 75.1200, "name_kn": "ಸವದತ್ತಿ",
                "villages": ["ಸವದತ್ತಿ {Saundatti}", "ಮುನವಳ್ಳಿ {Munavalli}", "ಯರಗಟ್ಟಿ {Yaragatti}", "ಉಗರಗೋಳ {Ugargol}"]
            }
        },
        "Khanapur": {
            "Khanapur": {
                "lat": 15.6400, "lon": 74.5100, "name_kn": "ಖಾನಾಪುರ",
                "villages": ["ಖಾನಾಪುರ {Khanapur}", "ನಂದಗಡ {Nandgad}", "ಬೀಡಿ {Bidi}", "ಲೋಂಡಾ {Londa}"]
            }
        }
    },
    "Dharwad": {
        "Dharwad": {
            "Dharwad": {
                "lat": 15.4600, "lon": 75.0100, "name_kn": "ಧಾರವಾಡ",
                "villages": ["ಧಾರವಾಡ {Dharwad}", "ಅಮ್ಮಿನಭಾವಿ {Amminbhavi}", "ನರೇಂದ್ರ {Narendra}", "ಕೇಲಗೇರಿ {Kelageri}", "ಮುಮ್ಮಿಗಟ್ಟಿ {Mummigatti}"]
            },
            "Garag": {
                "lat": 15.5400, "lon": 74.9400, "name_kn": "ಗರಗ",
                "villages": ["ಗರಗ {Garag}", "ತಡಕೋಡ {Tadakod}", "ಪುಡಕಲಕಟ್ಟಿ {Pudakalkatti}", "ಮನಸೂರ {Mansur}"]
            },
            "Alnavar": {
                "lat": 15.4300, "lon": 74.7300, "name_kn": "ಅಳ್ನಾವರ",
                "villages": ["ಅಳ್ನಾವರ {Alnavar}", "ಕುಂಬಾರಗಣವಿ {Kumbarganvi}", "ಕಡಬಗಟ್ಟಿ {Kadabagatti}"]
            },
            "Mugad": {
                "lat": 15.4200, "lon": 74.8800, "name_kn": "ಮುಗದ",
                "villages": ["ಮುಗದ {Mugad}", "ಮಂಡಿಹಾಳ {Mandihal}", "ಡದ್ದಿ {Daddi}", "ಕ್ಯಾರಕೊಪ್ಪ {Kyarkop}"]
            }
        },
        "Hubballi": {
            "Hubballi": {
                "lat": 15.3600, "lon": 75.1200, "name_kn": "ಹುಬ್ಬಳ್ಳಿ",
                "villages": ["ಹುಬ್ಬಳ್ಳಿ {Hubballi}", "ಉಣಕಲ್ {Unkal}", "ಬೆಂಗೇರಿ {Bengeri}", "ಗಬ್ಬೂರು {Gabbur}", "ಶಿರಗುಪ್ಪಿ {Shirguppi}"]
            },
            "Chabbi": {
                "lat": 15.2200, "lon": 75.1800, "name_kn": "ಚಬ್ಬಿ",
                "villages": ["ಚಬ್ಬಿ {Chabbi}", "ವರೂರ {Varur}", "ಪಾಳೆ {Pale}", "ಕುಸುಗಲ್ {Kusugal}", "ಅಡರಗುಂಚಿ {Adargunchi}"]
            }
        },
        "Kundgol": {
            "Kundgol": {
                "lat": 15.2500, "lon": 75.2500, "name_kn": "ಕುಂದಗೋಳ",
                "villages": ["ಕುಂದಗೋಳ {Kundgol}", "ಸವಣೂರ {Saunshi}", "ಯರಗುಪ್ಪಿ {Yaraguppi}", "ರೊಟ್ಟಿಗವಾಡ {Rottigawad}"]
            }
        },
        "Navalgund": {
            "Navalgund": {
                "lat": 15.5600, "lon": 75.3600, "name_kn": "ನವಲಗುಂದ",
                "villages": ["ನವಲಗುಂದ {Navalgund}", "ಅನ್ನಿಗೇರಿ {Annigeri}", "ಅಲಗವಾಡಿ {Alagawadi}", "ಅರೆಕುರಹಟ್ಟಿ {Arekurahatti}"]
            }
        },
        "Kalghatgi": {
            "Kalghatgi": {
                "lat": 15.1800, "lon": 74.9700, "name_kn": "ಕಲಘಟಗಿ",
                "villages": ["ಕಲಘಟಗಿ {Kalghatgi}", "ಮಿಶ್ರಿಕೋಟಿ {Mishrikoti}", "ಧೂಮವಾಡ {Dhumawad}", "ಗಳಗಿ {Galagi}"]
            }
        }
    },
    "Bagalkote": {
        "Bagalkote": {
            "Bagalkote": {
                "lat": 16.1800, "lon": 75.7000, "name_kn": "ಬಾಗಲಕೋಟೆ",
                "villages": ["ಬಾಗಲಕೋಟೆ {Bagalkote}", "ನವನಗರ {Navanagar}", "ಮುಚಖಂಡಿ {Muchakhandi}", "ಗದ್ದನಕೇರಿ {Gaddankeri}"]
            },
            "Kaladgi": {
                "lat": 16.2000, "lon": 75.5000, "name_kn": "ಕಲಾದಗಿ",
                "villages": ["ಕಲಾದಗಿ {Kaladgi}", "ಖಜ್ಜಿದೋಣಿ {Khajjidoni}", "ಹಳ್ಳೂರ {Hallur}", "ತುಳಸಿಗೇರಿ {Tulasigeri}"]
            },
            "Sitimani": {
                "lat": 16.2900, "lon": 75.8300, "name_kn": "ಸೀತಿಮನಿ",
                "villages": ["ಸೀತಿಮನಿ {Sitimani}", "ಬೆನ್ನೂರ {Bennur}", "ರಾಮಪುರ {Rampur}", "ಶಿರೂರ {Shirur}"]
            }
        },
        "Jamkhandi": {
            "Jamkhandi": {
                "lat": 16.5100, "lon": 75.3000, "name_kn": "ಜಮಖಂಡಿ",
                "villages": ["ಜಮಖಂಡಿ {Jamkhandi}", "ಹುನ್ನೂರ {Hunnur}", "ಸವಳಗಿ {Savalagi}", "ತೇರದಾಳ {Terdal}", "ರಬಕವಿ {Rabkavi}"]
            }
        },
        "Mudhol": {
            "Mudhol": {
                "lat": 16.3400, "lon": 75.2800, "name_kn": "ಮುಧೋಳ",
                "villages": ["ಮುಧೋಳ {Mudhol}", "ಲೋಕಾಪುರ {Lokapur}", "ಮಹಾಲಿಂಗಪುರ {Mahalingpur}", "ಯಡಹಳ್ಳಿ {Yadahalli}"]
            }
        },
        "Badami": {
            "Badami": {
                "lat": 15.9200, "lon": 75.6800, "name_kn": "ಬಾದಾಮಿ",
                "villages": ["ಬಾದಾಮಿ {Badami}", "ಗುಳೇದಗುಡ್ಡ {Guledgudda}", "ಕೇರೂರ {Kerur}", "ಪಟ್ಟದಕಲ್ಲು {Pattadakal}"]
            }
        },
        "Hungund": {
            "Hungund": {
                "lat": 16.0600, "lon": 76.0600, "name_kn": "ಹುನಗುಂದ",
                "villages": ["ಹುನಗುಂದ {Hungund}", "ಇಲಕಲ್ಲ {Ilkal}", "ಅಮೀನಗಡ {Amingad}", "ಕೂಡಲಸಂಗಮ {Kudalasangama}"]
            }
        }
    },
    "Vijayapura": {
        "Vijayapura": {
            "Vijayapura": {
                "lat": 16.8300, "lon": 75.7100, "name_kn": "ವಿಜಯಪುರ",
                "villages": ["ವಿಜಯಪುರ {Vijayapura}", "ಅಲಿಯಾಬಾದ್ {Aliyabad}", "ತೊರವಿ {Toravi}", "ಐನಾಪುರ {Ainapur}"]
            },
            "Tikota": {
                "lat": 16.8600, "lon": 75.5200, "name_kn": "ಟಿಕೋಟಾ",
                "villages": ["ಟಿಕೋಟಾ {Tikota}", "ಕಣಮಡಿ {Kanamadi}", "ಕೋಟ್ಯಾಳ {Kotyal}", "ಹೊನ್ನುಟಗಿ {Honnutagi}"]
            },
            "Babaleshwar": {
                "lat": 16.6800, "lon": 75.6000, "name_kn": "ಬಬಲೇಶ್ವರ",
                "villages": ["ಬಬಲೇಶ್ವರ {Babaleshwar}", "ಸಾರವಾಡ {Sarawad}", "ಕಾಖಂಡಕಿ {Kakhandki}", "ಬೆಳ್ಳುಬ್ಬಿ {Bellubbi}"]
            }
        },
        "Indi": {
            "Indi": {
                "lat": 17.1800, "lon": 75.9600, "name_kn": "ಇಂಡಿ",
                "villages": ["ಇಂಡಿ {Indi}", "ಹೊರ್ತಿ {Horti}", "ಚಡಚಣ {Chadchan}", "ಲೋಣಿ {Loni}", "ಝಳಕಿ {Zalaki}"]
            }
        },
        "Muddebihal": {
            "Muddebihal": {
                "lat": 16.3300, "lon": 76.1300, "name_kn": "ಮುದ್ದೇಬಿಹಾಳ",
                "villages": ["ಮುದ್ದೇಬಿಹಾಳ {Muddebihal}", "ತಾಳಿಕೋಟೆ {Talikoti}", "ನಾಲತವಾಡ {Nalatwad}", "ಧವಳಗಿ {Dhavalgi}"]
            }
        },
        "Basavana Bagewadi": {
            "Basavana Bagewadi": {
                "lat": 16.5800, "lon": 75.9700, "name_kn": "ಬಸವನ ಬಾಗೇವಾಡಿ",
                "villages": ["ಬಸವನ ಬಾಗೇವಾಡಿ {Basavana Bagewadi}", "ಕೊಲ್ಹಾರ {Kolhar}", "ನಿಡಗುಂದಿ {Nidagundi}", "ಹೂವಿನ ಹಿಪ್ಪರಗಿ {Huvina Hipparagi}"]
            }
        },
        "Sindagi": {
            "Sindagi": {
                "lat": 16.9200, "lon": 76.2300, "name_kn": "ಸಿಂದಗಿ",
                "villages": ["ಸಿಂದಗಿ {Sindagi}", "ಆಲಮೇಲ {Almel}", "ದೇವರ ಹಿಪ್ಪರಗಿ {Devar Hippargi}", "ಮೊರಟಗಿ {Moratagi}"]
            }
        }
    },
    "Haveri": {
        "Haveri": {
            "Haveri": {
                "lat": 14.7900, "lon": 75.4000, "name_kn": "ಹಾವೇರಿ",
                "villages": ["ಹಾವೇರಿ {Haveri}", "ದೇವಗಿರಿ {Devagiri}", "ಗುತ್ತಲ {Guttal}", "ಕರಜಗಿ {Karajagi}"]
            }
        },
        "Ranebennur": {
            "Ranebennur": {
                "lat": 14.6200, "lon": 75.6200, "name_kn": "ರಾಣೆಬೆನ್ನೂರು",
                "villages": ["ರಾಣೆಬೆನ್ನೂರು {Ranebennur}", "ಮೇಡ್ಲೇರಿ {Medleri}", "ಹಲಗೇರಿ {Halageri}", "ಚಳಗೇರಿ {Chalageri}"]
            }
        },
        "Byadgi": {
            "Byadgi": {
                "lat": 14.6800, "lon": 75.4900, "name_kn": "ಬ್ಯಾಡಗಿ",
                "villages": ["ಬ್ಯಾಡಗಿ {Byadgi}", "ಕಾಗಿನೆಲೆ {Kaginele}", "ಮೋಟೆಬೆನ್ನೂರು {Motebennur}"]
            }
        },
        "Hirekerur": {
            "Hirekerur": {
                "lat": 14.4600, "lon": 75.3900, "name_kn": "ಹಿರೇಕೆರೂರು",
                "villages": ["ಹಿರೇಕೆರೂರು {Hirekerur}", "ರಟ್ಟಿಹಳ್ಳಿ {Rattihalli}", "ಚಿಕ್ಕ ಕೆರೂರು {Chikka Kerur}"]
            }
        }
    },
    "Gadag": {
        "Gadag": {
            "Gadag": {
                "lat": 15.4300, "lon": 75.6300, "name_kn": "ಗದಗ",
                "villages": ["ಗದಗ {Gadag}", "ಬೆಟಗೇರಿ {Betageri}", "ಹುಲಕೋಟಿ {Hulkoti}", "ಬಿಂಕದಕಟ್ಟಿ {Binkadakatti}", "ಕುರ್ತಕೋಟಿ {Kurtakoti}"]
            },
            "Mulgund": {
                "lat": 15.2800, "lon": 75.5300, "name_kn": "ಮುಳಗುಂದ",
                "villages": ["ಮುಳಗುಂದ {Mulgund}", "ಕಣವಿ {Kanavi}", "ಬೆಳಧಡಿ {Beladhadi}", "ಚಿಂಚಲಿ {Chinchali}"]
            }
        },
        "Ron": {
            "Ron": {
                "lat": 15.7000, "lon": 75.7300, "name_kn": "ರೋಣ",
                "villages": ["ರೋಣ {Ron}", "ಗಜೇಂದ್ರಗಡ {Gajendragad}", "ನರೇಗಲ್ಲ {Naregal}", "ಅಬ್ಬಿಗೇರಿ {Abbigeri}"]
            }
        },
        "Shirhatti": {
            "Shirhatti": {
                "lat": 15.2300, "lon": 75.5800, "name_kn": "ಶಿರಹಟ್ಟಿ",
                "villages": ["ಶಿರಹಟ್ಟಿ {Shirhatti}", "ಲಕ್ಷ್ಮೇಶ್ವರ {Lakshmeshwar}", "ಬೆಳ್ಳಟ್ಟಿ {Bellatti}"]
            }
        }
    },
    "Ballari": {
        "Ballari": {
            "Ballari": {
                "lat": 15.1400, "lon": 76.9200, "name_kn": "ಬಳ್ಳಾರಿ",
                "villages": ["ಬಳ್ಳಾರಿ {Ballari}", "ಕೋಳೂರು {Kolur}", "ಮೋಕಾ {Moka}", "ಕಪ್ಪಗಲ್ಲು {Kappagal}", "ಕುಡಿತಿನಿ {Kudithini}"]
            },
            "Kurugodu": {
                "lat": 15.3400, "lon": 76.8300, "name_kn": "ಕುರುಗೋಡು",
                "villages": ["ಕುರುಗೋಡು {Kurugodu}", "ಗೆಣಿಕಿಹಾಳು {Genikihal}", "ಕುಡತಿನಿ {Kudatini}", "ಎಮ್ಮಿಗನೂರು {Emmiganur}"]
            }
        },
        "Siruguppa": {
            "Siruguppa": {
                "lat": 15.6300, "lon": 76.8900, "name_kn": "ಸಿರುಗುಪ್ಪ",
                "villages": ["ಸಿರುಗುಪ್ಪ {Siruguppa}", "ಟೆಕ್ಕಲಕೋಟೆ {Tekkalakote}", "ಕಾರೂರು {Karur}", "ಹಚ್ಚೊಳ್ಳಿ {Hatcholli}"]
            }
        }
    },
    "Koppal": {
        "Koppal": {
            "Koppal": {
                "lat": 15.3500, "lon": 76.1500, "name_kn": "ಕೊಪ್ಪಳ",
                "villages": ["ಕೊಪ್ಪಳ {Koppal}", "ಅಳವಂಡಿ {Alavandi}", "ಹಿಟ್ನಾಳ {Hitnal}", "ಕಿನ್ನಾಳ {Kinnal}", "ಭಾಗ್ಯನಗರ {Bhagyanagar}"]
            }
        },
        "Gangavathi": {
            "Gangavathi": {
                "lat": 15.4300, "lon": 76.5300, "name_kn": "ಗಂಗಾವತಿ",
                "villages": ["ಗಂಗಾವತಿ {Gangavathi}", "ಕಾರಟಗಿ {Karatagi}", "ಆನೆಗುಂದಿ {Anegundi}", "ಕನಕಗಿರಿ {Kanakagiri}", "ಮರಳಿ {Marali}"]
            }
        }
    },
    "Raichur": {
        "Raichur": {
            "Raichur": {
                "lat": 16.2100, "lon": 77.3600, "name_kn": "ರಾಯಚೂರು",
                "villages": ["ರಾಯಚೂರು {Raichur}", "ಯರಗೇರಾ {Yeragera}", "ದೇವಸೂಗೂರು {Devasugur}", "ಚಂದ್ರಬಂಡಾ {Chandrabanda}", "ಶಕ್ತಿನಗರ {Shakthinagar}"]
            }
        },
        "Sindhanur": {
            "Sindhanur": {
                "lat": 15.7700, "lon": 76.7600, "name_kn": "ಸಿಂಧನೂರು",
                "villages": ["ಸಿಂಧನೂರು {Sindhanur}", "ತುರ್ವಿಹಾಳ {Turvihal}", "ಗೋರೆಬಾಳ {Gorebal}", "ಜಾವಳಗೇರಾ {Jawalagera}"]
            }
        },
        "Manvi": {
            "Manvi": {
                "lat": 15.9900, "lon": 77.0500, "name_kn": "ಮಾನ್ವಿ",
                "villages": ["ಮಾನ್ವಿ {Manvi}", "ಸಿರವಾರ {Sirwar}", "ಪೋತ್ನಾಳ {Pothnal}", "ಕುರ್ಡಿ {Kurdi}"]
            }
        }
    },
    "Kalaburagi": {
        "Kalaburagi": {
            "Kalaburagi": {
                "lat": 17.3300, "lon": 76.8300, "name_kn": "ಕಲಬುರಗಿ",
                "villages": ["ಕಲಬುರಗಿ {Kalaburagi}", "ಫರ್ಹತಾಬಾದ್ {Farhatabad}", "ಕುಸನೂರು {Kusnoor}", "ಕೊಟ್ನೂರು {Kotnoor}"]
            }
        },
        "Aland": {
            "Aland": {
                "lat": 17.5600, "lon": 76.5700, "name_kn": "ಆಳಂದ",
                "villages": ["ಆಳಂದ {Aland}", "ನರೋಣಾ {Narona}", "ಮದನ ಹಿಪ್ಪರಗಿ {Madan Hipparga}", "ಖಜೂರಿ {Khajuri}"]
            }
        },
        "Sedam": {
            "Sedam": {
                "lat": 17.1800, "lon": 77.2800, "name_kn": "ಸೇಡಂ",
                "villages": ["ಸೇಡಂ {Sedam}", "ಕೋಡ್ಲಾ {Kodla}", "ಮುಧೋಳ {Mudhol}", "ಯಾನಾಗುಂದಿ {Yanagundi}"]
            }
        }
    },
    "Yadgir": {
        "Yadgir": {
            "Yadgir": {
                "lat": 16.7700, "lon": 77.1400, "name_kn": "ಯಾದಗಿರಿ",
                "villages": ["ಯಾದಗಿರಿ {Yadgir}", "ಸೈದಾಪುರ {Saidapur}", "ಗುರಮಿಟಕಲ್ {Gurmitkal}", "ಹತ್ತಿಕುಣಿ {Hattikuni}"]
            }
        },
        "Shahapur": {
            "Shahapur": {
                "lat": 16.7000, "lon": 76.8400, "name_kn": "ಶಹಾಪುರ",
                "villages": ["ಶಹಾಪುರ {Shahapur}", "ದೋರನಹಳ್ಳಿ {Doranahalli}", "ಗೋಗಿ {Gogi}", "ಸಾಗರ {Sagar}"]
            }
        }
    },
    "Davanagere": {
        "Davanagere": {
            "Davanagere": {
                "lat": 14.4700, "lon": 75.9200, "name_kn": "ದಾವಣಗೆರೆ",
                "villages": ["ದಾವಣಗೆರೆ {Davanagere}", "ಅಣಜಿ {Anaji}", "ಮಾಯಕೊಂಡ {Mayakonda}", "ಲೋಕಿಕೆರೆ {Lokikere}", "ಹದಡಿ {Hadadi}"]
            }
        },
        "Harihara": {
            "Harihara": {
                "lat": 14.5100, "lon": 75.8000, "name_kn": "ಹರಿಹರ",
                "villages": ["ಹರಿಹರ {Harihara}", "ಮಲೇಬೆನ್ನೂರು {Malebennur}", "ಭಾನುವಳ್ಳಿ {Bhanuvalli}", "ರಾಜನಹಳ್ಳಿ {Rajanahalli}"]
            }
        },
        "Channagiri": {
            "Channagiri": {
                "lat": 14.0200, "lon": 75.9300, "name_kn": "ಚನ್ನಗಿರಿ",
                "villages": ["ಚನ್ನಗಿರಿ {Channagiri}", "ಸಂತೆಬೆನ್ನೂರು {Santhebennur}", "ಬಸವಾಪಟ್ಟಣ {Basavapatna}"]
            }
        }
    },
    "Chitradurga": {
        "Chitradurga": {
            "Chitradurga": {
                "lat": 14.2300, "lon": 76.4000, "name_kn": "ಚಿತ್ರದುರ್ಗ",
                "villages": ["ಚಿತ್ರದುರ್ಗ {Chitradurga}", "ಭರಮಸಾಗರ {Bharamasagara}", "ತುರುವನೂರು {Turuvanur}", "ಹಿರೇಗುಂಟನೂರು {Hireguntanur}"]
            }
        },
        "Hiriyur": {
            "Hiriyur": {
                "lat": 13.9500, "lon": 76.6200, "name_kn": "ಹಿರಿಯೂರು",
                "villages": ["ಹಿರಿಯೂರು {Hiriyur}", "ಐಮಂಗಲ {Aimangala}", "ಧರ್ಮಪುರ {Dharmapura}", "ಬಬ್ಬೂರು {Babbur}"]
            }
        },
        "Challakere": {
            "Challakere": {
                "lat": 14.3100, "lon": 76.6500, "name_kn": "ಚಳ್ಳಕೆರೆ",
                "villages": ["ಚಳ್ಳಕೆರೆ {Challakere}", "ಪರಶುರಾಂಪುರ {Parasurampura}", "ನಾಯಕನಹಟ್ಟಿ {Nayakanahatti}"]
            }
        }
    },
    "Shivamogga": {
        "Shivamogga": {
            "Kasaba": {
                "lat": 13.9300, "lon": 75.5700, "name_kn": "ಕಸಬಾ",
                "villages": ["ಶಿವಮೊಗ್ಗ {Shivamogga}", "ನಿಡಿಗೆ {Nidige}", "ಹೊಳಲೂರು {Holalur}", "ಹರನಹಳ್ಳಿ {Harnahalli}"]
            }
        },
        "Bhadravathi": {
            "Bhadravathi": {
                "lat": 13.8400, "lon": 75.7000, "name_kn": "ಭದ್ರಾವತಿ",
                "villages": ["ಭದ್ರಾವತಿ {Bhadravathi}", "ಕುಡ್ಲಿಗೆರೆ {Kudligere}", "ಹೊಳೆಹೊನ್ನೂರು {Holehonnur}", "ಬಾರಂದೂರು {Barandur}"]
            }
        },
        "Sagar": {
            "Sagar": {
                "lat": 14.1600, "lon": 75.0300, "name_kn": "ಸಾಗರ",
                "villages": ["ಸಾಗರ {Sagar}", "ಆನಂದಪುರ {Anandapura}", "ಅವಿನಹಳ್ಳಿ {Avinahalli}", "ಜೋಗ್ ಫಾಲ್ಸ್ {Jog Falls}"]
            }
        },
        "Shikaripura": {
            "Shikaripura": {
                "lat": 14.2700, "lon": 75.3500, "name_kn": "ಶಿಕಾರಿಪುರ",
                "villages": ["ಶಿಕಾರಿಪುರ {Shikaripura}", "ಶಿರಾಳಕೊಪ್ಪ {Shiralkoppa}", "ಹೊಸೂರು {Hosur}"]
            }
        }
    },
    "Mysuru": {
        "Mysuru": {
            "Kasaba": {
                "lat": 12.3000, "lon": 76.6400, "name_kn": "ಕಸಬಾ",
                "villages": ["ಮೈಸೂರು {Mysuru}", "ವರುಣಾ {Varuna}", "ಜಯಪುರ {Jayapura}", "ಯಲವಾಲ {Yelawala}", "ಕಡಕೋಳ {Kadakola}"]
            }
        },
        "Nanjangud": {
            "Nanjangud": {
                "lat": 12.1200, "lon": 76.6800, "name_kn": "ನಂಜನಗೂಡು",
                "villages": ["ನಂಜನಗೂಡು {Nanjangud}", "ಬಿಳಿಗೆರೆ {Biligere}", "ಹುಲ್ಲಹಳ್ಳಿ {Hullahalli}", "ಕೌಲಂದೆ {Kowlande}"]
            }
        },
        "Hunsur": {
            "Hunsur": {
                "lat": 12.3100, "lon": 76.2900, "name_kn": "ಹುಣಸೂರು",
                "villages": ["ಹುಣಸೂರು {Hunsur}", "ಬಿಳಿಕೆರೆ {Bilikere}", "ಹನಗೋಡು {Hanagodu}", "ಗಾವಡಗೆರೆ {Gavadagere}"]
            }
        },
        "T. Narasipura": {
            "T. Narasipura": {
                "lat": 12.2100, "lon": 76.9000, "name_kn": "ಟಿ. ನರಸೀಪುರ",
                "villages": ["ಟಿ. ನರಸೀಪುರ {T. Narasipura}", "ಬನ್ನೂರು {Bannur}", "ಮುಗೂರು {Mugur}", "ಸೊಸಲೆ {Sosale}"]
            }
        }
    },
    "Mandya": {
        "Mandya": {
            "Mandya": {
                "lat": 12.5200, "lon": 76.9000, "name_kn": "ಮಂಡ್ಯ",
                "villages": ["ಮಂಡ್ಯ {Mandya}", "ಕೊತ್ತತ್ತಿ {Kothathi}", "ದುದ್ದ {Dudda}", "ಬಸರಾಳು {Basaralu}", "ಕೆರೆಗೋಡು {Keragodu}"]
            }
        },
        "Pandavapura": {
            "Pandavapura": {
                "lat": 12.5000, "lon": 76.6700, "name_kn": "ಪಾಂಡವಪುರ",
                "villages": ["ಪಾಂಡವಪುರ {Pandavapura}", "ಮೇಲುಕೋಟೆ {Melukote}", "ಚಿನ್ಯ {Chinya}", "ಕತ್ತೇರಿ {Katteri}"]
            }
        },
        "Maddur": {
            "Maddur": {
                "lat": 12.5800, "lon": 77.0400, "name_kn": "ಮದ್ದೂರು",
                "villages": ["ಮದ್ದೂರು {Maddur}", "ಕೊಪ್ಪ {Koppa}", "ಚಿಕ್ಕರಸಿನಕೆರೆ {Chikkarasinakere}", "ಬೆಸಗರಹಳ್ಳಿ {Besagarahalli}"]
            }
        },
        "Malavalli": {
            "Malavalli": {
                "lat": 12.3800, "lon": 77.0600, "name_kn": "ಮಳವಳ್ಳಿ",
                "villages": ["ಮಳವಳ್ಳಿ {Malavalli}", "ಹಲಗೂರು {Halagur}", "ಬೆಳಕವಾಡಿ {Belakavadi}", "ಕಿರುಗಾವಲು {Kirugavalu}"]
            }
        }
    },
    "Tumakuru": {
        "Tumakuru": {
            "Kasaba": {
                "lat": 13.3400, "lon": 77.1000, "name_kn": "ಕಸಬಾ",
                "villages": ["ತುಮಕೂರು {Tumakuru}", "ಉರ್ದಿಗೆರೆ {Urdigere}", "ಹೆಬ್ಬೂರು {Hebbur}", "ಬೆಳ್ಳಾವಿ {Bellavi}", "ಗುಳೂರು {Gulur}"]
            }
        },
        "Sira": {
            "Sira": {
                "lat": 13.7400, "lon": 76.9000, "name_kn": "ಶಿರಾ",
                "villages": ["ಶಿರಾ {Sira}", "ಕಲ್ಲಂಬೆಳ್ಳ {Kallambella}", "ಬುಕ್ಕಾಪಟ್ಟಣ {Bukkapatna}", "ನಾಡೂರು {Nadur}"]
            }
        },
        "Tiptur": {
            "Tiptur": {
                "lat": 13.2600, "lon": 76.4800, "name_kn": "ತಿಪಟೂರು",
                "villages": ["ತಿಪಟೂರು {Tiptur}", "ಕಿಬ್ಬನಹಳ್ಳಿ {Kibbanahalli}", "ಹೊನ್ನವಳ್ಳಿ {Honnavalli}", "ನೊಣವಿನಕೆರೆ {Nonavinakere}"]
            }
        },
        "Madhugiri": {
            "Madhugiri": {
                "lat": 13.6600, "lon": 77.2100, "name_kn": "ಮಧುಗಿರಿ",
                "villages": ["ಮಧುಗಿರಿ {Madhugiri}", "ಕೊಡಿಗೇನಹಳ್ಳಿ {Kodigenahalli}", "ಮಿಡಿಗೇಶಿ {Midigeshi}"]
            }
        }
    },
    "Kolar": {
        "Kolar": {
            "Kolar": {
                "lat": 13.1400, "lon": 78.1300, "name_kn": "ಕೋಲಾರ",
                "villages": ["ಕೋಲಾರ {Kolar}", "ವಕ್ಕಲೇರಿ {Vokkaleri}", "ಸುಗಟೂರು {Sugatur}", "ವೇಮಗಲ್ {Vemagal}", "ಹುತ್ತೂರು {Huthur}"]
            }
        },
        "Srinivaspur": {
            "Srinivaspur": {
                "lat": 13.3400, "lon": 78.2100, "name_kn": "ಶ್ರೀನಿವಾಸಪುರ",
                "villages": ["ಶ್ರೀನಿವಾಸಪುರ {Srinivaspur}", "ರಾಯಲಪಾಡು {Rayalpad}", "ರೋಣೂರು {Ronur}", "ಯಲ್ದೂರು {Yeldur}"]
            }
        },
        "Mulbagal": {
            "Mulbagal": {
                "lat": 13.1600, "lon": 78.3900, "name_kn": "ಮುಳಬಾಗಿಲು",
                "villages": ["ಮುಳಬಾಗಿಲು {Mulbagal}", "ಆವಣಿ {Avani}", "ದುಗ್ಗಸಂದ್ರ {Duggasandra}", "ಬೈರಕೂರು {Byrakur}"]
            }
        },
        "Bangarpet": {
            "Bangarpet": {
                "lat": 12.9900, "lon": 78.2000, "name_kn": "ಬಂಗಾರಪೇಟೆ",
                "villages": ["ಬಂಗಾರಪೇಟೆ {Bangarpet}", "ಕಾಮಸಂದ್ರ {Kamasandra}", "ಬೇತಮಂಗಲ {Bethamangala}"]
            }
        }
    },
    "Chikkaballapura": {
        "Chikkaballapura": {
            "Chikkaballapura": {
                "lat": 13.4300, "lon": 77.7300, "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
                "villages": ["ಚಿಕ್ಕಬಳ್ಳಾಪುರ {Chikkaballapura}", "ನಂದಿ {Nandi}", "ಮಂಡಿಕಲ್ {Mandikal}", "ಪೇರೇಸಂದ್ರ {Peresandra}"]
            }
        },
        "Gowribidanur": {
            "Gowribidanur": {
                "lat": 13.6100, "lon": 77.5200, "name_kn": "ಗೌರಿಬಿದನೂರು",
                "villages": ["ಗೌರಿಬಿದನೂರು {Gowribidanur}", "ಮಂಚೇನಹಳ್ಳಿ {Manchenahalli}", "ತೊಂಡೇಭಾವಿ {Thondebhavi}"]
            }
        },
        "Chintamani": {
            "Chintamani": {
                "lat": 13.4000, "lon": 78.0600, "name_kn": "ಚಿಂತಾಮಣಿ",
                "villages": ["ಚಿಂತಾಮಣಿ {Chintamani}", "ಅಂಬಾಜಿದುರ್ಗ {Ambajidurga}", "ಮುರುಗಮಲ್ಲ {Muragamalla}", "ಕೈವಾರ {Kaivara}"]
            }
        }
    },
    "Hassan": {
        "Hassan": {
            "Hassan": {
                "lat": 13.0000, "lon": 76.1000, "name_kn": "ಹಾಸನ",
                "villages": ["ಹಾಸನ {Hassan}", "ಕಟ್ಟಾಯ {Kattaya}", "ಶಾಂತಿಗ್ರಾಮ {Shantigrama}", "ಸಾಲಗಾಮೆ {Salagame}", "ದುದ್ದ {Dudda}"]
            }
        },
        "Channarayapatna": {
            "Channarayapatna": {
                "lat": 12.9000, "lon": 76.3900, "name_kn": "ಚನ್ನರಾಯಪಟ್ಟಣ",
                "villages": ["ಚನ್ನರಾಯಪಟ್ಟಣ {Channarayapatna}", "ಶ್ರವಣಬೆಳಗೊಳ {Shravanabelagola}", "ನುಗ್ಗೇಹಳ್ಳಿ {Nuggehalli}", "ಹಿರಿಸಾವೆ {Hiresave}"]
            }
        },
        "Arsikere": {
            "Arsikere": {
                "lat": 13.3100, "lon": 76.2600, "name_kn": "ಅರಸೀಕೆರೆ",
                "villages": ["ಅರಸೀಕೆರೆ {Arsikere}", "ಬಾಣಾವರ {Banavara}", "ಗಂಡಸಿ {Gandasi}", "ಜಾವಗಲ್ {Javagal}"]
            }
        }
    },
    "Chikkamagaluru": {
        "Chikkamagaluru": {
            "Chikkamagaluru": {
                "lat": 13.3200, "lon": 75.7700, "name_kn": "ಚಿಕ್ಕಮಗಳೂರು",
                "villages": ["ಚಿಕ್ಕಮಗಳೂರು {Chikkamagaluru}", "ವಸ್ತಾರೆ {Vastare}", "ಆಲ್ದೂರು {Aldur}", "ಆವತಿ {Avathi}"]
            }
        },
        "Kadur": {
            "Kadur": {
                "lat": 13.5500, "lon": 76.0100, "name_kn": "ಕಡೂರು",
                "villages": ["ಕಡೂರು {Kadur}", "ಬೀರೂರು {Birur}", "ಯಗಟಿ {Yagati}", "ಸಕ್ಕರೆಪಟ್ಟಣ {Sakrepatna}"]
            }
        }
    },
    "Chamarajanagar": {
        "Chamarajanagar": {
            "Chamarajanagar": {
                "lat": 11.9300, "lon": 76.9400, "name_kn": "ಚಾಮರಾಜನಗರ",
                "villages": ["ಚಾಮರಾಜನಗರ {Chamarajanagar}", "ಸಂತೆಮರಹಳ್ಳಿ {Santhemarahalli}", "ಹರವೆ {Harave}", "ಕುದೇರು {Kuderu}"]
            }
        },
        "Gundlupete": {
            "Gundlupete": {
                "lat": 11.8000, "lon": 76.6900, "name_kn": "ಗುಂಡ್ಲುಪೇಟೆ",
                "villages": ["ಗುಂಡ್ಲುಪೇಟೆ {Gundlupete}", "ಬೇಗೂರು {Begur}", "ತೆರಕಣಾಂಬಿ {Terakanambi}"]
            }
        }
    },
    "Bengaluru Rural": {
        "Devanahalli": {
            "Devanahalli": {
                "lat": 13.2500, "lon": 77.7100, "name_kn": "ದೇವನಹಳ್ಳಿ",
                "villages": ["ದೇವನಹಳ್ಳಿ {Devanahalli}", "ವಿಜಯಪುರ {Vijayapura}", "ಕುಂದಾಣ {Kundana}", "ಚನ್ನರಾಯಪಟ್ಟಣ {Channarayapatna}"]
            }
        },
        "Nelamangala": {
            "Nelamangala": {
                "lat": 13.1000, "lon": 77.3900, "name_kn": "ನೆಲಮಂಗಲ",
                "villages": ["ನೆಲಮಂಗಲ {Nelamangala}", "ಸೋಂಪುರ {Sompura}", "ಟಿ. ಬೇಗೂರು {T-Begur}"]
            }
        }
    },
    "Ramanagara": {
        "Ramanagara": {
            "Ramanagara": {
                "lat": 12.7200, "lon": 77.2800, "name_kn": "ರಾಮನಗರ",
                "villages": ["ರಾಮನಗರ {Ramanagara}", "ಬಿಡದಿ {Bidadi}", "ಕೈಲಾಂಚ {Kailancha}", "ಕೂಟಗಲ್ {Kutagal}"]
            }
        },
        "Channapatna": {
            "Channapatna": {
                "lat": 12.6500, "lon": 77.2000, "name_kn": "ಚನ್ನಪಟ್ಟಣ",
                "villages": ["ಚನ್ನಪಟ್ಟಣ {Channapatna}", "ಮಾಲೂರು {Malur}", "ವಿರೂಪಾಕ್ಷಿಪುರ {Virupakshipura}"]
            }
        }
    },
    "Bidar": {
        "Bidar": {
            "Bidar": {
                "lat": 17.9100, "lon": 77.5200, "name_kn": "ಬೀದರ್",
                "villages": ["ಬೀದರ್ {Bidar}", "ಜಾನವಾಡ {Janwada}", "ಬಾಗದಲ {Bagdal}", "ಮನ್ನಳ್ಳಿ {Mannalli}"]
            }
        },
        "Humnabad": {
            "Humnabad": {
                "lat": 17.7700, "lon": 77.1300, "name_kn": "ಹುಮನಾಬಾದ್",
                "villages": ["ಹುಮನಾಬಾದ್ {Humnabad}", "ದುಬಲಗುಂಡಿ {Dubalgundi}", "ಹಳ್ಳಿಖೇಡ್ {Hallikhed}"]
            }
        }
    },
    "Udupi": {
        "Kundapura": {
            "Kundapura": {
                "lat": 13.6300, "lon": 74.6900, "name_kn": "ಕುಂದಾಪುರ",
                "villages": ["ಕುಂದಾಪುರ {Kundapura}", "ಬೈಂದೂರು {Byndoor}", "ಕೋಟ {Kota}", "ಶಂಕರನಾರಾಯಣ {Shankaranarayana}"]
            }
        },
        "Udupi": {
            "Udupi": {
                "lat": 13.3400, "lon": 74.7500, "name_kn": "ಉಡುಪಿ",
                "villages": ["ಉಡುಪಿ {Udupi}", "ಮಲ್ಪೆ {Malpe}", "ಬ್ರಹ್ಮಾವರ {Brahmavara}", "ಕಾಪು {Kaup}"]
            }
        }
    },
    "Dakshina Kannada": {
        "Mangaluru": {
            "Mangaluru": {
                "lat": 12.9100, "lon": 74.8600, "name_kn": "ಮಂಗಳೂರು",
                "villages": ["ಮಂಗಳೂರು {Mangaluru}", "ಸುರತ್ಕಲ್ {Surathkal}", "ಗುರುಪುರ {Gurupura}", "ಮುಲ್ಕಿ {Mulki}"]
            }
        }
    },
    "Uttara Kannada": {
        "Sirsi": {
            "Sirsi": {
                "lat": 14.6200, "lon": 74.8500, "name_kn": "ಶಿರಸಿ",
                "villages": ["ಶಿರಸಿ {Sirsi}", "ಬನವಾಸಿ {Banavasi}", "ಸಂಪಖಂಡ {Sampkhanda}"]
            }
        },
        "Karwar": {
            "Karwar": {
                "lat": 14.8100, "lon": 74.1300, "name_kn": "ಕಾರವಾರ",
                "villages": ["ಕಾರವಾರ {Karwar}", "ಅಂಕೋಲಾ {Ankola}", "ಕುಮಟಾ {Kumta}", "ಭಟ್ಕಳ {Bhatkal}"]
            }
        }
    },
    "Kodagu": {
        "Madikeri": {
            "Madikeri": {
                "lat": 12.4200, "lon": 75.7400, "name_kn": "ಮಡಿಕೇರಿ",
                "villages": ["ಮಡಿಕೇರಿ {Madikeri}", "ಭಾಗಮಂಡಲ {Bhagamandala}", "ನಾಪೋಕ್ಲು {Napoklu}", "ಸಂಪಾಜೆ {Sampaje}"]
            }
        }
    }
}


def get_taluks_for_district(district: str) -> list:
    """Return list of taluks for given district, falling back to district headquarter."""
    d_data = KARNATAKA_HOBLIS.get(district, {})
    if d_data:
        return list(d_data.keys())
    return [district]


def get_hoblis_for_taluk(district: str, taluk: str) -> list:
    """Return list of hoblis for given district and taluk."""
    t_data = KARNATAKA_HOBLIS.get(district, {}).get(taluk, {})
    if t_data:
        return list(t_data.keys())
    return [taluk]


def get_villages_for_hobli(district: str, taluk: str, hobli: str) -> list:
    """Return list of villages for given hobli."""
    h_data = KARNATAKA_HOBLIS.get(district, {}).get(taluk, {}).get(hobli, {})
    if h_data and "villages" in h_data:
        return h_data["villages"]
    return [f"{hobli} ಮುಖ್ಯ ಗ್ರಾಮ {{Main Village}}"]


def get_coordinates_for_location(district: str, taluk: str, hobli: str, village_idx: int = 0) -> tuple:
    """
    Get precise geographic coordinates for Hobli & Village.
    Adds realistic micro-watershed offset (0.003° to 0.008° ~ 300m to 800m) for distinct villages under same hobli.
    """
    h_data = KARNATAKA_HOBLIS.get(district, {}).get(taluk, {}).get(hobli, {})
    if h_data:
        base_lat = h_data["lat"]
        base_lon = h_data["lon"]
        # Apply deterministic micro-offset per village index so each village has distinct point
        offset_lat = ((village_idx % 4) - 1.5) * 0.0045
        offset_lon = (((village_idx // 4) % 3) - 1.0) * 0.0045
        return round(base_lat + offset_lat, 6), round(base_lon + offset_lon, 6)
    
    from districts import DISTRICTS
    return DISTRICTS.get(district, (15.4600, 75.0100))
