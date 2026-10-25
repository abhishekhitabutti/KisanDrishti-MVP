package com.abhishek.krushinudi

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.abhishek.krushinudi.ui.screen.BorewellScreen
import com.abhishek.krushinudi.ui.screen.CropDoctorScreen
import com.abhishek.krushinudi.ui.screen.HomeScreen
import com.abhishek.krushinudi.ui.screen.MandiScreen
import com.abhishek.krushinudi.ui.screen.WeatherScreen
import com.abhishek.krushinudi.ui.theme.KrushiNudiTheme
import com.abhishek.krushinudi.viewmodel.BorewellViewModel
import com.abhishek.krushinudi.viewmodel.CropDoctorViewModel
import com.abhishek.krushinudi.viewmodel.MandiViewModel
import com.abhishek.krushinudi.viewmodel.WeatherViewModel
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            KrushiNudiTheme {
                val navController = rememberNavController()

                NavHost(navController = navController, startDestination = "home") {
                    composable("home") {
                        HomeScreen(
                            onNavigate = { route -> navController.navigate(route) }
                        )
                    }
                    composable("crop_doctor") {
                        val vm: CropDoctorViewModel = hiltViewModel()
                        CropDoctorScreen(
                            viewModel = vm,
                            onBack = { navController.popBackStack() }
                        )
                    }
                    composable("borewell") {
                        val vm: BorewellViewModel = hiltViewModel()
                        BorewellScreen(
                            viewModel = vm,
                            onBack = { navController.popBackStack() }
                        )
                    }
                    composable("weather") {
                        val vm: WeatherViewModel = hiltViewModel()
                        WeatherScreen(
                            viewModel = vm,
                            onBack = { navController.popBackStack() },
                            onNavigate = { route -> navController.navigate(route) }
                        )
                    }
                    composable("mandi") {
                        val vm: MandiViewModel = hiltViewModel()
                        MandiScreen(
                            viewModel = vm,
                            onBack = { navController.popBackStack() }
                        )
                    }
                }
            }
        }
    }
}

