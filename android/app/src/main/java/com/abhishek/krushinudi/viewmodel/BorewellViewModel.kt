package com.abhishek.krushinudi.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.abhishek.krushinudi.data.remote.BorewellRequestDto
import com.abhishek.krushinudi.data.remote.BorewellResponseDto
import com.abhishek.krushinudi.data.repository.BorewellRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import javax.inject.Inject

sealed class BorewellUiState {
    object Idle : BorewellUiState()
    object Calculating : BorewellUiState()
    data class Success(val response: BorewellResponseDto) : BorewellUiState()
    data class Error(val message: String) : BorewellUiState()
}

@HiltViewModel
class BorewellViewModel @Inject constructor(
    private val repository: BorewellRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow<BorewellUiState>(BorewellUiState.Idle)
    val uiState: StateFlow<BorewellUiState> = _uiState.asStateFlow()

    private val _taluks = MutableStateFlow<List<String>>(emptyList())
    val taluks: StateFlow<List<String>> = _taluks.asStateFlow()

    private val _hoblis = MutableStateFlow<List<String>>(emptyList())
    val hoblis: StateFlow<List<String>> = _hoblis.asStateFlow()

    private val _villages = MutableStateFlow<List<String>>(emptyList())
    val villages: StateFlow<List<String>> = _villages.asStateFlow()

    fun loadTaluks(district: String) {
        viewModelScope.launch {
            repository.getTaluks(district).onSuccess { _taluks.value = it }
        }
    }

    fun loadHoblis(district: String, taluk: String) {
        viewModelScope.launch {
            repository.getHoblis(district, taluk).onSuccess { _hoblis.value = it }
        }
    }

    fun loadVillages(district: String, taluk: String, hobli: String) {
        viewModelScope.launch {
            repository.getVillages(district, taluk, hobli).onSuccess { _villages.value = it }
        }
    }

    fun calculate(
        district: String,
        taluk: String,
        hobli: String,
        village: String,
        surveyNo: String,
        customLat: Double?,
        customLon: Double?,
        acres: Double,
        topography: String,
        soilType: String,
        workingWells: Int,
        dryWells: Int,
        hasWaterBody: Boolean
    ) {
        viewModelScope.launch {
            _uiState.value = BorewellUiState.Calculating
            val req = BorewellRequestDto(
                district = district,
                taluk = taluk,
                hobli = hobli,
                village = village,
                surveyNo = surveyNo,
                customLat = customLat,
                customLon = customLon,
                landAcres = acres,
                topography = topography,
                soilType = soilType,
                nearbyWorkingWells = workingWells,
                nearbyDryWells = dryWells,
                hasWaterBody = hasWaterBody
            )
            repository.calculateAdvisory(req).onSuccess {
                _uiState.value = BorewellUiState.Success(it)
            }.onFailure { err ->
                _uiState.value = BorewellUiState.Error(err.localizedMessage ?: "ಲೆಕ್ಕಾಚಾರ ವಿಫಲವಾಗಿದೆ {Calculation failed}")
            }
        }
    }
}

