import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder , StandardScaler
from sklearn.model_selection import train_test_split , GridSearchCV
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
import pickle
from imblearn.over_sampling import SMOTE

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="writeyour",
        database="PC"
    )

query="SELECT * FROM health"

df=pd.read_sql(query,db)

db.close()

print(df.head())

## drop loggin time as its of no use in prediction

df=df.drop(["log_time"],axis=1)

print(df.head())

## now defining input and output features

x=df.drop(columns=['pc_status'])
print("INPUT PARAMETERS")
print(x.head())

y=df['pc_status']
print("OUTPUT PARAMETERS")
print(y.head())

## convert categorical y into numerical form

encoder=LabelEncoder()
y=encoder.fit_transform(y)
print(y)


## Sampling as Healthy ones (ie 1) were a lot

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(x, y)

## split the data

x_train,x_test,y_train,y_test= train_test_split(X_resampled,y_resampled,test_size=0.3,random_state=42)

## Various models and parameters defining

def model_parameters(actual,predicted):
    cf=classification_report(actual,predicted)
    ac=accuracy_score(actual,predicted)
    cm=confusion_matrix(actual,predicted)
    
    return cf,ac,cm

models = {
    "Logistic Regression": LogisticRegression(),
    "Naive Bayes": GaussianNB(),
    "KNN": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier(),
    "SVM": SVC(probability=True),
    "Random Forest": RandomForestClassifier(),
    "Bagging": BaggingClassifier(),
    "AdaBoost": AdaBoostClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "XGBoost": XGBClassifier()
}

## Performance Prediction for all classification models 

for i in range(len(list(models))):
    model = list(models.values())[i]

    model.fit(x_train,y_train)

    y_train_pred=model.predict(x_train)
    y_test_pred=model.predict(x_test)

    cf_train,ac_train,cm_train=model_parameters(y_train,y_train_pred)
    cf_test,ac_test,cm_test=model_parameters(y_test,y_test_pred)

    print(list(models.keys())[i])

    print("--------TRAINING PERFORMANCE---------")
    print("Confusion matrix : \n {}".format(cm_train))
    print("accuracy score {}".format(ac_train))
    print("classification report : \n {}".format(cf_train))

    print("--------TEST PERFORMANCE---------")
    print("Confusion matrix : \n {}".format(cm_test))
    print("accuracy score {}".format(ac_test))
    print("classification report : \n {}".format(cf_test))

    print("\n")


## Hyper-parameter tuning

chosenmodel=SVC()

params={
    'C':[0.1,1,10,100],
    'gamma':[1,0.1,0.01,0.001],
    'kernel':['linear','sigmoid','poly','rbf']
}

grid=GridSearchCV(chosenmodel,params,cv=5,refit=True,verbose=2)

grid.fit(x_train,y_train)

print("best paramaters : ",grid.best_params_)

print("best_score : " ,grid.best_score_)

## Apply the best parameter to improve the accuracy to best possible way

final_model=SVC(C=0.1,kernel='linear')
final_model.fit(x_train,y_train)
y_final_pred=final_model.predict(x_test)
final_accuracy=accuracy_score(y_test,y_final_pred)

print("Best Optimised Accuracy for the given dataset",final_accuracy)

## visualisation

plt.figure(figsize=(8,6))
sns.heatmap(confusion_matrix(y_test,y_final_pred),annot=True,fmt='d',cmap='Blues')
plt.xlabel("Predicted values")
plt.ylabel("Actual values")
plt.title("CONFUSION MATRIX FOR FINAL SVC MODEL")
plt.show()

## create a pickle file

pickle.dump(final_model,open('PC_Health_modelling.pkl','wb'))
