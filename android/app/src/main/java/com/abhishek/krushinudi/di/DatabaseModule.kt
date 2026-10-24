package com.abhishek.krushinudi.di

import android.content.Context
import androidx.room.Room
import com.abhishek.krushinudi.data.local.AppDatabase
import com.abhishek.krushinudi.data.local.BorewellDao
import com.abhishek.krushinudi.data.local.CropAnalysisDao
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.android.qualifiers.ApplicationContext
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {

    @Provides
    @Singleton
    fun provideDatabase(@ApplicationContext context: Context): AppDatabase {
        return Room.databaseBuilder(
            context,
            AppDatabase::class.java,
            "krushinudi_offline.db"
        ).fallbackToDestructiveMigration().build()
    }

    @Provides
    fun provideCropAnalysisDao(db: AppDatabase): CropAnalysisDao = db.cropAnalysisDao()

    @Provides
    fun provideBorewellDao(db: AppDatabase): BorewellDao = db.borewellDao()
}
