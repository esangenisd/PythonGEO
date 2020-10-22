# importing googlemaps module 
import googlemaps 
import json
import pymssql  
#import json_normalize
  
# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyCV2jZvUNWNhBw9ijE6IITvi9-JGQpFfGg') 
  
# Requires cities name 

my_dist = gmaps.distance_matrix('19.540735,-99.19072|20.2083,-99.0582','20.2083,-99.0582|19.540735,-99.19072') #['rows'][0]['elements'][0] 
  

# Printing the result 
#matrixdf = json_normalize(my_dist,['rows','elements'])
print(my_dist['rows'][0]['elements'][0]['duration']['value']/60) 
print ("\n")
print(my_dist['rows'][1]) 
print ("\n")
print(my_dist)


