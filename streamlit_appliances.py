
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

#dictionary keys represent which column you want them in
items = {'Washer_(Side_by_Side)':1,
         'Dryer_(Side_by_Side)':1,
         'Washer_&_Dryer_(Stackable)':1,
         'Fridge':2,
         'Stove':2,
         'Outside_Cleanup':2,
         'ReGlazing':3,
         'Stairs':3,
         'Awning':3,
         'AC_unit':4,
         'Roof_Foaming':4,
         'Granite_Countertops':4}

db = firestore.client()
entire_collection = db.collection('Appliances').get()

st.write('Below is shit we need to do (lets goooo)')
col1, col2, col3, col4 = st.columns(4)

def writetostreamlit(todoitem,col):
    collection = db.collection('Appliances').where("type", "==", todoitem).get()
    if col == 1:
        col1.subheader(todoitem)
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                line = entry + ': ' + d[entry]
                col1.markdown(line)
    if col == 2:
        col2.subheader(todoitem)
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                line = entry + ': ' + d[entry]
                col2.markdown(line)
    if col == 3:
        col3.subheader(todoitem)
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                line = entry + ': ' + d[entry]
                col3.markdown(line)
    if col == 4:
        col4.subheader(todoitem)
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                line = entry + ': ' + d[entry]
                col4.markdown(line)

for i in items:
    writetostreamlit(i,items[i])