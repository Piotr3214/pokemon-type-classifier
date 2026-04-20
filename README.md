# 🛡️ Pokémon AI: Type Classifier

A web application that uses Machine Learning to predict a Pokémon's primary type based on its base statistics.

## 🚀 About the Project
This project combines Data Science analysis with practical Model Deployment. The model was trained on Pokémon data from Generations 1-7 and is made accessible through an interactive web interface built with Streamlit.

## 📊 Analysis & Modeling
The `pokemon.ipynb` (or `pokemon.py`) file contains the complete research process:
- **Preprocessing:** Data cleaning, handling missing values, and feature engineering (e.g., calculating **BMI** and **Base Stat Total**).
- **Visual Analysis:** Using the **PCA** algorithm to map 18 types into 2D space and **K-Means** clustering to find patterns.
- **Modeling:** Performance comparison of Logistic Regression, Random Forest, and Gradient Boosting.
- **Evaluation:** A detailed **Confusion Matrix** showing which types are most similar according to their stats.

## 🛠️ Tech Stack
- **Python 3.x**
- **Streamlit**: User interface.
- **Scikit-learn**: Machine Learning engine (Random Forest).
- **Pandas & Numpy**: Data manipulation.
- **Matplotlib & Seaborn**: Statistical visualizations.
- **Joblib**: Model and scaler serialization.

## 📂 File Structure
- `app.py` – Main Streamlit application code.
- `pokemon.ipynb` – Training script with full data analysis and visualizations.
- `pokemon_model.pkl` – Trained Random Forest model.
- `scaler.pkl` – StandardScaler object fitted to the training data.
- `label_encoder.pkl` – Mapping of type IDs to type names.
- `features_list.pkl` – List of input features in the correct order.
- `requirements.txt` – List of dependencies required to run the project.

## 📦 Installation & Local Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/Piotr3214/pokemon-type-classifier.git](https://github.com/Piotr3214/pokemon-type-classifier.git)
