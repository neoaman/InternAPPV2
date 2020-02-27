import pandas as pd
import numpy as np
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import resample
import pickle

def final_model(testdata): 
    df_s = pd.read_csv('final.csv')[['Python (out of 3)','R Programming (out of 3)','Data Science (out of 3)','Current Year Of Graduation','skillsown','Approval']]
    df_s.iloc[-1] = testdata
    df_dummy = pd.get_dummies(df_s, columns=df_s.columns[:-1])
    testdummy = df_dummy.iloc[-2:]
    df_dummy = df_dummy.iloc[:-2]
    df_majority = df_dummy[df_dummy.Approval=='No']
    df_minority = df_dummy[df_dummy.Approval=='Yes']
    df_minority_upsampled = resample(df_minority, 
                                 replace=True,     # sample with replacement
                                 n_samples=567,    # to match majority class
                                 random_state=101) # reproducible results
    df_balance = pd.concat([df_majority, df_minority_upsampled])
    X = df_balance[df_balance.columns[1:]]
    Y = df_balance['Approval']
    Approve_Tree_final = DecisionTreeClassifier(criterion='entropy',max_depth=10,min_samples_leaf=1,random_state=4,splitter='random')
    Approve_Tree_final.fit(X,Y)
    return Approve_Tree_final.predict(testdummy[testdummy.columns[1:]])[-1]

    
    
    model = pickle.load(open("Approve_Tree_final", 'rb'))
    return model.predict(testvalue)
    


