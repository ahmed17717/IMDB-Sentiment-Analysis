import streamlit as st
import joblib
import io
from huggingface_hub import hf_hub_download

# Download model from Hugging Face Hub
model_path = hf_hub_download(
    repo_id="ahmed159260/imdb-sentiment-analysis-model",
    filename="sentiment_model.pkl"
)
vectorizer_path = hf_hub_download(
    repo_id="ahmed159260/imdb-sentiment-analysis-model",
    filename="vectorizer.pkl"
)

# Load them
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

st.title("🎬 IMDb Sentiment Analysis")
st.write("Type a movie review and find out if it's Positive or Negative!")

# Input box
review = st.text_area("Enter your review here:")

if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        review_vec = vectorizer.transform([review])
        prediction = model.predict(review_vec)[0]
        sentiment = "🌟 Positive" if prediction == 1 else "💔 Negative"
        st.success(f"Prediction: {sentiment}")





