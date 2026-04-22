# 🏗️ Civic Tech Grievance & Delay Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-F7931E)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)

## 📌 Project Overview
The **Civic Tech Grievance & Delay Analyzer** is an end-to-end Machine Learning project designed to predict the estimated resolution time for public infrastructure complaints (e.g., Road Construction, Water Supply, Street Lights). 

By analyzing historical grievance patterns, this tool provides citizens and civic authorities with a realistic timeline for issue resolution, promoting transparency and better expectation management.

**🌐 Live Web App:** [Experience the Predictor Here](https://civic-tech-grievance-analyzer-dihsse5pjhefbjgzdp6str.streamlit.app/)

---

## 🚀 Key Features
* **Synthetic Data Generation:** Engineered a highly realistic dataset of 50,000 civic complaints using Python and Faker to mimic real-world municipal grievance portals.
* **Exploratory Data Analysis (EDA):** Visualized grievance volume across different geographic zones and categories to identify systematic bottlenecks.
* **Machine Learning Predictive Engine:** Utilized a **Random Forest Regressor** to learn complex, non-linear relationships between geographical areas, priority levels, and infrastructure categories.
* **Interactive UI:** Deployed a user-friendly web interface using **Streamlit**, allowing end-users to input their complaint details and instantly receive an estimated delay in days.

---

## 🧠 Technical Architecture & Workflow

1. **Data Engineering (`data_generation.py`):** Created features like `Filing_Date`, `Resolution_Date`, and calculated the core target variable `Delay_Days`.
2. **Data Preprocessing (`eda_analysis.ipynb`):** Handled null values for 'Pending' statuses and performed One-Hot Encoding on categorical variables.
3. **Model Training (`model_training.ipynb`):** Split data (80/20) and trained a robust ensemble model. 
4. **Deployment (`app.py`):** Serialized the trained model using `joblib` and integrated it with a Streamlit front-end.

---

## 📊 Model Performance
* **Algorithm:** Random Forest Regressor
* **Mean Absolute Error (MAE):** `~17.01 days`
* **Technical Note on MAE:** The MAE of 17 days accurately reflects the inherent real-world variance in public works. Variables like weather disruptions, contractor delays, and budget approvals introduce natural unpredictability. The model successfully captures the baseline distribution while respecting this operational variance.

---

## 💻 How to Run Locally

Follow these steps to run the predictor on your local machine:

**1. Clone the repository**
```bash
git clone [https://github.com/YourUsername/Civic-Tech-Grievance-Analyzer.git](https://github.com/VaibhavGit25/Civic-Tech-Grievance-Analyzer.git)
cd Civic-Tech-Grievance-Analyzer

**2. Install dependencies**
pip install -r requirements.txt

**3. Run the Streamlit App**
streamlit run app.py