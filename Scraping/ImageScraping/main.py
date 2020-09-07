#Importing
from PIL import Image

#Opening the images
matrix=Image.open("word_matrix.png")
mask=Image.open("mask.png")

#Formatting the images
mask=mask.resize((1015,559)) #Resizing dimensions of mask to matrix
mask.putalpha(128) #Opaquing the mask

matrix.paste(im=mask,box=(0,0),mask=mask) #Pasting mask on the matrix
matrix.save("edited.png") #Saving the matrix as a new file