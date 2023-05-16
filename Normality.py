import streamlit as st

st.set_page_config(page_title="Chemistry App", page_icon=":microscope:")

st.title("Aplikasi Normalitas & Molaritas")

menu = ["Pengertian","Kalkulator Molaritas", "Kalkulator Normalitas"]
choice = st.sidebar.selectbox("Select a tool", menu)

if choice == "Pengertian":
    st.title("Pengertian")
    st.write("molaritas diartikan sebagai jumlah mol zat terlarut per liter zat pelarut. Sederhananya, molaritas menyatakan jumlah mol zat terlarut dalam setiap liter larutan.")
    st.write("Normalitas adalah ukuran yang menunjukkan konsentrasi dengan berat setara dalam gram per liter larutan, dimana berat setara itu sendiri adalah ukuran kapasitas reaktif dari suatu molekul yang terlarut dalam larutan. Dalam reaksi")




elif choice == "Kalkulator Molaritas":
    st.title("Kalkulator Molaritas")
    st.write("M = n/V ")
    st.write("n=Jumlah mol")
    st.write("V=volume")
        

    volume = st.number_input("Masukkan volume dari senawa (dalam liter):", min_value=0.0, step=0.1)
    moles = st.number_input("Masukkan jumlah mol :", min_value=0.0, step=0.1)

    if st.button("Hitung"):
        molarity = moles / volume
        st.write(f"Molaritas senyawa adalah {molarity:.2f} M")

elif choice == "Kalkulator Normalitas":
    st.title("Kalkulator Normalitas")
    st.write("N= M x a")
    st.write("M=molaritas")
    st.write("a=Jumlah valensi")


    # Input fields for molarity and valence
    molarity = st.number_input("Masukkan jumlah molaritas:", min_value=0.0, step=0.1)
    valence = st.number_input("Masukkan jumlah valensi:", min_value=1, step=1)

    # Calculate the normality based on the inputs
    normality = molarity * valence

    # Display the result
    if st.button("Hitung"):
        st.write(f"Normalitas dari senyawa adalah {normality:.2f} N")
