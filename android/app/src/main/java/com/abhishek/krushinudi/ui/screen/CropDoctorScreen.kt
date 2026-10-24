package com.abhishek.krushinudi.ui.screen

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.abhishek.krushinudi.ui.theme.*
import com.abhishek.krushinudi.viewmodel.CropDoctorUiState
import com.abhishek.krushinudi.viewmodel.CropDoctorViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CropDoctorScreen(
    viewModel: CropDoctorViewModel,
    onBack: () -> Unit
) {
    val uiState by viewModel.uiState.collectAsState()
    var selectedCrop by remember { mutableStateOf("Cotton (ಹತ್ತಿ)") }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("🩺 ಬೆಳೆ ವೈದ್ಯ {Crop Doctor}") },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back")
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = PrimaryGreen,
                    titleContentColor = Color.White,
                    navigationIconContentColor = Color.White
                )
            )
        }
    ) { paddingValues ->
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .background(SurfaceLight)
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            item {
                Card(
                    modifier = Modifier.fillMaxWidth(),
                    colors = CardDefaults.cardColors(containerColor = CardBackground),
                    shape = RoundedCornerShape(12.dp)
                ) {
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text("📷 ಪೀಡಿತ ಬೆಳೆಯ ಫೋಟೋ ತೆಗೆಯಿರಿ ಅಥವಾ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ", style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
                        Text("ರೋಗ ಅಥವಾ ಕೀಟವಿರುವ ಎಲೆ, ಹೂವು ಅಥವಾ ಕಾಯಿಯನ್ನು ಹತ್ತಿರದಿಂದ ಫೋಟೋ ತೆಗೆಯಿರಿ", style = MaterialTheme.typography.bodyMedium, color = TextSecondary)
                        Spacer(modifier = Modifier.height(16.dp))

                        Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(12.dp)) {
                            Button(
                                onClick = { /* Camera Intent */ },
                                modifier = Modifier.weight(1f),
                                colors = ButtonDefaults.buttonColors(containerColor = PrimaryGreen)
                            ) {
                                Icon(Icons.Default.PhotoCamera, contentDescription = null)
                                Spacer(modifier = Modifier.width(6.dp))
                                Text("ಕ್ಯಾಮರಾ")
                            }
                            OutlinedButton(
                                onClick = { /* Gallery Intent */ },
                                modifier = Modifier.weight(1f)
                            ) {
                                Icon(Icons.Default.PhotoLibrary, contentDescription = null)
                                Spacer(modifier = Modifier.width(6.dp))
                                Text("ಗ್ಯಾಲರಿ")
                            }
                        }

                        Spacer(modifier = Modifier.height(12.dp))
                        Button(
                            onClick = { viewModel.diagnose(selectedCrop, "Belagavi") },
                            modifier = Modifier.fillMaxWidth(),
                            colors = ButtonDefaults.buttonColors(containerColor = DarkGreen)
                        ) {
                            Icon(Icons.Default.Search, contentDescription = null)
                            Spacer(modifier = Modifier.width(8.dp))
                            Text("🔬 ಎಐ ತಪಾಸಣೆ ನಡೆಸಿ {Run AI Diagnosis}")
                        }
                    }
                }
            }

            when (val state = uiState) {
                is CropDoctorUiState.Analyzing -> {
                    item {
                        Card(
                            modifier = Modifier.fillMaxWidth(),
                            colors = CardDefaults.cardColors(containerColor = CardBackground)
                        ) {
                            Column(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .padding(32.dp),
                                horizontalAlignment = Alignment.CenterHorizontally
                            ) {
                                CircularProgressIndicator(color = PrimaryGreen)
                                Spacer(modifier = Modifier.height(16.dp))
                                Text("ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ (AI) ಮೂಲಕ ಫೋಟೋ ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ...", style = MaterialTheme.typography.titleMedium)
                                Text("ಜ್ಞಾನಕೋಶದೊಂದಿಗೆ ಲಕ್ಷಣಗಳನ್ನು ಹೋಲಿಸಲಾಗುತ್ತಿದೆ...", style = MaterialTheme.typography.bodyMedium, color = TextSecondary)
                            }
                        }
                    }
                }
                is CropDoctorUiState.Success -> {
                    val report = state.report
                    item {
                        // Diagnostic Result Header
                        Card(
                            modifier = Modifier.fillMaxWidth(),
                            colors = CardDefaults.cardColors(containerColor = LightGreen),
                            shape = RoundedCornerShape(12.dp)
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Text("ಪತ್ತೆಯಾದ ಸಮಸ್ಯೆ {Diagnosis}:", style = MaterialTheme.typography.bodyMedium, color = DarkGreen)
                                Text(report.nameKn, style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold, color = DarkGreen)
                                Text("ಖಾತರಿ ಮಟ್ಟ {Confidence}: ${report.confidence.uppercase()}", style = MaterialTheme.typography.labelSmall, color = TextSecondary)
                            }
                        }
                    }

                    // Symptoms Observed
                    item {
                        Card(
                            modifier = Modifier.fillMaxWidth(),
                            colors = CardDefaults.cardColors(containerColor = CardBackground)
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Text("🔍 ನಿಮ್ಮ ಫೋಟೋದಲ್ಲಿ ಕಂಡ ಲಕ್ಷಣಗಳು {Symptoms}:", style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
                                Spacer(modifier = Modifier.height(8.dp))
                                report.symptomsSeen.forEach { sym ->
                                    Text("• $sym", style = MaterialTheme.typography.bodyMedium)
                                }
                            }
                        }
                    }

                    // First Do This (Non-Chemical Organic First)
                    item {
                        Card(
                            modifier = Modifier.fillMaxWidth(),
                            colors = CardDefaults.cardColors(containerColor = CardBackground),
                            shape = RoundedCornerShape(12.dp)
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Row(verticalAlignment = Alignment.CenterVertically) {
                                    Icon(Icons.Default.Eco, contentDescription = null, tint = PrimaryGreen)
                                    Spacer(modifier = Modifier.width(8.dp))
                                    Text("ಮೊದಲು ಇದನ್ನು ಮಾಡಿ (ಸಿಂಪಡಣೆ ಇಲ್ಲದೆ) {Organic First}:", style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold, color = DarkGreen)
                                }
                                Spacer(modifier = Modifier.height(8.dp))
                                report.firstDoThis.forEach { step ->
                                    Text("✅ $step", style = MaterialTheme.typography.bodyMedium)
                                }
                            }
                        }
                    }
                }
                is CropDoctorUiState.Error -> {
                    item {
                        Card(
                            modifier = Modifier.fillMaxWidth(),
                            colors = CardDefaults.cardColors(containerColor = Color(0xFFFFEBEE))
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Text("⚠️ ದೋಷ {Error}:", style = MaterialTheme.typography.titleMedium, color = DangerRed, fontWeight = FontWeight.Bold)
                                Text(state.message, style = MaterialTheme.typography.bodyMedium, color = DangerRed)
                            }
                        }
                    }
                }
                CropDoctorUiState.Idle -> {}
            }
        }
    }
}
