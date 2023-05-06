import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Chemistry App", page_icon=":microscope:")
st.title("Chemistry App")

menu = [ "Molarity Calculator", "Gas Laws Calculator"]
choice = st.sidebar.selectbox("Select a tool", menu)

if choice == "Periodic Table":
    st.header("Periodic Table")
    pt = pd.read_csv("periodic_table.csv")
    st.dataframe(pt)
    
    element = st.text_input("Enter an element symbol:")
    if element:
        selected_element = pt[pt["Symbol"] == element.capitalize()]
        if not selected_element.empty:
            st.subheader(f"{selected_element.iloc[0]['Name']} ({selected_element.iloc[0]['Symbol']})")
            st.write(f"Atomic Number: {selected_element.iloc[0]['AtomicNumber']}")
            st.write(f"Atomic Mass: {selected_element.iloc[0]['AtomicMass']}")
            st.write(f"Category: {selected_element.iloc[0]['Category']}")
            st.write(f"Electron Configuration: {selected_element.iloc[0]['ElectronConfiguration']}")
        else:
            st.warning("Invalid element symbol. Please enter a valid symbol.")
            
elif choice == "Molarity Calculator":
    st.header("Molarity Calculator")
    volume = st.number_input("Enter the volume of the solution (in liters):", min_value=0.0, step=0.1)
    mass = st.number_input("Enter the mass of the solute (in grams):", min_value=0.0, step=0.1)
    molar_mass = st.number_input("Enter the molar mass of the solute (in g/mol):", min_value=0.0, step=0.1)
    
    if st.button("Calculate"):
        molarity = mass / (molar_mass * volume)
        st.write(f"The molarity of the solution is {molarity:.2f} M")
        
elif choice == "Gas Laws Calculator":
    st.header("Gas Laws Calculator")
    variables = ["Pressure (P)", "Volume (V)", "Temperature (T)", "Number of moles (n)"]
    variable1 = st.selectbox("Select the first variable:", variables)
    variable2 = st.selectbox("Select the second variable:", variables)
    if variable1 == variable2:
        st.warning("Please select two different variables.")
    else:
        value1 = st.number_input(f"Enter the value of {variable1}:", min_value=0.0, step=0.1)
        value2 = st.number_input(f"Enter the value of {variable2}:", min_value=0.0, step=0.1)
        R = 0.0821 # L·atm/K·mol
        if variable1 == "Pressure (P)" and variable2 == "Volume (V)":
            st.write(f"The number of moles of gas is {value1 * value2 / (R * st.number_input('Enter the temperature (in K):', min_value=0.0, step=0.1)):.2f}")
        elif variable1 == "Volume (V)" and variable2 == "Temperature (T)":
            st.write(f"The pressure of the gas is {value1 * R * st.number_input('Enter the number of moles of gas:', min_value=0.0, step=0.1) / value2:.2f} atm")
        elif variable1== "Volume (V)" and variable2 == "Temperature (T)":
            st.write(f"The number of moles of gas is {value1 * value2 / (R * st.number_input('Enter the volume (in L) of gas:', min_value=0.0, step=0.1)):.2f}")
        elif variable1 == "Number of moles (n)" and variable2 == "Volume (V)":
            st.write(f"The pressure of the gas is {value1 * R * st.number_input('Enter the temperature (in K):', min_value=0.0, step=0.1) / value2:.2f} atm")
        elif variable1 == "Number of moles (n)" and variable2 == "Temperature (T)":
            st.write(f"The pressure of the gas is {value1 * R * st.number_input('Enter the volume (in L) of gas:', min_value=0.0, step=0.1) / value2:.2f} atm")
        elif variable1 == "Pressure (P)" and variable2 == "Number of moles (n)":
            st.write(f"The volume of the gas is {value1 * value2 * R / st.number_input('Enter the temperature (in K):', min_value=0.0, step=0.1):.2f} L")
        elif variable1 == "Volume (V)" and variable2 == "Number of moles (n)":
            st.write(f"The pressure of the gas is {value1 * value2 * R / st.number_input('Enter the temperature (in K):', min_value=0.0, step=0.1):.2f} atm")