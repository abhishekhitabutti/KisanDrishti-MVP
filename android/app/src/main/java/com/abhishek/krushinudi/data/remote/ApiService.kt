package com.abhishek.krushinudi.data.remote

import okhttp3.MultipartBody
import okhttp3.RequestBody
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.Multipart
import retrofit2.http.POST
import retrofit2.http.Part
import retrofit2.http.Query

interface ApiService {

    @GET("api/v1/geography/districts")
    suspend fun getDistricts(): Response<List<DistrictDto>>

    @GET("api/v1/geography/taluks")
    suspend fun getTaluks(@Query("district") district: String): Response<List<String>>

    @GET("api/v1/geography/hoblis")
    suspend fun getHoblis(
        @Query("district") district: String,
        @Query("taluk") taluk: String
    ): Response<List<String>>

    @GET("api/v1/geography/villages")
    suspend fun getVillages(
        @Query("district") district: String,
        @Query("taluk") taluk: String,
        @Query("hobli") hobli: String
    ): Response<List<String>>

    @POST("api/v1/borewell/advisory")
    suspend fun getBorewellAdvisory(
        @Body request: BorewellRequestDto
    ): Response<BorewellResponseDto>

    @Multipart
    @POST("api/v1/crop-doctor/analyze")
    suspend fun analyzeCropPhoto(
        @Part image: MultipartBody.Part,
        @Part("crop_hint") cropHint: RequestBody,
        @Part("district") district: RequestBody,
        @Part("language") language: RequestBody
    ): Response<CropAnalysisResponseDto>

    @GET("api/v1/mandi/prices")
    suspend fun getMandiPrices(
        @Query("district") district: String,
        @Query("crop") crop: String? = null
    ): Response<List<MandiPriceDto>>
}
