import streamlit as st
from helpers import process_uploaded_files, match_names, prepare_download
import pandas as pd
import urllib.parse

def display_results(matched_data):
    st.write("Matching results:")
    st.table(matched_data)

def main():
    st.title("Text Matching App")

    st.markdown("[Read the instructions here](https://github.com/bernard-rr/text_matching#usage)")

    email = "bernardchidi5@gmail.com"
    subject = urllib.parse.quote("Feedback on the Text Matching App")
    feedback_link = f"[Send me feedback](mailto:{email}?subject={subject})"
    st.markdown(feedback_link)
    
    uploaded_file1 = st.file_uploader("Upload File 1 (CSV)", type=["csv"])
    uploaded_file2 = st.file_uploader("Upload File 2 (CSV)", type=["csv"])
    
    if uploaded_file1 and uploaded_file2:
        file1_data, file2_data = process_uploaded_files(uploaded_file1, uploaded_file2)
        matched_data = match_names(file1_data, file2_data)
        display_results(matched_data)
        
        # Add a download button for the matching results
        download_button = st.download_button(
            label="Download Matching Results (CSV)",
            data=prepare_download(matched_data),
            key="download_button",
            mime='text/csv'  # Specify the MIME type as CSV
        )

if __name__ == "__main__":
    main()
