#       Supervised Machine Learning
# Play Predictor using K Nearest Neighbour Algorithm

# There is one data set of whether conditions.
# That dataset contains information as wether and we have to decides whether to play or not.
# Data set contains the target variable as Play which indicates whether to play or not.
# Consider below Marvellous Infosystems Play Predictor Dataset as

# According to above dataset there are two features as
#       1. whether
#       2. Temperature

# We have two labels as
#       1. Yes
#       2. No

# There are three types of different entries under whether as
#       1. Sunny
#       2. Overcast
#       3. Rainy

# There are three types of different entries under Temperature as
#       1. Hot
#       2. Cold
#       3. Mild

# Consider below characteristics of Machine Learning Application:

#   Classifier          :   K Nearest Neighbour
#   DataSet             :   Play Predictor Dataset
#   Features            :   Whether, Temperature
#   Labels              :   Yew, No
#   Training Dataset    :   30 Entries
#   Testing Dataset     :   1 Entry


import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):

    # Step 1 : Load Data
    data = pd.read_csv(data_path, index_col=0)
    print("Size of Actual dataset",len(data))

    # Step 2 : Clean, Prepare and manipulate data
    feature_names = ['Whether','Temperature']
    print("Names of Features",feature_names)

    Whether = data.Whether
    Temperature = data.Temperature
    play = data.Play

    # Creating label Encoder
    le = preprocessing.LabelEncoder()

    # Converting string labels into numbers.
    Whether_encoded = le.fit_transform(Temperature)
    print(Whether_encoded)

    # Converting string labels into numbers.
    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)
    print(temp_encoded)

    # Combining weather and tem into single list of tuples
    features = list(zip(Whether_encoded, temp_encoded))

    # Step 3 : Train Data
    model = KNeighborsClassifier(n_neighbors=3)

    # Train the model using the training sets
    model.fit(features,label)

    # Step 4 : Test data
    predicted = model.predict([[0,2]])  # 0 : Overcast, 2 : Mild
    print(predicted)

def main():
    print("----------- Marvellous Infosystems by Piyush Khairnar -----------")
    print("Machine Learning Application")
    print("Play predictor application using K Nearest Neighbour Algorithm")
    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()