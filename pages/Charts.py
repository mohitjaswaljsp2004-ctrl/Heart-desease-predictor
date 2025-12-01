######################\\
import streamlit as st
def add_bg_from_url():
    st.markdown(
        """
        <style>
        .stApp {
            /* 1. The Main Dark Color */
            background-color:   #121212;
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
#####################

# st.markdown(
#     """
#     <style>
#     [data-testid="stAppViewContainer"] {
#         background-image: url("https://w.wallhaven.cc/full/zy/wallhaven-zy27zo.png"); /* Replace with actual base64 */
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

# #########################################    new 
# df=pd.read_csv("heart_disease.csv")


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
df=pd.read_csv("heart_disease.csv")

# --- 1. PAGE & THEME CONFIGURATION ---
st.set_page_config(
    page_title="Heart Disease Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Dark Theme CSS from the image
st.markdown("""
    <style>

        /* Custom Header Styling */
        h1, h2, h3, .stSubheader, p {
            color: #FFFFFF !important;
            font-family: 'Arial', sans-serif;
        }
        /* Plot background */
        .plot-container {
            background-color: #0a0e17;
            padding: 10px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# --- 2. DATA LOADING (Using your original feature importance data) ---
feature_names = ["Age", "Hypertension", "Diabetes", "Previous Heart Attack", "Cholesterol"]
scores = np.array([0.19480143, 0.2149715 , 0.1918075 , 0.11988657, 0.278533 ])
feature_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": scores
}).sort_values(by="Importance", ascending=False)


custom_palette = sns.color_palette(["#FD6C9E", "#00FFFF", "#BAACF7", "#ED4171", "#FFD606"])


# --- 4. LAYOUT: ROW 1 (Feature Importance & Impact Distribution) ---
col1, col2 = st.columns([3, 2], gap="medium")

# --- 4a. FEATURE IMPORTANCE BAR CHART (Left) ---
with col1:
    st.subheader("Feature Importance Scores")
    fig_bar, ax = plt.subplots(figsize=(8, 4), facecolor="#121212")
    ax.set_facecolor("#121212")#121212

    sns.barplot(
        data=feature_df,
        x="Importance",
        y="Feature",
        palette=custom_palette,
        ax=ax
    )

    # Styling
    ax.set_xlabel("Importance", color='#FFFFFF', fontsize=20)
    ax.set_ylabel("Feature", color='#FFFFFF', fontsize=20)
    ax.tick_params(axis='x', colors='#FFFFFF')
    ax.tick_params(axis='y', colors='#FFFFFF')
    sns.despine(left=True, bottom=True)
    ax.grid(False)
    
    st.pyplot(fig_bar, use_container_width=True)

# --- 4b. IMPACT DISTRIBUTION DONUT CHART (Right) ---
with col2:
    st.subheader("Impact Distribution")
    fig_pie, ax = plt.subplots(figsize=(5, 5), facecolor="#121212")
    ax.set_facecolor('#0a0e17')
    
    # Use a slightly different palette for the pie chart
    pie_palette = sns.color_palette(["#FD6C9E", "#00FFFF", "#BAACF7", "#ED4171", "#FFD606"])

    wedges, texts, autotexts = ax.pie(
        feature_df["Importance"],
        labels=feature_df["Feature"],
        colors=pie_palette,
        autopct='%.1f%%',
        startangle=90,
        pctdistance=0.75,
        wedgeprops=dict(width=0.5, edgecolor="#191F2C"), # Donut hole
        textprops={'color': '#FFFFFF', 'fontsize': 9}
    )
    plt.setp(autotexts, size=9, weight="bold", color="#FFFFFF")
    
    st.pyplot(fig_pie, use_container_width=True)


####################
with col1:
    st.subheader("Line Chart")
    fig, ax = plt.subplots(figsize=(8,5),facecolor='#121212')
    sns.lineplot(x="Cholesterol_Total", y= 'Heart_Disease', data=df, color="#FF69B4",ax=ax)
    plt.title("line chart", color="white")
    ax.grid(True, linestyle="--", alpha=0.1)
    # ax.set_facecolor('#0E1117')   # light background
    ax.set_facecolor('#121212')
    ax.tick_params(axis="x", colors="white", labelsize=10, rotation=30)
    ax.tick_params(axis="y", colors="white", labelsize=10)

    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')

    st.pyplot(fig)



############# chart 4: ---
gender_counts = df["Gender"].value_counts()
with col2: 
    st.subheader("Gender Breakdown")

    fig, ax = plt.subplots(figsize=(10, 5), facecolor="#121212")
    ax.set_facecolor("#007BFF26")

    # Capture the returned texts from ax.pie
    wedges, texts, autotexts = ax.pie(
        gender_counts.values,
        labels=gender_counts.index,
        autopct="%1.1f%%",
        startangle=55,
        colors=["#FD6C9E", "#00F0FF"]
    )

    # Change text color to white
    for text in texts:
        text.set_color("white")
    for autotext in autotexts:
        autotext.set_color("white")

    st.pyplot(fig)




# ####################
# --- 5. LAYOUT: ROW 2 (Correlation Matrix) ---
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap # Import for custom cmap

# Define the custom colors
custom_colors = ["#FD6C9E", "#00FFFF", "#BAACF7", "#ED4171", "#FFD606"] 

cmap_list = ["#ED4171", "#BAACF7", "#000000", "#00FFFF", "#FFFFFF"] # Red -> Purple -> Black (Center) -> Cyan -> Pink
custom_cmap = LinearSegmentedColormap.from_list("custom_heatmap", cmap_list, N=256)


with col1:

    st.subheader("Feature Correlations")
    
    feature_names = ['Age', 'Hypertension', 'Diabetes', 'Previous Heart Attack', 'Cholesterol']
    np.random.seed(42)
    dummy_data = pd.DataFrame(np.random.rand(100, 5), columns=feature_names)
    corr_matrix = dummy_data.corr()

    fig_corr, ax = plt.subplots(figsize=(8, 5), facecolor='#121212')
    ax.set_facecolor('#121212') # Use the same dark background color for consistency

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap=custom_cmap, # <--- **MODIFIED: Using the custom colormap**
        fmt=".2f",
        linewidths=0.5,
        linecolor='#0E1117',
        cbar_kws={"shrink": .8},
        ax=ax,
        annot_kws={"size": 9, "color": "white"}
        )
# Styling
    ax.tick_params(axis='x', colors='white', rotation=45)
    ax.tick_params(axis='y', colors='white')
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=9, colors='white')

    st.pyplot(fig_corr, use_container_width=True)

###########################


with col2:
  
    
    st.subheader("Line Chart")
 
    fig, ax = plt.subplots(facecolor='#121212') 
    sns.lineplot(x="Heart_Rate", y='Age', data=df, color="#FF69B4", ax=ax)
    
    plt.title("Line Chart", color="white")
    ax.grid(True, linestyle="--", alpha=0.1)
    
    ax.set_facecolor('#121212')
    ax.tick_params(axis="x", colors="white", labelsize=10, rotation=30)
    ax.tick_params(axis="y", colors="white", labelsize=10)

    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')

    st.pyplot(fig)


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
######################################################################################
######################################################################################

##############################

# with col1:
#     st.write("") # Spacing
#     # st.title("Correlation Matrix")
#     st.subheader("Feature Correlations")

#     np.random.seed(42)
#     dummy_data = pd.DataFrame(np.random.rand(100, 5), columns=feature_names)
#     corr_matrix = dummy_data.corr()

#     fig_corr, ax = plt.subplots(figsize=(10, 5), facecolor='#121212')
#     ax.set_facecolor('#007BFF26')

#     sns.heatmap(
#         corr_matrix,
#         annot=True,
#         cmap='mako', # Dark coolwarm-like palette
#         fmt=".2f",
#         linewidths=0.5,
#         linecolor='#0E1117',
#         cbar_kws={"shrink": .8},
#         ax=ax,
#         annot_kws={"size": 9, "color": "white"}
#         )
# # Styling
#     ax.tick_params(axis='x', colors='white', rotation=45)
#     ax.tick_params(axis='y', colors='white')
#     cbar = ax.collections[0].colorbar
#     cbar.ax.tick_params(labelsize=9, colors='white')

#     st.pyplot(fig_corr, use_container_width=True)




###########################################################################################################
########## PIE CHART :---- 4 ---
# import streamlit as st
# import plotly.express as px
# df=pd.read_csv("heart_disease.csv")
# with col2: 
#     st.subheader("Gender Breakdown")
#     gender_counts = df["Gender"].value_counts()

#     fig = px.pie(
#         names=gender_counts.index, # Labels for the slices
#         values=gender_counts.values, # Values/Counts for the slices
#         title="Proportion of Genders in the Dataset",
#         color_discrete_sequence=["skyblue", "lightcoral"] # Adjusted to 3 colors for the sample data
       
#     )

#     fig.update_layout(showlegend=True)
#     fig.update_traces(textinfo='percent+label')

#     st.plotly_chart(fig, use_container_width=True)


#########


# with col2: 
#     st.subheader("Gender Breakdown")
#     gender_counts = df["Gender"].value_counts()

#     fig = px.pie(
#         names=gender_counts.index, 
#         values=gender_counts.values, 
#         title="Proportion of Genders in the Dataset",
#         color_discrete_sequence=["skyblue", "lightcoral"]
#     )

#     fig.update_layout(showlegend=True)
    
#     # --- FINAL CORRECT FIX: Use 'rotation' instead of 'start_angle' ---
#     fig.update_traces(
#         textinfo='percent+label',
        
#         # Use patch to explicitly set the 'rotation' property.
#         # 90 degrees rotates the starting point from 3 o'clock to 12 o'clock.
#         patch={'rotation': 30}, 
        
#         # Selector remains necessary to target the pie trace.
#         selector={'type': 'pie'} 
#     )

#     st.plotly_chart(fig, use_container_width=True)

#??????????????????



# st.write("") # Spacing
# st.title("Correlation Matrix")
# st.subheader("Feature Correlations")

# # --- 5a. CORRELATION HEATMAP ---
# # Generate dummy data for correlation since the file isn't provided
# np.random.seed(42)
# dummy_data = pd.DataFrame(np.random.rand(100, 5), columns=feature_names)
# corr_matrix = dummy_data.corr()

# fig_corr, ax = plt.subplots(figsize=(10, 5), facecolor='#0E1117')
# ax.set_facecolor('#0E1117')

# sns.heatmap(
#     corr_matrix,
#     annot=True,
#     cmap='mako', # Dark coolwarm-like palette
#     fmt=".2f",
#     linewidths=0.5,
#     linecolor='#0E1117',
#     cbar_kws={"shrink": .8},
#     ax=ax,
#     annot_kws={"size": 9, "color": "white"}
# )

# # Styling
# ax.tick_params(axis='x', colors='white', rotation=45)
# ax.tick_params(axis='y', colors='white')
# cbar = ax.collections[0].colorbar
# cbar.ax.tick_params(labelsize=9, colors='white')

# st.pyplot(fig_corr, use_container_width=True)












# X = df[["Age", "Hypertension", "Diabetes", "Previous_Heart_Attack", "Cholesterol_Total", "Heart_Disease"]]

# st.subheader("Feature Correlation Matrix :-")
# fig = plt.figure(figsize=(10, 8))
# sns.heatmap(X.corr(), annot=True, cmap='coolwarm', fmt=".2f")

# st.pyplot(fig)

# st.write("")
# st.write("")
# ##############  2nd :---

# st.set_page_config(page_title="Feature Importance", layout="centered")

# st.title("Feature Importance Analysis :-")
# # st.write("Visualizing which factors have the highest impact on the model.")

# # --- DATA PREPARATION ---
# feature_names = ["Age", "Hypertension", "Diabetes", "Previous_Heart_Attack", "Cholesterol_Total"]
# scores = np.array([0.19480143, 0.2149715 , 0.1918075 , 0.11988657, 0.278533 ])

# feature_df = pd.DataFrame({
#     "Feature": feature_names,
#     "Importance": scores
# })

# feature_df = feature_df.sort_values(by="Importance", ascending=False)
# fig, ax = plt.subplots(figsize=(10, 6))

# sns.barplot(
#     data=feature_df, 
#     x="Importance", 
#     y="Feature", 
#     palette="viridis", 
#     ax=ax
# )
# ax.set_title("Feature Importance: Which factors matter most?")
# ax.set_xlabel("Importance Score")
# ax.set_ylabel("Features")

# st.pyplot(fig)

# with st.expander("View Raw Data"):
#     st.dataframe(feature_df)



# st.write("")
# st.write("")
# ################### 3rd :---


# st.set_page_config(page_title="Feature Importance", layout="centered")

# st.title("Pie Chart :-")
# # st.write("Visualizing the proportion of impact each feature has.")


# palette_color = sns.color_palette('viridis', len(feature_df))

# fig, ax = plt.subplots(figsize=(8, 8))

# ax.pie(
#     feature_df["Importance"], 
#     labels=feature_df["Feature"], 
#     colors=palette_color, 
#     autopct='%.1f%%',
#     startangle=140,
#     textprops={'fontsize': 12}
# )
# ax.set_title("Feature Importance Distribution")
# st.pyplot(fig)

# with st.expander("View Raw Data"):
#     st.dataframe(feature_df)





# ###################
## old code


# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import streamlit as st

# import joblib
# st.set_page_config(page_title="Charts")

# # df=joblib.load("heart_disease_pred.joblib")

# st.title("Health Data Visualization")



# df=pd.read_csv("heart_disease.csv")


# col1, col2 = st.columns(2)
# ############## 1st
# with col1:
#     X = df[["Age", "Hypertension", "Diabetes", "Previous_Heart_Attack", "Cholesterol_Total", "Heart_Disease"]]

#     st.subheader("Feature Correlation Matrix")
  
#     fig = plt.figure(figsize=(10, 8))
#     sns.heatmap(X.corr(), annot=True, cmap='coolwarm', fmt=".2f")

#     st.pyplot(fig)

#     st.write("")
#     st.write("")

# ##############  2nd :---

# # with col2:
#     st.set_page_config(page_title="Feature Importance", layout="centered")

#     st.subheader("Feature Importance Analysis :-")
# # st.write("Visualizing which factors have the highest impact on the model.")

# # --- DATA PREPARATION ---
#     feature_names = ["Age", "Hypertension", "Diabetes", "Previous_Heart_Attack", "Cholesterol_Total"]
#     scores = np.array([0.19480143, 0.2149715 , 0.1918075 , 0.11988657, 0.278533 ])

#     feature_df = pd.DataFrame({
#     "Feature": feature_names,
#     "Importance": scores
#     })

#     feature_df = feature_df.sort_values(by="Importance", ascending=False)
#     fig, ax = plt.subplots(figsize=(10, 6))

#     sns.barplot(
#         data=feature_df, 
#         x="Importance", 
#         y="Feature", 
#         palette="viridis", 
#         ax=ax
#         )
#     ax.set_title("Feature Importance: Which factors matter most?")
#     ax.set_xlabel("Importance Score")
#     ax.set_ylabel("Features")

#     st.pyplot(fig)

#     with st.expander("View Raw Data"):
#         st.dataframe(feature_df)



# st.write("")
# st.write("")
# ################### 3rd :---



# with col2:
#     st.set_page_config(page_title="Feature Importance", layout="centered")

#     st.subheader("Pie Chart :-")
#     # st.write("Visualizing the proportion of impact each feature has.")


#     palette_color = sns.color_palette('viridis', len(feature_df))

#     fig, ax = plt.subplots(figsize=(8, 8))

#     ax.pie(
#         feature_df["Importance"], 
#         labels=feature_df["Feature"], 
#         colors=palette_color, 
#         autopct='%.1f%%',
#         startangle=140,
#         textprops={'fontsize': 12}
#     )
#     ax.set_title("Feature Importance Distribution")
#     st.pyplot(fig)

#     with st.expander("View Raw Data"):
#         st.dataframe(feature_df)





########## pie chart 



#     fig = px.pie(
#         names=gender_counts.index, 
#         values=gender_counts.values, 
#         title="Proportion of Genders in the Dataset",
#         color_discrete_sequence=["skyblue", "lightcoral"]
#     )
    
#     fig.update_layout(
#         showlegend=True,
        
#         paper_bgcolor='#0E1117', 
#         plot_bgcolor='#007BFF26' 
#     )
    
#     fig.update_traces(
#         textinfo='percent+label',
#         patch={'rotation': 30}, 
#         selector={'type': 'pie'} 
#     )
    
#     st.plotly_chart(fig, use_container_width=True)
###########################################################################################################




# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # --- 1. Example Data (Derived from your provided summary statistics) ---
# # We are manually creating a DataFrame for the mean values shown in the chart.
# data = {
#     'Indicator': [
#         'Systolic_BP', 'Diastolic_BP', 'Heart_Rate', 
#         'Cholesterol_Total'
#     ],
#     'Mean_Value': [
#         139.30, 89.53, 84.45, 224.56
#     ]
# }
# mean_df = pd.DataFrame(data)

# # --- 2. Define the Custom Palette ---
# # Based on the image's vibrant, high-contrast cool-to-warm colors:
# custom_palette = [
#     '#55C5FF',  # Bright Blue (Systolic_BP)
#     '#32D4C5',  # Light Teal (Diastolic_BP)
#     '#68D432',  # Neon Green (Heart_Rate)
#     '#FFC832'   # Vibrant Yellow/Gold (Cholesterol_Total)
# ]

# # --- 3. Seaborn Plot Setup ---
# # Set the plot style for a dark theme background
# plt.style.use('dark_background') 

# # Create the figure and axes
# fig, ax = plt.subplots(figsize=(10, 5)) 

# # Plot the horizontal bar chart
# sns.barplot(
#     data=mean_df,
#     x='Mean_Value',
#     y='Indicator',
#     palette=custom_palette,
#     ax=ax,
#     orient='h' # Ensures horizontal bars
# )

# # --- 4. Styling for Dark Dashboard Look ---
# ax.set_title('Average Values of Key Indicators', color='white', fontsize=16, pad=15)
# ax.set_xlabel('Mean Value', color='#AAAAAA', fontsize=12)
# ax.set_ylabel('') # Remove y-axis label since the features are self-explanatory

# # Customize ticks and spines
# ax.tick_params(axis='x', colors='#AAAAAA')
# ax.tick_params(axis='y', colors='white')
# ax.spines['bottom'].set_color('#444444')
# ax.spines['left'].set_color('#444444')
# ax.grid(axis='x', color='#333333', linestyle='--', linewidth=0.5)

# # Optional: Remove top and right border spines
# sns.despine(ax=ax, top=True, right=True)

# plt.tight_layout()
# plt.show()