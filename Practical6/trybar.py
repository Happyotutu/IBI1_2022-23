# try bar graphs
import matplotlib.pyplot as plt
import numpy as np
N=10
sizes = [73, 42, 38, 28, 22, 19, 18, 12, 8, 7]
ind=np.arange(N)
width=0.3
p1=plt.bar(ind, sizes,width)
plt.ylabel('the number of student')
plt.title("Students' favourite movie genre")
plt.xticks(ind, ('Comedy', 'Action', 'Romance', 'Fantasy', 'Science-fiction', 'Horro', 'Crime', 'Document', 'History', 'War'))
plt.yticks(np.arange(0,81,10))
plt.show()




