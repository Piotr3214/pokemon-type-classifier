import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Konfiguracja strony
st.set_page_config(page_title="Pokémon Type Predictor", layout="wide", page_icon="🔮")

# Ładowanie zasobów
@st.cache_resource
def load_assets():
    model = joblib.load('pokemon_model.pkl')
    scaler = joblib.load('scaler.pkl')
    le = joblib.load('label_encoder.pkl')
    features = joblib.load('features_list.pkl')
    return model, scaler, le, features

try:
    model, scaler, le, features = load_assets()
except Exception as e:
    st.error(f"Błąd ładowania modelu: {e}")
    st.stop()

st.title("🛡️ Pokémon AI: Klasyfikacja Typów")
st.markdown("Model przewiduje typ na podstawie statystyk bazowych (bez analizy odporności).")

# Sidebar
menu = st.sidebar.selectbox("Menu", ["Predykcja Typu", "O projekcie"])

if menu == "Predykcja Typu":
    st.header("Wprowadź statystyki Pokémona")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        hp = st.slider("HP", 1, 255, 70)
        atk = st.slider("Attack", 1, 200, 110)
        dfn = st.slider("Defense", 1, 230, 70)
        
    with col2:
        sp_atk = st.slider("Sp. Attack", 1, 200, 150)
        sp_dfn = st.slider("Sp. Defense", 1, 230, 90)
        speed = st.slider("Speed", 1, 200, 100)

    with col3:
        height = st.number_input("Height (m)", 0.1, 20.0, 1.7)
        weight = st.number_input("Weight (kg)", 0.1, 1000.0, 90.5)
        legendary = st.selectbox("Is Legendary?", [0, 1])
        gen = st.number_input("Generation", 1, 9, 7)

    # Obliczanie cech identycznie jak w Colabie
    base_total = hp + atk + dfn + sp_atk + sp_dfn + speed
    bmi = weight / (height**2 + 1)
    
    # Tworzenie DataFrame z zachowaniem KOLEJNOŚCI cech
    input_data = pd.DataFrame([[
        hp, atk, dfn, sp_atk, sp_dfn, speed, base_total, bmi, legendary, gen
    ]], columns=features)
    
    if st.button("🔮 Przewidź Typ"):
        # 1. Skalowanie
        scaled_data = scaler.transform(input_data)
        # 2. Predykcja
        prediction = model.predict(scaled_data)
        # 3. Dekodowanie nazwy
        type_name = le.inverse_transform(prediction)[0]
        
        st.success(f"Model uważa, że to typ: **{type_name.upper()}**")
        
        #Pokaż prawdopodobieństwo
        probs = model.predict_proba(scaled_data)
        top_idx = np.argsort(probs[0])[-3:][::-1]
        
        st.write("---")
        st.write("Top 3 prawdopodobne typy:")
        for idx in top_idx:
            st.write(f"- {le.classes_[idx].capitalize()}: {probs[0][idx]*100:.1f}%")
        
        st.balloons()

else:
    st.info("Projekt wykorzystuje algorytm Random Forest wytrenowany na statystykach z generacji 1-7.")