import requests
from requests import status_codes
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation


st.write("""
# SMS Classification app
""")

st.write('Input pesan SMS beserta nomor pengirim')

nomer = st.text_input("Masukan No.HP pengirim")
pesan = st.text_input("Masukan pesan SMS")
nomer = [nomer]
pesan = [pesan]

datafile = st.file_uploader("Upload CSV",type=['csv'])
if datafile is not None:
   file_details = {"FileName":datafile.name,"FileType":datafile.type}

sw_indo = stopwords.words('indonesian') + list(punctuation)
df = pd.read_csv(datafile)
df.head()
X = df.Teks
y = df.label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    stratify=y, random_state=42)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from jcopml.tuning import random_search_params as rsp


pipeline = Pipeline([
    ('prep', TfidfVectorizer(tokenizer=word_tokenize, stop_words=sw_indo)),
    ('algo', LogisticRegression(solver='lbfgs', n_jobs=-1, random_state=42))
])

model = RandomizedSearchCV(pipeline, rsp.logreg_params, cv=3, n_iter=50, n_jobs=-1, verbose=1, random_state=42)
model.fit(X_train, y_train)

st.subheader('Prediction')
def check(pesan,nomer):
    hasil = model.predict(pesan), model.predict_proba(pesan)
    hasil1 = hasil[0]
    hasil2 = hasil[1]

    if int(hasil1) == 1:
        st.write(nomer[0], " mengirim SPAM")
        st.write("probabilitas ( 0 = bukan spam, 1 = spam)", hasil2)
        requests.post('http://localhost:3000/api/Spammer',json=
        {
            "$class": "org.example.smsc.Spammer",
            "phoneNumber": nomer,
             "description": "SPAM",
            "owner": "spam"
        })
        ## Belum dapet cara extract status code ##
        # if status_codes == 200:
        #     st.write("Nomor SPAM berhasil disimpan dalam Blockchain!")
        # else:
        #     st.write("Nomor SPAM gagal dikirim ke blockchain...")

    else:
        st.write(nomer[0], " adalah pesan asli")
        st.write("probabilitas ( 0 = bukan spam, 1 = spam)", hasil2)
        print("ini bukan spam")
        requests.post('http://localhost:3000/api/Spammer',json=
        {
        "$class": "org.example.smsc.Spammer",
        "phoneNumber": nomer,
        "description": "bukan SPAM",
        "owner": "bukan"
        }
        )
        # st.write(status_codes)
        # if status_codes == 200:
        #     st.write("Nomor berhasil disimpan dalam Blockchain sebagai bukan pengirim spam")
        # else:
        #     st.write("Nomor gagal dikirim ke blockchain...")


check(pesan, nomer)