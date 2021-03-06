# -*- coding: utf-8 -*-
#author: ANDY

import numpy as np
import random
from sklearn import cross_validation

class naive_bayes:

    def __init__(self,trainx,trainy,testx,testy,n,a,c):
   
        self.n=n#the number of x
        self.c=c#c==[0,1]
        self.a=a#the features of x
        self.len_a=len(a)
        self.len_c=len(c)
    #define x and y
        self.trainx,self.trainy,self.testx,self.testy=trainx,trainy,testx,testy
        
   #read data from input     
    def read(self,filename):
        
        with open(filename,'r')as f:
            x,y=f.readlines()
        
        trainx,trainy,testx,testy=cross_validation(x,y)
        return trainx,trainy,testx,testy
    
    #calculate the probability
    def cal_probab(m,n):

        return m/n
        
    #calculate the occurrence numbers of all possible probability events
    def cal_occur(self,x,y):
        #define a matrix to store the occurrence numbers
        countedlist=np.zeros(self.len_c,self.len_a)
        count=0
        
        for feature in self.a:
            for i in range(self.len_a):                
                if feature==x[i] and y[i]==0:
                    countedlist[0][count]+=1
                else:
                    if feature==x[i] and y[i]==1:
                        countedlist[1][count]+=1
                    
            count+=1
            
        return countedlist
    
    # train the data                    
    def train(self):
        
        
        posteriori_event=self.cal_occur(self.trainx,self.trainy)
        y_event=np.zeros(self.len_c)        
        
        #calculate the number of each y events
        sum_event=0 
        for i in range(self.len_c):
            for j in range(self.len_a):                
                y_event[i]+=posteriori_event[i][j]
                
        #calculate the sum of the number of the posteriori events
        for i in range(self.len_c):
            sum_event+=y_event[i]
         
        #calculate the probability of each y event 
        y_probab=np.zeros(self.len_c)
        for i in range(self.len_c):
            y_probab[i]=self.cal_probab(y_event,sum_event)
            
        #calculate the probability of each posteriori event            
        posteriori_probab=np.zeros(self.len_c,self.len_a)
        for i in range(self.len_a):
            for j in range(self.len_c):
                posteriori_probab[i][j]=self.cal_probab(posteriori_event[i][j],sum_event)
        
        return posteriori_probab,y_probab
    
    
    def predict(self,testx):
        
        
        posteriori_probab,y_probab=self.train()
        
        test_probab=np.zeros(self.len_c)
        test_probab+=1
        test_predict=0
        
        #predix
        len_testx=len(testx)
        
        for i in range(len_testx):
            for j in range(self.len_a):
                if self.testx[i] == self.a[j]:
                    test_probab[0]=test_probab[0]*posteriori_probab[0][j]*y_probab[0]
                    test_probab[1]=test_probab[1]*posteriori_probab[1][j]*y_probab[1]
        
        #rank the most probable y and select it as predicted class
        if test_probab[0]>test_probab[1]:
            test_predict=test_probab[0]
        else:
            test_predict=test_probab[1]
            
        return test_predict
        
        
    def score(self):
            
        score=0
        
        len_testx=len(self.testx)
        
        for i in range(len_testx):
            testy_predict=self.predict(self.testx[i])
            if testy_predict==self.testy[i]:
                score+=1
                
        score/=len_testx
        
        return score
             
def generate_data(n,nc):
    
    pass
    
                        
if __name__=="__main__":
    pass
                       
       
        
        
        
