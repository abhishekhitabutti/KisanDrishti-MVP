-- ==============================================================================
-- KrushiNudi PostgreSQL Database Schema
-- Author: Abhishek Hitabutti
-- Copyright: © 2026 Abhishek Hitabutti. All rights reserved.
-- ==============================================================================

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Farmers Profile Table
CREATE TABLE IF NOT EXISTS farmers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name VARCHAR(120) NOT NULL,
    phone_number VARCHAR(15) UNIQUE,
    preferred_language VARCHAR(5) DEFAULT 'kn',
    district VARCHAR(60) NOT NULL DEFAULT 'Belagavi',
    taluk VARCHAR(60),
    hobli VARCHAR(60),
    village VARCHAR(100),
    survey_no VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Crop Doctor Analyses History Table
CREATE TABLE IF NOT EXISTS crop_analyses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    farmer_id UUID REFERENCES farmers(id) ON DELETE SET NULL,
    crop_name VARCHAR(60) NOT NULL,
    issue_category VARCHAR(30) NOT NULL, -- pest, disease, weed, deficiency
    diagnosis_name_kn VARCHAR(150) NOT NULL,
    diagnosis_name_en VARCHAR(150),
    confidence_level VARCHAR(20) NOT NULL,
    image_url TEXT,
    symptoms_seen JSONB DEFAULT '[]'::jsonb,
    could_also_be JSONB DEFAULT '[]'::jsonb,
    first_do_this JSONB DEFAULT '[]'::jsonb,
    chemical_options JSONB DEFAULT '[]'::jsonb,
    latitude DECIMAL(10, 6),
    longitude DECIMAL(10, 6),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Borewell Feasibility Advisories Table
CREATE TABLE IF NOT EXISTS borewell_advisories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    farmer_id UUID REFERENCES farmers(id) ON DELETE SET NULL,
    district VARCHAR(60) NOT NULL,
    taluk VARCHAR(60) NOT NULL,
    hobli VARCHAR(60) NOT NULL,
    village VARCHAR(100) NOT NULL,
    survey_no VARCHAR(50),
    plot_acres DECIMAL(6, 2) NOT NULL DEFAULT 2.0,
    topography VARCHAR(30) NOT NULL DEFAULT 'plain',
    soil_type VARCHAR(30) NOT NULL DEFAULT 'red',
    user_latitude DECIMAL(10, 6) NOT NULL,
    user_longitude DECIMAL(10, 6) NOT NULL,
    success_assurance_pct INT NOT NULL,
    recommended_min_depth_ft INT NOT NULL,
    recommended_max_depth_ft INT NOT NULL,
    estimated_yield_inches VARCHAR(20) NOT NULL,
    cgwb_status VARCHAR(60) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. Borewell Exact Prospective Points Table
CREATE TABLE IF NOT EXISTS borewell_points (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    advisory_id UUID NOT NULL REFERENCES borewell_advisories(id) ON DELETE CASCADE,
    point_number INT NOT NULL, -- 1 = Primary, 2 = Secondary, 3 = High Risk Avoid
    point_name_kn VARCHAR(100) NOT NULL,
    point_name_en VARCHAR(100) NOT NULL,
    grade VARCHAR(5) NOT NULL, -- A+, A, D
    latitude DECIMAL(10, 6) NOT NULL,
    longitude DECIMAL(10, 6) NOT NULL,
    distance_meters INT NOT NULL,
    direction_kn VARCHAR(50) NOT NULL,
    direction_en VARCHAR(50) NOT NULL,
    strike_depth_ft VARCHAR(50) NOT NULL,
    yield_force VARCHAR(50) NOT NULL,
    field_marking_guide TEXT NOT NULL,
    hydrogeology_reason TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. Mandi Market Prices Table
CREATE TABLE IF NOT EXISTS mandi_prices (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    district VARCHAR(60) NOT NULL,
    market_center VARCHAR(100) NOT NULL,
    crop_name VARCHAR(60) NOT NULL,
    variety VARCHAR(60),
    min_price_quintal DECIMAL(10, 2) NOT NULL,
    modal_price_quintal DECIMAL(10, 2) NOT NULL,
    max_price_quintal DECIMAL(10, 2) NOT NULL,
    price_date DATE NOT NULL DEFAULT CURRENT_DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for lightning fast queries
CREATE INDEX IF NOT EXISTS idx_crop_analyses_farmer ON crop_analyses(farmer_id);
CREATE INDEX IF NOT EXISTS idx_borewell_advisories_farmer ON borewell_advisories(farmer_id);
CREATE INDEX IF NOT EXISTS idx_borewell_points_advisory ON borewell_points(advisory_id);
CREATE INDEX IF NOT EXISTS idx_mandi_prices_district_crop ON mandi_prices(district, crop_name);

