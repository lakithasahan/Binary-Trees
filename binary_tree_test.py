import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.decomposition import PCA
scaler = MinMaxScaler()

 
 
 
 
 
 
 
 
 
 
class Node(object):
	
	 def __init__(self,d_sample):
		 self.d_sample=d_sample
		 self.left=None
		 self.right=None
	 def insert_(self,d_sample,e,l,ld,rd):
		 if(ld==1): 
			 if self.left is None:
				self.left=Node(d_sample)
			 else:
				 self.left.insert_(d_sample,e,l,ld,rd)
		 if(rd==1):
			 self.right=Node(d_sample)
		 
		 
	 def PrintTree(self):
		 if self.left:
		     self.left.PrintTree()
		 print('######'+str(self.d_sample)+'###### \n'),
		 if self.right:
		     self.right.PrintTree()
		 
		 
class BinaryTree(object):
	 def __init__(self,root):
		 self.root=Node(root)		 
		 
		 
		 






dfRaw = pd.read_csv('iforest.csv')
x_train = np.array(dfRaw.iloc[:,0:4])
y_train = np.array(dfRaw.iloc[:,4])

target=[]


for x in range(len(y_train)):
	if(y_train[x]=="'Normal'"):
		target.append(1)
	else:
		target.append(-1)	


#print(target)

scaler.fit(x_train)
normalised_input_data=scaler.transform(x_train)

pca = PCA(n_components=3)
normalised_input_data = pca.fit_transform(normalised_input_data)

scaler.fit(normalised_input_data)
normalised_input_data=scaler.transform(normalised_input_data)


e=0
l=40

data=normalised_input_data[0:10]
data2=normalised_input_data[0:5]
data3=normalised_input_data[5:10]



tree=BinaryTree(data)


ld=1
rd=0
tree.root.insert_(data2,e,l,ld,rd)



ld=0
rd=1
tree.root.insert_(data3,e,l,ld,rd)


tree.root.PrintTree()
print('after the addition')




ld=1
rd=0
tree.root.insert_(data3,e,l,ld,rd)

ld=1
rd=0
tree.root.insert_(data3,e,l,ld,rd)

tree.root.PrintTree()








