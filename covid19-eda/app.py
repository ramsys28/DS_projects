import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import shap

st.title("COVID-19 Death Rate Drivers: Interactive App")
df = pd.read_csv("data/owid-covid-data.csv")

df['date'] = pd.to_datetime(df['date'])

# Step 2: Select required columns
df = df[['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'population', 'median_age', 'gdp_per_capita', 'population_density', 'hospital_beds_per_thousand', 'people_vaccinated_per_hundred', 'stringency_index']]
df['deaths_per_100k'] = (df['total_deaths'] / df['population']) * 100000
df['cfr'] = df['total_deaths'] / df['total_cases']

# Step 3: Get the latest snapshot per location
latest = df.sort_values('date').groupby('location').tail(1)
latest = latest[latest['continent'].notnull()]

# Step 4: Define a function to fill missing values
def fill_na_and_zero_with_group_or_global_mean(df, group_col):
    """
    For each numeric column:
    - Replace NaN with group mean.
    - If the group mean is zero, replace with global mean.
    - Replace zero values with global mean.
    """
    numeric_cols = df.select_dtypes(include=['number']).columns.drop(['population'])  # exclude any ID columns
    for col in numeric_cols:
        if col == group_col:
            continue  # skip the group column itself

        print(f"\nProcessing column: {col}")

        # Step 1: Calculate group mean (per location)
        group_mean = df.groupby(group_col)[col].transform('mean')
        global_mean = df[col].mean(skipna=True)

        # Step 2: Replace NaN with group mean, then global mean if still NaN or zero
        df[col] = df[col].fillna(group_mean)
        df[col] = df[col].replace(0, global_mean)
        df[col] = df[col].fillna(global_mean)

    return df


# Step 5: Apply the function
latest  = latest.drop(columns=['stringency_index'])
latest = fill_na_and_zero_with_group_or_global_mean(latest, group_col='location')


X = latest[['median_age', 'population_density', 'gdp_per_capita', 'hospital_beds_per_thousand', 'people_vaccinated_per_hundred']]
y = latest['deaths_per_100k'][X.index]

analysis = st.sidebar.selectbox("Choose analysis", ["Correlation", "Regression", "Feature Importance", "Clustering"])
if analysis == "Correlation":
    st.write(sns.heatmap(latest.select_dtypes(include=['number']).corr(), annot=True, cmap="coolwarm"))
elif analysis == "Regression":
    model = LinearRegression().fit(X, y)
    st.write(pd.Series(model.coef_, index=X.columns))
elif analysis == "Feature Importance":
    rf = RandomForestRegressor(n_estimators=100, random_state=42).fit(X, y)
    st.bar_chart(pd.Series(rf.feature_importances_, index=X.columns))
elif analysis == "Clustering":
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    kmeans = KMeans(n_clusters=3, random_state=42).fit(X_scaled)
    latest['Cluster'] = kmeans.labels_
    st.plotly_chart(px.scatter(latest, x='gdp_per_capita', y='deaths_per_100k', color=latest['Cluster'].astype(str), hover_name='location'))
