import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# Load the training dataset
train_data = pd.read_csv("dataset.csv")
train_data.fillna(train_data.mean(), inplace=True)


# Define the features to be used for training the model
features = ["Education", "Experience", "Skill1", "Skill2", "Skill3"]

# Preprocess the training data using one-hot encoding and standard scaling
preprocessor = ColumnTransformer(transformers=[
    ("cat", OneHotEncoder(handle_unknown='ignore'),
     ["Education", "Skill1", "Skill2", "Skill3"]),
    ("num", StandardScaler(), ["Experience"])
])
X_train = preprocessor.fit_transform(train_data[features])
y_train = train_data["JFS"]

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Load the input data
input_data = pd.DataFrame({
    "Education": ["BE"],
    "Experience": [3],
    "Skill1": ["HTML/CSS"],
    "Skill2": ["Python"],
    "Skill3": ["Analysis"]
})

# Preprocess the input data using the same transformer as used for the training data
X_input = preprocessor.transform(input_data[features])

# Predict the JFS for the input data
y_pred = model.predict(X_input)
print(y_pred)
