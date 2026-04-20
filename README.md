# 🛡️ Pokémon AI: Type Classifier

Aplikacja webowa wykorzystująca uczenie maszynowe do przewidywania głównego typu Pokémona na podstawie jego statystyk bazowych.

## 🚀 O projekcie
Projekt łączy analizę danych (Data Science) z praktycznym wdrożeniem modelu (Deployment). Model został wytrenowany na danych o Pokémonach z generacji 1-7, a następnie udostępniony w formie interaktywnej aplikacji webowej.

## 📊 Analiza i Modelowanie
W pliku `pokemon.py` znajduje się pełny proces badawczy:
- **Preprocessing:** Czyszczenie danych, uzupełnianie brakujących wartości i inżynieria cech (np. obliczanie **BMI** oraz **Base Stat Total**).
- **Analiza wizualna:** Wykorzystanie algorytmu **PCA** do zmapowania 18 typów na przestrzeń 2D oraz klasteryzacja **K-Means**.
- **Modelowanie:** Porównanie wyników Regresji Logistycznej, Random Forest oraz Gradient Boosting.
- **Ewaluacja:** Szczegółowa macierz pomyłek (Confusion Matrix) pokazująca, które typy są do siebie najbardziej podobne według statystyk.

## 🛠️ Technologie
- **Python 3.x**
- **Streamlit**: Interfejs użytkownika.
- **Scikit-learn**: Serce uczenia maszynowego (Random Forest).
- **Pandas & Numpy**: Manipulacja danymi.
- **Matplotlib & Seaborn**: Wizualizacje statystyczne.
- **Joblib**: Serializacja modelu i skalerów.

## 📂 Struktura plików
- `app.py` – Kod źródłowy aplikacji Streamlit.
- `pokemon.py` – Skrypt treningowy z pełną analizą danych.
- `pokemon_model.pkl` – Wytrenowany model Random Forest.
- `scaler.pkl` – Obiekt StandardScaler dopasowany do danych treningowych.
- `label_encoder.pkl` – Mapowanie identyfikatorów na nazwy typów.
- `features_list.pkl` – Lista cech wejściowych w odpowiedniej kolejności.
- `requirements.txt` – Lista zależności niezbędnych do uruchomienia projektu.

## 📦 Instalacja i uruchomienie lokalne
1. Sklonuj repozytorium:
   ```bash
   git clone [https://github.com/TWOJA-NAZWA-UZYTKOWNIKA/NAZWA-REPOZYTORIUM.git](https://github.com/TWOJA-NAZWA-UZYTKOWNIKA/NAZWA-REPOZYTORIUM.git)
