
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


import joblib
df=joblib.load("heart_disease_pred.joblib")

st.title("Heart Disease Predection")

st.sidebar.title("Sidebar")
# st.page_link("Charts", label="Charts Page")


#################
col1, col2 = st.columns(2)

with col1:
#### Age :---
    Age = st.number_input("Age", min_value=18, max_value=100, value=30)
    
    # st.write("")

##### Hypertension :--
    options_hyp = {"NO": 0, "YES": 1}
    hyp_label = st.selectbox("Hypertension", list(options_hyp.keys()))
    
    hypertension_value = options_hyp[hyp_label]

with col2:
###### Diabetes :--
    options_dia = {"NO": 0, "YES": 1}
    dia_label = st.selectbox("Diabetes", list(options_dia.keys()))
    diabetes_value = options_dia[dia_label]

    # st.write("") 
    
###### Previous Heart Attack Mapping
    options_att = {"NO": 0, "YES": 1}
    att_label = st.selectbox("Previous_Heart_Attack", list(options_att.keys()))
    heart_attack_value = options_att[att_label]

###### Cholesterol Section ---
c1, c2, c3 = st.columns([1, 2, 1]) 
with c2:
    Cholesterol = st.slider("Cholesterol (mg/dL)", min_value=100, max_value=600, value=200,width=1000)



###### Prediction Logic ---
# if st.button("Predict"):
# if st.button("Predict", key="heart_disease_predict"):
#     input_data = np.array([[Age, hypertension_value, diabetes_value, heart_attack_value, Cholesterol]])
#     prediction = df.predict(input_data)
    
#     if prediction[0] == 1:
#         st.error("Prediction: High Risk of Heart Disease")
#     else:
#         st.success("Prediction: Low Risk / Healthy")


###########################
def add_bg_from_url():
    st.markdown(
        """
        <style>
        .stApp {
            /* 1. The Main Dark Color */
            background-color:  #121212;
        }
        
        /* Optional: This fixes the text inputs to match the glass look in your screenshot */
        .stTextInput > div > div, .stTextArea > div > div {
            background-color: rgba(255, 255, 255, 0.05) !important;
            color: #e9ecef !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()
###################################################
##### Prediction Logic ---


if st.button("Predict"):

    input_data = np.array([[Age, hypertension_value, diabetes_value, heart_attack_value, Cholesterol]])
    
    prediction_proba = df.predict_proba(input_data)
    
    risk_probability = prediction_proba[0][1]
    
    risk_percentage = int(round(risk_probability * 100))
    
    prediction = df.predict(input_data)

    
    # The custom HTML/CSS block is used to replicate the dark background,
    # large red percentage text, and the styled progress bar from your image.
    st.markdown(
        f"""
        <style>
            .prediction-container {{
                background-color: #1e1e1e; /* Dark background matching the image */
                padding: 20px;
                border-radius: 10px;
                margin-top: 30px;
            }}
            .prediction-title {{
                color: #e0e0e0;
                font-size: 18px;
                margin-bottom: 10px;
            }}
            .risk-probability-text {{
                color: #ff5733; /* A bright red/orange color for the percentage */
                font-size: 68px;
                font-weight: bold;
                line-height: 1;
                text-align-top:40px;    ##############
            }}
            .progress-bar-container {{
                width: 100%;
                height: 10px;
                background-color: #383838; /* Background color of the bar */
                border-radius: 5px;
                margin-top: 15px;
            }}
            .progress-bar-fill {{
                height: 100%;
                width: {risk_percentage}%; /* Dynamic width based on prediction */
                background-color: #ff5733;
                border-radius: 5px;
            }}
        </style>
        
        <div class="prediction-container">
            <div class="prediction-title">Prediction Result</div>
            <div class="prediction-title">Risk Probability:</div>
            <div class="risk-probability-text">{risk_percentage}%</div>
            <div class="progress-bar-container">
                <div class="progress-bar-fill"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    ## 3. Display the simple text outcome below the styled result
    
    # st.write("") # Add a little space
    if prediction[0] == 1:
        st.error(" High Risk of Heart Disease")
    else:
        st.success(" Low Risk / Healthy")



#######################################
############## CHARTS #################

# sns.lineplot(x="Heart_Rate", y= 'Age', data=df)

# plt.title("line chart")
# plt.show()

# df=joblib.load("heart_disease_pred.joblib")

df=pd.read_csv("heart_disease.csv")


col1, col2 = st.columns(2)
############################################
  
# with col1:
#     # st.subheader("Line Chart")
#     fig, ax = plt.subplots(facecolor='#121212')
#     sns.lineplot(x="Heart_Rate", y= 'Age', data=df, color="#FF69B4",ax=ax)
#     plt.title("line chart", color="white")
#     ax.grid(True, linestyle="--", alpha=0.1)
#     # ax.set_facecolor('#0E1117')   # light background
#     ax.set_facecolor('#121212')
#     ax.tick_params(axis="x", colors="white", labelsize=10, rotation=30)
#     ax.tick_params(axis="y", colors="white", labelsize=10)

#     ax.xaxis.label.set_color('white')
#     ax.yaxis.label.set_color('white')

#     st.pyplot(fig)



# with col1:?????????????????
 
#     fig, ax = plt.subplots(figsize=(20, 15), facecolor='#121212') 
    
#     # st.subheader("Line Chart") # You commented this out, but it's good practice to have a title outside the plot
    
#     # NOTE: Ensure 'df' here is your DataFrame containing 'Heart_Rate' and 'Age', NOT your model.
#     sns.lineplot(x="Heart_Rate", y='Age', data=df, color="#FF69B4", ax=ax)
    
#     plt.title("Line Chart", color="white")
#     ax.grid(True, linestyle="--", alpha=0.1)
    
#     ax.set_facecolor('#121212')
#     ax.tick_params(axis="x", colors="white", labelsize=10, rotation=30)
#     ax.tick_params(axis="y", colors="white", labelsize=10)

#     ax.xaxis.label.set_color('white')
#     ax.yaxis.label.set_color('white')

    # st.pyplot(fig)


    ################################
#     sns.kdeplot(x="Heart_Rate", y= 'Age', data=df)
# plt.show()
# with col1:
 
#     fig, ax = plt.subplots(figsize=(20, 15), facecolor='#121212') 
   
#     sns.kdeplot(x="Heart_Rate", y='Age', data=df, color="#FF69B4", ax=ax)
    
#     plt.title("Line Chart", color="white")
#     ax.grid(True, linestyle="--", alpha=0.1)
    
#     ax.set_facecolor('#121212')
#     ax.tick_params(axis="x", colors="white", labelsize=10, rotation=30)
#     ax.tick_params(axis="y", colors="white", labelsize=10)

#     ax.xaxis.label.set_color('white')
#     ax.yaxis.label.set_color('white')

#     st.pyplot(fig)