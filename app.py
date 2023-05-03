import streamlit as st

st.header(':violet[ini aplikasi kalkulator]')
st.subheader('silahkan input angka numerik')

number1 = st.number_input('masukan bilangan pertama')
st.write(f'bilangan pertama adalah {number1}')

number2 = st.number_input('masukan bilangan kedua')
st.write(f'bilangan kedua adalah{number2}')

if st.button('hitung'):
	hasil = number1+number2
	st.success(f'hasil penjumlahan dari {number1}+{number2}={hasil}',icon="✅")
	st.balloons()
else:
	st.write('silahkan klik tombol "hitung"')
