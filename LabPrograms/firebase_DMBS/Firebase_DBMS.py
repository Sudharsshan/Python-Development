import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("C:/Games/Python Dev folder/Python-Development/LabPrograms/firebase_DMBS/pythonDevelopment.json")
app = firebase_admin.initialize_app(cred)
firestore_client = firestore.client()

while(True):
    userChoice = int(input('Please enter:\n1. Add data\n2. Update data\n3. delete data \n4. Exit'))
    match userChoice:
        case 1: # Add data
            data = {"AverageDemant": 400, "FeederID": 2, "FeederName": "Kengeri", "MaxDemand": 800}
            firestore_client.collection("PowerStation").document("3").set(data)
        case 2: # Update data
            coll_ref = firestore_client.collection("PowerStation").document("subStation")
            coll_ref.update({"MaxDemand": 1400})
        case 3: # Delete data
            firestore_client.collection("PowerStation").document("subStation").delete()
            coll_ref = firestore_client.collection('PowerStation')
        case 4: # Exit loop
            break

#display the data
docs = coll_ref.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')