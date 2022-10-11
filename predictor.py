import numpy as np
from joblib import dump, load
import warnings
warnings.filterwarnings('ignore')
def predict_class(input_data):
  saved_model  = load('models/saved_model.sav')
  # changing input data to a numpy array
  data = np.asarray(input_data)
  # reshape the numpy array
  data = data.reshape(1,-1)
  # standardize the data
  prediction = saved_model.predict(data)
  if (prediction[0] == 1):
    result = "This person may have survived"
  else:
    result = "This person may have not survived"
  return result
