import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

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

