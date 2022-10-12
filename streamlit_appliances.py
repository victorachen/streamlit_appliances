print('whateverz')
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
    cred = credentials.Certificate(st.secrets["firestore_keys_baby"])
    firebase_admin.initialize_app(cred)

db = firestore.client()
entire_collection = db.collection('Appliances').get()

for doc in entire_collection:
    d = doc.to_dict()
    for entry in d:
        line = entry + ': ' + d[entry]
        st.write(line)