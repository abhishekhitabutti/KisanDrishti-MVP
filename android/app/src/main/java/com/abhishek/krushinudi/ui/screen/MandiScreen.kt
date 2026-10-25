package com.abhishek.krushinudi.ui.screen

import androidx.compose.foundation.background
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
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.abhishek.krushinudi.data.remote.MandiPriceDto
import com.abhishek.krushinudi.ui.theme.*
import com.abhishek.krushinudi.viewmodel.MandiUiState
import com.abhishek.krushinudi.viewmodel.MandiViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun MandiScreen(
    viewModel: MandiViewModel,
    onBack: () -> Unit
) {
    val uiState by viewModel.uiState.collectAsState()
    val selectedDistrict by viewModel.selectedDistrict.collectAsState()
    val searchQuery by viewModel.searchQuery.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Column {
                        Text("💰 ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು {Mandi Prices}", fontWeight = FontWeight.Bold)
                        Text("ಕರ್ನಾಟಕ ಎಪಿಎಂಸಿ ದೈನಂದಿನ ದರಗಳು (₹/ಕ್ವಿಂಟಾಲ್)", style = MaterialTheme.typography.labelSmall)
                    }
                },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back", tint = Color.White)
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = Color(0xFFD97706),
                    titleContentColor = Color.White,
                    navigationIconContentColor = Color.White
                )
            )
        }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .background(Color(0xFFF9FAFB))
        ) {
            // District Filter Chips Row
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(Color.White)
                    .padding(horizontal = 16.dp, vertical = 10.dp)
                    .horizontalScroll(rememberScrollState()),
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                viewModel.districts.forEach { dist ->
                    val isSelected = (dist == selectedDistrict)
                    FilterChip(
                        selected = isSelected,
                        onClick = { viewModel.selectDistrict(dist) },
                        label = { Text(dist, fontSize = 12.sp) },
                        colors = FilterChipDefaults.filterChipColors(
                            selectedContainerColor = Color(0xFFFEF3C7),
                            selectedLabelColor = Color(0xFFB45309)
                        )
                    )
                }
            }

            // Search Bar
            OutlinedTextField(
                value = searchQuery,
                onValueChange = { viewModel.searchCrop(it) },
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 16.dp, vertical = 8.dp),
                placeholder = { Text("ಬೆಳೆ ಹುಡುಕಿ (ಉದಾ: ಹತ್ತಿ, ಸೋಯಾಬೀನ್)...", fontSize = 13.sp) },
                leadingIcon = { Icon(Icons.Default.Search, contentDescription = null, tint = Color.Gray) },
                trailingIcon = {
                    if (searchQuery.isNotEmpty()) {
                        IconButton(onClick = { viewModel.searchCrop("") }) {
                            Icon(Icons.Default.Close, contentDescription = "Clear")
                        }
                    }
                },
                shape = RoundedCornerShape(12.dp),
                colors = OutlinedTextFieldDefaults.colors(
                    focusedBorderColor = Color(0xFFD97706),
                    unfocusedContainerColor = Color.White,
                    focusedContainerColor = Color.White
                ),
                singleLine = true
            )

            // Content Area
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(horizontal = 16.dp)
            ) {
                when (val state = uiState) {
                    is MandiUiState.Loading -> {
                        CircularProgressIndicator(
                            modifier = Modifier.align(Alignment.Center),
                            color = Color(0xFFD97706)
                        )
                    }
                    is MandiUiState.Error -> {
                        Column(
                            modifier = Modifier.align(Alignment.Center),
                            horizontalAlignment = Alignment.CenterHorizontally
                        ) {
                            Text(state.message, color = ErrorRed)
                            Spacer(modifier = Modifier.height(8.dp))
                            Button(onClick = { viewModel.loadPrices(selectedDistrict) }) {
                                Text("Retry")
                            }
                        }
                    }
                    is MandiUiState.Success -> {
                        if (state.prices.isEmpty()) {
                            Text(
                                "ಯಾವುದೇ ದರ ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ",
                                modifier = Modifier.align(Alignment.Center),
                                color = Color.Gray
                            )
                        } else {
                            LazyColumn(
                                verticalArrangement = Arrangement.spacedBy(12.dp),
                                contentPadding = PaddingValues(bottom = 24.dp, top = 4.dp)
                            ) {
                                items(state.prices) { price ->
                                    MandiPriceCard(price)
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

@Composable
fun MandiPriceCard(price: MandiPriceDto) {
    Card(
        modifier = Modifier.fillMaxWidth(),
        shape = RoundedCornerShape(14.dp),
        colors = CardDefaults.cardColors(containerColor = Color.White),
        elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            // Header Row: Crop Name & Trend Badge
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Column {
                    Text(
                        price.cropKn,
                        fontWeight = FontWeight.Bold,
                        fontSize = 17.sp,
                        color = Color(0xFF1F2937)
                    )
                    Text(
                        "ತಳಿ: ${price.variety} • ${price.market}",
                        fontSize = 12.sp,
                        color = Color(0xFF6B7280)
                    )
                }

                // Trend Badge
                val (trendText, trendColor, trendBg) = when (price.trend) {
                    "up" -> Triple("⬆️ ಏರಿಕೆ", Color(0xFF16A34A), Color(0xFFDCFCE7))
                    "down" -> Triple("⬇️ ಇಳಿಕೆ", Color(0xFFDC2626), Color(0xFFFEE2E2))
                    else -> Triple("➡️ ಸ್ಥಿರ", Color(0xFFD97706), Color(0xFFFEF3C7))
                }

                Surface(
                    shape = RoundedCornerShape(8.dp),
                    color = trendBg
                ) {
                    Text(
                        trendText,
                        fontSize = 11.sp,
                        fontWeight = FontWeight.Bold,
                        color = trendColor,
                        modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                    )
                }
            }

            Spacer(modifier = Modifier.height(14.dp))

            // Price Columns: Min | Modal (Average) | Max
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(Color(0xFFF9FAFB), RoundedCornerShape(10.dp))
                    .padding(vertical = 10.dp, horizontal = 12.dp),
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text("ಕನಿಷ್ಠ {Min}", fontSize = 11.sp, color = Color.Gray)
                    Text("₹${price.minPrice.toInt()}", fontWeight = FontWeight.SemiBold, fontSize = 14.sp)
                }

                Divider(
                    modifier = Modifier
                        .height(30.dp)
                        .width(1.dp),
                    color = Color.LightGray
                )

                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text("ಮಧ್ಯಮ {Modal}", fontSize = 11.sp, color = DarkGreen, fontWeight = FontWeight.Bold)
                    Text("₹${price.modalPrice.toInt()}", fontWeight = FontWeight.ExtraBold, fontSize = 17.sp, color = DarkGreen)
                }

                Divider(
                    modifier = Modifier
                        .height(30.dp)
                        .width(1.dp),
                    color = Color.LightGray
                )

                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text("ಗರಿಷ್ಠ {Max}", fontSize = 11.sp, color = Color.Gray)
                    Text("₹${price.maxPrice.toInt()}", fontWeight = FontWeight.SemiBold, fontSize = 14.sp)
                }
            }
        }
    }
}

