from pickle import load
import streamlit as st


model = load(open("models/rfc_default_21.sav", "rb"))
tfidf = load(open("models/tfidf_vectorizer.sav", "rb"))

with open("models/tfidf_vectorizer.sav", "rb") as f:
    tfidf = load(f)


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