package com.abhishek.krushinudi.data.local

import androidx.room.Database
import androidx.room.RoomDatabase

@Database(
    entities = [CropAnalysisEntity::class, BorewellEntity::class],
    version = 1,
    exportSchema = false
)
abstract class AppDatabase : RoomDatabase() {
    abstract fun cropAnalysisDao(): CropAnalysisDao
    abstract fun borewellDao(): BorewellDao
}
