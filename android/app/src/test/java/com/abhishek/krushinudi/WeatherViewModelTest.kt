package com.abhishek.krushinudi

import com.abhishek.krushinudi.data.remote.DayForecastDto
import com.abhishek.krushinudi.data.remote.PrecautionDto
import com.abhishek.krushinudi.data.remote.WeatherForecastResponseDto
import com.abhishek.krushinudi.data.repository.WeatherRepository
import com.abhishek.krushinudi.viewmodel.WeatherUiState
import com.abhishek.krushinudi.viewmodel.WeatherViewModel
import io.mockk.coEvery
import io.mockk.mockk
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.test.StandardTestDispatcher
import kotlinx.coroutines.test.advanceUntilIdle
import kotlinx.coroutines.test.resetMain
import kotlinx.coroutines.test.runTest
import kotlinx.coroutines.test.setMain
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test

@OptIn(ExperimentalCoroutinesApi::class)
class WeatherViewModelTest {

    private val testDispatcher = StandardTestDispatcher()
    private val repository = mockk<WeatherRepository>()
    private lateinit var viewModel: WeatherViewModel

    private val sampleForecast = WeatherForecastResponseDto(
        district = "Bengaluru",
        state = "Karnataka",
        currentTempC = 28.0,
        feelsLikeC = 30.0,
        conditionEn = "Partly Cloudy",
        conditionKn = "ಭಾಗಶಃ ಮೋಡ",
        humidityPct = 68,
        windSpeedKmh = 16.0,
        windDirection = "WSW",
        precautions = listOf(
            PrecautionDto(
                id = "p1",
                instructionEn = "Irrigate crops in the morning or evening",
                instructionKn = "ಬೆಳಿಗ್ಗೆ ಅಥವಾ ಸಂಜೆ ನೀರು ಹರಿಸಿ",
                actionLabelEn = "Irrigate Now",
                actionLabelKn = "ನೀರು ಹರಿಸಿ",
                priority = "High"
            )
        ),
        forecast7Day = listOf(
            DayForecastDto("Today", "24 May", "Partly Cloudy", "partly_cloudy", 29, 20, 0.0, false)
        ),
        advisoryTipKn = "ಹವಾಮಾನ ತಿಳಿದು, ಸಮರ್ಥ ಕೃಷಿ ಮಾಡಿ",
        advisoryTipEn = "Know the weather, farm efficiently"
    )

    @Before
    fun setUp() {
        Dispatchers.setMain(testDispatcher)
        coEvery { repository.getWeatherForecast(any()) } returns Result.success(sampleForecast)
        viewModel = WeatherViewModel(repository)
    }

    @After
    fun tearDown() {
        Dispatchers.resetMain()
    }

    @Test
    fun `initial load transitions to Success state with 7-day forecast`() = runTest {
        advanceUntilIdle()
        assertTrue(viewModel.uiState.value is WeatherUiState.Success)
        val state = viewModel.uiState.value as WeatherUiState.Success
        assertEquals("Bengaluru", state.forecast.district)
        assertEquals(28.0, state.forecast.currentTempC, 0.1)
        assertEquals(1, state.forecast.precautions.size)
        assertEquals(1, state.forecast.forecast7Day.size)
    }

    @Test
    fun `changing district updates selectedDistrict and reloads weather`() = runTest {
        advanceUntilIdle()
        viewModel.selectDistrict("Belagavi, Karnataka")
        advanceUntilIdle()
        assertEquals("Belagavi, Karnataka", viewModel.selectedDistrict.value)
    }
}

