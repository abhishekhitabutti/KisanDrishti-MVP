package com.abhishek.krushinudi.data.remote

import com.google.gson.annotations.SerializedName

data class DistrictDto(
    @SerializedName("id") val id: String,
    @SerializedName("name_en") val nameEn: String,
    @SerializedName("name_kn") val nameKn: String
)

data class BorewellRequestDto(
    @SerializedName("district") val district: String,
    @SerializedName("taluk") val taluk: String,
    @SerializedName("hobli") val hobli: String,
    @SerializedName("village") val village: String,
    @SerializedName("survey_no") val surveyNo: String,
    @SerializedName("custom_lat") val customLat: Double?,
    @SerializedName("custom_lon") val customLon: Double?,
    @SerializedName("land_acres") val landAcres: Double,
    @SerializedName("topography") val topography: String,
    @SerializedName("soil_type") val soilType: String,
    @SerializedName("nearby_working_wells") val nearbyWorkingWells: Int,
    @SerializedName("nearby_dry_wells") val nearbyDryWells: Int,
    @SerializedName("has_water_body") val hasWaterBody: Boolean
)

data class BorewellPointDto(
    @SerializedName("point_id") val pointId: Int,
    @SerializedName("name_kn") val nameKn: String,
    @SerializedName("name_en") val nameEn: String,
    @SerializedName("grade") val grade: String,
    @SerializedName("assurance_pct") val assurancePct: Int,
    @SerializedName("lat") val lat: Double,
    @SerializedName("lon") val lon: Double,
    @SerializedName("distance_m") val distanceM: Int,
    @SerializedName("direction_kn") val directionKn: String,
    @SerializedName("direction_en") val directionEn: String,
    @SerializedName("yield_inches") val yieldInches: String,
    @SerializedName("yield_lpm") val yieldLpm: String,
    @SerializedName("main_strike_ft") val mainStrikeFt: String,
    @SerializedName("first_water_ft") val firstWaterFt: String,
    @SerializedName("field_marking_kn") val fieldMarkingKn: String,
    @SerializedName("field_marking_en") val fieldMarkingEn: String,
    @SerializedName("nav_url") val navUrl: String
)

data class BorewellResponseDto(
    @SerializedName("district") val district: String,
    @SerializedName("taluk") val taluk: String,
    @SerializedName("hobli") val hobli: String,
    @SerializedName("village") val village: String,
    @SerializedName("survey_no") val surveyNo: String,
    @SerializedName("user_lat") val userLat: Double,
    @SerializedName("user_lon") val userLon: Double,
    @SerializedName("est_min_ft") val estMinFt: Int,
    @SerializedName("est_max_ft") val estMaxFt: Int,
    @SerializedName("yield_inches") val yieldInches: String,
    @SerializedName("final_prob") val finalProb: Int,
    @SerializedName("prob_category_kn") val probCategoryKn: String,
    @SerializedName("cgwb_status_kn") val cgwbStatusKn: String,
    @SerializedName("candidate_points") val candidatePoints: List<BorewellPointDto>
)

data class CropAnalysisResponseDto(
    @SerializedName("crop") val crop: String,
    @SerializedName("category") val category: String,
    @SerializedName("name_kn") val nameKn: String,
    @SerializedName("name_en") val nameEn: String,
    @SerializedName("confidence") val confidence: String,
    @SerializedName("symptoms_seen") val symptomsSeen: List<String>,
    @SerializedName("could_also_be") val couldAlsoBe: List<String>,
    @SerializedName("first_do_this") val firstDoThis: List<String>,
    @SerializedName("chemical_options") val chemicalOptions: List<Map<String, Any>>,
    @SerializedName("spray_timing") val sprayTiming: List<String>,
    @SerializedName("safety") val safety: List<String>
)

data class MandiPriceDto(
    @SerializedName("crop_kn") val cropKn: String,
    @SerializedName("variety") val variety: String,
    @SerializedName("market") val market: String,
    @SerializedName("min_price") val minPrice: Double,
    @SerializedName("modal_price") val modalPrice: Double,
    @SerializedName("max_price") val maxPrice: Double,
    @SerializedName("trend") val trend: String
)
