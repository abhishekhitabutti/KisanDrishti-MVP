package com.abhishek.krushinudi.ui.screen

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material.icons.outlined.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.abhishek.krushinudi.data.remote.DayForecastDto
import com.abhishek.krushinudi.data.remote.PrecautionDto
import com.abhishek.krushinudi.data.remote.WeatherForecastResponseDto
import com.abhishek.krushinudi.ui.theme.*
import com.abhishek.krushinudi.viewmodel.WeatherUiState
import com.abhishek.krushinudi.viewmodel.WeatherViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun WeatherScreen(
    viewModel: WeatherViewModel,
    onBack: () -> Unit,
    onNavigate: (String) -> Unit = {}
) {
    val uiState by viewModel.uiState.collectAsState()
    val selectedDistrict by viewModel.selectedDistrict.collectAsState()
    var showDistrictMenu by remember { mutableStateOf(false) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text(
                            "Weather Forecast ⛅",
                            style = MaterialTheme.typography.titleLarge,
                            fontWeight = FontWeight.Bold,
                            color = Color.White
                        )
                    }
                },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.Menu, contentDescription = "Menu", tint = Color.White)
                    }
                },
                actions = {
                    IconButton(onClick = { /* Notifications */ }) {
                        Icon(Icons.Outlined.Notifications, contentDescription = "Alerts", tint = Color.White)
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = PrimaryGreen
                )
            )
        },
        bottomBar = {
            NavigationBar(
                containerColor = Color.White,
                tonalElevation = 8.dp
            ) {
                NavigationBarItem(
                    selected = false,
                    onClick = { onNavigate("home") },
                    icon = { Icon(Icons.Default.Home, contentDescription = null) },
                    label = { Text("Home", fontSize = 11.sp) },
                    colors = NavigationBarItemDefaults.colors(selectedIconColor = PrimaryGreen, unselectedIconColor = Color.Gray)
                )
                NavigationBarItem(
                    selected = false,
                    onClick = { onNavigate("crop_doctor") },
                    icon = { Icon(Icons.Default.Spa, contentDescription = null) },
                    label = { Text("Crop Info", fontSize = 11.sp) },
                    colors = NavigationBarItemDefaults.colors(selectedIconColor = PrimaryGreen, unselectedIconColor = Color.Gray)
                )
                NavigationBarItem(
                    selected = true,
                    onClick = { },
                    icon = { Icon(Icons.Default.WbSunny, contentDescription = null) },
                    label = { Text("Weather", fontSize = 11.sp, fontWeight = FontWeight.Bold) },
                    colors = NavigationBarItemDefaults.colors(selectedIconColor = PrimaryGreen, selectedTextColor = PrimaryGreen, indicatorColor = LightGreen)
                )
                NavigationBarItem(
                    selected = false,
                    onClick = { onNavigate("borewell") },
                    icon = { Icon(Icons.Default.MenuBook, contentDescription = null) },
                    label = { Text("Learn", fontSize = 11.sp) },
                    colors = NavigationBarItemDefaults.colors(selectedIconColor = PrimaryGreen, unselectedIconColor = Color.Gray)
                )
                NavigationBarItem(
                    selected = false,
                    onClick = { },
                    icon = { Icon(Icons.Default.Person, contentDescription = null) },
                    label = { Text("My Profile", fontSize = 11.sp) },
                    colors = NavigationBarItemDefaults.colors(selectedIconColor = PrimaryGreen, unselectedIconColor = Color.Gray)
                )
            }
        }
    ) { paddingValues ->
        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .background(Color(0xFFF8FAF7))
        ) {
            when (val state = uiState) {
                is WeatherUiState.Loading -> {
                    CircularProgressIndicator(
                        modifier = Modifier.align(Alignment.Center),
                        color = PrimaryGreen
                    )
                }
                is WeatherUiState.Error -> {
                    Column(
                        modifier = Modifier
                            .align(Alignment.Center)
                            .padding(24.dp),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Text(state.message, color = ErrorRed, style = MaterialTheme.typography.bodyLarge)
                        Spacer(modifier = Modifier.height(12.dp))
                        Button(
                            onClick = { viewModel.loadWeather(selectedDistrict.split(",")[0].trim()) },
                            colors = ButtonDefaults.buttonColors(containerColor = PrimaryGreen)
                        ) {
                            Text("Retry / ಪುನಃ ಪ್ರಯತ್ನಿಸಿ")
                        }
                    }
                }
                is WeatherUiState.Success -> {
                    WeatherContent(
                        forecast = state.forecast,
                        selectedDistrict = selectedDistrict,
                        availableDistricts = viewModel.availableDistricts,
                        onSelectDistrict = { viewModel.selectDistrict(it) }
                    )
                }
            }
        }
    }
}

@Composable
fun WeatherContent(
    forecast: WeatherForecastResponseDto,
    selectedDistrict: String,
    availableDistricts: List<String>,
    onSelectDistrict: (String) -> Unit
) {
    var expandedDistrict by remember { mutableStateOf(false) }

    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .padding(horizontal = 16.dp, vertical = 12.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        // Location Selector Row
        item {
            Box {
                Row(
                    modifier = Modifier
                        .clip(RoundedCornerShape(8.dp))
                        .clickable { expandedDistrict = true }
                        .padding(vertical = 4.dp, horizontal = 2.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Icon(
                        Icons.Default.LocationOn,
                        contentDescription = "Location",
                        tint = DarkGreen,
                        modifier = Modifier.size(22.dp)
                    )
                    Spacer(modifier = Modifier.width(6.dp))
                    Text(
                        selectedDistrict,
                        style = MaterialTheme.typography.titleMedium,
                        fontWeight = FontWeight.Bold,
                        color = Color(0xFF1F2937)
                    )
                    Spacer(modifier = Modifier.width(4.dp))
                    Icon(
                        Icons.Default.KeyboardArrowDown,
                        contentDescription = "Select",
                        tint = Color.Gray,
                        modifier = Modifier.size(20.dp)
                    )
                }

                DropdownMenu(
                    expanded = expandedDistrict,
                    onDismissRequest = { expandedDistrict = false }
                ) {
                    availableDistricts.forEach { dist ->
                        DropdownMenuItem(
                            text = { Text(dist) },
                            onClick = {
                                onSelectDistrict(dist)
                                expandedDistrict = false
                            }
                        )
                    }
                }
            }
        }

        // 1. Current Weather Hero Card
        item {
            Card(
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(18.dp),
                colors = CardDefaults.cardColors(containerColor = Color.Transparent),
                elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
            ) {
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(
                            Brush.verticalGradient(
                                colors = listOf(Color(0xFFE8F1FC), Color(0xFFD6E6F8))
                            )
                        )
                        .padding(18.dp)
                ) {
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        // Left: Icon + Big Temperature & Condition
                        Column {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Text(
                                    "⛅",
                                    fontSize = 42.sp
                                )
                                Spacer(modifier = Modifier.width(10.dp))
                                Text(
                                    "${forecast.currentTempC.toInt()}°C",
                                    fontSize = 48.sp,
                                    fontWeight = FontWeight.ExtraBold,
                                    color = Color(0xFF1E293B)
                                )
                            }
                            Text(
                                forecast.conditionEn,
                                style = MaterialTheme.typography.titleMedium,
                                fontWeight = FontWeight.SemiBold,
                                color = Color(0xFF334155)
                            )
                            Spacer(modifier = Modifier.height(4.dp))
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Text("🌡️", fontSize = 12.sp)
                                Spacer(modifier = Modifier.width(4.dp))
                                Text(
                                    "Feels like ${forecast.feelsLikeC.toInt()}°C",
                                    style = MaterialTheme.typography.bodySmall,
                                    color = Color(0xFF64748B)
                                )
                            }
                        }

                        // Right: Humidity & Wind Speed Pillars
                        Column(verticalArrangement = Arrangement.spacedBy(12.dp)) {
                            Surface(
                                shape = RoundedCornerShape(12.dp),
                                color = Color.White.copy(alpha = 0.85f),
                                modifier = Modifier.width(135.dp)
                            ) {
                                Row(
                                    modifier = Modifier.padding(horizontal = 10.dp, vertical = 8.dp),
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Text("💧", fontSize = 18.sp)
                                    Spacer(modifier = Modifier.width(8.dp))
                                    Column {
                                        Text("Humidity", fontSize = 11.sp, color = Color.Gray)
                                        Text("${forecast.humidityPct}%", fontSize = 14.sp, fontWeight = FontWeight.Bold, color = Color(0xFF1E293B))
                                    }
                                }
                            }

                            Surface(
                                shape = RoundedCornerShape(12.dp),
                                color = Color.White.copy(alpha = 0.85f),
                                modifier = Modifier.width(135.dp)
                            ) {
                                Row(
                                    modifier = Modifier.padding(horizontal = 10.dp, vertical = 8.dp),
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Text("💨", fontSize = 18.sp)
                                    Spacer(modifier = Modifier.width(8.dp))
                                    Column {
                                        Text("Wind Speed", fontSize = 11.sp, color = Color.Gray)
                                        Text("${forecast.windSpeedKmh.toInt()} km/h", fontSize = 13.sp, fontWeight = FontWeight.Bold, color = Color(0xFF1E293B))
                                        Text(forecast.windDirection, fontSize = 10.sp, color = Color.Gray)
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        // 2. Farmer Precautions Card
        item {
            Card(
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(18.dp),
                colors = CardDefaults.cardColors(containerColor = Color(0xFFFFFBEB)),
                border = androidx.compose.foundation.BorderStroke(1.dp, Color(0xFFFDE68A)),
                elevation = CardDefaults.cardElevation(defaultElevation = 1.dp)
            ) {
                Column(modifier = Modifier.padding(16.dp)) {
                    // Precautions Header
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Surface(
                                shape = CircleShape,
                                color = Color(0xFFFEF3C7),
                                modifier = Modifier.size(32.dp)
                            ) {
                                Box(contentAlignment = Alignment.Center) {
                                    Text("🌾", fontSize = 16.sp)
                                }
                            }
                            Spacer(modifier = Modifier.width(8.dp))
                            Text(
                                "Farmer Precautions",
                                style = MaterialTheme.typography.titleMedium,
                                fontWeight = FontWeight.Bold,
                                color = Color(0xFF92400E)
                            )
                        }

                        Surface(
                            shape = RoundedCornerShape(12.dp),
                            color = Color(0xFFFEF3C7)
                        ) {
                            Text(
                                "⚠️ Take Action",
                                fontSize = 11.sp,
                                fontWeight = FontWeight.Bold,
                                color = Color(0xFFD97706),
                                modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                            )
                        }
                    }

                    Spacer(modifier = Modifier.height(14.dp))

                    // Precautions List
                    forecast.precautions.forEachIndexed { idx, item ->
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(vertical = 8.dp),
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Icon(
                                Icons.Default.CheckCircle,
                                contentDescription = null,
                                tint = Color(0xFF16A34A),
                                modifier = Modifier.size(20.dp)
                            )
                            Spacer(modifier = Modifier.width(10.dp))
                            Text(
                                item.instructionEn,
                                style = MaterialTheme.typography.bodyMedium,
                                color = Color(0xFF374151),
                                modifier = Modifier.weight(1f),
                                fontSize = 13.sp
                            )
                            Spacer(modifier = Modifier.width(8.dp))
                            Row(
                                modifier = Modifier.clickable { /* action */ },
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text(
                                    item.actionLabelEn,
                                    fontSize = 11.sp,
                                    fontWeight = FontWeight.SemiBold,
                                    color = Color(0xFFD97706)
                                )
                                Icon(
                                    Icons.Default.ChevronRight,
                                    contentDescription = null,
                                    tint = Color(0xFFD97706),
                                    modifier = Modifier.size(16.dp)
                                )
                            }
                        }
                        if (idx < forecast.precautions.size - 1) {
                            Divider(color = Color(0xFFFDE68A).copy(alpha = 0.5f), thickness = 0.8.dp)
                        }
                    }
                }
            }
        }

        // 3. 7-Day Forecast Section
        item {
            Column {
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text("📅", fontSize = 18.sp)
                        Spacer(modifier = Modifier.width(6.dp))
                        Text(
                            "7-Day Forecast",
                            style = MaterialTheme.typography.titleMedium,
                            fontWeight = FontWeight.Bold,
                            color = Color(0xFF1F2937)
                        )
                    }
                    Text(
                        "View Full Forecast >",
                        style = MaterialTheme.typography.bodySmall,
                        fontWeight = FontWeight.Medium,
                        color = PrimaryGreen
                    )
                }

                Spacer(modifier = Modifier.height(12.dp))

                // Horizontal Row of 7 Days
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .horizontalScroll(rememberScrollState()),
                    horizontalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    forecast.forecast7Day.forEach { day ->
                        DayForecastCard(day)
                    }
                }
            }
        }

        // 4. Agri Knowledge Banner
        item {
            Card(
                modifier = Modifier
                    .fillMaxWidth()
                    .clickable { /* open guide */ },
                shape = RoundedCornerShape(14.dp),
                colors = CardDefaults.cardColors(containerColor = Color(0xFFF0FDF4)),
                border = androidx.compose.foundation.BorderStroke(1.dp, Color(0xFFBBF7D0))
            ) {
                Row(
                    modifier = Modifier.padding(14.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Surface(
                        shape = CircleShape,
                        color = PrimaryGreen.copy(alpha = 0.15f),
                        modifier = Modifier.size(38.dp)
                    ) {
                        Box(contentAlignment = Alignment.Center) {
                            Text("🌱", fontSize = 18.sp)
                        }
                    }
                    Spacer(modifier = Modifier.width(12.dp))
                    Column(modifier = Modifier.weight(1f)) {
                        Text(
                            "ಹವಾಮಾನ ತಿಳಿದು, ಸಮರ್ಥ ಕೃಷಿ ಮಾಡಿ",
                            fontWeight = FontWeight.Bold,
                            fontSize = 13.sp,
                            color = DarkGreen
                        )
                        Text(
                            "ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ, ಉತ್ತಮ ಫಲಿತಾಂಶ ಪಡೆಯಿರಿ.",
                            fontSize = 11.sp,
                            color = Color(0xFF4B5563)
                        )
                    }
                    Icon(
                        Icons.Default.ChevronRight,
                        contentDescription = null,
                        tint = DarkGreen,
                        modifier = Modifier.size(20.dp)
                    )
                }
            }
        }
    }
}

@Composable
fun DayForecastCard(day: DayForecastDto) {
    // Dynamic Gradient based on Rain vs Clear Weather
    val gradientColors = if (day.isRainy) {
        listOf(Color(0xFFF59E0B), Color(0xFFEA580C))
    } else {
        listOf(Color(0xFF22C55E), Color(0xFF15803D))
    }

    Box(
        modifier = Modifier
            .width(68.dp)
            .clip(RoundedCornerShape(16.dp))
            .background(Brush.verticalGradient(gradientColors))
            .padding(vertical = 12.dp, horizontal = 4.dp),
        contentAlignment = Alignment.Center
    ) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.spacedBy(6.dp)
        ) {
            Text(
                day.dayLabel,
                fontSize = 11.sp,
                fontWeight = FontWeight.Bold,
                color = Color.White
            )
            Text(
                day.dateStr,
                fontSize = 9.sp,
                color = Color.White.copy(alpha = 0.85f)
            )

            // Icon
            val iconEmoji = when (day.conditionIcon) {
                "rain" -> "🌧️"
                "thunder" -> "⛈️"
                "heavy_rain" -> "⛈️"
                "partly_cloudy" -> "⛅"
                else -> "☀️"
            }
            Text(iconEmoji, fontSize = 20.sp)

            // Temps
            Text(
                "${day.tempMaxC}°C",
                fontSize = 13.sp,
                fontWeight = FontWeight.Bold,
                color = Color.White
            )
            Text(
                "${day.tempMinC}°C",
                fontSize = 11.sp,
                color = Color.White.copy(alpha = 0.8f)
            )

            // Rain mm
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text("💧", fontSize = 8.sp)
                Text(
                    "${day.rainfallMm} mm",
                    fontSize = 9.sp,
                    color = Color.White.copy(alpha = 0.9f)
                )
            }
        }
    }
}
