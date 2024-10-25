import pickle
import numpy as np
import streamlit as st

# Load model yang telah disimpan
model = pickle.load(open('penyakit_jantung.sav', 'rb'))

# Judul web
st.title('Prediksi Penyakit Jantung')

# Membuat kolom untuk input data
col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Umur')

with col2:
    sex = st.text_input('Jenis Kelamin')

with col3:
    cp = st.text_input('Jenis Nyeri Dada')

with col1:
    trestbps = st.text_input('Tekanan Darah')

with col2:
    chol = st.text_input('Nilai Kolesterol')

with col3:
    fbs = st.text_input('Gula Darah')

with col1:
    restecg = st.text_input('Hasil Elektrokardiografi')

with col2:
    thalach = st.text_input('Detak Jantung Maksimum')

with col3:
    exang = st.text_input('Induksi Angina')

with col1:
    oldpeak = st.text_input('ST Depression')

with col2:
    slope = st.text_input('Slope')

with col3:
    ca = st.text_input('Nilai CA')

with col1:
    thal = st.text_input('Nilai Thal')

# Variabel untuk menampilkan hasil prediksi
heart_diagnosis = ''

# Tombol untuk melakukan prediksi
if st.button('Prediksi Penyakit Jantung'):
    try:
        # Mengonversi input ke tipe float
        input_data = [
            float(age), float(sex), float(cp), float(trestbps), float(chol), 
            float(fbs), float(restecg), float(thalach), float(exang), 
            float(oldpeak), float(slope), float(ca), float(thal)
        ]

        # Melakukan prediksi
        heart_prediction = model.predict([input_data])

        # Menentukan hasil prediksi
        if heart_prediction[0] == 0:
            heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
        else:
            heart_diagnosis = 'Pasien Terkena Penyakit Jantung'

        # Menampilkan hasil
        st.success(heart_diagnosis)

    except ValueError:
        st.error("Masukkan semua nilai dengan benar dalam format numerik.")
