package com.abhishek.krushinudi.data.repository

import com.abhishek.krushinudi.data.local.BorewellDao
import com.abhishek.krushinudi.data.local.BorewellEntity
import com.abhishek.krushinudi.data.remote.ApiService
import com.abhishek.krushinudi.data.remote.BorewellRequestDto
import com.abhishek.krushinudi.data.remote.BorewellResponseDto
import com.google.gson.Gson
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.withContext
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class BorewellRepository @Inject constructor(
    private val apiService: ApiService,
    private val dao: BorewellDao
) {
    val savedBorewells: Flow<List<BorewellEntity>> = dao.getAllBorewells()

    suspend fun getTaluks(district: String): Result<List<String>> = withContext(Dispatchers.IO) {
        try {
            val res = apiService.getTaluks(district)
            if (res.isSuccessful && res.body() != null) Result.success(res.body()!!)
            else Result.failure(Exception("Failed to fetch taluks"))
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getHoblis(district: String, taluk: String): Result<List<String>> = withContext(Dispatchers.IO) {
        try {
            val res = apiService.getHoblis(district, taluk)
            if (res.isSuccessful && res.body() != null) Result.success(res.body()!!)
            else Result.failure(Exception("Failed to fetch hoblis"))
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun getVillages(district: String, taluk: String, hobli: String): Result<List<String>> = withContext(Dispatchers.IO) {
        try {
            val res = apiService.getVillages(district, taluk, hobli)
            if (res.isSuccessful && res.body() != null) Result.success(res.body()!!)
            else Result.failure(Exception("Failed to fetch villages"))
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun calculateAdvisory(request: BorewellRequestDto): Result<BorewellResponseDto> = withContext(Dispatchers.IO) {
        try {
            val res = apiService.getBorewellAdvisory(request)
            if (res.isSuccessful && res.body() != null) {
                val data = res.body()!!
                
                // Cache locally into Room
                val gson = Gson()
                val entity = BorewellEntity(
                    district = data.district,
                    taluk = data.taluk,
                    hobli = data.hobli,
                    village = data.village,
                    surveyNo = data.surveyNo,
                    latitude = data.userLat,
                    longitude = data.userLon,
                    assurancePct = data.finalProb,
                    minDepthFt = data.estMinFt,
                    maxDepthFt = data.estMaxFt,
                    yieldInches = data.yieldInches,
                    cgwbStatus = data.cgwbStatusKn,
                    pointsJson = gson.toJson(data.candidatePoints)
                )
                dao.insertBorewell(entity)

                Result.success(data)
            } else {
                Result.failure(Exception("Borewell calculation failed with code: ${res.code()}"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}
