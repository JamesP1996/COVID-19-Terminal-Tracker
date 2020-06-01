# Imports Needed for The Web Scraping
from bs4 import BeautifulSoup
import requests
import lxml
from bs4.element import SoupStrainer
import urllib.request



# Setup URL String and Make a Request on the set URL Variable
URL = "https://www.worldometers.info/coronavirus/"
r = requests.get(URL) 
links = SoupStrainer("div")

# URl Checker. Checks if Status Returned is 200 and Returns True or False
def url_check(URL):
    r = requests.head(URL)
    if (r.status_code == 200):
        return True
    else:
        return False

# Prints the Coronavirus Statistics by Scrapping the Website URL
def printStats():
    # Make Beautiful Soup grab the Content from our Request and Parse it using the LXML(Faster Parsing then html5lib)
    soup = BeautifulSoup(r.content,'lxml',parse_only=links)

    #Store Relevant Number Categories
    Data = []

    # Total,Deaths,Recovered Segment from the URL. Store into a List
    Results = soup.findAll('div', attrs = {'class':'maincounter-number'})

    # Retrive The Active and Closed Cases Section of the URL Webpage and store it into a List.
    Active_and_Closed_Cases = soup.findAll('div',attrs={'class':'number-table-main'})

    # Parse the Results into Data and Append it
    for result in Results:
        Data.append(result.text)

    # Parse the Active and Closed Cases into our Data List/Array
    for result in Active_and_Closed_Cases:
        Data.append(result.text)
    
    # The First Result in Results is the Total Cases thus far since January 2020   
    Total = Data[0]
    # The Second Result is the number of Deaths Thus Far Since January 2020
    Deaths = Data[1]
    # The Third Result is the number of People who have recovered from COVID-19
    Recovered = Data[2]
    # The Fourth Result is the Number of Active Cases as of today according to the Website
    Active = Data[3]
    # The Fith Result is the number of Closed Cases as of Today According to the Website
    Closed = Data[4]


    print("===============COVID-19 Terminal Tracker===============")
    print(f"Total Cases : {Total}") 
    print(f"Total Deaths : {Deaths}") 
    print(f"Total Recoveries : {Recovered}")
    print(f"Active Cases :\n{Active}\n") 
    print(f"Cases Closed :\n{Closed}")
    print("======================================================") 

# Check if Website Is Available, If it is not Exit!
if(url_check(URL)==True):
    printStats()
else:
    print("Website is Not Available Currently. Try Again Later!")

# Stop Terminal From Closing Automatically. Closes When User Presses Enter 
input('Press ENTER to exit')