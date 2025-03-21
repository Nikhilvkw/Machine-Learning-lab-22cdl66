import csv
num_attributes=3
a=[]
print("\n The given training data set \n") 
csvfile=open('4.csv','r') 
reader=csv.reader(csvfile)
for row in reader: 
    a.append(row) 
    print(row)
print("The initial values of hypothesis ") 
hypothesis=['0']*num_attributes 
print(hypothesis)

for j in range(0,num_attributes): 
    hypothesis[j]=a[0][j]

for i in range(0,len(a)): 
    if(a[i][num_attributes]=='Yes'):
        for j in range(0,num_attributes): 
            if(a[i][j]!=hypothesis[j]):
                hypothesis[j]='?' 
            else:
                hypothesis[j]=a[i][j]
    print("For training instance no:",i," the hypothesis is ",hypothesis) 
print("The maximally specific hypothesis is ",hypothesis)




output
The given training data set 

['Big', 'Red', 'Circle', 'No']
['Small', 'Red', 'Triangle', 'No']
['Small', 'Red', 'Circle', 'Yes']
['Big', 'Blue', 'Circle', 'No']
['Small', 'Blue', 'Circle', 'Yes']
The initial values of hypothesis 
['0', '0', '0']
For training instance no: 0  the hypothesis is  ['Big', 'Red', 'Circle']
For training instance no: 1  the hypothesis is  ['Big', 'Red', 'Circle']
For training instance no: 2  the hypothesis is  ['?', 'Red', 'Circle']
For training instance no: 3  the hypothesis is  ['?', 'Red', 'Circle']
For training instance no: 4  the hypothesis is  ['?', '?', 'Circle']
The maximally specific hypothesis is  ['?', '?', 'Circle']


