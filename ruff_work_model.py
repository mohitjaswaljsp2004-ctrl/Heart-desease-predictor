# import numpy as np
# import pandas as pd
# import streamlit as st
# import joblib

# # Load model (make sure 'heart_disease_pred.joblib' is loaded correctly)
# # df = joblib.load("heart_disease_pred.joblib") # Re-include this line in your full script

# st.title("Heart Disease Predectiom")

# # 1. Define the main columns for the layout
# # [2, 1] means the input column is 2/3 of the width, and the results column is 1/3
# col_inputs, col_results = st.columns([2, 1])

# # --- INPUTS SECTION ---
# # All your input widgets go into the first column
# with col_inputs:
    
#     # Use nested columns for Age/Diabetes and Hypertension/HeartAttack
#     input_row1_col1, input_row1_col2 = st.columns(2)

#     with input_row1_col1:
#         # Assuming Age is defined here
#         Age = st.number_input("Age", min_value=18, max_value=100, value=22, key="age_input") 
        
#     with input_row1_col2:
#         # Assuming diabetes_value is defined here
#         options_dia = {"NO": 0, "YES": 1}
#         dia_label = st.selectbox("Diabetes", list(options_dia.keys()), key="dia_select", index=1) # index=1 for YES
#         diabetes_value = options_dia[dia_label]

#     input_row2_col1, input_row2_col2 = st.columns(2)

#     with input_row2_col1:
#         # Assuming hypertension_value is defined here
#         options_hyp = {"NO": 0, "YES": 1}
#         hyp_label = st.selectbox("Hypertension", list(options_hyp.keys()), key="hyp_select")
#         hypertension_value = options_hyp[hyp_label]

#     with input_row2_col2:
#         # Assuming heart_attack_value is defined here
#         options_att = {"NO": 0, "YES": 1}
#         att_label = st.selectbox("Previous_Heart_Attack", list(options_att.keys()), key="att_select", index=1) # index=1 for YES
#         heart_attack_value = options_att[att_label]


#     # Cholesterol slider across the width of the input column
#     Cholesterol = st.slider("Cholesterol (mg/dL)", min_value=100, max_value=600, value=122, key="chol_slider")

#     # The Predict button goes below the inputs
#     predict_button = st.button("Predict", key="heart_disease_predict")


# # --- RESULTS SECTION ---
# # The prediction output and all related logic go into the second column
# with col_results:
    
#     # Initialize variables for demonstration if they aren't available globally
#     # In a real app, these values are only calculated if the button is clicked
#     risk_percentage = 0 
#     prediction = [0] 
    
#     # Check if the button was clicked
#     if predict_button:
        
#         # NOTE: You MUST include the actual calculation logic here.
#         # This is a placeholder section. Replace with your actual prediction logic.
#         # --- START OF PREDICTION LOGIC ---
#         try:
#             # Placeholder/Mock data for demonstration since the rest of the script is missing
#             input_data = np.array([[Age, hypertension_value, diabetes_value, heart_attack_value, Cholesterol]])
            
#             # Use mock values if df is not loaded, otherwise use df.predict_proba
#             # Assuming you have the df loaded correctly:
#             prediction_proba = df.predict_proba(input_data)
#             risk_probability = prediction_proba[0][1]
#             risk_percentage = int(round(risk_probability * 100))
#             prediction = df.predict(input_data)
            
#         except NameError:
#              # This error would occur if df is not loaded
#             st.error("Model 'df' not found. Please ensure joblib.load('heart_disease_pred.joblib') is working.")
#             risk_percentage = 68 # Mock value for display
#             prediction = [1]
#         # --- END OF PREDICTION LOGIC ---

        
#         ## 2. Display the Styled Prediction Result (Your HTML/CSS block)
#         st.markdown(
#             f"""
#             <style>
#                 .prediction-container {{
#                     background-color: #1e1e1e; /* Dark background matching the image */
#                     padding: 20px;
#                     border-radius: 10px;
#                     margin-top: 0px; /* Aligned to the top of the column */
#                 }}
#                 /* ... (Rest of your CSS classes: prediction-title, risk-probability-text, etc.) ... */
#                 .prediction-title {{
#                     color: #e0e0e0; 
#                     font-size: 18px; 
#                     margin-bottom: 10px; 
#                 }}
#                 .risk-probability-text {{
#                     color: #ff5733; 
#                     font-size: 68px;
#                     font-weight: bold;
#                     line-height: 1;
#                 }}
#                 .progress-bar-container {{
#                     width: 100%;
#                     height: 10px;
#                     background-color: #383838;
#                     border-radius: 5px;
#                     margin-top: 15px;
#                 }}
#                 .progress-bar-fill {{
#                     height: 100%;
#                     width: {risk_percentage}%; 
#                     background-color: #ff5733;
#                     border-radius: 5px;
#                 }}
#             </style>
            
#             <div class="prediction-container">
#                 <div class="prediction-title">Prediction Result</div>
#                 <div class="prediction-title">Risk Probability:</div>
#                 <div class="risk-probability-text">{risk_percentage}%</div>
#                 <div class="progress-bar-container">
#                     <div class="progress-bar-fill"></div>
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         ## 3. Display the simple text outcome below the styled result
#         st.write("") 
#         if prediction[0] == 1:
#             st.error(" High Risk of Heart Disease")
#         else:
#             st.success(" Low Risk / Healthy")

# # --- End of main script ---



###########################################################################
########################### FEATURE CONTRIBUTION #########################
###### Prediction Logic ---
# ????????????????????????????????????????????????????????????????????????????????????
# import shap
# import altair as alt

# # --- Configuration and Initialization ---
# # Load model (make sure 'heart_disease_pred.joblib' is in the same directory)
# # try:
# #     df = joblib.load("heart_disease_pred.joblib")
# #     # A placeholder/example dataset for SHAP to estimate background distribution
# #     # IMPORTANT: For accurate SHAP, replace this with a small, representative sample 
# #     # of your actual training data X.
# #     # We will use a dummy one here for execution, assuming 5 features.
# #     example_data = np.array([[30, 0, 0, 0, 200], [50, 1, 0, 1, 250], [60, 0, 1, 0, 180]])
# #     feature_names_global = ['Age', 'Hypertension', 'Diabetes', 'Previous_Heart_Attack', 'Cholesterol']
# #     example_df = pd.DataFrame(example_data, columns=feature_names_global)
    
# # except FileNotFoundError:
# #     st.error("Error: Model file 'heart_disease_pred.joblib' not found. Please ensure it is in the correct path.")
# #     st.stop()
# # except Exception as e:
# #     st.error(f"Error loading model or initializing SHAP data: {e}")
# #     st.stop()


# # st.title("Heart Disease Overview")

# # Use columns for the main input area and the results area
# main_col, result_col = st.columns([1.5, 1])

# with main_col:
#     st.markdown("### Average Values of Key Indicators")
    
#     # --- Input Widgets ---
#     input_col1, input_col2 = st.columns(2)

#     with input_col1:
#         Age = st.number_input("Age", min_value=18, max_value=100, value=30, key="age_input")
#         st.write("")
#         options_hyp = {"NO": 0, "YES": 1}
#         hyp_label = st.selectbox("Hypertension", list(options_hyp.keys()), key="hyp_select")
#         hypertension_value = options_hyp[hyp_label]

#     with input_col2:
#         options_dia = {"NO": 0, "YES": 1}
#         dia_label = st.selectbox("Diabetes", list(options_dia.keys()), key="dia_select")
#         diabetes_value = options_dia[dia_label]
#         st.write("") 
#         options_att = {"NO": 0, "YES": 1}
#         att_label = st.selectbox("Previous_Heart_Attack", list(options_att.keys()), key="att_select")
#         heart_attack_value = options_att[att_label]

#     # Cholesterol Slider takes up full width in the main column
#     Cholesterol = st.slider("Cholesterol (mg/dL)", min_value=100, max_value=600, value=200, key="chol_slider")

#     # Single Predict Button
#     st.write("")
#     predict_button = st.button("Predict", key="heart_disease_predict")


# # --- Prediction Logic and Results Display ---
# with result_col:
#     # This empty markdown acts as a placeholder or initial empty space
#     # until the button is clicked.
#     if not predict_button:
#         st.markdown(
#             """
#             <div style='background-color: #1e1e1e; padding: 20px; border-radius: 10px; margin-top: 30px; height: 100%;'>
#                 <p style='color: #666666; text-align: center; margin-top: 50px;'>Results will appear here after prediction.</p>
#             </div>
#             """, 
#             unsafe_allow_html=True
#         )

#     # --- RESULTS: Run this block ONLY after the button is clicked ---
#     if predict_button:
        
#         # 1. Prepare Input Data
#         input_data_array = np.array([[Age, hypertension_value, diabetes_value, heart_attack_value, Cholesterol]])
#         input_data_df = pd.DataFrame(input_data_array, columns=feature_names)@@@@@@@@@@@@@@@@@@@@@@eatu

#         # 2. Get Probability and Outcome
#         prediction_proba = df.predict_proba(input_data_array)
#         risk_probability = prediction_proba[0][1]
#         risk_percentage = int(round(risk_probability * 100))
#         prediction = df.predict(input_data_array)
        
#         # ----------------------------------------------------
#         # | PART 1: Prediction Result (Risk Probability)       |
#         # ----------------------------------------------------
#         st.markdown("### Prediction Result")
        
#         # --- Custom Styled Risk Percentage (HTML/CSS) ---
#         # Using the custom HTML/CSS from the previous example for a perfect match
#         st.markdown(
#             f"""
#             <style>
#                 .prediction-container {{
#                     background-color: #1e1e1e;
#                     padding: 20px 20px 10px 20px; /* Reduced bottom padding */
#                     border-radius: 10px;
#                     margin-top: -15px; /* Pull it up a bit to align with heading */
#                 }}
#                 .prediction-title {{
#                     color: #e0e0e0;
#                     font-size: 18px;
#                     margin-bottom: 10px;
#                 }}
#                 .risk-probability-text {{
#                     color: #ff5733; /* Red/Orange for risk */
#                     font-size: 68px;
#                     font-weight: bold;
#                     line-height: 1;
#                 }}
#                 .progress-bar-container {{
#                     width: 100%;
#                     height: 10px;
#                     background-color: #383838;
#                     border-radius: 5px;
#                     margin-top: 15px;
#                     margin-bottom: 15px;
#                 }}
#                 .progress-bar-fill {{
#                     height: 100%;
#                     width: {risk_percentage}%;
#                     background-color: #ff5733;
#                     border-radius: 5px;
#                 }}
#             </style>
            
#             <div class="prediction-container">
#                 <div class="prediction-title">Risk Probability:</div>
#                 <div class="risk-probability-text">{risk_percentage}%</div>
#                 <div class="progress-bar-container">
#                     <div class="progress-bar-fill"></div>
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
        
#         # Optional: Display the text outcome below
#         if prediction[0] == 1:
#             st.error("Text Outcome: High Risk of Heart Disease")
#         else:
#             st.success("Text Outcome: Low Risk / Healthy")
        
#         st.markdown("---") # Separator
        
#         # ----------------------------------------------------
#         # | PART 2: Feature Contribution Chart (SHAP/Altair) |
#         # ----------------------------------------------------
#         st.markdown("### Feature Contribution")
        
#         try:
#             # 3. SHAP Explanation
#             # Using KernelExplainer is generally safer if the model type is unknown, 
#             # but requires a background dataset. TreeExplainer is faster if applicable.
#             explainer = shap.TreeExplainer(df, data=example_df)
#             shap_values = explainer.shap_values(input_data_df)
            
#             if isinstance(shap_values, list):
#                 shap_values_to_plot = shap_values[1][0] # Class 1 (High Risk)
#             else:
#                 shap_values_to_plot = shap_values[0]

#             # 4. Create DataFrame for Chart
#             contribution_df = pd.DataFrame({
#                 'Feature': feature_names_global,
#                 'Contribution': shap_values_to_plot,
#                 'Abs_Contribution': np.abs(shap_values_to_plot)
#             })
            
#             # Sort by absolute contribution for the bar chart order
#             contribution_df = contribution_df.sort_values(by='Abs_Contribution', ascending=False)
            
#             # Calculate the percentage contribution (simplistic, for display)
#             total_abs = contribution_df['Abs_Contribution'].sum()
#             contribution_df['Percentage'] = (contribution_df['Abs_Contribution'] / total_abs) * 100
#             contribution_df['Label'] = contribution_df.apply(
#                 lambda row: f"{'+' if row['Contribution'] > 0 else '-'}{row['Percentage']:.0f}%", 
#                 axis=1
#             )
            
#             # Color assignment for Altair
#             # Red for positive contribution (increase risk), Green for negative (decrease risk)
#             contribution_df['Color'] = np.where(contribution_df['Contribution'] > 0, '#ff5733', '#4CAF50')

#             # 5. Altair Chart Generation
#             chart = alt.Chart(contribution_df).mark_bar().encode(
#                 y=alt.Y('Feature:N', sort=alt.EncodingSortField(field="Abs_Contribution", op="average", order='descending'), title=None),
#                 x=alt.X('Contribution:Q', title=None, axis=None), # Hide axis for cleaner look
#                 color=alt.Color('Color', scale=None),
#                 tooltip=['Feature', alt.Tooltip('Contribution', format='.2f')]
#             ).properties(
#                 title=alt.TitleParams("Higher values increase risk", anchor='start', fontSize=12, color='#e0e0e0')
#             ).interactive()

#             # Add text labels on the bars
#             text = chart.mark_text(align='left', baseline='middle', dx=5, color='white').encode(
#                 text=alt.Text('Label:N'),
#                 x=alt.X('Contribution:Q'),
#             )

#             # Combine bar and text
#             final_chart = (chart + text).configure_view(
#                 strokeWidth=0
#             ).configure_axis(
#                 grid=False
#             )

#             st.altair_chart(final_chart, use_container_width=True)

#         except Exception as e:
#             st.warning(f"Could not generate Feature Contribution chart. Ensure your model supports SHAP TreeExplainer or try KernelExplainer. Error: {e}")

# # --- Background Styling (from your original code) ---
# def add_bg_from_url():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             /* 1. The Main Dark Color */
#             background-color: #121212;
#         }
        
#         /* Optional: Fix text inputs to match the glass look */
#         .stTextInput > div > div, .stTextArea > div > div, .stSelectbox > div, .stSlider > div {{
#             background-color: rgba(255, 255, 255, 0.05) !important;
#             color: #e9ecef !important;
#             border: 1px solid rgba(255, 255, 255, 0.1) !important;
#             border-radius: 5px;
#         }}
        
#         .stMarkdown h3 {{
#             color: #e0e0e0;
#             font-size: 20px;
#             margin-bottom: 20px;
#         }}
        
#         /* Style the main result column background to match the image's card style */
#         .st-emotion-cache-1cpxqw2 {{ 
#              /* This targets the column div directly, adjust selector if needed for exact match */
#             background-color: #1e1e1e;
#             padding: 20px;
#             border-radius: 10px;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# add_bg_from_url()
# ????????????????????????????????????????????????????????????????????????????
###############################################################################################
#########################################

# st.markdown(
#     """
#     <style>
#     [data-testid="stAppViewContainer"] {
#         background-image: url("https://img.freepik.com/premium-photo/black-wall-texture-background-dark-concrete-floor_322958-4234.jpg"); /* Replace with actual base64 */
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title("Custom Background Image")
# st.write("Your Streamlit app now has a custom background.")

# background-image: url("https://w.wallhaven.cc/full/zy/wallhaven-zy27zo.png"); /* Replace with actual base64 */
#########################################

# def add_bg_from_url():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             /* 1. The Main Dark Color */
#             background-color: #0a0e17;
            
#             /* 2. The Two Glowing Gradients (Blue & Purple) to match your screenshot */
#             background-image: 
#                 radial-gradient(circle at 20% 30%, rgba(0, 123, 255, 0.15) 0%, transparent 50%),
#                 radial-gradient(circle at 80% 70%, rgba(102, 16, 242, 0.15) 0%, transparent 50%);
            
#             /* 3. Blending them together */
#             background-blend-mode: screen;
#             background-attachment: fixed;
#             background-size: cover;
#             color: #e9ecef;
#         }
        
#         /* Optional: This fixes the text inputs to match the glass look in your screenshot */
#         .stTextInput > div > div, .stTextArea > div > div {
#             background-color: rgba(255, 255, 255, 0.05) !important;
#             color: #e9ecef !important;
#             border: 1px solid rgba(255, 255, 255, 0.1) !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# add_bg_from_url()












# if st.button("Predict"):

#     input_data = np.array([[Age, hypertension_value, diabetes_value, heart_attack_value, Cholesterol]])
    
#     prediction_proba = df.predict_proba(input_data)
    
#     risk_probability = prediction_proba[0][1]
    
#     risk_percentage = int(round(risk_probability * 100))
    
#     prediction = df.predict(input_data)

    
#     # The custom HTML/CSS block is used to replicate the dark background,
#     # large red percentage text, and the styled progress bar from your image.
#     st.markdown(
#         f"""
#         <style>
#             .prediction-container {{
#                 background-color: #1e1e1e; /* Dark background matching the image */
#                 padding: 20px;
#                 border-radius: 10px;
#                 margin-top: 30px;
#             }}
#             .prediction-title {{
#                 color: #e0e0e0;
#                 font-size: 18px;
#                 margin-bottom: 10px;
#             }}
#             .risk-probability-text {{
#                 color: #ff5733; /* A bright red/orange color for the percentage */
#                 font-size: 68px;
#                 font-weight: bold;
#                 line-height: 1;
#                 text-align-top:40px;    ##############
#             }}
#             .progress-bar-container {{
#                 width: 100%;
#                 height: 10px;
#                 background-color: #383838; /* Background color of the bar */
#                 border-radius: 5px;
#                 margin-top: 15px;
#             }}
#             .progress-bar-fill {{
#                 height: 100%;
#                 width: {risk_percentage}%; /* Dynamic width based on prediction */
#                 background-color: #ff5733;
#                 border-radius: 5px;
#             }}
#         </style>
        
#         <div class="prediction-container">
#             <div class="prediction-title">Prediction Result</div>
#             <div class="prediction-title">Risk Probability:</div>
#             <div class="risk-probability-text">{risk_percentage}%</div>
#             <div class="progress-bar-container">
#                 <div class="progress-bar-fill"></div>
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     ## 3. Display the simple text outcome below the styled result
    
#     st.write("") # Add a little space
#     if prediction[0] == 1:
#         st.error(" High Risk of Heart Disease")
#     else:
#         st.success(" Low Risk / Healthy")
