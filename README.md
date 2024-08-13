
**AQI Prediction Using Machine Learning Techniques**

**Introduction**

In our project, we're utilizing machine learning techniques to predict the Air Quality Index (AQI) using real-time environmental data. By analyzing historical air quality and meteorological parameters, we're crafting models that enable proactive decision-making, efficient resource allocation, and effective pollution mitigation to protect and enhance environmental and public health. This project aims to predict AQI levels, enabling early preventive measures against air pollution and promoting public health.
 

**Problem Statement**

Air pollution is a significant concern worldwide, impacting millions of people and causing serious health problems. High levels of pollutants like SO2, NOx, RSPM, and SPM can aggravate respiratory and heart conditions, reduce overall well-being, and harm ecosystems. Poor air quality also contributes to climate change and affects economic productivity.

Given this context, there is a pressing need for effective solutions to monitor, predict, and manage air quality. Our AQI prediction project addresses this need by using machine learning to accurately forecast air quality based on historical data, enabling early preventive measures and supporting public health.

**Project Objectives**

- Predict AQI Levels: Develop a robust model to predict AQI based on key pollutants.
- Enhance Public Health: Enable early preventive measures against air pollution.
- Support Environmental Management: Provide tools for proactive decision-making and pollution mitigation.

**Technologies and Tools**

- Programming Language: Python
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- Visualization: Tableau
- Web Framework: Flask
- Version Control: Git

**Project Phases**

1. **Data Collection:**
   - Scraped historical air quality data from the Maharashtra Pollution Control Board's website, covering the period from 2001 to 2024.

2. **Data Cleaning and Preparation:**
   - Addressed missing values by removing NaN rows and using the 'coerce' method for numeric columns.
   - Filled gaps in location data using the mean of respective groups and dropped locations with significant missing data.

3. **Exploratory Data Analysis (EDA):**
   - Conducted visual analysis using boxplots, histograms, and scatter plots to understand pollutant distribution and correlations.
   - Identified strong correlations between RSPM and AQI, and detected outliers for better model accuracy.

4. **Model Building:**
   - Encoded categorical location data and split the dataset into training and testing sets.
   - Tested various machine learning algorithms, with Random Forest proving most effective, achieving a Mean Squared Error of 130 and an R² score of 95%.

5. **Model Evaluation:**
   - Assessed model performance using RMSE and R² to fine-tune the Random Forest model for optimal AQI prediction.

6. **Deployment and User Interface:**
   - Developed a web interface using Flask, allowing users to input environmental parameters and receive real-time AQI predictions.
   - Integrated Tableau dashboards to visualize pollutant impacts and AQI trends.

**Comparison and Code Explanation**

**1. Model Comparison Table**

| Model            | MAE  | MSE    | RMSE | R² Score |
|------------------|------|--------|------|----------|
| Random Forest    | 2.63 | 129.31 | 11.37| 0.96     |
| AdaBoost         | 18.17| 552.79 | 23.51| 0.81     |
| CatBoost         | 3.20 | 133.15 | 11.54| 0.95     |
| XGBoost          | 5.19 | 287.84 | 16.97| 0.90     |
| Linear Regression| 8.15 | 293.22 | 17.12| 0.90     |
| Naive Bayes      | 9.15 | 1072.53| 32.75| 0.63     |
| Decision Tree    | 2.76 | 171.82 | 13.11| 0.94     |

**2. Code Explanation**

- **Data Preprocessing:**
  - **Handling Missing Values**: Removed rows with NaN values and used methods like `mean` for filling gaps to ensure the dataset is clean and complete.
  - **Encoding Categorical Data**: Transformed non-numeric categorical variables into numeric formats using techniques like one-hot encoding.

- **Model Building:**
  - **Training and Testing Split**: Divided the dataset into training and testing sets to evaluate model performance.
  - **Algorithm Selection**: Random Forest was selected for its robustness and performance, compared to other algorithms such as Decision Tree, AdaBoost, and XGBoost.

- **Model Evaluation:**
  - **RMSE (Root Mean Squared Error)**: Measures the average magnitude of errors in predictions. A lower RMSE indicates better model performance.
  - **R² (Coefficient of Determination)**: Indicates how well the model explains the variability of the response variable. A higher R² signifies a better fit.

**Results**

The project successfully predicted AQI levels with high accuracy. The analysis highlighted significant impacts of NOx and RSPM on AQI, providing actionable insights. The deployed model, accessible via a web interface, offers practical value by aiding users in making informed decisions based on real-time AQI predictions.

**Future Work**

- Real-Time Data Integration: Enhancing the model with real-time data for continuous AQI monitoring.
- Advanced Algorithms: Experimenting with XGBoost or deep learning models to improve accuracy.
- UI/UX Enhancements: Improving the web application’s UI for a better user experience.

**Conclusion**

This project provided a meaningful opportunity to address a crucial public health issue through technology. The skills developed in data collection, cleaning, analysis, machine learning, and deployment have been invaluable. The potential impact of this work in promoting public health and environmental management is exciting.

**Contributions**

Contributions are welcome! Feel free to fork this repository and submit a pull request with your improvements.

**Contact**

For any questions or feedback, please reach out to Alkesh Lajurkar.

---
