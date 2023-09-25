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

3. Upload two CSV files using the "Upload File 1 (CSV)" and "Upload File 2 (CSV)" buttons. Make sure both files contain a column with names you want to match.

4. The app will perform the name matching using a Sentence Transformer model and display the matching results in a table.

5. To download the matching results in CSV format, click the "Download Matching Results (CSV)" button.

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
