import streamlit as st

st.set_page_config(page_title="Chemistry App", page_icon=":microscope:")

st.title("Chemistry App")

menu = ["Molarity Calculator", "Normality Calculator"]
choice = st.sidebar.selectbox("Select a tool", menu)

if choice == "Molarity Calculator":
    st.header("Molarity Calculator")
    volume = st.number_input("Enter the volume of the solution (in liters):", min_value=0.0, step=0.1)
    mass = st.number_input("Enter the mass of the solute (in grams):", min_value=0.0, step=0.1)
    molar_mass = st.number_input("Enter the molar mass of the solute (in g/mol):", min_value=0.0, step=0.1)

    if st.button("Calculate"):
        molarity = mass / (molar_mass * volume)
        st.write(f"The molarity of the solution is {molarity:.2f} M")

elif choice == "Normality Calculator":
    st.header("Normality Calculator")
    volume = st.number_input("Enter the volume of the solution (in liters):", min_value=0.0, step=0.1)
    mass = st.number_input("Enter the mass of the solute (in grams):", min_value=0.0, step=0.1)
    molar_mass = st.number_input("Enter the molar mass of the solute (in g/mol):", min_value=0.0, step=0.1)
    acid_or_base = st.selectbox("Is the solute an acid or a base?", ["Acid", "Base"])
    number_of_h_or_oh = st.number_input("Enter the number of H+ or OH- ions produced per molecule of the acid or base:", min_value=1, step=1)

    if st.button("Calculate"):
        if acid_or_base == "Acid":
            normality = (mass / molar_mass) * number_of_h_or_oh / volume
            st.write(f"The normality of the acid is {normality:.2f} N")
        else:
            normality = (mass / molar_mass) * number_of_h_or_oh / volume
            st.write(f"The normality of the base is {normality:.2f} N")
