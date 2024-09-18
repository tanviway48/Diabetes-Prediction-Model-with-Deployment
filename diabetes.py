import numpy as np
import pickle

# loading the saved model
loaded_model=pickle.load(open("diabetes_trained_model.sav",'rb'))

input_data=(4,110,92,0,0,37.6,0.191,30)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
# std_data=scaler.transform(input_data_reshaped)
# print(std_data)

prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')