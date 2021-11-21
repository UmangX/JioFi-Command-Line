from bs4 import BeautifulSoup 
from os import system 
from time import sleep 

#standard location for jiofi homepage 
system("wget 192.168.1.1")
src = open("index.html")

document = BeautifulSoup(src,'lxml')
Status = document.find(attrs={"id":"connectedStatus"})
battery_Status = document.find(attrs={"id":"batterystatus"})
number_client  = document.find(attrs={"id":"noOfClient"})
Connection_time  = document.find(attrs={"id":"ConnectionTime"})
battery_level  = document.find(attrs={"id":"batterylevel"})

print("Connection Status : " + Status["value"])
print("Battery State : " + battery_Status["value"])
print("Number Of Client : " + number_client["value"])
print("Connection Time : " + Connection_time["value"])
print("Battery Level : " + battery_level["value"])
src.close()
system("rm index.html")

