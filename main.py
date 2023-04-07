import streamlit as st

st.title('Aplikasi Perhitungan Molaritas')

bobot = st.number_input('Masukkan Nilai bobot')
volume = st.number_input('Masukkan Nilai Volume')
mr = st.number_input('Masukkan Nilai Mr')

tombol = st.button('Hitung Nilai Molaritas')

if tombol:
    nilai_molaritas = bobot/(mr*volume)
    st.success(f'Nilai Molaritas Adalah {nilai_molaritas}')