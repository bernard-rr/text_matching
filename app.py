import streamlit as st
from helpers import process_uploaded_files, match_names

def display_results(matched_data):
    st.write("Matching results:")
    st.table(matched_data)


def main():
    st.title("Name Matching App")
    
    uploaded_file1 = st.file_uploader("Upload File 1 (CSV)", type=["csv"])
    uploaded_file2 = st.file_uploader("Upload File 2 (CSV)", type=["csv"])
    
    if uploaded_file1 and uploaded_file2:
        file1_data, file2_data = process_uploaded_files(uploaded_file1, uploaded_file2)
        matched_data = match_names(file1_data, file2_data)
        display_results(matched_data)

if __name__ == "__main__":
    main()
