
# Diabetes Predection Model

A pre-trained Support Vector Machine (SVM) model, saved using the pickle module, is used to make predictions on whether a person is diabetic based on input features.

The pickle.load function loads the saved SVM model, which was trained previously for diabetes prediction and stored in the file diabetes_trained_model.sav.

The model makes a prediction on the reshaped input data. The predict method returns a value (either 0 or 1), where 0 typically indicates "non-diabetic" and 1 indicates "diabetic".

The model used in this code is an SVM (Support Vector Machine), a supervised machine learning algorithm commonly used for classification tasks like predicting diabetes in this case. The SVM was trained on diabetes-related data, and the trained model was saved using pickle for future predictions.




## Deployment

I developed and deployed a machine learning model for diabetes prediction in a web application using Streamlit, a popular Python framework for building data-driven applications with ease. The model, trained using a Support Vector Machine (SVM), was integrated into the web app to allow users to input relevant health parameters and receive predictions on whether they are likely to have diabetes.


#### Real-time Predictions: 
Upon submitting the data, the web app uses the model to predict if the user is diabetic or not, displaying the result instantly in a clear and interpretable manner.

#### Scalability and Accessibility: 
Streamlit's simplicity allowed for the rapid deployment of the web app, making the predictive model easily accessible through a browser.

- This solution enables users to interact with the machine learning model in real-time, providing a practical demonstration of AI in healthcare.


## 📌Some essential libraries used 


```bash
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
```


## Screenshots

![Screenshot 2024-09-19 192810](https://github.com/user-attachments/assets/08c44940-0e09-405c-80b4-8f8b5966e13e)



## Run Locally

Clone the project

```bash
  git clone https://github.com/tanviway48/Diabetes-Prediction-Model-with-Deployment.git
```

Go to the project directory

```bash
  cd DiabetesWebApp.py
```

Install Streamlit

```bash
  pip install streamlit
```

Run the app

```bash
  streamlit run 'DiabetesWebApp.py'
```

## 💡What I learned ? 

The learning outcomes from this project include:

- I deepened my understanding of Support Vector Machines (SVM) and how to effectively use them for classification tasks, specifically for predicting diabetes.
- How to save and load machine learning models using the pickle library, enabling me to reuse the trained model for future predictions without retraining it.
- I became proficient in Streamlit, a framework that allows rapid development of interactive web applications with minimal coding.
- Gained hands-on experience in deploying a machine learning model as a web app, making it functional and accessible through a web browser.
- This project helped me learn how to take a project from the development phase to deployment, connecting different components such as data input, model integration, and real-time predictions into a cohesive, production-ready solution.
- I learned how to solve real-world problems using machine learning, applying a healthcare use case to predict diabetes, which enhances my understanding of AI applications in various domains.
