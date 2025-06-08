
# 📊 NeoStats Excel Chatbot

**NeoStats Excel Chatbot** is an interactive data analysis assistant built using **Streamlit**, **Pandas**, **Plotly**, and **Ollama** (for local LLM processing). It allows users to upload an Excel file and ask natural language questions to derive insights instantly with summaries, charts, and tables.

---

## 🚀 Features

- ✅ Upload `.xlsx` Excel files
- 💬 Ask natural language questions (e.g., "What is the average sales?")
- 📈 Auto-generates visualizations: bar charts, histograms, line plots
- 🧠 Uses LLM (via `ollama`) to parse natural queries
- 🧹 Handles basic operations: mean, count, group by, filters
- 🔁 Query history and debug mode for transparency

---

## 📁 Project Structure

```
neostats-excel-chatbot/
│
├── app.py                        # Streamlit main app
├── requirements.txt              # Python dependencies
├── README.md                     # Project info
│
└── src/
    ├── query_processors.py       # Handles query parsing & processing
    ├── utils.py                  # Utilities like column normalization
    └── visualizations.py         # Chart generation with Plotly
```

---

## 🧠 Powered By

- **[Streamlit](https://streamlit.io/)** — for building the web app
- **[Ollama](https://ollama.com/)** — for local LLM querying (Mistral)
- **Pandas** — for DataFrame manipulation
- **Plotly** — for beautiful interactive charts

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/SainandaG/neostats-excel-chatbot.git
cd neostats-excel-chatbot
```

### 2. Install Python Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then install the requirements:

```bash
pip install -r requirements.txt
```

### 3. Install & Run Ollama (if not installed)

Install Ollama:  
👉 https://ollama.com/download

Pull the Mistral model locally:

```bash
ollama pull mistral
```

### 4. Run the App

```bash
streamlit run app.py
```

---

npm install -g localtunnel
lt --port 8501

password:152.57.105.37

## 💡 Example Questions You Can Ask

- "What is the average salary?"
- "Show a bar chart of count by department."
- "Count the number of employees older than 30."
- "Plot a histogram of sales data."

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sai Nanda Gurram**  
[GitHub](https://github.com/SainandaG) • [LinkedIn](https://linkedin.com/in/SainandaG)
