#type_cost is a list to store input number and 
type_cost=list(input("please supply a set of eight Olympic costs(using comma to seperate the numbers):").split(','))
print(type_cost)


#draw bar graphs
import matplotlib.pyplot as plt
import numpy as np
N=8
costs=[1, 8, 15, 7, 5, 14, 43, 40]
width=0.4 #the width of each bar
ind=np.arange(N)
plt.figure(figsize=(15,5)) #change figure size
plt.ylabel('costs/billions')
plt.title('Cost of Hosting the Summer Olympic Games')
plt.xticks(ind,('Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012') )
plt.yticks(np.arange(0,45,6))
plt.bar(ind, costs, width, color="green") #make sure the image type
plt.show()



