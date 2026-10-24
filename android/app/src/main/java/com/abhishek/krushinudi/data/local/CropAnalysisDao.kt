package com.abhishek.krushinudi.data.local

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow

@Dao
interface CropAnalysisDao {
    @Query("SELECT * FROM crop_analyses ORDER BY timestamp DESC")
    fun getAllAnalyses(): Flow<List<CropAnalysisEntity>>

    @Query("SELECT * FROM crop_analyses WHERE id = :id LIMIT 1")
    suspend fun getAnalysisById(id: Long): CropAnalysisEntity?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAnalysis(entity: CropAnalysisEntity): Long

    @Query("DELETE FROM crop_analyses WHERE id = :id")
    suspend fun deleteAnalysis(id: Long)
}
