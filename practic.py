# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # import plotly.express as px
# # import plotly.graph_objects as go
# # # import joblib  # Uncomment when using your real model

# # # 1. PAGE CONFIGURATION (Must be the first command)
# # st.set_page_config(
# #     page_title="Heart Health AI",
# #     page_icon="❤️",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # 2. CUSTOM CSS FOR "GLASSMORPHISM" LOOK
# # def local_css():
# #     st.markdown("""
# #         <style>
# #         .stApp {
# #             background-color: #0e1117;
# #             background-image: radial-gradient(circle at 50% 0%, #1c093a 0%, #0e1117 60%);
# #         }
# #         /* Style the tabs */
# #         .stTabs [data-baseweb="tab-list"] {
# #             gap: 24px;
# #         }
# #         .stTabs [data-baseweb="tab"] {
# #             height: 50px;
# #             white-space: pre-wrap;
# #             background-color: rgba(255, 255, 255, 0.05);
# #             border-radius: 4px 4px 0px 0px;
# #             gap: 1px;
# #             padding-top: 10px;
# #             padding-bottom: 10px;
# #         }
# #         .stTabs [aria-selected="true"] {
# #             background-color: rgba(0, 123, 255, 0.2);
# #             border-bottom: 2px solid #007bff;
# #         }
# #         /* Cards for metrics */
# #         div[data-testid="metric-container"] {
# #             background-color: rgba(255, 255, 255, 0.05);
# #             border: 1px solid rgba(255, 255, 255, 0.1);
# #             padding: 15px;
# #             border-radius: 10px;
# #             color: white;
# #         }
# #         </style>
# #         """, unsafe_allow_html=True)

# # local_css()

# # # 3. LOAD DATA (Mock data for demo - replace with your real file)
# # @st.cache_data
# # def load_data():
# #     # REPALCE THIS with: df = pd.read_csv("heart_disease.csv")
# #     data = {
# #         "Age": np.random.randint(20, 80, 100),
# #         "Hypertension": np.random.choice([0, 1], 100),
# #         "Diabetes": np.random.choice([0, 1], 100),
# #         "Previous_Heart_Attack": np.random.choice([0, 1], 100),
# #         "Cholesterol_Total": np.random.randint(150, 300, 100),
# #         "Heart_Disease": np.random.choice([0, 1], 100)
# #     }
# #     return pd.DataFrame(data)

# # df = load_data()

# # # 4. LOAD MODEL (Mock model for demo)
# # # model = joblib.load("heart_disease_pred.joblib") # Uncomment this

# # st.title("❤️ Heart Disease Prediction & Analytics")
# # st.markdown("### AI-Powered Health Assessment Dashboard")

# # # --- TABS LAYOUT ---
# # tab1, tab2 = st.tabs(["🔍 Prediction Engine", "📊 Data Insights"])

# # # ================= TAB 1: PREDICTION =================
# # with tab1:
# #     col1, col2 = st.columns([1, 2])
    
# #     with col1:
# #         st.info("Input Patient Details")
        
# #         age = st.number_input("Age", 18, 100, 45)
        
# #         c1, c2 = st.columns(2)
# #         with c1:
# #             hyp = st.selectbox("Hypertension", ["No", "Yes"])
# #         with c2:
# #             dia = st.selectbox("Diabetes", ["No", "Yes"])
            
# #         att = st.selectbox("Previous Heart Attack", ["No", "Yes"])
        
# #         chol = st.slider("Cholesterol (mg/dL)", 100, 600, 200)
        
# #         # Mapping inputs
# #         hyp_val = 1 if hyp == "Yes" else 0
# #         dia_val = 1 if dia == "Yes" else 0
# #         att_val = 1 if att == "Yes" else 0

# #     with col2:
# #         st.write("### Risk Assessment")
        
# #         # Visualize Cholesterol
# #         fig_gauge = go.Figure(go.Indicator(
# #             mode = "gauge+number",
# #             value = chol,
# #             domain = {'x': [0, 1], 'y': [0, 1]},
# #             title = {'text': "Cholesterol Level"},
# #             gauge = {
# #                 'axis': {'range': [100, 600]},
# #                 'bar': {'color': "#007bff"},
# #                 'steps': [
# #                     {'range': [0, 200], 'color': "rgba(0, 255, 0, 0.3)"},
# #                     {'range': [200, 240], 'color': "rgba(255, 255, 0, 0.3)"},
# #                     {'range': [240, 600], 'color': "rgba(255, 0, 0, 0.3)"}],
# #             }
# #         ))
# #         fig_gauge.update_layout(height=250, margin=dict(l=20, r=20, t=30, b=20), paper_bgcolor="rgba(0,0,0,0)")
# #         st.plotly_chart(fig_gauge, use_container_width=True)

# #         if st.button("Analyze Risk Profile", type="primary", use_container_width=True):
# #             input_data = np.array([[age, hyp_val, dia_val, att_val, chol]])
            
# #             # MOCK PREDICTION (Replace with: pred = model.predict(input_data))
# #             # Simulating prediction logic
# #             pred = 1 if (age > 50 and chol > 240) else 0 
            
# #             if pred == 1:
# #                 st.error("⚠️ HIGH RISK DETECTED: Immediate consultation recommended.")
# #             else:
# #                 st.success("✅ LOW RISK: Patient appears healthy.")

# # # ================= TAB 2: INSIGHTS =================
# # with tab2:
# #     st.subheader("Dataset Analytics")
    
# #     # Row 1: Feature Importance & Pie Chart
# #     r1_col1, r1_col2 = st.columns([2, 1])
    
# #     with r1_col1:
# #         # Feature Importance (Plotly Bar)
# #         feature_names = ["Age", "Hypertension", "Diabetes", "Previous Heart Attack", "Cholesterol"]
# #         scores = [0.19, 0.21, 0.19, 0.12, 0.28] # Your scores
        
# #         df_imp = pd.DataFrame({"Feature": feature_names, "Importance": scores})
# #         df_imp = df_imp.sort_values("Importance", ascending=True)
        
# #         fig_bar = px.bar(
# #             df_imp, x="Importance", y="Feature", orientation='h',
# #             title="Feature Importance Scores",
# #             color="Importance", color_continuous_scale='Viridis'
# #         )
# #         fig_bar.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
# #         st.plotly_chart(fig_bar, use_container_width=True)
        
# #     with r1_col2:
# #         # Donut Chart (Modern Pie)
# #         fig_pie = px.pie(
# #             df_imp, values='Importance', names='Feature', 
# #             title='Impact Distribution',
# #             hole=0.4, # Makes it a donut chart
# #             color_discrete_sequence=px.colors.sequential.Viridis
# #         )
# #         fig_pie.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
# #         st.plotly_chart(fig_pie, use_container_width=True)

# #     # Row 2: Correlation Heatmap
# #     st.subheader("Correlation Matrix")
# #     corr = df.corr()
# #     fig_corr = px.imshow(
# #         corr, text_auto=True, aspect="auto",
# #         color_continuous_scale='RdBu_r',
# #         title="Feature Correlations"
# #     )
# #     fig_corr.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
# #     st.plotly_chart(fig_corr, use_container_width=True)






# #     ###############

# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go
# # import joblib  # Uncomment when using your real model

# # 1. PAGE CONFIGURATION (Must be the first command)
# st.set_page_config(
#     page_title="Heart Health AI",
#     page_icon="❤️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # 2. CUSTOM CSS FOR "GLASSMORPHISM" LOOK
# def local_css():
#     st.markdown("""
#         <style>
#         .stApp {
#             background-color: #0e1117;
#             background-image: radial-gradient(circle at 50% 0%, #1c093a 0%, #0e1117 60%);
#         }
#         /* Style the tabs */
#         .stTabs [data-baseweb="tab-list"] {
#             gap: 24px;
#         }
#         .stTabs [data-baseweb="tab"] {
#             height: 50px;
#             white-space: pre-wrap;
#             background-color: rgba(255, 255, 255, 0.05);
#             border-radius: 4px 4px 0px 0px;
#             gap: 1px;
#             padding-top: 10px;
#             padding-bottom: 10px;
#         }
#         .stTabs [aria-selected="true"] {
#             background-color: rgba(0, 123, 255, 0.2);
#             border-bottom: 2px solid #007bff;
#         }
#         /* Cards for metrics */
#         div[data-testid="metric-container"] {
#             background-color: rgba(255, 255, 255, 0.05);
#             border: 1px solid rgba(255, 255, 255, 0.1);
#             padding: 15px;
#             border-radius: 10px;
#             color: white;
#         }
#         /* Custom Result Card */
#         .result-card {
#             background: rgba(255, 255, 255, 0.05);
#             border-radius: 15px;
#             padding: 20px;
#             border: 1px solid rgba(255, 255, 255, 0.1);
#             text-align: center;
#             margin-bottom: 20px;
#         }
#         </style>
#         """, unsafe_allow_html=True)

# local_css()

# # 3. LOAD DATA (Mock data for demo - replace with your real file)
# @st.cache_data
# def load_data():
#     # REPALCE THIS with: df = pd.read_csv("heart_disease.csv")
#     data = {
#         "Age": np.random.randint(20, 80, 100),
#         "Hypertension": np.random.choice([0, 1], 100),
#         "Diabetes": np.random.choice([0, 1], 100),
#         "Previous_Heart_Attack": np.random.choice([0, 1], 100),
#         "Cholesterol_Total": np.random.randint(150, 300, 100),
#         "Heart_Disease": np.random.choice([0, 1], 100)
#     }
#     return pd.DataFrame(data)

# df = load_data()

# # 4. LOAD MODEL (Mock model for demo)
# # model = joblib.load("heart_disease_pred.joblib") # Uncomment this

# st.title("❤️ Heart Disease Prediction & Analytics")
# st.markdown("### AI-Powered Health Assessment Dashboard")

# # --- TABS LAYOUT ---
# tab1, tab2 = st.tabs(["🔍 Prediction Engine", "📊 Data Insights"])

# # ================= TAB 1: PREDICTION =================
# with tab1:
#     # Use columns to separate inputs from visualization
#     col_input, col_viz = st.columns([1, 1.5])
    
#     with col_input:
#         st.markdown("#### 📝 Patient Profile")
#         with st.container():
#             # Demographic Inputs
#             age = st.slider("Age", 18, 100, 45, help="Patient's age in years")
#             chol = st.slider("Cholesterol (mg/dL)", 100, 600, 200, help="Total cholesterol level")
            
#             st.markdown("---")
#             st.markdown("#### 🩺 Medical History")
            
#             # Switch to radio buttons for clearer "Yes/No" selection
#             c1, c2, c3 = st.columns(3)
#             with c1:
#                 hyp = st.radio("Hypertension", ["No", "Yes"], horizontal=True)
#             with c2:
#                 dia = st.radio("Diabetes", ["No", "Yes"], horizontal=True)
#             with c3:
#                 att = st.radio("Prev. Attack", ["No", "Yes"], horizontal=True)
            
#             # Mapping inputs
#             hyp_val = 1 if hyp == "Yes" else 0
#             dia_val = 1 if dia == "Yes" else 0
#             att_val = 1 if att == "Yes" else 0

#         st.markdown("###") # Spacer
#         predict_btn = st.button("🚀 Run AI Diagnosis", type="primary", use_container_width=True)

#     with col_viz:
#         if predict_btn:
#             # MOCK PREDICTION LOGIC (Replace with your actual model)
#             # Generating a "risk score" to make it more visual than just 0/1
#             base_risk = 0.1
#             if age > 50: base_risk += 0.2
#             if chol > 240: base_risk += 0.3
#             if hyp_val: base_risk += 0.15
#             if dia_val: base_risk += 0.15
#             if att_val: base_risk += 0.2
            
#             # Cap risk at 0.99
#             risk_score = min(base_risk, 0.99)
#             risk_percentage = int(risk_score * 100)
            
#             # 1. GAUGE CHART FOR RISK PROBABILITY
#             fig_gauge = go.Figure(go.Indicator(
#                 mode = "gauge+number",
#                 value = risk_percentage,
#                 title = {'text': "Heart Disease Probability (%)"},
#                 gauge = {
#                     'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
#                     'bar': {'color': "#ff2b2b"},
#                     'bgcolor': "rgba(0,0,0,0)",
#                     'borderwidth': 2,
#                     'bordercolor': "#333",
#                     'steps': [
#                         {'range': [0, 30], 'color': "rgba(0, 255, 0, 0.3)"},
#                         {'range': [30, 70], 'color': "rgba(255, 255, 0, 0.3)"},
#                         {'range': [70, 100], 'color': "rgba(255, 0, 0, 0.3)"}],
#                     'threshold': {
#                         'line': {'color': "white", 'width': 4},
#                         'thickness': 0.75,
#                         'value': risk_percentage}
#                 }
#             ))
#             fig_gauge.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "white", 'family': "Arial"}, height=250)
            
#             # 2. RADAR CHART (Patient vs Healthy Baseline)
#             # Normalize values for the radar chart (Scale 0-1)
#             categories = ['Age', 'Cholesterol', 'Hypertension', 'Diabetes', 'Prev Attack']
            
#             # Patient values (normalized loosely for visual)
#             patient_vals = [
#                 age/100, 
#                 chol/600, 
#                 hyp_val, 
#                 dia_val, 
#                 att_val
#             ]
            
#             # "Healthy" Baseline (Approximate safe values)
#             healthy_vals = [0.3, 0.33, 0, 0, 0] # e.g. Age 30, Chol 200, No diseases
            
#             fig_radar = go.Figure()
#             fig_radar.add_trace(go.Scatterpolar(
#                 r=patient_vals,
#                 theta=categories,
#                 fill='toself',
#                 name='Patient Profile',
#                 line_color='#ff2b2b'
#             ))
#             fig_radar.add_trace(go.Scatterpolar(
#                 r=healthy_vals,
#                 theta=categories,
#                 fill='toself',
#                 name='Healthy Baseline',
#                 line_color='#00ff00',
#                 opacity=0.5
#             ))
            
#             fig_radar.update_layout(
#                 polar=dict(
#                     radialaxis=dict(visible=True, range=[0, 1], showticklabels=False),
#                     bgcolor='rgba(255,255,255,0.05)'
#                 ),
#                 paper_bgcolor="rgba(0,0,0,0)",
#                 font=dict(color="white"),
#                 title="Biological Risk Footprint",
#                 height=300,
#                 showlegend=True
#             )

#             # DISPLAY RESULTS
#             c_gauge, c_radar = st.columns(2)
#             with c_gauge:
#                 st.plotly_chart(fig_gauge, use_container_width=True)
#             with c_radar:
#                 st.plotly_chart(fig_radar, use_container_width=True)

#             # FINAL VERDICT CARD
#             if risk_percentage > 50:
#                 st.markdown(f"""
#                 <div class="result-card" style="border-color: #ff4b4b; box-shadow: 0 0 15px rgba(255, 75, 75, 0.5);">
#                     <h2 style="color: #ff4b4b; margin:0;">⚠️ HIGH RISK DETECTED</h2>
#                     <p style="margin:5px 0 0 0;">Probability: {risk_percentage}%</p>
#                     <p style="font-size: 0.9em; opacity: 0.8;">Consult a cardiologist immediately.</p>
#                 </div>
#                 """, unsafe_allow_html=True)
#             else:
#                 st.markdown(f"""
#                 <div class="result-card" style="border-color: #00cc66; box-shadow: 0 0 15px rgba(0, 204, 102, 0.5);">
#                     <h2 style="color: #00cc66; margin:0;">✅ LOW RISK</h2>
#                     <p style="margin:5px 0 0 0;">Probability: {risk_percentage}%</p>
#                     <p style="font-size: 0.9em; opacity: 0.8;">Maintain healthy lifestyle habits.</p>
#                 </div>
#                 """, unsafe_allow_html=True)

#         else:
#             # Placeholder State
#             st.info("👈 Enter patient data and click 'Run AI Diagnosis' to see the risk analysis.")
            
#             # Show a decorative generic radar chart
#             placeholder_radar = go.Figure(go.Scatterpolar(
#                 r=[0.5, 0.5, 0.5, 0.5, 0.5],
#                 theta=['Age', 'Chol', 'Hyp', 'Dia', 'Att'],
#                 fill='toself',
#                 line_color='#333'
#             ))
#             placeholder_radar.update_layout(
#                 polar=dict(radialaxis=dict(visible=False), bgcolor='rgba(255,255,255,0.02)'),
#                 paper_bgcolor="rgba(0,0,0,0)",
#                 font=dict(color="#555"),
#                 height=400,
#                 showlegend=False,
#                 title="Awaiting Input..."
#             )
#             st.plotly_chart(placeholder_radar, use_container_width=True)

# # ================= TAB 2: INSIGHTS =================
# with tab2:
#     st.subheader("Dataset Analytics")
    
#     # Row 1: Feature Importance & Pie Chart
#     r1_col1, r1_col2 = st.columns([2, 1])
    
#     with r1_col1:
#         # Feature Importance (Plotly Bar)
#         feature_names = ["Age", "Hypertension", "Diabetes", "Previous Heart Attack", "Cholesterol"]
#         scores = [0.19, 0.21, 0.19, 0.12, 0.28] # Your scores
        
#         df_imp = pd.DataFrame({"Feature": feature_names, "Importance": scores})
#         df_imp = df_imp.sort_values("Importance", ascending=True)
        
#         fig_bar = px.bar(
#             df_imp, x="Importance", y="Feature", orientation='h',
#             title="Feature Importance Scores",
#             color="Importance", color_continuous_scale='Viridis'
#         )
#         fig_bar.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
#         st.plotly_chart(fig_bar, use_container_width=True)
        
#     with r1_col2:
#         # Donut Chart (Modern Pie)
#         fig_pie = px.pie(
#             df_imp, values='Importance', names='Feature', 
#             title='Impact Distribution',
#             hole=0.4, # Makes it a donut chart
#             color_discrete_sequence=px.colors.sequential.Viridis
#         )
#         fig_pie.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
#         st.plotly_chart(fig_pie, use_container_width=True)

#     # Row 2: Correlation Heatmap
#     st.subheader("Correlation Matrix")
#     corr = df.corr()
#     fig_corr = px.imshow(
#         corr, text_auto=True, aspect="auto",
#         color_continuous_scale='RdBu_r',
#         title="Feature Correlations"
#     )
#     fig_corr.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
#     st.plotly_chart(fig_corr, use_container_width=True)



###############################################



import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
# import joblib  # Uncomment when using your real model

# 1. PAGE CONFIGURATION (Must be the first command)
st.set_page_config(
    page_title="Heart Health AI (Classic)",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CUSTOM CSS FOR SIMPLE, CLASSIC DARK THEME
def local_css():
    st.markdown("""
        <style>
        /* BASE THEME - Charcoal Background */
        .stApp {
            background-color: #20232a; /* Subtle dark charcoal */
            color: #f0f0f0; /* Light text */
            font-family: Arial, sans-serif;
        }

        /* CARD CONTAINERS */
        .card-container {
            background-color: #2c313a; /* Slightly lighter card background */
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            border: 1px solid #3e4451; /* Soft border */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* HEADERS - Simple White */
        h1, h2, h3 {
            color: #ffffff;
            font-weight: 600;
        }

        /* METRIC STYLING */
        div[data-testid="stMetricValue"] {
            font-size: 2.5rem;
            font-weight: 700;
            color: #00bcd4; /* Teal color for key numbers */
        }
        
        /* TABS STYLING */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            border-bottom: 2px solid #3e4451;
        }
        .stTabs [data-baseweb="tab"] {
            color: #aaa;
            background-color: transparent;
        }
        .stTabs [aria-selected="true"] {
            color: #00bcd4; /* Active tab color */
            border-bottom: 2px solid #00bcd4 !important;
            font-weight: 600;
        }
        
        /* Input widgets */
        div[data-baseweb="select"] > div, 
        div[data-baseweb="input"] > div,
        div[class*="stSlider"] {
            background-color: #2c313a !important;
            border-color: #3e4451 !important;
            color: #f0f0f0 !important;
        }

        </style>
        """, unsafe_allow_html=True)

local_css()

# 3. LOAD DATA (Mock data for demo - replace with your real file)
@st.cache_data
def load_data():
    # REPALCE THIS with: df = pd.read_csv("heart_disease.csv")
    data = {
        "Age": np.random.randint(20, 80, 100),
        "Hypertension": np.random.choice([0, 1], 100),
        "Diabetes": np.random.choice([0, 1], 100),
        "Previous_Heart_Attack": np.random.choice([0, 1], 100),
        "Cholesterol_Total": np.random.randint(150, 300, 100),
        "Heart_Disease": np.random.choice([0, 1], 100)
    }
    return pd.DataFrame(data)

df = load_data()

# 4. LOAD MODEL (Mock model for demo)
# model = joblib.load("heart_disease_pred.joblib") # Uncomment this

st.title("📋 Heart Disease Prediction Model")

# --- DATA FOR CHARTS (Used in both tabs) ---
feature_names = ["Age", "Hypertension", "Diabetes", "Previous Heart Attack", "Cholesterol"]
scores = np.array([0.19480143, 0.2149715 , 0.1918075 , 0.11988657, 0.278533 ])
df_imp = pd.DataFrame({"Feature": feature_names, "Importance": scores})
df_imp = df_imp.sort_values("Importance", ascending=True)

# --- TABS LAYOUT ---
tab1, tab2 = st.tabs(["🔍 Prediction Engine", "📊 Data Insights"])

# ================= TAB 1: PREDICTION (Simplified Look) =================
with tab1:
    col_input, col_viz = st.columns([1, 1.5], gap="large")
    
    with col_input:
        st.markdown('<div class="card-container">', unsafe_allow_html=True)
        st.subheader("Patient Profile")
        
        # Demographic Inputs
        age = st.slider("Age", 18, 100, 45, help="Patient's age in years")
        chol = st.slider("Cholesterol (mg/dL)", 100, 600, 200, help="Total cholesterol level")
        
        st.markdown("---")
        st.subheader("Medical History")
        
        # Radio buttons
        c1, c2, c3 = st.columns(3)
        with c1:
            hyp = st.radio("Hypertension", ["No", "Yes"], horizontal=True, index=0)
        with c2:
            dia = st.radio("Diabetes", ["No", "Yes"], horizontal=True, index=0)
        with c3:
            att = st.radio("Prev. Attack", ["No", "Yes"], horizontal=True, index=0)
        
        st.markdown('</div>', unsafe_allow_html=True) # End card container

        # Mapping inputs
        hyp_val = 1 if hyp == "Yes" else 0
        dia_val = 1 if dia == "Yes" else 0
        att_val = 1 if att == "Yes" else 0

        predict_btn = st.button("Run AI Diagnosis", type="primary", use_container_width=True)

    with col_viz:
        st.markdown('<div class="card-container">', unsafe_allow_html=True)
        st.subheader("Risk Assessment Visualization")
        
        if predict_btn:
            # MOCK PREDICTION LOGIC
            base_risk = 0.1
            if age > 50: base_risk += 0.2
            if chol > 240: base_risk += 0.3
            if hyp_val: base_risk += 0.15
            if dia_val: base_risk += 0.15
            if att_val: base_risk += 0.2
            
            risk_score = min(base_risk, 0.99)
            risk_percentage = int(risk_score * 100)
            
            # GAUGE CHART (Teal and Red colors)
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = risk_percentage,
                title = {'text': "Disease Risk Probability (%)", 'font': {'color': 'white'}},
                gauge = {
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
                    'bar': {'color': "#00bcd4"},
                    'bgcolor': "#3e4451",
                    'borderwidth': 0,
                    'steps': [
                        {'range': [0, 30], 'color': "#00ff7f"}, # Green
                        {'range': [30, 70], 'color': "#ffff00"}, # Yellow
                        {'range': [70, 100], 'color': "#ff4d4d"} # Red
                        ]
                }
            ))
            fig_gauge.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"}, height=300)
            st.plotly_chart(fig_gauge, use_container_width=True)

            # FINAL VERDICT
            if risk_percentage > 50:
                st.error(f"⚠️ HIGH RISK DETECTED: Probability {risk_percentage}%. Immediate consultation recommended.")
            else:
                st.success(f"✅ LOW RISK: Probability {risk_percentage}%. Maintain healthy habits.")

        else:
            st.info("Awaiting input to generate risk analysis.")
        
        st.markdown('</div>', unsafe_allow_html=True) # End card container

# ================= TAB 2: INSIGHTS (Matching the Classic Image Look) =================
with tab2:
    st.subheader("Model and Data Insights")
    
    # --- ROW 1: METRICS AND GAUGE (Top three cards in the image) ---
    col_metric_1, col_metric_2, col_metric_3 = st.columns(3)
    
    # 1. Risk Factors Bar Chart (Matches Image Card 1)
    with col_metric_1:
        st.markdown('<div class="card-container" style="height: 250px;">', unsafe_allow_html=True)
        st.markdown("#### Risk Factors")
        
        fig_bar = px.bar(
            df_imp, x="Importance", y="Feature", orientation='h',
            color_discrete_sequence=['#00bcd4'], # Single Teal color
            template="plotly_dark"
        )
        fig_bar.update_layout(
            plot_bgcolor="rgba(0,0,0,0)", 
            paper_bgcolor="rgba(0,0,0,0)", 
            margin=dict(l=0, r=0, t=20, b=0),
            font=dict(color="#f0f0f0"),
            height=180
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 2. LARGE GAUGE (Overall Risk Prediction - Matches Image Card 2: Risk Prediction)
    with col_metric_2:
        st.markdown('<div class="card-container" style="text-align: center; height: 250px;">', unsafe_allow_html=True)
        st.markdown("#### Overall Prediction Score")
        
        # Large Simple Gauge for Overall Risk (Mock Value: 28.39)
        fig_large_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 28.39,
            title = {'text': "Risk Score", 'font': {'color': 'white'}},
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 0, 'visible': False},
                'bar': {'color': "#00bcd4", 'thickness': 1},
                'bgcolor': "#3e4451",
                'borderwidth': 0,
                'steps': [
                    {'range': [0, 30], 'color': "rgba(0, 255, 127, 0.2)"}, 
                    {'range': [30, 70], 'color': "rgba(255, 255, 0, 0.2)"}, 
                    {'range': [70, 100], 'color': "rgba(255, 77, 77, 0.2)"} 
                    ],
                'threshold': {'line': {'color': "white", 'width': 4}, 'thickness': 0.75, 'value': 28.39}
            }
        ))
        fig_large_gauge.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "white", 'size': 24}, height=200, margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig_large_gauge, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    # 3. Metric (Average Risk in Population - Matches Image Card 3: Overall Risk Predication)
    with col_metric_3:
        st.markdown('<div class="card-container" style="text-align: center; padding-top: 50px; height: 250px;">', unsafe_allow_html=True)
        st.metric("Population Risk Average", "32.75")
        st.markdown("<p style='text-align: center; color: #aaa; margin-top: -10px;'>Dataset Mean Score</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # --- ROW 2: COMPLEX CHARTS (Bottom two cards in the image) ---
    col_chart_1, col_chart_2 = st.columns(2)

    # 4. Prediction Probability (Line Chart - Matches Image Card 4)
    with col_chart_1:
        st.markdown('<div class="card-container">', unsafe_allow_html=True)
        st.markdown("#### Prediction Probability Trend")
        
        # Create mock time-series data
        trend_df = pd.DataFrame({
            'Time': np.arange(20),
            'Patient_A': np.sin(np.arange(20) * 0.4) * 15 + 40,
            'Patient_B': np.cos(np.arange(20) * 0.3) * 10 + 30
        })
        
        fig_line = px.line(
            trend_df, x='Time', y=['Patient_A', 'Patient_B'], 
            title='', 
            template="plotly_dark",
            color_discrete_sequence=['#00bcd4', '#ff8c00'] # Teal and Orange for contrast
        )
        
        fig_line.update_layout(
            plot_bgcolor="rgba(0,0,0,0)", 
            paper_bgcolor="rgba(0,0,0,0)", 
            margin=dict(l=40, r=20, t=20, b=40),
            font=dict(color="#f0f0f0"),
            height=300,
            showlegend=False
        )
        st.plotly_chart(fig_line, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 5. Model Feature Risk Contribution (Simple Metric Card - Matches Image Card 5)
    with col_chart_2:
        st.markdown('<div class="card-container" style="text-align: center; padding-top: 50px; height: 350px;">', unsafe_allow_html=True)
        st.metric("F1 Score (Model Health)", "91.8%")
        st.markdown("<p style='text-align: center; color: #aaa; margin-top: -10px;'>Primary performance metric</p>", unsafe_allow_html=True)
        st.markdown('<div style="margin-top: 30px;">', unsafe_allow_html=True)
        st.metric("Validation Accuracy", "94.2%")
        st.markdown("<p style='text-align: center; color: #aaa; margin-top: -10px;'>Data split performance</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


        ################################################################
#         ################################################################

# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder
# import joblib # Used to save the model and encoder

# # --- 1. Simulate DataFrame from User's Data ---
# # We use a simulated dataset structure based on the provided column list
# def create_simulated_data(n_samples=5000):
#     np.random.seed(42)
    
#     data = {}
#     data['Age'] = np.random.randint(30, 80, n_samples)
#     data['Gender'] = np.random.choice(['Male', 'Female'], n_samples)
#     data['Weight'] = np.random.normal(85, 10, n_samples)
#     data['Height'] = np.random.normal(170, 8, n_samples)
#     data['BMI'] = data['Weight'] / ((data['Height'] / 100)**2)
    
#     # Binary/Categorical features
#     data['Smoking'] = np.random.choice(['Never', 'Former', 'Current'], n_samples, p=[0.6, 0.2, 0.2])
#     data['Alcohol_Intake'] = np.random.choice(['Low', 'Moderate', 'High', 'NaN'], n_samples, p=[0.4, 0.3, 0.2, 0.1])
#     data['Physical_Activity'] = np.random.choice(['Sedentary', 'Moderate', 'Active'], n_samples)
#     data['Diet'] = np.random.choice(['Healthy', 'Average', 'Unhealthy'], n_samples)
#     data['Stress_Level'] = np.random.choice(['Low', 'Medium', 'High'], n_samples)
    
#     # Binary (0/1) indicators
#     for col in ['Diabetes', 'Hyperlipidemia', 'Family_History', 'Previous_Heart_Attack', 'Hypertension']:
#         data[col] = np.random.randint(0, 2, n_samples)
        
#     # Continuous Clinical Metrics
#     data['Systolic_BP'] = np.random.normal(140, 15, n_samples)
#     data['Diastolic_BP'] = np.random.normal(90, 10, n_samples)
#     data['Heart_Rate'] = np.random.normal(85, 10, n_samples)
#     data['Blood_Sugar_Fasting'] = np.random.normal(125, 30, n_samples)
#     data['Cholesterol_Total'] = np.random.normal(225, 40, n_samples)

#     # Target variable: Heart_Disease (simulated based on risk factors)
#     risk_score = (data['Cholesterol_Total'] / 250) + (data['Systolic_BP'] / 150) + (data['Age'] / 70)
#     risk_score += data['Hypertension'] * 0.5 + data['Diabetes'] * 0.7
    
#     # Create the binary target (Heart_Disease)
#     data['Heart_Disease'] = (risk_score > np.percentile(risk_score, 50)).astype(int) 

#     return pd.DataFrame(data)

# # --- 2. Preprocessing and Training ---
# def train_heart_disease_model():
#     df = create_simulated_data()
    
#     # Drop columns that are combinations (BMI) or unnecessary for this simple model
#     df = df.drop(columns=['Weight', 'Height', 'BMI'])
    
#     # Handle NaN in Alcohol_Intake (using mode/most frequent for simplicity)
#     df['Alcohol_Intake'].fillna(df['Alcohol_Intake'].mode()[0], inplace=True)

#     # Encode categorical features
#     df_processed = pd.get_dummies(df, drop_first=True)
    
#     # Separate features (X) and target (y)
#     X = df_processed.drop('Heart_Disease', axis=1)
#     y = df_processed['Heart_Disease']
    
#     # Fit a simple Random Forest model
#     model = RandomForestClassifier(n_estimators=100, random_state=42)
#     model.fit(X, y)
    
#     # Save the model and the feature names needed for SHAP/XAI
#     joblib.dump(model, 'rf_model.joblib')
#     joblib.dump(X.columns.tolist(), 'model_features.joblib')
#     print("Model and features saved successfully.")

# # Run training
# train_heart_disease_model()



###################################################################################################################

# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import shap
# import matplotlib.pyplot as plt

# # --- 1. Load Model and Initialize SHAP Explainer (Caching for performance) ---

# @st.cache_resource
# def load_model_components():
#     """Loads the trained model, feature list, and initializes the SHAP explainer."""
#     try:
#         model = joblib.load('rf_model.joblib')
#         model_features = joblib.load('model_features.joblib')
        
#         # NOTE: In a production app, you would load X_train or a background subset here.
#         # Since we use a simulated model, we create a small, temporary background sample.
#         # This part requires the ability to import the create_simulated_data function 
#         # from data_preprocessing.py (which is assumed to be accessible in the environment).
#         # For this self-contained demo, we simulate a simple background DataFrame:
#         # We need a dummy DF with the structure defined in data_preprocessing.py
        
#         dummy_data = {
#             'Age': [50], 'Weight': [80], 'Height': [170], 'BMI': [27.68],
#             'Diabetes': [0], 'Hyperlipidemia': [0], 'Family_History': [0], 
#             'Previous_Heart_Attack': [0], 'Hypertension': [0],
#             'Systolic_BP': [130], 'Diastolic_BP': [80], 'Heart_Rate': [80],
#             'Blood_Sugar_Fasting': [120], 'Cholesterol_Total': [200],
#             # Categorical placeholders (must match the training set's DUMMY columns)
#             'Gender_Male': [1], 'Smoking_Former': [0], 'Smoking_Current': [0], 
#             'Alcohol_Intake_Low': [1], 'Alcohol_Intake_Moderate': [0], 
#             'Alcohol_Intake_NaN': [0], 'Physical_Activity_Moderate': [0],
#             'Physical_Activity_Sedentary': [1], 'Diet_Unhealthy': [0], 
#             'Diet_Healthy': [1], 'Stress_Level_Low': [0], 'Stress_Level_Medium': [1]
#         }
        
#         background_df = pd.DataFrame(dummy_data).reindex(columns=model_features, fill_value=0)
        
#         explainer = shap.TreeExplainer(model, background_df)
        
#         return model, model_features, explainer
#     except Exception as e:
#         st.error(f"Error loading model files. Please ensure data_preprocessing.py has been run. Error: {e}")
#         return None, None, None

# MODEL, MODEL_FEATURES, EXPLAINER = load_model_components()

# # --- 2. XAI / Prediction Function ---

# def run_prediction_and_xai(user_input_dict):
#     """Prepares input, runs prediction, and calculates SHAP contributions."""
#     if not MODEL:
#         return 0, []

#     # 1. Create base DataFrame matching the input structure
#     input_df = pd.DataFrame([user_input_dict])
    
#     # 2. One-Hot Encode Categorical/Text Features
#     categorical_cols = ['Gender', 'Smoking', 'Alcohol_Intake', 'Physical_Activity', 
#                         'Diet', 'Stress_Level']

#     # Drop non-feature columns that were dropped during training
#     input_df = input_df.drop(columns=['Weight', 'Height', 'BMI'], errors='ignore')
    
#     # Apply one-hot encoding
#     X_pred = pd.get_dummies(input_df, drop_first=True)
    
#     # 3. Reindex to match the exact feature order and presence of the trained model
#     X_pred = X_pred.reindex(columns=MODEL_FEATURES, fill_value=0)
    
#     # 4. Run Prediction
#     # Predict probability of Heart Disease (class 1)
#     probability_risk = MODEL.predict_proba(X_pred)[0][1] * 100
    
#     # 5. Get SHAP (XAI) Contributions
#     shap_values = EXPLAINER.shap_values(X_pred)[1] # Get SHAP values for the positive class (1)
    
#     contributions = []
    
#     # Combine feature names with their SHAP values
#     for feature, value in zip(MODEL_FEATURES, shap_values):
#         # Only include features with a notable impact
#         if abs(value) > 0.005: 
#             contributions.append({
#                 'name': feature.replace('_', ' ').replace(' one', '').title(),
#                 'value': value,
#                 'magnitude': abs(value)
#             })

#     # Sort by magnitude (largest impact first)
#     contributions.sort(key=lambda x: x['magnitude'], reverse=True)
    
#     # Scale contributions for visualization (max contribution = 100%)
#     max_abs_shap = max([c['magnitude'] for c in contributions]) if contributions else 1
    
#     xai_results = []
#     for c in contributions:
#         # Scale magnitude to 0-100% for the visualization bar length
#         scaled_value = round((c['magnitude'] / max_abs_shap) * 100) 
        
#         # Determine the sign and simplified name
#         sign = '+' if c['value'] > 0 else '-'
        
#         xai_results.append({
#             'name': c['name'].replace('_', ' '),
#             'value': scaled_value,
#             'sign': sign
#         })
        
#     return round(probability_risk), xai_results[:5] # Return top 5 contributions

# # --- 3. Streamlit UI Components ---

# def display_risk_panel(probability):
#     """Displays the Risk Probability and Bar."""
#     if probability >= 60:
#         color = 'red'
#         risk_text = 'HIGH Risk'
#     elif probability >= 30:
#         color = 'orange'
#         risk_text = 'MODERATE Risk'
#     else:
#         color = 'green'
#         risk_text = 'LOW Risk'

#     st.markdown(f"""
#         <div style="padding: 15px; border-radius: 8px; background-color: #1F1F2B;">
#             <p style="font-size: 14px; color: #AAAAAA; margin-bottom: 5px;">Risk Probability:</p>
#             <p style="font-size: 48px; font-weight: bold; color: {color}; margin: 0;">{probability}%</p>
            
#             <div style="height: 10px; background-color: #333333; border-radius: 5px; margin: 10px 0;">
#                 <div style="height: 100%; width: {probability}%; background-color: {color}; border-radius: 5px;"></div>
#             </div>
#             <p style="font-size: 20px; font-weight: bold; color: {color};">Prediction: {risk_text} of Heart Disease</p>
#         </div>
#     """, unsafe_allow_html=True)


# def display_contribution_panel(contributions):
#     """Displays the Feature Contribution bars (XAI)."""
#     st.markdown("---")
#     st.markdown("### Feature Contribution (XAI)")
    
#     if not contributions:
#         st.info("No significant feature contributions found for this input.")
#         return

#     # Use Matplotlib/Seaborn for the contribution plot for better visual control
#     fig, ax = plt.subplots(figsize=(6, 3))
    
#     # Prepare data for plotting
#     contrib_df = pd.DataFrame(contributions)
    
#     # Separate positive and negative contributions
#     positive_df = contrib_df[contrib_df['sign'] == '+'].sort_values('value', ascending=False)
#     negative_df = contrib_df[contrib_df['sign'] == '-'].sort_values('value', ascending=False)
    
#     # Combine for display order
#     plot_df = pd.concat([positive_df, negative_df])
    
#     # Plot using horizontal bar chart
#     ax.barh(
#         plot_df['name'], 
#         plot_df['value'], 
#         color=[
#             '#38C7A3' if s == '+' else '#FFB300' 
#             for s in plot_df['sign']
#         ],
#         alpha=0.8
#     )

#     # Styling for dark dashboard aesthetic
#     ax.set_facecolor('#1F1F2B')
#     fig.patch.set_facecolor('#1F1F2B')
#     ax.spines['right'].set_visible(False)
#     ax.spines['top'].set_visible(False)
#     ax.spines['left'].set_color('white')
#     ax.spines['bottom'].set_color('white')
#     ax.tick_params(axis='x', colors='white')
#     ax.tick_params(axis='y', colors='white')
#     ax.set_xlabel("Relative Impact (%)", color='white')
#     plt.tight_layout()
#     st.pyplot(fig)

# # --- 4. Main Streamlit App Layout ---

# def main_app():
#     """Defines the Streamlit application layout and logic."""
#     st.set_page_config(layout="wide", page_title="Heart Risk Predictor")

#     # Custom styling for dark mode inputs
#     st.markdown(
#         """
#         <style>
#         .stSlider label { color: #AAAAAA; }
#         .stNumberInput label { color: #AAAAAA; }
#         .stSelectbox label { color: #AAAAAA; }
#         .stButton>button { 
#             background-color: #5C6BC0; 
#             color: white; 
#             font-weight: bold;
#             border-radius: 8px;
#         }
#         .block-container {
#             padding-top: 2rem;
#             padding-bottom: 2rem;
#         }
#         </style>
#         """, 
#         unsafe_allow_html=True
#     )
    
#     st.title("Heart Disease Prediction")
#     st.markdown("Adjust the patient parameters and click 'Predict' to assess risk and feature contribution.")

#     # --- Input Collection Layout ---
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Demographics & Lifestyle")
        
#         # Age
#         age = st.number_input("Age", min_value=18, max_value=100, value=55, step=1)
        
#         # Gender
#         gender = st.selectbox("Gender", options=['Female', 'Male'])
        
#         # Smoking
#         smoking = st.selectbox("Smoking Status", options=['Never', 'Former', 'Current'])
        
#         # Diet
#         diet = st.selectbox("Diet Quality", options=['Healthy', 'Average', 'Unhealthy'])
        
#         # Stress_Level
#         stress = st.selectbox("Stress Level", options=['Low', 'Medium', 'High'])
        
#         # Physical_Activity
#         activity = st.selectbox("Physical Activity", options=['Active', 'Moderate', 'Sedentary'])
        
#         # Alcohol_Intake
#         alcohol = st.selectbox("Alcohol Intake", options=['Low', 'Moderate', 'High', 'NaN'])

#     with col2:
#         st.subheader("Clinical & History")
        
#         # Continuous Metrics
#         cholesterol = st.slider("Cholesterol Total (mg/dL)", min_value=100, max_value=350, value=250)
#         systolic_bp = st.slider("Systolic BP (mmHg)", min_value=90, max_value=180, value=140)
#         diastolic_bp = st.slider("Diastolic BP (mmHg)", min_value=60, max_value=120, value=90)
        
#         # Binary Metrics (using checkboxes for YES/NO)
#         hypertension = st.checkbox("Hypertension", value=True)
#         diabetes = st.checkbox("Diabetes", value=False)
#         prev_heart_attack = st.checkbox("Previous Heart Attack", value=False)
#         hyperlipidemia = st.checkbox("Hyperlipidemia", value=True)
#         family_history = st.checkbox("Family History", value=False)

    
#     # --- Prediction Button ---
#     st.markdown("---")
#     if st.button("Predict Heart Disease Risk", use_container_width=True):
        
#         # Prepare input dictionary (matching model input schema)
#         user_input_dict = {
#             'Age': age,
#             'Gender': gender,
#             'Smoking': smoking,
#             'Alcohol_Intake': alcohol,
#             'Physical_Activity': activity,
#             'Diet': diet,
#             'Stress_Level': stress,
#             'Diabetes': 1 if diabetes else 0,
#             'Hyperlipidemia': 1 if hyperlipidemia else 0,
#             'Family_History': 1 if family_history else 0,
#             'Previous_Heart_Attack': 1 if prev_heart_attack else 0,
#             'Hypertension': 1 if hypertension else 0,
#             'Systolic_BP': systolic_bp,
#             'Diastolic_BP': diastolic_bp,
#             'Heart_Rate': 85.0, # Using default if not provided by user
#             'Blood_Sugar_Fasting': 125.0, # Using default if not provided by user
#             'Cholesterol_Total': cholesterol,
#             'Weight': 85.0,
#             'Height': 170.0,
#             'BMI': 27.68 # Calculated but needed for compatibility, using default
#         }
        
#         # Run prediction and XAI
#         risk_prob, xai_results = run_prediction_and_xai(user_input_dict)
        
#         # --- Display Results ---
#         st.subheader("Prediction Analysis")
#         result_col, xai_col = st.columns([1, 2])
        
#         with result_col:
#             display_risk_panel(risk_prob)

#         with xai_col:
#             display_contribution_panel(xai_results)
#             st.info("Positive contribution (+) means the feature increases risk; negative (-) means it decreases risk.")

# # Check if model is loaded before running the app
# if MODEL:
#     main_app()
# else:
#     st.error("Model files not found. Please run data_preprocessing.py first to train the model and generate the necessary files (rf_model.joblib, model_features.joblib).")