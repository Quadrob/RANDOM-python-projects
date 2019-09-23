favMovies = ["kingsmen","kingsmen golden crcile","never back down","fear pong","ready player one"]
   
#this just counts each item in the list and prints out each item along with the number of the position it holds within the list 
#the ,1 at the end tells the function where the number should start so index (0) in the list will be numbered 1 and index (1) in the list 2 and so forth
for movie in enumerate(favMovies,1):
   print(movie)