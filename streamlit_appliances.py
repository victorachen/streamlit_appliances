
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from natsort import natsorted, ns
import json
from google.oauth2 import service_account

# if not firebase_admin._apps:
#     cred = credentials.Certificate(st.secrets["firestore_keys_baby"])
#     firebase_admin.initialize_app(cred)

#to do: try this https://levelup.gitconnected.com/4-easy-steps-to-set-up-a-firestore-database-for-your-streamlit-apps-825c5de5b5bc#5ea8\

# try:
#     app = firebase_admin.get_app()
# except ValueError as e:
#     cred = credentials.Certificate(st.secrets["firestore_keys_baby"])
#     firebase_admin.initialize_app(cred)

key_dict = json.loads(st.secrets['firestore_keys_baby'])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds)

st.set_page_config(
    page_title='To Do Items',
    layout="wide",
    initial_sidebar_state="expanded",
    )

padding_top = 0
#the margins to be made narrower?
st.markdown(f"""
    <style>
        .reportview-container .main .block-container{{
            padding-top: {padding_top}rem;
        }}
    </style>""",
    unsafe_allow_html=True,
)

#testing some shit here (css styling)
# st.markdown(""" <style> .font {
# font-size:20px ; font-family: 'Cooper Black'; color: #FF9633;}
# </style> """, unsafe_allow_html=True)
#
# st.markdown('<p class="font">Guess the object Names</p>', unsafe_allow_html=True)

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

# st.header('To Do Items:')
col1, col2, col3, col4 = st.columns(4)

def format(string):
    return string.replace('_', ' ')

def writetostreamlit(todoitem,col):
    collection = db.collection('Appliances').where("type", "==", todoitem).get()
    L = []
    s = """"""
    # put everything into a list -> alphabetize list --> put alpha list into """ """ string.
    if col == 1:
        col1.caption(format(todoitem))
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                if entry!='type':
                    L.append(format(entry))
        Sorted_L = natsorted(L, alg=ns.IGNORECASE)
        for i in Sorted_L:
            s+= '- '+ i +'\n'
        col1.markdown(s)
    if col == 2:
        col2.caption(format(todoitem))
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                if entry != 'type':
                    L.append(format(entry))
        Sorted_L = natsorted(L, alg=ns.IGNORECASE)
        for i in Sorted_L:
            s += '- ' + i + '\n'
        col2.markdown(s)
    if col == 3:
        col3.caption(format(todoitem))
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                if entry != 'type':
                    L.append(format(entry))
        Sorted_L = natsorted(L, alg=ns.IGNORECASE)
        for i in Sorted_L:
            s += '- ' + i + '\n'
        col3.markdown(s)
    if col == 4:
        col4.caption(format(todoitem))
        for doc in collection:
            d = doc.to_dict()
            for entry in d:
                if entry != 'type':
                    L.append(format(entry))
        Sorted_L = natsorted(L, alg=ns.IGNORECASE)
        for i in Sorted_L:
            s += '- ' + i + '\n'
        col4.markdown(s)

for i in items:
    writetostreamlit(i,items[i])

st.write('')
st.write('')
st.write('Make Updates Here: https://forms.gle/pxtLTzNwjVGrUEZHA')

