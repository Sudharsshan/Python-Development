import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("C:/Games/Python Dev folder/Python-Development/LabPrograms/firebase_DMBS/pythonDevelopment.json")
app = firebase_admin.initialize_app(cred)
firestore_client = firestore.client()

coll_ref = firestore_client.collection('PowerStation')
docs = coll_ref.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')