import os, sys, random, images2gif, subprocess
from PIL import Image

directory = 'tempdir'

process = subprocess.Popen('rm -R out.gif', #issues with having the output file existing
    shell=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE )

if not os.path.exists(directory): #create a directory for your temporary jpgs
	os.makedirs(directory)

#copy the file to txt as thats apparently the ONLY way it'll work
process = subprocess.Popen('cp opensource.jpg temp.txt',  #complete hack, very interesting that it works
    shell=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE )


with open("temp.txt","rb") as yam:
	img = yam.read()  #image is a string somehow, call it magic


sequence = []
x = 0
while x <= 10: #would error out with a for x in range(10), or would make interesting repititions
	if x <= -1:
		x = 10
	splitpoint = len(img)/(random.randrange(120,20000)/100) #the point where you will add your garbage string (dont mess with header at beginning of file)
	final=''
	s1 ='' #strings are immutable so you need temporary strings for copying and inserting
	s2 =''
	for y in range(0, splitpoint): #first fraction of image
		s1 += img[y]
	for y in range(splitpoint, len(img)): #second fraction of image
		s2 += img[y]

	sequence.append(directory+"/"+str(x)+".jpg") #remember the file you created

	final = s1 + "oliveiuapieaue48964104189auda.oeaiaeies" + s2   			#insert the garbage string

	with open(directory+"/"+str(x)+".jpg","wb") as output:
		output.write(final)
	try:
		Image.open(directory+"/"+str(x)+".jpg").verify() #if actual image returns none, no probs
		x += 1
	except:
		#x -= 1
		continue


sequence = list(set(sequence)) 		#you don't want any repititions so order it as a set
for x in range(len(sequence)):		
	sequence[x] = Image.open(sequence[x])	#create PIL instances of open images for images2gif
	print sequence[x]
images2gif.writeGif('out.gif', sequence) 	#more parameters here you can mess with, see line  480 of images2gif.py
