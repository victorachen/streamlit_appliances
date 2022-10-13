
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
items = {'Washer':1,
         'Dryer':1,
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

st.write('https://forms.gle/pxtLTzNwjVGrUEZHA')
st.header('To Do Items:')
col1, col2, col3, col4 = st.columns(4)

def format(string):
    return string.replace('_', ' ')

def writetostreamlit(todoitem,col):
    collection = db.collection('Appliances').where("type", "==", todoitem).get()
    s = """"""
    if col == 1:
        col1.subheader(format(todoitem))
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                if entry!='type':
                    line = format(entry)
                    s+= line+'\n'+'\n'
        col1.code(s)
    if col == 2:
        col2.subheader(format(todoitem))
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                if entry!='type':
                    line = format(entry)
                    s+= line+'\n'+'\n'
        col2.code(s)
    if col == 3:
        col3.subheader(format(todoitem))
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                if entry!='type':
                    line = format(entry)
                    s+= line+'\n'+'\n'
        col3.code(s)
    if col == 4:
        col4.subheader(format(todoitem))
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                if entry!='type':
                    line = format(entry)
                    s+= line+'\n'+'\n'
        col4.code(s)

for i in items:
    writetostreamlit(i,items[i])

