#Importing packages
import csv
import PyPDF2
import re

#Getting data from spreadsheet
spreadsheet = open('find_the_link.csv',encoding="utf-8") #Opening file
data = csv.reader(spreadsheet) #Reading file
lines = list(data) #Assigning data to a list

link = '' #Placeholder for link
for row_num,data in enumerate(lines):
    link+=data[row_num] #Getting the link from the diagnols
print(link) #Printing the link

#Getting data from pdf
file = open('Find_the_Phone_Number.pdf','rb') #Opening file
pdf = PyPDF2.PdfFileReader(file) #Reading file

#Looping through the pages in thge pdf
for n in range(pdf.numPages):
    page = pdf.getPage(n) #Get the current page
    text = page.extractText() #Get the text from the page
    match = re.search(r'\d{3}.\d{3}.\d{4}', text) #Check if the pattern exists in the page
    if match:
        print(match.group()) #Print the number obtained