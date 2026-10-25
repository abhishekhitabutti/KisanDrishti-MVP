package com.abhishek.krushinudi.data.local

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "borewell_records")
data class BorewellEntity(
    @PrimaryKey(autoGenerate = true)
    val id: Long = 0,
    val district: String,
    val taluk: String,
    val hobli: String,
    val village: String,
    val surveyNo: String,
    val latitude: Double,
    val longitude: Double,
    val assurancePct: Int,
    val minDepthFt: Int,
    val maxDepthFt: Int,
    val yieldInches: String,
    val cgwbStatus: String,
    val pointsJson: String,        // JSON serialized candidate points
    val timestamp: Long = System.currentTimeMillis()
)

