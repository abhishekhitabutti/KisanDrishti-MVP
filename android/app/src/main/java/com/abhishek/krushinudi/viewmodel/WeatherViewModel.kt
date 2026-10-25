package com.abhishek.krushinudi.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.abhishek.krushinudi.data.remote.WeatherForecastResponseDto
import com.abhishek.krushinudi.data.repository.WeatherRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import javax.inject.Inject

sealed class WeatherUiState {
    object Loading : WeatherUiState()
    data class Success(val forecast: WeatherForecastResponseDto) : WeatherUiState()
    data class Error(val message: String) : WeatherUiState()
}

@HiltViewModel
class WeatherViewModel @Inject constructor(
    private val repository: WeatherRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow<WeatherUiState>(WeatherUiState.Loading)
    val uiState: StateFlow<WeatherUiState> = _uiState.asStateFlow()

    private val _selectedDistrict = MutableStateFlow("Bengaluru, Karnataka")
    val selectedDistrict: StateFlow<String> = _selectedDistrict.asStateFlow()

    val availableDistricts = listOf(
        "Bengaluru, Karnataka",
        "Belagavi, Karnataka",
        "Mysuru, Karnataka",
        "Ballari, Karnataka",
        "Shivamogga, Karnataka",
        "Dharwad, Karnataka",
        "Kalaburagi, Karnataka",
        "Hassan, Karnataka",
        "Tumakuru, Karnataka"
    )

    init {
        loadWeather("Bengaluru")
    }

    fun selectDistrict(districtFullName: String) {
        _selectedDistrict.value = districtFullName
        val districtName = districtFullName.split(",")[0].trim()
        loadWeather(districtName)
    }

    fun loadWeather(district: String) {
        viewModelScope.launch {
            _uiState.value = WeatherUiState.Loading
            val result = repository.getWeatherForecast(district)
            result.onSuccess { data ->
                _uiState.value = WeatherUiState.Success(data)
            }.onFailure { err ->
                _uiState.value = WeatherUiState.Error(err.localizedMessage ?: "ಹವಾಮಾನ ಲೋಡ್ ಮಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತಿಲ್ಲ")
            }
        }
    }
}

