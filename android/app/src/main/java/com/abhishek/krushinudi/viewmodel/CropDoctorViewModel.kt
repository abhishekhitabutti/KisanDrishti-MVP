package com.abhishek.krushinudi.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.abhishek.krushinudi.data.remote.CropAnalysisResponseDto
import com.abhishek.krushinudi.data.repository.CropDoctorRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import java.io.File
import javax.inject.Inject

sealed class CropDoctorUiState {
    object Idle : CropDoctorUiState()
    object Analyzing : CropDoctorUiState()
    data class Success(val report: CropAnalysisResponseDto) : CropDoctorUiState()
    data class Error(val message: String) : CropDoctorUiState()
}

@HiltViewModel
class CropDoctorViewModel @Inject constructor(
    private val repository: CropDoctorRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow<CropDoctorUiState>(CropDoctorUiState.Idle)
    val uiState: StateFlow<CropDoctorUiState> = _uiState.asStateFlow()

    private val _selectedImage = MutableStateFlow<File?>(null)
    val selectedImage: StateFlow<File?> = _selectedImage.asStateFlow()

    fun setImage(file: File) {
        _selectedImage.value = file
    }

    fun diagnose(cropHint: String, district: String, language: String = "kn") {
        val file = _selectedImage.value
        if (file == null) {
            _uiState.value = CropDoctorUiState.Error("ದಯವಿಟ್ಟು ಮೊದಲು ಬೆಳೆಯ ಫೋಟೋ ಆಯ್ಕೆಮಾಡಿ {Please select photo}")
            return
        }

        viewModelScope.launch {
            _uiState.value = CropDoctorUiState.Analyzing
            val result = repository.diagnosePhoto(file, cropHint, district, language)
            result.onSuccess { report ->
                _uiState.value = CropDoctorUiState.Success(report)
            }.onFailure { err ->
                _uiState.value = CropDoctorUiState.Error(err.localizedMessage ?: "ವಿಶ್ಲೇಷಣೆ ವಿಫಲವಾಗಿದೆ {Analysis failed}")
            }
        }
    }

    fun reset() {
        _uiState.value = CropDoctorUiState.Idle
        _selectedImage.value = null
    }
}
