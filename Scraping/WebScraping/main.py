#Importing packages
import requests
import bs4

#Variable Declerations
authors=[]
qoutes=[]
tags=[]
counter=1 #Counter to track the pages
end=True #Condition for end of page

#Loop while the site does not end
while end:
    baseURL = "http://quotes.toscrape.com/page/{}/"
    currentURL = "http://quotes.toscrape.com/page/{}/".format(counter)
    req=requests.get(currentURL) #Access current URL
    page = bs4.BeautifulSoup(req.text, "lxml") #Format the data
    for item in page.select(".col-md-8"): #Check for end of site
        if "No quotes found!" in item.text:
            end=False #Exit loop
    for item in page.select(".author"): #Check for author
        authors.append(item.text)
    for item in page.select(".text"): #Check for qoutes
        qoutes.append(item.text)
    for item in page.select(".tag-item"): #Check for tag
        tags.append(item.text)
    counter=counter+1

#Printing the data
print(authors)
print(qoutes)
print(tags)