package com.abhishek.krushinudi.ui.screen

import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.abhishek.krushinudi.ui.theme.*
import com.abhishek.krushinudi.viewmodel.BorewellUiState
import com.abhishek.krushinudi.viewmodel.BorewellViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun BorewellScreen(
    viewModel: BorewellViewModel,
    onBack: () -> Unit
) {
    val context = LocalContext.current
    val uiState by viewModel.uiState.collectAsState()

    var selectedDistrict by remember { mutableStateOf("Belagavi") }
    var selectedTaluk by remember { mutableStateOf("Chikkodi") }
    var selectedHobli by remember { mutableStateOf("Sadalga") }
    var selectedVillage by remember { mutableStateOf("Sadalga") }
    var surveyNo by remember { mutableStateOf("") }
    var acres by remember { mutableStateOf(2.0) }
    var topography by remember { mutableStateOf("plain") }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("🎯 ಬೋರ್‌ವೆಲ್ ಸಲಹೆಗಾರ {Borewell Advisor}") },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back")
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = InfoBlue,
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
                        Text("📍 ಜಮೀನಿನ ಸ್ಥಳ ಆಯ್ಕೆ (ಜಿಲ್ಲೆ ➔ ತಾಲೂಕು ➔ ಹೋಬಳಿ ➔ ಗ್ರಾಮ):", style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
                        Spacer(modifier = Modifier.height(12.dp))

                        // District / Taluk / Hobli / Village Badges
                        Surface(
                            color = LightGreen,
                            shape = RoundedCornerShape(8.dp),
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Column(modifier = Modifier.padding(12.dp)) {
                                Text("ಜಿಲ್ಲೆ: $selectedDistrict", fontWeight = FontWeight.SemiBold, color = DarkGreen)
                                Text("ತಾಲೂಕು: $selectedTaluk | ಹೋಬಳಿ: $selectedHobli", color = DarkGreen)
                                Text("ಗ್ರಾಮ: $selectedVillage", color = DarkGreen)
                            }
                        }

                        Spacer(modifier = Modifier.height(12.dp))
                        OutlinedTextField(
                            value = surveyNo,
                            onValueChange = { surveyNo = it },
                            label = { Text("ಸರ್ವೆ ನಂ. / ಜಮೀನಿನ ಹೆಸರು {Survey No. / Plot ID}") },
                            placeholder = { Text("ಉದಾ: Sy No 142/2A") },
                            modifier = Modifier.fillMaxWidth()
                        )

                        Spacer(modifier = Modifier.height(16.dp))
                        Button(
                            onClick = {
                                viewModel.calculate(
                                    district = selectedDistrict,
                                    taluk = selectedTaluk,
                                    hobli = selectedHobli,
                                    village = selectedVillage,
                                    surveyNo = surveyNo,
                                    customLat = null,
                                    customLon = null,
                                    acres = acres,
                                    topography = topography,
                                    soilType = "red",
                                    workingWells = 1,
                                    dryWells = 0,
                                    hasWaterBody = false
                                )
                            },
                            modifier = Modifier.fillMaxWidth(),
                            colors = ButtonDefaults.buttonColors(containerColor = InfoBlue)
                        ) {
                            Icon(Icons.Default.Explore, contentDescription = null)
                            Spacer(modifier = Modifier.width(8.dp))
                            Text("ವೈಜ್ಞಾನಿಕ ಪಾಯಿಂಟ್ ಲೆಕ್ಕಾಚಾರ ಮಾಡಿ {Calculate Points}")
                        }
                    }
                }
            }

            when (val state = uiState) {
                is BorewellUiState.Calculating -> {
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
                                CircularProgressIndicator(color = InfoBlue)
                                Spacer(modifier = Modifier.height(16.dp))
                                Text("ಭಾರತ ಸರ್ಕಾರದ {India-WRIS / CGWB} ದತ್ತಾಂಶ ಪರಿಶೀಲಿಸಲಾಗುತ್ತಿದೆ...", style = MaterialTheme.typography.titleMedium)
                                Text("ಶಿಲಾ ಬಿರುಕುಗಳ (Secondary Fracture Lineaments) ಸಂಗಮ ಲೆಕ್ಕಾಚಾರ...", style = MaterialTheme.typography.bodyMedium, color = TextSecondary)
                            }
                        }
                    }
                }
                is BorewellUiState.Success -> {
                    val res = state.response

                    // Feasibility Summary
                    item {
                        Card(
                            modifier = Modifier.fillMaxWidth(),
                            colors = CardDefaults.cardColors(containerColor = LightGreen),
                            shape = RoundedCornerShape(12.dp)
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Text("ವರದಿ ಸ್ಥಳ: ${res.district} > ${res.taluk} > ${res.hobli} > ${res.village}", fontWeight = FontWeight.Bold, color = DarkGreen)
                                Spacer(modifier = Modifier.height(8.dp))
                                Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
                                    Column {
                                        Text("ನೀರು ಸಿಗುವ ಆಳ", style = MaterialTheme.typography.labelSmall, color = TextSecondary)
                                        Text("${res.estMinFt} - ${res.estMaxFt} ಅಡಿ", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold, color = DarkGreen)
                                    }
                                    Column {
                                        Text("ಅಂದಾಜು ಜಲಬಲ", style = MaterialTheme.typography.labelSmall, color = TextSecondary)
                                        Text(res.yieldInches, style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold, color = DarkGreen)
                                    }
                                    Column {
                                        Text("ಖಾತರಿ ಪ್ರಮಾಣ", style = MaterialTheme.typography.labelSmall, color = TextSecondary)
                                        Text("${res.finalProb}%", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold, color = DarkGreen)
                                    }
                                }
                            }
                        }
                    }

                    // Candidate Points Header
                    item {
                        Text("🎯 ಜಮೀನಿನಲ್ಲಿ ಗುರುತಿಸಲಾದ ನಿಖರ ಬೋರ್‌ವೆಲ್ ಪಾಯಿಂಟ್‌ಗಳು:", style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
                    }

                    // 3 Pinpoint Candidate Cards
                    items(res.candidatePoints.size) { idx ->
                        val pt = res.candidatePoints[idx]
                        val badgeColor = when (pt.grade) {
                            "A+" -> PrimaryGreen
                            "A" -> Color(0xFF388E3C)
                            else -> DangerRed
                        }

                        Card(
                            modifier = Modifier.fillMaxWidth(),
                            colors = CardDefaults.cardColors(containerColor = CardBackground),
                            shape = RoundedCornerShape(12.dp),
                            elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    horizontalArrangement = Arrangement.SpaceBetween,
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Text(pt.nameKn, style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold)
                                    Surface(
                                        color = badgeColor,
                                        shape = RoundedCornerShape(12.dp)
                                    ) {
                                        Text("ಗ್ರೇಡ್ ${pt.grade} (${pt.assurancePct}%)", color = Color.White, style = MaterialTheme.typography.labelSmall, modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp))
                                    }
                                }

                                Spacer(modifier = Modifier.height(10.dp))
                                Text("📍 ನಿರ್ದೇಶಾಂಕಗಳು: ${pt.lat}° N, ${pt.lon}° E", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold)
                                Text("📏 ಅಂತರ & ದಿಕ್ಕು: ${pt.distanceM}m (${pt.directionKn})", style = MaterialTheme.typography.bodyMedium)
                                Text("⛏️ ಜಲಸೆಲೆ ಸಿಗುವ ಆಳ: ${pt.mainStrikeFt}", style = MaterialTheme.typography.bodyMedium)
                                Text("🚩 ಜಮೀನಿನಲ್ಲಿ ಗುರುತು: ${pt.fieldMarkingKn}", style = MaterialTheme.typography.bodyMedium, color = TextSecondary)

                                Spacer(modifier = Modifier.height(12.dp))
                                Button(
                                    onClick = {
                                        val intent = Intent(Intent.ACTION_VIEW, Uri.parse(pt.navUrl))
                                        context.startActivity(intent)
                                    },
                                    modifier = Modifier.fillMaxWidth(),
                                    colors = ButtonDefaults.buttonColors(containerColor = PrimaryGreen)
                                ) {
                                    Icon(Icons.Default.Navigation, contentDescription = null)
                                    Spacer(modifier = Modifier.width(6.dp))
                                    Text("🧭 ಗೂಗಲ್ ಮ್ಯಾಪ್‌ನಲ್ಲಿ ನಡೆಯಿರಿ {Navigate}")
                                }
                            }
                        }
                    }
                }
                is BorewellUiState.Error -> {
                    item {
                        Card(
                            modifier = Modifier.fillMaxWidth(),
                            colors = CardDefaults.cardColors(containerColor = Color(0xFFFFEBEE))
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Text("⚠️ ದೋಷ: ${state.message}", color = DangerRed, fontWeight = FontWeight.Bold)
                            }
                        }
                    }
                }
                BorewellUiState.Idle -> {}
            }
        }
    }
}
