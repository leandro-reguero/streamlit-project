from pickle import load
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# accediendo a los datos
model = load(open("models/rfc_default_21.sav", "rb"))
@st.cache_data(ttl= 60*5, max_entries=20)
def load_data():
    df = pd.read_csv("data/processed/balanced_data.csv")
    return df

df = load_data()

# vectorizador:
def word(password):
    character=[]
    for i in password:
        character.append(i)
    return character

X = np.array(df["password"])
y = np.array(df["strength"])
tfidf = TfidfVectorizer(tokenizer=word, lowercase=False, token_pattern=None)
X = tfidf.fit_transform(X)

class_dict = {
    "0": "Weak",
    "1": "Medium",
    "2": "Strong"
}

st.title("Password strenght test")

user_password = st.text_area("Enter your password: ")



if st.button("Check vulnerability"):

    data = tfidf.transform([user_password]).toarray()
    prediction = model.predict(data)
    pred_class = class_dict[str(prediction[0])]
    st.write("Password strenght:", pred_class)