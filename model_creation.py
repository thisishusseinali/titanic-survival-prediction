import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
warnings.filterwarnings('ignore')
def model_creation():
  titanic_data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Titanic Survival Prediction/train.csv')
  # printing the first 5 rows of the dataframe
  # check the number of missing values in each column
  titanic_data.isnull().sum()
  # drop the "Cabin" column from the dataframe
  titanic_data = titanic_data.drop(columns='Cabin', axis=1)
  # replacing the missing values in "Age" column with mean value
  titanic_data['Age'].fillna(titanic_data['Age'].mean(), inplace=True)
  # replacing the missing values in "Embarked" column with mode value
  titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)
  titanic_data.replace({'Sex':{'male':0,'female':1}, 'Embarked':{'S':0,'C':1,'Q':2}}, inplace=True)
  X = titanic_data.drop(columns = ['PassengerId','Name','Ticket','Survived'],axis=1)
  Y = titanic_data['Survived']
  X = X.values
  Y = Y.values
  X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)
  model = LogisticRegression()
  # training the Logistic Regression model with training data
  model.fit(X_train, Y_train)
  # accuracy on training data
  X_train_prediction = model.predict(X_train)
  training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
  print('Accuracy score of training data : ', training_data_accuracy)
  # accuracy on test data
  X_test_prediction = model.predict(X_test)
  print(X_test_prediction)
  test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
  print('Accuracy score of test data : ', test_data_accuracy)
  dump(model,'saved_model.sav')
  print("Model Saved Succefull ! please check (/models/saved_model.sav)")