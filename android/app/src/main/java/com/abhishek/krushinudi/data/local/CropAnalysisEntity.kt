package com.abhishek.krushinudi.data.local

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "crop_analyses")
data class CropAnalysisEntity(
    @PrimaryKey(autoGenerate = true)
    val id: Long = 0,
    val cropName: String,
    val category: String,
    val issueNameKn: String,
    val issueNameEn: String,
    val confidence: String,
    val imageUri: String,
    val symptomsJson: String,      // JSON stringified list
    val solutionsJson: String,     // JSON stringified non-chemical steps
    val chemicalOptionsJson: String,
    val timestamp: Long = System.currentTimeMillis()
)
