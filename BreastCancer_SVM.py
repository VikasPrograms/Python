#---------------------------------------------------------------------------------
# >>>>> Steps to folow while programming :-

# Step 1  Understand the problem statement
# Step 2  Write the algorithm
# Step 3  Decide the programming language
# Step 4  Write the program
# Step 5  Test the program
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
# Required Python Packages
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
# Breast Cancer Dataset with Support Vector Machine
#---------------------------------------------------------------------------------

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

#---------------------------------------------------------------------------------
# Function Name : SVM
# Description : Load the dataset
# Author : Bade Vikas Vasudeo
# Date : 23/12/2022
#---------------------------------------------------------------------------------

def SVM():
    # Load Dataset
    cancer = datasets.load_breast_cancer()

    # print the names of the 13 features
    print("Features of the cancer dataset : ",cancer.feature_names)

    # print the label type of cancer ('malignant' 'benign')
    print("Labels of the cancer dataset : ",cancer.target_names)

    # print data (feature) shape
    print("Shape of dataset is : ",cancer.data.shape)

    # pring the cancer data features (top 5 records)
    print("First 5 records are : ")
    print(cancer.data[0:5])

    # print the cancer labels (0:malignant, 1:benign)
    print("Target of dataset : ",cancer.target)

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3, random_state=109)
    # 70 % training and 30 % test

    # Create a svm Classifier
    clf = svm.SVC(kernel='linear')      # Linear Kernel

    # Train the model using the training sets
    clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Model Accuracy : How often is the classifier correct ?
    print("Accuracy of the model is : ",metrics.accuracy_score(y_test, y_pred)*100)

#---------------------------------------------------------------------------------
# Function Name : main
# Description : main function from where execution starts
# Author : Bade Vikas Vasudeo
# Date : 23/12/2022
#---------------------------------------------------------------------------------

def main():
    print("--------------------------------- By Vikas Bade -------------------------------------")    
    print("------------------------------ Support Vector Machine -------------------------------")
    print("------------------------------ Breast Cancer Dataset --------------------------------")
    
    SVM()

#---------------------------------------------------------------------------------
# Application Starter
#---------------------------------------------------------------------------------

if __name__ == "__main__":
    main()