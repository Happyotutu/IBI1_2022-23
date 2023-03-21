#a dictionary that record the favorite movie genre of university students in China
favor_movie = {'Comedy' :73, 
               'Action' :42, 
               'Romance' :38, 
               'Fantasy' :28, 
               'Science-fiction' :22,
               'Horro' :19,
               'Crime' :18,
               'Document' :12,
               'History' :8,
               'War' :7}
#if you want to change the input, please directly change in the 'favor_movie' dictionary above.
print(favor_movie)

genre=input("Please give me a movie genre:") #store the input movie genre
number = favor_movie.get(genre) #the number of students of given movie genre
print('The number of students that like this genre is', number)

import matplotlib.pyplot as plt
# construct a pie chart from the data above
labels = favor_movie.keys() #labels is the list of keys
sizes = favor_movie.values() #sizes is the list of values
explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#specifies the fraction of the radius with which to offset each wedge
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()

#to get the number of studednts for which the genre is their favorite one
num=[] # num is a list to store the value of fovor_movie 
for i in favor_movie: #i means key in the favor_movie
    num.append(favor_movie[i]) #add values into the num list
    num.sort(reverse=True) #let the value in the list in reverse order
for j in favor_movie: #j means the value's key
  if favor_movie[j]==num[0]  :
      print(j)
      favor=j #favor is used to store the biggest value's key
big=num[0] #big means the biggest value
print(big)
print('Their favorite movie genre is', favor,".", "And there are", big, "students." )
