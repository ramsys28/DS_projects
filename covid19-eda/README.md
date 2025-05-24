
# Unmasking the Pandemic: COVID-19 Death Rate Drivers

A comprehensive data science project that investigates the global impact of COVID-19 by identifying and quantifying key factors contributing to elevated death rates across countries. This project is designed to showcase expertise in **data analysis, statistical modeling, machine learning, causal inference**, and **interactive data visualization**—targeted at recruiters evaluating data science portfolios.

---

## Project Summary

**Objective**  
To explore how socio-economic, demographic, and healthcare infrastructure factors influenced COVID-19 death rates around the world—and to derive actionable insights using advanced data science techniques.

**Key Contributions**
- Built an end-to-end data science pipeline from raw data acquisition to deployment
- Combined public health data with socio-economic indicators to perform multi-level analysis
- Demonstrated the use of **causal inference** through Difference-in-Differences modeling
- Deployed an **interactive Streamlit app** to communicate insights to non-technical audiences

---

## Data Sources
- [Our World in Data – COVID-19 Dataset](https://github.com/owid/covid-19-data)
- World Bank Open Data (GDP, population, healthcare indicators)
- United Nations Development Programme (Human Development Index)

---

## Tools & Technologies Used

| Category                    | Tools / Skills                                                  |
|-----------------------------|------------------------------------------------------------------|
| **Programming Language**     | Python                                                          |
| **Data Wrangling**           | `pandas`, `numpy`                                               |
| **Data Visualization**       | `matplotlib`, `seaborn`, `plotly`, `Streamlit`                  |
| **Statistical Analysis**     | Pearson correlation, linear regression, Difference-in-Differences |
| **Machine Learning**         | Random Forest Regressor, KMeans Clustering                      |
| **Model Explainability**     | SHAP (SHapley Additive exPlanations)                            |
| **Deployment**               | `Streamlit` (interactive web app)                               |
| **Version Control & Packaging** | `Git`, `Jupyter Notebook`, `requirements.txt`                |

---

## Analytical Highlights

- **Exploratory Data Analysis (EDA)**: Identified global and country-level trends in cases, deaths, and policy responses.
- **Correlation and Regression**: Assessed the strength of associations between demographic and healthcare variables and COVID-19 death rates.
- **Random Forest Modeling**: Ranked feature importance and uncovered key drivers such as population density, GDP per capita, and hospital capacity.
- **SHAP Explainability**: Provided transparent model interpretation for stakeholders.
- **Clustering**: Grouped countries with similar pandemic characteristics to reveal geographic and economic clusters.
- **Difference-in-Differences**: Estimated causal effect of early vaccine rollout on death rates by comparing high vs low vaccination countries over time.

---

## How to Run

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the analysis notebook:
   ```bash
   jupyter notebook covid19_eda_negative_factors.ipynb
   ```
4. Run the interactive dashboard:
   ```bash
   streamlit run app.py
   ```

---

## Skills depicted in this project

This project demonstrates my ability to:
- Conduct independent, data-driven investigations on real-world problems
- Apply robust statistical and machine learning techniques
- Build interpretable models with real policy implications
- Communicate findings via clean visualizations and an interactive web app
- Deliver production-ready, reproducible, and well-documented code

---

## Author

**Manousos Klados**  
Data Scientist | Neuroscience Researcher | Python Enthusiast


Personal websites: https://linktr.ee/thephdmentor
Twitter: https://twitter.com/mklados
LinkedIn: https://www.linkedin.com/in/mklados
