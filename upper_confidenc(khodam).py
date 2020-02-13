# Upper Confidence Bound

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Change Directory
import os 
os.chdir('/Users/parsaahani/Downloads/Machine Learning A-Z /Part 6 - Reinforcement Learning/Section 32 - Upper Confidence Bound (UCB)')

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing UCB

import math
N = 10000
d = 10
parsamax=0
index=0
total_reward = 0
sum_of_reward = [0] * d
number_select = [1] * d
selected = []
item = 0
item2=0
check = []
## yek dor anjam shod ! 
for i in range(10):
    
    reward = dataset.values[i, i]
    sum_of_reward[i]= sum_of_reward[i]+reward
    total_reward = total_reward + reward
    number = i
    print(number)
    selected.append(number)


for i in range(10,N):
    item2 = item2 +1
    parsamax = 0
    index = 0    
    for j in range(0,10):
            r = sum_of_reward[j] / number_select[j]
            delta = math.sqrt((3/2)*math.log(i+1)/number_select[j] ) 
            parsa = r + delta
            if (parsa > parsamax):
                    parsamax=parsa
                    index=j
    check.append(i)            
    reward = 0
    reward = dataset.values[i, index]
    check.append(reward)
    sum_of_reward[index]= sum_of_reward[index]+reward
    total_reward = total_reward + reward
    number_select[index]= number_select[index]+1 
    selected.append(index)
        
    if reward==1 :
      item=item+1
                    
  
plt.hist(selected)
print (item)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

    # Bye Bye