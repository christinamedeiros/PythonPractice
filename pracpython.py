# 
# words = ['cat', 'frog', 'snake','something']
# for w in words:
#     print (w, len(w))
#     if len(w)>6:
#         words.insert(0,w)



rhym= "Mary had a little lamb"
rhym= rhym.split(" ")

# len is interpreting length of array, range is parsing
for i in range(len(rhym)):
    print(i,rhym[i])




URL = "http://api.openweathermap.org/data/2.5/forecast/daily?q=Boston&units=imperial&cnt=10&appid=f5f76fc80be1dfc220492acb706cb7e3"
import requests
response= requests.get(URL)
data= response.json()
# import pprint
# pprint.pprint(data)

day_list= data['list']
for day in day_list:
    #prints temp for each day
    print(day['temp']['max'])
