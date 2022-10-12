
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
    cred = credentials.Certificate(st.secrets["firestore_keys_baby"])
    firebase_admin.initialize_app(cred)

st.set_page_config(
    page_title='Vacancies!',
    layout="wide",
    initial_sidebar_state="expanded",
    )

items = ['Washer_(Side_by_Side)','Dryer_(Side_by_Side)','Washer_&_Dryer_(Stackable)','Fridge','Stove','Outside_Cleanup','ReGlazing','Stairs','Awning','AC_unit','Roof_Foaming','Granite_Countertops']

db = firestore.client()
entire_collection = db.collection('Appliances').get()

st.write('Below is shit we need to do (lets goooo)')
col1, col2, col3, col4, col5 = st.columns(5)

def writetostreamlit(todoitem):
    col1.subheader(todoitem)
    collection = db.collection('Appliances').where("type", "==", todoitem).get()
    for doc in collection:
        d = doc.to_dict()
        for entry in d:
            line = entry + ': ' + d[entry]
            col1.markdown(line)

for i in items:
    writetostreamlit(i)