
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from natsort import natsorted, ns

# if not firebase_admin._apps:
#     cred = credentials.Certificate(st.secrets["firestore_keys_baby"])
#     firebase_admin.initialize_app(cred)

creds_dict = json.loads(decrypt(os.environ.get(
    ({
  "type": "service_account",
  "project_id": "streamlit-6ad82",
  "private_key_id": "7f70292cf2d75f6edfc4ba21fa9537c2c7ff864e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC264PWWmbhUOvL\nzmzWUEp6PmLUgCWWext/gJb2W7bVR5g5CIxT5f05lG6M3AQMj5IoAqx2Qk0zKtRV\nAvqOebCk8AfRWp3o2F8OutLUisOHt1UiD97gqn8BFMSYUY8EZn+Pxv3hnCrJIFfP\nACqRUtOitHL4hxROB1cA4UrXAix/SEYq77V9WDsNZGSxo25aUoDajvRYZyn4ZeMG\nUOfk85+R8hybhVafj9Vd7vRYj8130lC8Cg9pPFh6lwWLw98syxcJ5S54VZPP6A/T\nfyw03+It6ulQYgm+v5DjW7s0dZQiAMk43XT6XcrbGbECpyirKMqaNjRZLfnuZ3TO\nuVg5KcIfAgMBAAECggEACQSdcFDup4cUyOx5Yyt8MICo4K8cq0mQdn3Bc43b+rHX\n6F/qgyxgipktxhYGwRPG8eAH3qCwK6id5T8LWUDYm5kV2ZVtGZCpRxGg2UeqEiPQ\nt6gupcbiEgyTEKtcsKvY+B6oX5oSZe4JRjRM5PM/adMZo/UM5DfqaymwRd9ekDvL\nmPCQonL1OWNs2UsvPiNZn8RwT3Jm17J0cFSLl/pX+Pc9UKDfMBsHTMwMx3d5wEPR\nEOq2VH7P+sNWADIPXPfHUX6hDbl70UKRLAMndz5a/NC3iVdbYnuWWHUiXUe7BHpN\nrzbbXyteMrDISNtXNVLx8DJL+ICZUl1mb16eFgUL6QKBgQDfFpjDnudx58PcdS8Q\nKkyjSTjBSb5fYx/IqIH3zQ6/JrGNTsoUN4kR6oCRTjCoEVDmInPLbwFL5x9ztBpC\nogDhsvU3ej8sqitTlyoIcA1Sk0PpnOzq5Dkn8H7dJkBfQut1IoQ3a2uXt19mGNgD\n4JF//q9zyvmo/Cv+VWaVvIIVqwKBgQDR5+Ca8ycL1VAr8+AAlqlC+dbd5Dasd4nB\nuO1KN+ivCFpyT6X13p7HRJO9KoUUyDu+r8okqglA5zDVdv6BICG8zi+0F6MTqB+V\nSWFNuwMIa4hO2X9c/ArmcwXYPRsdj4IuVOY6TsnXYj5gBIpJGzzJhtP9lJO52lN8\nb0GwSs6pXQKBgEVHPymAr18wGiLcQUFD4YjTtExSGkyE+9nUeof5phq2aWz4isi8\ndlSZ/lMhdPq8ZeMRz+PdFQn9PEcyJvWKWbu9V2ljDTtRnSLYTrVQFtMN6Ikjsm8/\ncIB2ru7+cf8jSPuXPHf5Y/A5geay0GJj2stkzBepcN6JcSAKZVEauUsBAoGBAIxB\no1wGI04N3/8uerwJ79m39XHY/wto6JyQQ8Y263yhWUZOoDdU5MWDtjBNTBVh4kH9\nVlX/ZCWBFaldVJvVa5WsNEXjEW2eBlSLbsAwuMsUh0UgobDxHRt1Oi+OTSMIdFUf\nF6NYaBhKJiGkhv5oe8qxE8+6SqeCEgzwjnUM12BlAoGAUc4aBIuBYN/ewTzmQ/GJ\nsF4MuqiJ45Jh34saCKIiDycTHh5v1bAqV41ybyHsfMOjWFFWlRa1lN1GNRVaiUwh\nF0jPCWw2Bn6LPPI8hWdUcocMxjkm5C0WGZJoIXxmNjJD8H6o5sjSIXaQOb6YQHYg\nrcX2nbqp2koIlwEDucCIe5w=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-iawtw@streamlit-6ad82.iam.gserviceaccount.com",
  "client_id": "106402300995454004707",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-iawtw%40streamlit-6ad82.iam.gserviceaccount.com"
}
    ))))

creds = credentials.Certificate(creds_dict)
firebase_admin.initialize_app(creds)

# try:
#     app = firebase_admin.get_app()
# except ValueError as e:
#     cred = credentials.Certificate(st.secrets["firestore_keys_baby"])
#     firebase_admin.initialize_app(cred)

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

