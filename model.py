# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 21:43:32 2022

@author: 3460
"""

# In[1] model
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("C:/Users/miao3/Desktop/ML Algorithm/Web/IAQ4EDU_app_prototype/IAQ4EDU.csv")
df.info()

# In[2] dataset
features = df[["VOLUME", "TOTAL_STUDENTS", "OCCUPIED_TIME", "OPENING_SIZE_WINDOW", "OPENINNG_WINDOW_TIME", "OPENING_SIZE_DOOR", "OPENING_DOOR_TIME"]]
labels = df["IAQ_LEVEL"]

# In[3] train and validate
from sklearn.model_selection import train_test_split
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.2, random_state = 42, shuffle= True)
# In[3] create pkl
iaq = RandomForestClassifier(n_estimators= 100, max_features = 'sqrt', oob_score = True, 
                              max_depth=10, random_state = 42) 
iaq.fit(train_features, train_labels)
rfr_y_pred = iaq.predict(test_features)

# In[4] accuracy
from sklearn import metrics
from sklearn.metrics import r2_score
print('Accuracy: %.4f' % metrics.accuracy_score(test_labels, rfr_y_pred))
print('R2: %.4f' % r2_score(test_labels, rfr_y_pred))

# In[4] load pkl
import joblib
joblib.dump(iaq, "iaq.pkl")
