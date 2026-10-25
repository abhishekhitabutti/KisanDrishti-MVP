package com.abhishek.krushinudi.ui.screen

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.abhishek.krushinudi.ui.theme.*

data class HomeFeature(
    val titleKn: String,
    val titleEn: String,
    val icon: ImageVector,
    val badge: String,
    val color: Color,
    val route: String
)

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun HomeScreen(
    onNavigate: (String) -> Unit
) {
    val features = listOf(
        HomeFeature("ಬೆಳೆ ವೈದ್ಯ", "Crop Doctor (AI Vision)", Icons.Default.MedicalServices, "AI ತಪಾಸಣೆ", PrimaryGreen, "crop_doctor"),
        HomeFeature("ಬೋರ್‌ವೆಲ್ ಸಲಹೆಗಾರ", "Borewell Advisor (GPS)", Icons.Default.WaterDrop, "ನಿಖರ ಪಾಯಿಂಟ್", InfoBlue, "borewell"),
        HomeFeature("ಹವಾಮಾನ ಮುನ್ನೆಚ್ಚರಿಕೆ", "Weather & Spray Windows", Icons.Default.WbSunny, "3-ದಿನ ಮುನ್ಸೂಚನೆ", AccentAmber, "weather"),
        HomeFeature("ಕಳೆ & ಪೋಷಕಾಂಶಗಳು", "Weed & Nutrition Manager", Icons.Default.Grass, "ರಾಸಾಯನಿಕ ರಹಿತ", DarkGreen, "weed_nutrient"),
        HomeFeature("ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆ", "Mandi Live Prices", Icons.Default.Storefront, "ದೈನಂದಿನ ದರ", PrimaryGreen, "mandi"),
        HomeFeature("ಋತುಮಾನ ಯೋಜನೆ", "Crop Season Planner", Icons.Default.CalendarMonth, "ಹಂತ-ಹಂತದ ಪಟ್ಟಿ", DarkGreen, "planner")
    )

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Column {
                        Text("🌾 ಕೃಷಿನುಡಿ {KrushiNudi}", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold)
                        Text("ಕರ್ನಾಟಕ ರೈತರ ವಿಶ್ವಾಸಾರ್ಹ ಡಿಜಿಟಲ್ ಕೃಷಿ ಸಂಗಾತಿ", style = MaterialTheme.typography.labelSmall)
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = PrimaryGreen,
                    titleContentColor = Color.White
                )
            )
        }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .background(SurfaceLight)
                .padding(16.dp)
        ) {
            // Live Weather & Spray Badge Card
            Card(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(bottom = 16.dp),
                colors = CardDefaults.cardColors(containerColor = LightGreen),
                shape = RoundedCornerShape(12.dp)
            ) {
                Row(
                    modifier = Modifier.padding(16.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Icon(Icons.Default.CheckCircle, contentDescription = null, tint = DarkGreen, modifier = Modifier.size(32.dp))
                    Spacer(modifier = Modifier.width(12.dp))
                    Column {
                        Text("ಸಿಂಪರಣೆಗೆ ಉತ್ತಮ ದಿನ {Good Spray Day}", style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold, color = DarkGreen)
                        Text("ಬೆಳಗಾವಿ: 28°C | ಗಾಳಿ 14 km/h | ಮುಂದಿನ 6 ಗಂಟೆಗಳಲ್ಲಿ ಮಳೆಯಿಲ್ಲ", style = MaterialTheme.typography.bodyMedium, color = TextSecondary)
                    }
                }
            }

            Text("ಕೃಷಿ ಪರಿಕರಗಳು & ಸೇವೆಗಳು {Farmer Services}", style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
            Spacer(modifier = Modifier.height(12.dp))

            // Grid of Agricultural Features
            LazyVerticalGrid(
                columns = GridCells.Fixed(2),
                horizontalArrangement = Arrangement.spacedBy(12.dp),
                verticalArrangement = Arrangement.spacedBy(12.dp),
                modifier = Modifier.weight(1f)
            ) {
                items(features.size) { index ->
                    val feature = features[index]
                    Card(
                        modifier = Modifier
                            .fillMaxWidth()
                            .clip(RoundedCornerShape(12.dp))
                            .clickable { onNavigate(feature.route) },
                        colors = CardDefaults.cardColors(containerColor = CardBackground),
                        elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
                    ) {
                        Column(modifier = Modifier.padding(16.dp)) {
                            Box(
                                modifier = Modifier
                                    .size(44.dp)
                                    .background(feature.color.copy(alpha = 0.15f), RoundedCornerShape(8.dp)),
                                contentAlignment = Alignment.Center
                            ) {
                                Icon(feature.icon, contentDescription = null, tint = feature.color)
                            }
                            Spacer(modifier = Modifier.height(10.dp))
                            Text(feature.titleKn, style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
                            Text(feature.titleEn, style = MaterialTheme.typography.bodyMedium, color = TextSecondary, fontSize = 11.sp)
                            Spacer(modifier = Modifier.height(8.dp))
                            Surface(
                                color = LightGreen,
                                shape = RoundedCornerShape(4.dp)
                            ) {
                                Text(feature.badge, color = DarkGreen, style = MaterialTheme.typography.labelSmall, modifier = Modifier.padding(horizontal = 6.dp, vertical = 2.dp))
                            }
                        }
                    }
                }
            }

            // Copyright Banner
            Text(
                "© 2026 Abhishek Hitabutti | ಕೃಷಿನುಡಿ",
                style = MaterialTheme.typography.labelSmall,
                color = TextSecondary,
                modifier = Modifier
                    .align(Alignment.CenterHorizontally)
                    .padding(top = 8.dp)
            )
        }
    }
}

