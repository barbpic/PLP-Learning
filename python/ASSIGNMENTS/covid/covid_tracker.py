# covid_tracker.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="COVID-19 Global Tracker", layout="wide")

# Title
st.title("🌍 COVID-19 Global Data Tracker")

# Load data function
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('owid-covid-data.csv')
        df['date'] = pd.to_datetime(df['date'])
        return df
    except FileNotFoundError:
        st.error("Error: File 'owid-covid-data.csv' not found. Please download it first.")
        return None

# Load data
df = load_data()

if df is not None:
    # Sidebar controls
    st.sidebar.header("Controls")
    countries = st.sidebar.multiselect(
        "Select countries",
        options=sorted(df['location'].unique()),
        default=['United States', 'India', 'Brazil', 'United Kingdom']
    )
    
    start_date, end_date = st.sidebar.date_input(
        "Date range",
        value=[df['date'].min(), df['date'].max()],
        min_value=df['date'].min(),
        max_value=df['date'].max()
    )
    
    # Filter data
    filtered_df = df[
        (df['location'].isin(countries)) & 
        (df['date'] >= pd.to_datetime(start_date)) & 
        (df['date'] <= pd.to_datetime(end_date))
    ]
    
    # Tabs for different views
    tab1, tab2, tab3 = st.tabs(["Cases", "Deaths", "Vaccinations"])
    
    with tab1:
        st.header("Cases Over Time")
        if not filtered_df.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            for country in countries:
                country_data = filtered_df[filtered_df['location'] == country]
                ax.plot(country_data['date'], country_data['total_cases'], label=country)
            ax.set_title('Total COVID-19 Cases')
            ax.legend()
            st.pyplot(fig)
        else:
            st.warning("No data available for selected filters")
    
    with tab2:
        st.header("Deaths Analysis")
        if not filtered_df.empty and 'total_deaths' in filtered_df.columns:
            # Deaths over time
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            for country in countries:
                country_data = filtered_df[filtered_df['location'] == country]
                ax1.plot(country_data['date'], country_data['total_deaths'], label=country)
            ax1.set_title('Total Deaths Over Time')
            ax1.legend()
            st.pyplot(fig1)
            
            # Death rate comparison
            latest = filtered_df.groupby('location').last()
            if 'total_cases' in latest.columns:
                latest['death_rate'] = latest['total_deaths'] / latest['total_cases']
                fig2, ax2 = plt.subplots(figsize=(10, 4))
                sns.barplot(x=latest.index, y=latest['death_rate'], ax=ax2)
                ax2.set_title('Death Rate (Deaths/Cases)')
                ax2.tick_params(axis='x', rotation=45)
                st.pyplot(fig2)
        else:
            st.warning("Death data not available")
    
    with tab3:
        st.header("Vaccination Progress")
        if not filtered_df.empty and 'people_vaccinated' in filtered_df.columns:
            # Vaccination rates
            fig, ax = plt.subplots(figsize=(10, 6))
            for country in countries:
                country_data = filtered_df[filtered_df['location'] == country]
                ax.plot(country_data['date'], country_data['people_vaccinated'], label=country)
            ax.set_title('Vaccinations Over Time')
            ax.legend()
            st.pyplot(fig)
        else:
            st.warning("Vaccination data not available")
    
    # Show raw data option
    if st.checkbox("Show raw data"):
        st.dataframe(filtered_df)