import streamlit as st
import pickle
import numpy as np

# Page Layout Configuration
st.set_page_config(page_title="KisanDrishti Portal", page_icon="🌾", layout="wide")

st.title("🌾 KisanDrishti AI Advisory Platform")
st.markdown("### Production-Grade Precision Agriculture Engine")
st.write("Adjust the environmental attributes below to generate machine learning crop recommendations.")

# Safe Artifact Parsing
with open("crop_recommendation_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("crop_profiles.pkl", "rb") as f:
    crop_profiles = pickle.load(f)

# Sidebar UI Controls
st.sidebar.header("📊 Soil & Weather Attributes")
n = st.sidebar.slider("Nitrogen (N) Content", 0, 150, 40)
p = st.sidebar.slider("Phosphorus (P) Content", 0, 150, 40)
k = st.sidebar.slider("Potassium (K) Content", 0, 150, 40)
temp = st.sidebar.slider("Temperature in Celsius", 10.0, 50.0, 25.0)
humidity = st.sidebar.slider("Relative Humidity Percentage", 10.0, 100.0, 60.0)
ph = st.sidebar.slider("Soil pH Level", 3.5,9.0, 6.5)
rainfall = st.sidebar.slider("Rainfall Index in mm", 20.0, 300.0, 100.0)

# Process Model Inference
if st.button("Generate Precision Advisory", type="primary"):
    input_features = np.array([[n, p, k, temp, humidity, ph, rainfall]])
    prediction = model.predict(input_features)[0]
    
    st.success(f"### Optimized Target Crop: {prediction.upper()}")
    st.markdown("---")
    st.markdown("### 🧪 Real-Time Nutrient Gap Analysis")
    
    # Flattened Logic - No extra nested blocks to mess upindentations
    profile = crop_profiles.get(prediction, {'N': 40, 'P': 40, 'K': 40})
    
    ideal_n = profile['N']
    ideal_p = profile['P']
    ideal_k = profile['K']
    
    diff_n = ideal_n - n
    diff_p = ideal_p - p
    diff_k = ideal_k - k
    
    # Professional Metric Columns Layout
    m1, m2, m3 = st.columns(3)
    
    with m1:
        st.metric(label='Nitrogen (N)', value=f'{n} mg/kg', delta=f'{diff_n:.1f} mg/kg required' if diff_n > 0 else f'{abs(diff_n):.1f} mg/kg surplus', delta_color='inverse' if diff_n > 0 else 'normal')
            
    with m2:
        st.metric(label='Phosphorus (P)', value=f'{p} mg/kg', delta=f'{diff_p:.1f} mg/kg required' if diff_p > 0 else f'{abs(diff_p):.1f} mg/kg surplus', delta_color='inverse' if diff_p > 0 else 'normal')
            
    with m3:
        st.metric(label='Potassium ()', value=f'{k} mg/kg', delta=f'{diff_k:.1f} mg/kg required' if diff_k > 0 else f'{abs(diff_k):.1f} mg/kg surplus', delta_color='inverse' if diff_k > 0 else 'normal')

           
    st.markdown("---")
    st.info("💡 **Agronomic Advisory Note:** Modify your fertilizer applications to match the target soil conditions outlined above.")
