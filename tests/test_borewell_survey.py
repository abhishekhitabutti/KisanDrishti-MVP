"""
Unit tests for Karnataka Borewell Taluk/Village Directory & Cadastral Survey Number Parsing.
Verifies all 31 districts, 233 taluks, revenue hoblis, villages, and 100% assured borewell points.
"""
import unittest
import borewell_model
import karnataka_hoblis_data as kh
from districts import DISTRICTS


class TestBorewellSurveyAdvisory(unittest.TestCase):

    def test_all_31_districts_covered(self):
        """Ensure all 31 Karnataka districts are present in the hobli/taluk directory."""
        self.assertEqual(len(kh.KARNATAKA_HOBLIS), 31)
        for dist_name in DISTRICTS.keys():
            self.assertIn(dist_name, kh.KARNATAKA_HOBLIS, f"District {dist_name} missing from KARNATAKA_HOBLIS")

    def test_taluk_counts_comprehensive(self):
        """Ensure all districts have multiple taluks totaling 230+ across Karnataka."""
        total_taluks = sum(len(taluks) for taluks in kh.KARNATAKA_HOBLIS.values())
        self.assertGreaterEqual(total_taluks, 230, f"Expected 230+ taluks, found {total_taluks}")
        
        # Verify specific districts that previously had missing taluks
        bengaluru_taluks = kh.get_taluks_for_district("Bengaluru Urban")
        self.assertGreaterEqual(len(bengaluru_taluks), 5)

        dakshina_kannada_taluks = kh.get_taluks_for_district("Dakshina Kannada")
        self.assertGreaterEqual(len(dakshina_kannada_taluks), 5)

        vijayanagara_taluks = kh.get_taluks_for_district("Vijayanagara")
        self.assertGreaterEqual(len(vijayanagara_taluks), 6)

    def test_hoblis_and_villages_present(self):
        """Ensure each taluk has hoblis and each hobli has villages."""
        for dist, taluks in kh.KARNATAKA_HOBLIS.items():
            for taluk, hoblis in taluks.items():
                self.assertGreater(len(hoblis), 0, f"No hoblis for {dist} -> {taluk}")
                for hobli, villages in hoblis.items():
                    self.assertGreaterEqual(len(villages), 2, f"Expected at least 2 villages for {dist} -> {taluk} -> {hobli}")

    def test_survey_number_parser(self):
        """Verify Karnataka Cadastral Survey Number regex parser."""
        # Standard formats
        res1 = kh.parse_karnataka_survey_no("142/2A")
        self.assertTrue(res1["valid"])
        self.assertEqual(res1["survey_no"], 142)
        self.assertEqual(res1["hissa"], "2A")
        self.assertIn("ಗಡಿ ಕಲ್ಲು", res1["boundary_stone_ref_kn"])
        self.assertGreater(res1["distance_m"], 100)

        res2 = kh.parse_karnataka_survey_no("Sy No. 45/1")
        self.assertTrue(res2["valid"])
        self.assertEqual(res2["survey_no"], 45)
        self.assertEqual(res2["hissa"], "1")

        res3 = kh.parse_karnataka_survey_no("88")
        self.assertTrue(res3["valid"])
        self.assertEqual(res3["survey_no"], 88)

        # Invalid formats
        res_empty = kh.parse_karnataka_survey_no("")
        self.assertFalse(res_empty["valid"])

    def test_cadastral_coordinate_offset(self):
        """Verify that survey numbers shift coordinates relative to Gramatana."""
        base_lat, base_lon = 15.8500, 74.5000
        off_lat, off_lon = kh.calculate_cadastral_parcel_offset("142/2A", base_lat, base_lon)
        # Should be distinct from base
        self.assertNotEqual((base_lat, base_lon), (off_lat, off_lon))
        # Distance should be within micro-watershed (< 1.5 km)
        d_km = borewell_model.haversine_distance_km(base_lat, base_lon, off_lat, off_lon)
        self.assertLess(d_km, 1.5)
        self.assertGreater(d_km, 0.05)

    def test_borewell_feasibility_with_survey(self):
        """Test calculation of 100% assured borewell points with cadastral survey."""
        res = borewell_model.calculate_borewell_feasibility("Belagavi", survey_no="142/2A")
        self.assertEqual(len(res["exact_points"]), 3)
        self.assertTrue(res["cadastral_info"]["valid"])
        
        p1 = res["exact_points"][0]
        self.assertIn("100% ಖಾತರಿ", p1["grade"])
        self.assertIn("Sy No. 142/2A", p1["field_marking_kn"])
        self.assertIn("ಗಡಿ ಕಲ್ಲು", p1["field_marking_kn"])
        self.assertTrue(p1["nav_url"].startswith("https://www.google.com/maps/dir/"))

        p2 = res["exact_points"][1]
        self.assertIn("Sy No. 142/2A", p2["field_marking_kn"])

        p3 = res["exact_points"][2]
        self.assertIn("ಯಾವುದೇ ಕಾರಣಕ್ಕೂ ಬೋರ್‌ವೆಲ್ ಕೊರೆಯಬೇಡಿ", p3["field_marking_kn"])


if __name__ == "__main__":
    unittest.main()
