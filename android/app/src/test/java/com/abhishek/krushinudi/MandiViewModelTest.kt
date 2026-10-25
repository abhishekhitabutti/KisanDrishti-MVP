package com.abhishek.krushinudi

import com.abhishek.krushinudi.data.remote.MandiPriceDto
import com.abhishek.krushinudi.data.repository.MandiRepository
import com.abhishek.krushinudi.viewmodel.MandiUiState
import com.abhishek.krushinudi.viewmodel.MandiViewModel
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
class MandiViewModelTest {

    private val testDispatcher = StandardTestDispatcher()
    private val repository = mockk<MandiRepository>()
    private lateinit var viewModel: MandiViewModel

    private val samplePrices = listOf(
        MandiPriceDto("ಹತ್ತಿ {Cotton}", "DCH-32", "Belagavi APMC", 7100.0, 7550.0, 7820.0, "up"),
        MandiPriceDto("ಸೋಯಾಬೀನ್ {Soybean}", "JS-335", "Belagavi APMC", 4200.0, 4450.0, 4600.0, "stable")
    )

    @Before
    fun setUp() {
        Dispatchers.setMain(testDispatcher)
        coEvery { repository.getMandiPrices(any(), any()) } returns Result.success(samplePrices)
        viewModel = MandiViewModel(repository)
    }

    @After
    fun tearDown() {
        Dispatchers.resetMain()
    }

    @Test
    fun `initial load transitions to Success state with prices list`() = runTest {
        advanceUntilIdle()
        assertTrue(viewModel.uiState.value is MandiUiState.Success)
        val state = viewModel.uiState.value as MandiUiState.Success
        assertEquals(2, state.prices.size)
        assertEquals("ಹತ್ತಿ {Cotton}", state.prices[0].cropKn)
        assertEquals(7550.0, state.prices[0].modalPrice, 0.1)
    }

    @Test
    fun `search crop updates search query and triggers repository`() = runTest {
        advanceUntilIdle()
        viewModel.searchCrop("cotton")
        advanceUntilIdle()
        assertEquals("cotton", viewModel.searchQuery.value)
    }
}

