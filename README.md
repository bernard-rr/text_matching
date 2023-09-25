# Name Matching Streamlit App

This Streamlit app allows users to upload two CSV files and perform name matching using a Sentence Transformer model. It then displays the matching results in a table and provides an option to download the results in CSV format.

**Live Deployment**: [Text Matching App on Streamlit Cloud](https://textmatching.streamlit.app/)

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Getting Started

### Prerequisites

To run this Streamlit app locally, you need the following prerequisites:

- Python 3.x
- Pip (Python package manager)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/bernard-rr/text_matching.git
   ```


1. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Online Usage (Live Deployment)**:

   You can use the app directly online by visiting the following link:

   [Text Matching App on Streamlit Cloud](https://textmatching.streamlit.app/)

1. **Local Usage**:

   If you want to run the app locally for development or customization:

   ```bash
   streamlit run app.py
   ```

   The app will open in your default web browser.

The Text Matching Streamlit App is designed to match names in the first uploaded CSV file to the row with the highest similarity score in the second uploaded CSV file. The app assumes the following data structure:

- **File 1 (CSV)**: This file should contain a maximum of two columns. Typically, the first column is used to store unique codes or identifiers, and the second column contains names you want to match.

- **File 2 (CSV)**: This file should contain a maximum of one column. It usually contains names that you want to match against those in the first file.

Here's how the app works:

1. **Upload CSV Files**:
   - Use the "Upload File 1 (CSV)" button to upload the first CSV file. Ensure that it adheres to the specified structure.
   - Use the "Upload File 2 (CSV)" button to upload the second CSV file with the names you want to match.

1. **Name Matching**:
   - The app processes the uploaded files and computes similarity scores between the names in the second file and those in the first file using a Sentence Transformer model.
   - For each name in the second file, the app identifies the best match from the first file based on the highest similarity score.
   - It also calculates and displays the similarity score for each match.

1. **Matching Results Display**:
   - The app displays the matching results in a table format, showing the following columns:
     - "Name from File 2": The name from the second uploaded file.
     - "Matched Code": The code or identifier corresponding to the best match from the first file.
     - "Matched Name from File 1": The name from the first file that has the highest similarity score with the name from the second file.
     - "Similarity Score": The similarity score between the names, indicating the degree of similarity.

1. **Download Matching Results (CSV)**:
   - Users can download the matching results in CSV format by clicking the "Download Matching Results (CSV)" button. The downloaded CSV file contains the same information as displayed in the table.

By following these steps, users can efficiently match names and obtain detailed matching results for further analysis or reference.

**Note**: For more accurate results, it is recommended to provide column headers in the uploaded CSV files.


## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository to your GitHub account.

2. Clone your forked repository to your local machine:

   ```bash
   git clone https://github.com/bernard-rr/text_matching.git
   ```

3. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Make your changes and commit them:

   ```bash
   git commit -m "Add your commit message here"
   ```

5. Push your changes to your forked repository:

   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request (PR) from your forked repository to the original repository on GitHub. Describe your changes and explain why they should be merged.

7. Your PR will be reviewed, and once approved, it will be merged into the main branch of the original repository.


## Contact

For feedback and inquiries, please feel free to reach out to the project owner:

- Email: [bernardchidi5@gmail.com](mailto:bernardchidi5@gmail.com?subject=Feedback%20on%20Text%20Matching%20App)
