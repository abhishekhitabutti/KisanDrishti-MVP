package com.abhishek.krushinudi

import com.abhishek.krushinudi.data.remote.CropAnalysisResponseDto
import com.abhishek.krushinudi.data.repository.CropDoctorRepository
import com.abhishek.krushinudi.viewmodel.CropDoctorUiState
import com.abhishek.krushinudi.viewmodel.CropDoctorViewModel
import io.mockk.coEvery
import io.mockk.mockk
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.test.StandardTestDispatcher
import kotlinx.coroutines.test.resetMain
import kotlinx.coroutines.test.runTest
import kotlinx.coroutines.test.setMain
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test
import java.io.File

@OptIn(ExperimentalCoroutinesApi::class)
class CropDoctorViewModelTest {

    private val testDispatcher = StandardTestDispatcher()
    private val repository = mockk<CropDoctorRepository>()
    private lateinit var viewModel: CropDoctorViewModel

    @Before
    fun setUp() {
        Dispatchers.setMain(testDispatcher)
        viewModel = CropDoctorViewModel(repository)
    }

    @After
    fun tearDown() {
        Dispatchers.resetMain()
    }

    @Test
    fun `initial state is Idle`() {
        assertEquals(CropDoctorUiState.Idle, viewModel.uiState.value)
    }

    @Test
    fun `diagnose without image transitions to Error state`() {
        viewModel.diagnose("cotton", "Belagavi")
        assertTrue(viewModel.uiState.value is CropDoctorUiState.Error)
    }

    @Test
    fun `diagnose with valid image transitions to Success state`() = runTest {
        val mockFile = mockk<File>()
        viewModel.setImage(mockFile)

        val mockReport = CropAnalysisResponseDto(
            crop = "cotton",
            category = "pest",
            nameKn = "ಗುಲಾಬಿ ಕಾಯಿಕೊರಕ {Pink Bollworm}",
            nameEn = "Pink Bollworm",
            confidence = "high",
            symptomsSeen = listOf("Rosetted flowers"),
            couldAlsoBe = emptyList(),
            firstDoThis = listOf("Pheromone traps"),
            chemicalOptions = emptyList(),
            sprayTiming = listOf("Spray in evening"),
            safety = listOf("Wear protective equipment")
        )

        coEvery { repository.diagnosePhoto(mockFile, any(), any(), any()) } returns Result.success(mockReport)

        viewModel.diagnose("cotton", "Belagavi")
        testDispatcher.scheduler.advanceUntilIdle()

        assertTrue(viewModel.uiState.value is CropDoctorUiState.Success)
        val success = viewModel.uiState.value as CropDoctorUiState.Success
        assertEquals("cotton", success.report.crop)
    }
}

