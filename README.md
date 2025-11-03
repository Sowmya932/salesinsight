# 📈 SalesInsight AI

An **interactive sales analytics dashboard** built with **Streamlit**, **Pandas**, and **Scikit-learn** for analyzing and forecasting sales trends.  
Easily upload your data, view KPIs, visualize trends, and get automated future sales forecasts — all in one elegant interface.

---

## 🚀 Features

- 📊 Interactive data visualization  
- 💰 Key performance metrics (KPIs)  
- 🔮 6-month linear regression–based sales forecasting  
- 📤 Upload your own CSV file  
- ⬇️ Export forecast results  
- ⚙️ Configurable parameters via YAML  

---

## 🧩 Folder Structure

salesinsight/
│
├── app.py # Main Streamlit app
├── data_loader.py # Data loading logic
├── analysis.py # KPIs and forecasting logic
├── config.yaml # Configuration file
├── requirements.txt # Dependencies
├── data/
│ └── sample_sales.csv # Sample dataset
└── README.md # Project documentation



---

## 🛠️ Installation

### 1️⃣ Clone the repository
```bash
git clone 
cd salesinsight-ai

### 2️⃣ Create and activate a virtual environment

python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the app locally

streamlit run app.py


Then open your browser and navigate to 👉 http://localhost:8501/



