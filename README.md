# 🎬 IMDb Sentiment Analysis

A machine learning-powered web app that predicts whether a movie review is **positive** or **negative**.  
This project demonstrates the application of **Natural Language Processing (NLP)**, sentiment classification, and model deployment.

---

## 🚀 Demo

🌐 [Live App](https://imdb-sentiment-analysis-jgnxtzby3uuwsimweuny3s.streamlit.app/)

---

## 📌 Features

- Predicts sentiment (**positive / negative**) from IMDb reviews  
- Uses a trained **Logistic Regression Classifier** with TF-IDF vectorization  
- Clean and simple UI for text input and results  
- Lightweight and easy to deploy  

---

## 🧠 ML Model Details

- **Model**: Logistic Regression Classifier  
- **Vectorization**: TF-IDF (Term Frequency–Inverse Document Frequency)  
- **Dataset**: [IMDb Movie Reviews Dataset]([https://ai.stanford.edu/~amaas/data/sentiment/](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews))  
- **Target**: Sentiment (Positive / Negative)  

---

## ☁️ Why Hugging Face Hub?

Since model files (`sentiment_model.pkl` and `vectorizer.pkl`) can be **large**, they are not stored directly in the GitHub repo.  
Instead, they are hosted on **Hugging Face Hub**, which allows:

- Free and secure storage of ML models  
- Easy integration with Python apps via `huggingface_hub`  
- Keeping the GitHub repo lightweight and under size limits  
- Option to keep models **private** while still using them in deployment  

In this project, the app downloads the trained model and vectorizer at runtime using the Hugging Face Hub.

---

## 🛠 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python, Scikit-learn  
- **NLP**: NLTK, Scikit-learn TF-IDF  
- **Data Handling**: Pandas, NumPy  
- **Model Serialization**: Joblib  
- **Model Hosting**: Hugging Face Hub  
- **Deployment**: Streamlit Cloud  

---

## 🙋‍♂️ Author

**Ahmed Ragab**  
🎓 Final Year CS Student | AI & Machine Learning Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/ahmed-ragab-29a547218/)
