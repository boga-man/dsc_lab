import keras
from keras.models import Sequential   # For building the Neural Network layer by layer
from keras.layers import Dense        # used to add fully connected layer in ANN#Simple Neural Network Model Code using Tensorflow
import pandas as pd                   # import pandas and numpy for datafram and numpy operations
import numpy as np
import matplotlib.pyplot as plt       # import matplotlib for graphical visualizations 
import io                             # import io for reading csv files
from sklearn.preprocessing import StandardScaler      # for standardizing the data
from sklearn.metrics import accuracy_score            # to determine the accuracy score

## importing the dataset
df= pd.read_csv('insurance_data.csv')           
print(df.head())

n=df.shape[1]               # n--> number of columns
m=df.shape[0]               # m--> number of rows

x_train=np.array(df.iloc[:int(0.9*m),:n-1])      # we take 90% of rows in training data
y_train=np.array(df.iloc[:int(0.9*m),-1])        # only the last column is in y_train  
x_test=np.array(df.iloc[int(0.9*m):,:n-1])       # only 10 % of rows is in testing dataset
y_test=np.array(df.iloc[int(0.9*m):,-1])         # splitting into training and testing dataset 



## here bought_insurance is already encoded as it can be a binary number
sc = StandardScaler()
x_train_scaled= sc.fit_transform(x_train)    # here we standardize the training and testing data using standardscaler()
x_test_scaled=sc.fit_transform(x_test)       # we standardize them so that they are easy to compute

model=Sequential()                                      # we create our neural network model here
model.add(Dense(2, input_dim=2, activation='relu'))     # input dimensions to this layer is 2 and we use reLU activation function
model.add(Dense(2, input_dim=2, activation='relu'))     # input dimensions to this layer is 2 and we use reLU activation function 
model.add(Dense(1, activation='softmax'))               # finally the output dimension has only 1 parameter(0 or 1) so we use softmax activation function  
                                                        # output dimension has 1 parameter as output

#"compile" is a method of Tensorflow. “adam’ is the optimizer that can perform the gradient descent.
# loss function as binary_crossentropy as we have 2 cases only 0 or 1
# The optimizer updates the weights during training and reduces the loss.                                                        
model.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])

model.fit(x_train_scaled, y_train, epochs=50,batch_size=25) # we fit our model using this
model.evaluate(x_test_scaled,y_test)                        # we evaluate using our scaled testing data
y_pred=model.predict(x_test_scaled)                         # we predict based on scaled testing data
actual_res=y_test.tolist()                                  # actual_res contains the actual result list  
pred_res=y_pred.tolist()                                    # pred_res contains the predicted result list


a = accuracy_score(pred_res,actual_res)                     # we compute the accuracy based on accuracy_score function from sklearn.metrics
print('Accuracy is:', a*100)                                # final accuracy result 