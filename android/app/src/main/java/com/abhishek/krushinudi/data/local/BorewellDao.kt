package com.abhishek.krushinudi.data.local

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow

@Dao
interface BorewellDao {
    @Query("SELECT * FROM borewell_records ORDER BY timestamp DESC")
    fun getAllBorewells(): Flow<List<BorewellEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertBorewell(entity: BorewellEntity): Long

    @Query("DELETE FROM borewell_records WHERE id = :id")
    suspend fun deleteBorewell(id: Long)
}
