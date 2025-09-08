import streamlit as st
import joblib
import os

# Load model and vectorizer
model_path = os.path.join("models", "sentiment_model.pkl")
model = joblib.load(model_path)
vectorizer_path = os.path.join("models", "vectorizer.pkl")
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



