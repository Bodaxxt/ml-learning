import streamlit as st
import pickle
import re
import string

# Page configuration
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="centered"
)

# Text cleaning function matching the model training
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load saved vectorizer and model
@st.cache_resource
def load_artifacts():
    vectorizer_path = os.path.join(BASE_DIR, 'vectorizer.pkl')
    model_path = os.path.join(BASE_DIR, 'model.pkl')
    with open(vectorizer_path, 'rb') as f:
        vectorizer = pickle.load(f)
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return vectorizer, model

vectorizer, model = load_artifacts()

# App UI
st.title("📩 SMS Spam Detector")
st.write("Enter an SMS message below to classify whether it is **Ham** (Legitimate) or **Spam**.")

user_input = st.text_area("Message Content:", placeholder="Type or paste SMS message here...", height=120)

if st.button("Classify Message", type="primary"):
    if user_input.strip() == "":
        st.warning("Please enter a message first.")
    else:
        # Preprocess input
        cleaned_input = clean_text(user_input)
        features = vectorizer.transform([cleaned_input])
        
        # Predict
        prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]
        classes = model.classes_
        
        prob_dict = dict(zip(classes, probabilities))
        
        st.divider()
        if prediction == "spam":
            st.error(f"🚨 **Prediction: SPAM** (Confidence: {prob_dict['spam']*100:.1f}%)")
        else:
            st.success(f"✅ **Prediction: HAM (Legitimate)** (Confidence: {prob_dict['ham']*100:.1f}%)")
            
        st.caption(f"Raw Input Cleaned: `{cleaned_input}`")
