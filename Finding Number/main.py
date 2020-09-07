#Importing packages
import shutil
import os
import re

#Unzipping the archive
filename='unzip_me_for_instructions.zip'
destination=os.getcwd()
shutil.unpack_archive(filename,destination,'zip')

#Declerations
unpack=False #A check for the instruction file
number=0 #Placeholder for the number

#Loop to traverse through the extracted content
for folder, sub_folders, files in os.walk("extracted_content"):
    folder_directory = destination+"\\"+folder
    #Looping through the files
    for f in files:
        file_directory=folder_directory+"\\"+f
        file = open(file_directory, 'r')
        #Condition to print only the first/instruction file
        if unpack==False:
            print(file.read())
            unpack=True
            file.close()
            break
        phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',file.read()) #Checking for the pattern in the files
        if phone:
            number=phone.group() #Assign the number found
        file.close()

#Print the number
print("\nThe number is:",number)