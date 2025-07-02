# 🎓 College Feedback Classifier

This project uses **IBM watsonx.ai** to automatically classify student feedback into relevant categories such as **Academics**, **Facilities**, and **Administration**.  
> ⚠️ Note: This project **does not perform sentiment analysis** — the focus is purely on identifying the **category** or **topic area** of the feedback.

---

## 🧠 Project Objective

To streamline and automate the classification of student feedback so institutions can efficiently route concerns, suggestions, or praise to the appropriate departments.

---

## ⚙️ How It Works

- **Input**: A CSV file containing open-ended student feedback with optional sentiment labels.
- **Model**: The few-shot classification capability of **IBM watsonx.ai** analyzes each feedback entry and predicts its relevant **category**.
- **Output**: The original CSV file is updated with a new column named **Predicted Category**.

---

## 🧪 Sample Output

| Feedback                                             | Sentiment | Category        | Predicted Category |
|------------------------------------------------------|-----------|------------------|---------------------|
| The professors explain concepts very clearly.        | positive  | Academics        | Academics           |
| The canteen food is not hygienic.                    | negative  | Facilities        | Facilities          |
| The admin staff is friendly and helpful.             | positive  | Administration    | Administration      |
| The online learning platform is easy to use.         | positive  | Academics         | Academics           |

> ✅ *Sentiment is not predicted — it is assumed to be pre-existing in the dataset for context.*

---

## 🛠 Tools Used

- 🧠 **IBM watsonx.ai** – for few-shot text classification  
- 📊 **Jupyter Notebook / Python** – for reading/writing CSV and preparing input/output  
- 🗃️ **CSV Files** – for input and output feedback data  
- 🧾 **GitHub** – for version control and collaboration

---

## 📂 Files

- `college_feedback_classified.csv` – Final output with a `Predicted Category` column  
- `feedback_data.csv` – Input file containing raw feedback and sentiment  
- `notebook.ipynb` – Jupyter notebook to run the classification  
- `README.md` – Project description (this file)

---

## 🗃️ Use Cases

- Automatically categorize large-scale student surveys  
- Help academic institutions quickly identify department-specific feedback  
- Save time by avoiding manual classification of open-text responses  
- Improve routing of grievances, praise, or suggestions to respective teams

---

## 👨‍💻 Developed By

**Nitheeshwar S**  
Feel free to reach out for questions, collaboration, or feedback!

📬 Email: `your.email@example.com`  
🔗 LinkedIn: [linkedin.com/in/nitheeshwar-s](https://linkedin.com/in/nitheeshwar-s)  
📁 Project Repo: [GitHub - College Feedback Classifier](#)

---

