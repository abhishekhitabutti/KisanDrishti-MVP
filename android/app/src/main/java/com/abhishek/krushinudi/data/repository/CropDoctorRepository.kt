package com.abhishek.krushinudi.data.repository

import com.abhishek.krushinudi.data.local.CropAnalysisDao
import com.abhishek.krushinudi.data.local.CropAnalysisEntity
import com.abhishek.krushinudi.data.remote.ApiService
import com.abhishek.krushinudi.data.remote.CropAnalysisResponseDto
import com.google.gson.Gson
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.withContext
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.MultipartBody
import okhttp3.RequestBody.Companion.asRequestBody
import okhttp3.RequestBody.Companion.toRequestBody
import java.io.File
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class CropDoctorRepository @Inject constructor(
    private val apiService: ApiService,
    private val dao: CropAnalysisDao
) {
    val pastAnalyses: Flow<List<CropAnalysisEntity>> = dao.getAllAnalyses()

    suspend fun diagnosePhoto(
        imageFile: File,
        cropHint: String,
        district: String,
        language: String = "kn"
    ): Result<CropAnalysisResponseDto> = withContext(Dispatchers.IO) {
        try {
            val reqFile = imageFile.asRequestBody("image/*".toMediaTypeOrNull())
            val imagePart = MultipartBody.Part.createFormData("image", imageFile.name, reqFile)
            val cropBody = cropHint.toRequestBody("text/plain".toMediaTypeOrNull())
            val distBody = district.toRequestBody("text/plain".toMediaTypeOrNull())
            val langBody = language.toRequestBody("text/plain".toMediaTypeOrNull())

            val response = apiService.analyzeCropPhoto(imagePart, cropBody, distBody, langBody)
            if (response.isSuccessful && response.body() != null) {
                val data = response.body()!!
                
                // Cache into Room database
                val gson = Gson()
                val entity = CropAnalysisEntity(
                    cropName = data.crop,
                    category = data.category,
                    issueNameKn = data.nameKn,
                    issueNameEn = data.nameEn,
                    confidence = data.confidence,
                    imageUri = imageFile.absolutePath,
                    symptomsJson = gson.toJson(data.symptomsSeen),
                    solutionsJson = gson.toJson(data.firstDoThis),
                    chemicalOptionsJson = gson.toJson(data.chemicalOptions)
                )
                dao.insertAnalysis(entity)

                Result.success(data)
            } else {
                Result.failure(Exception("Diagnosis server returned error: ${response.code()}"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}

