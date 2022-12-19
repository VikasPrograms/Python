from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.spatial import distance

def euc(a,b):               # " euc " is inbuilt method.
    return distance.euclidean(a,b)

class MarvellousKNeighborsClassifier:

    def fit(self, trainingdata, trainingtarget):
        self.TrainingData = trainingdata
        self.TrainingTarget = trainingtarget

    def closest(self, row):
        minimumdistance = euc(row, self.TrainingData[0])
        minimumindex = 0

        for i in range(1, len(self.TrainingData)):
            Distance = euc(row, self.TrainingData[i])
            if Distance < minimumdistance:
                minimumdistance = Distance
                minimumindex = i

        return self.TrainingTarget[minimumindex]
        
    def predict(self, TestData):
        predictions = []
        for value in TestData:
            result = self.closest(value)
            predictions.append(result)

        return predictions

def MarvellousML():
    
    # 1 : Load the data
    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    # 2 : Manipulate the Data
    Data_train, Data_test, Target_train, Target_test = train_test_split(Data, Target, test_size = 0.5)
    
    Classifier = MarvellousKNeighborsClassifier()       # Class object Creation.

    # 3 : Build the model
    Classifier.fit(Data_train, Target_train)

    # 4 : Test; the model
    Predictions = Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test, Predictions)

    # 5 : Improve -- Missing
    return Accuracy

def main():
    Ret = MarvellousML()

    print("Accuracy of Iris dataset with kNN is : ",Ret * 100)

if __name__ == "__main__":
    main()