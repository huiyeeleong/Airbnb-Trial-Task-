
#Author : Hui Yee Leong
#Date : 13/06/2020

#Description 
#This is a simple service to allow us to 
#input ANY user’s Airbnb URL
#and returns a relative ranking of how that user’s profile ranks based initially on 
#just how many reviews they have had.


import bs4
import urllib.request
from urllib.request import urlopen as urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

from urllib.request import Request, urlopen

#user input
user_input = input("Please enter airbnb URL: ")
req = Request(user_input, headers={'User-Agent' : 'Chrome/5.0'})

#opening up connect grabbing the page
#req = Request('https://www.airbnb.com.au/users/show/15840608', headers={'User-Agent': 'Chrome/5.0'})
uClient = urlopen(req).read()
#uClient.close()

#html parsing
page_soup = soup(uClient, "html.parser")
#page_soup.p
#page_soup.body.span

#grabs the review
review = page_soup.findAll("div",{"dir" :  "ltr"}, {"class" :  "_czm8crp"})

reviewnumber = page_soup.findAll("div", {"class" :  "_1p0spma2"})
number = reviewnumber[4]

number = str(number)
print("The service determine he/she has total of: " + number[23:34])


#calculate the percentage
ratings = page_soup.findAll("span", {"class" :  "_3zgr580"})
ratings = str(ratings)

convert_ratings = int(ratings[43])
percentage = (convert_ratings / 5 )*100

print(" ")

print(user_input, "is in the top of", int(percentage), "%", "of Melbourne Airbnb usesrs based on number of reviews")

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

print("#################################Review List#####################################################")
#Review List
i = 1
reviewList = len(review)
while i < reviewList:
	print(review[i])
	i += 1
