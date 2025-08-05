# 🔍 Semantic Search with Sentence Embeddings

This project is a simple yet powerful **semantic search demo** built using [Sentence Transformers](https://www.sbert.net/) and [Streamlit](https://streamlit.io/). It allows you to input a query sentence and returns the most semantically similar sentences from a predefined set, based on sentence embeddings and cosine similarity.

---

## 🚀 Features

- Uses the `all-mpnet-base-v2` pre-trained model from Sentence Transformers
- Computes semantic similarity using cosine similarity
- Interactive interface with Streamlit
- Adjustable number of top similar results
- Real-time sentence encoding and search

---

## 🧠 Example Sentences

The following sentences are embedded and stored in memory:

- "I love playing football."
- "Soccer is a fun sport to play."
- "The weather is sunny today."
- "He enjoys watching football games."
- "It is raining outside."
- "I prefer rainy days."
- "Today is a cold and wet day."

You can enter your own query (e.g. `"I enjoy soccer"`) and the app will find the closest matching sentences semantically.

---

## 🛠️ Requirements

- Python 3.7+
- `sentence-transformers`
- `streamlit`
- `scikit-learn`
- `numpy`

### 📦 Install dependencies:

```bash
pip install -r requirements.txt
````

Or manually:

```bash
pip install sentence-transformers streamlit scikit-learn numpy
```

---

## ▶️ How to Run

Start the Streamlit app by running the following command in the terminal:

```bash
streamlit run your_script_name.py
```

Replace `your_script_name.py` with the name of your file.

---

## 📸 Screenshot

![semantic search demo](https://user-images.githubusercontent.com/your_screenshot_here) <sub>*Replace with your own screenshot if needed*</sub>

---

## 📂 Folder Structure (optional)

```
├── semantic_search.py
├── requirements.txt
└── README.md
```

---

> This is a great starting point for building more advanced NLP applications like semantic document search, FAQ bots, or intent matching systems.


- فایل `requirements.txt` رو هم برات بسازم ✅  
- نمونه تصویر (Screenshot) بسازم برای بخش 📸  
- نسخه پیشرفته‌تر با ورودی دیتاست یا فایل متنی طراحی کنم ✅

فقط کافیه بگی تا کمک کنم.
```
