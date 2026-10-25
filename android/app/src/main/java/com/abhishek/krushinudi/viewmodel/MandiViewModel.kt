package com.abhishek.krushinudi.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.abhishek.krushinudi.data.remote.MandiPriceDto
import com.abhishek.krushinudi.data.repository.MandiRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import javax.inject.Inject

sealed class MandiUiState {
    object Loading : MandiUiState()
    data class Success(val prices: List<MandiPriceDto>) : MandiUiState()
    data class Error(val message: String) : MandiUiState()
}

@HiltViewModel
class MandiViewModel @Inject constructor(
    private val repository: MandiRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow<MandiUiState>(MandiUiState.Loading)
    val uiState: StateFlow<MandiUiState> = _uiState.asStateFlow()

    private val _selectedDistrict = MutableStateFlow("Belagavi")
    val selectedDistrict: StateFlow<String> = _selectedDistrict.asStateFlow()

    private val _searchQuery = MutableStateFlow("")
    val searchQuery: StateFlow<String> = _searchQuery.asStateFlow()

    val districts = listOf("Belagavi", "Bengaluru", "Ballari", "Mysuru", "Dharwad", "Kalaburagi", "Shivamogga")

    init {
        loadPrices("Belagavi")
    }

    fun selectDistrict(district: String) {
        _selectedDistrict.value = district
        loadPrices(district, _searchQuery.value.ifBlank { null })
    }

    fun searchCrop(query: String) {
        _searchQuery.value = query
        loadPrices(_selectedDistrict.value, query.ifBlank { null })
    }

    fun loadPrices(district: String, crop: String? = null) {
        viewModelScope.launch {
            _uiState.value = MandiUiState.Loading
            val result = repository.getMandiPrices(district, crop)
            result.onSuccess { data ->
                _uiState.value = MandiUiState.Success(data)
            }.onFailure { err ->
                _uiState.value = MandiUiState.Error(err.localizedMessage ?: "ಮಾರುಕಟ್ಟೆ ದರಗಳು ಲಭ್ಯವಿಲ್ಲ")
            }
        }
    }
}

