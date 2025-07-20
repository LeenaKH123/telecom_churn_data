# telecom_churn_data
Telecom Customer Churn – Exploratory Data Analysis (EDA)
This project explores the behavioral patterns behind customer churn in the telecom sector using real-world data. The goal is to identify churn drivers and translate them into actionable business insights through data cleaning, analysis, and visual storytelling.

This is Part 1 of a two-part project. Part 2 focuses on predictive modeling using logistic regression.

🔍 Project Objectives
Understand what factors contribute to customer churn
Clean and preprocess a real-world telecom dataset
Perform visual exploratory data analysis (EDA)
Identify business-relevant patterns
Prepare for machine learning in the next stage

📁 Folder Structure
bash
Copy
Edit
telecom_churn_eda/
├── eda_churn.py            # Python script for loading, cleaning, and plotting
├── Telco-Customer-Churn.csv # Dataset (from Kaggle)
├── churn_tenure.png        # Plot: Churn vs Tenure
├── churn_contract.png      # Plot: Churn by Contract Type
├── requirements.txt        # Python dependencies
└── README.md               # Project overview



📊 Sample Visualizations
🖼️ Churn Distribution by Tenure
Shows that most churn happens in the first 20 months.
🖼️ Churn by Contract Type
Shows that month-to-month customers are at highest risk of churn.


📖 Related Article
This project is featured in the Medium article:

▶️ Read Part 1:
https://leenamk.medium.com/part-1-how-to-uncover-telecom-churn-drivers-with-data-a-real-business-use-case-75ee47ff4985

🧪 Coming Soon:
Part 2 – Building a Churn Prediction Model That Works

🧰 How to Run the Code
1. Clone the repository:
git clone https://github.com/LeenaKH123/telecom_churn_eda.git
cd telecom_churn_eda


2. (Recommended) Create a virtual environment:
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt
Run the script:

4. Run the script
python eda_churn.py


🧪 Dependencies
Python 3.8+
pandas
matplotlib
seaborn

These are listed in requirements.txt

📌 Future Work
✅ Part 2: Train and evaluate a logistic regression churn prediction model
✅ Use AUC, precision, recall, and feature importance
✅ Deploy model scoring and simulate retention strategies

