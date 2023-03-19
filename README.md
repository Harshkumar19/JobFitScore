# JobFitScore
For firebase connectivity refer the following information
To integrate the code with Firebase, you can use the Firebase Admin SDK to retrieve the data from Firebase and convert it to a Pandas DataFrame that can be used as input for the model. Here is an example code snippet to retrieve data from Firebase and use it as input for the model:

import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Retrieve data from Firebase
docs = db.collection('collection_name').stream()
data = []
for doc in docs:
    doc_data = doc.to_dict()
    data.append(doc_data)
    
# Convert the data to a Pandas DataFrame
input_data = pd.DataFrame(data)

# Preprocess the input data using the same transformer as used for the training data
X_input = preprocessor.transform(input_data[features])

# Predict the JFS for the input data
y_pred = model.predict(X_input)
print(y_pred)
