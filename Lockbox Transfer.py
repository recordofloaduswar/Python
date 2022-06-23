#To install Pillow Image eidtor, type these 2 commands in CMD:
#https://www.tutorialspoint.com/python_pillow/python_pillow_environment_setup.htm
#       python -m pip install pip
#       python -m pip install pillow

from PIL import Image
import os 
from datetime import datetime
import os.path
from os import path

def create_dir():    #Function to create timestamped directory for output files
    parent_dir = (os.getcwd())  #get current directory python is active
    new_dir = datetime.now().strftime("%I_%M_%p_%m_%Y")  #get current timestamp to name new folder
    new_path = os.path.join(parent_dir,new_dir) #combines main directory info and new directory
    if (os.path.exists(new_path))== False:
        os.mkdir(new_path) #makes new timestamped folder, program output files will be saved here
        print("Made new folder named " + new_dir)
    else:
        print("Current timestamp folder already present.")  #Won't create a new directory if identically named dir already present
    return new_path

def delete_file(file):    
    location = (os.getcwd())  
    path = os.path.join(location,file) 
    os.remove(path)    

def get_concat_v(im1, im2):   #joins 2 iamges vertically
    dst = Image.new('RGB', (im2.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def get_concat_pages(im2):  #joins all pages in Tif vertically
    page_list = []
    pages =(im2.n_frames)   #get number of pages in Tif

    for p in range(pages):  #Goes through the Tif file page by page, saves each one as temp_page_1 and so on
                                                    #for i in range(pages)
        try:                
            im2.seek(p)
            im2.save('temp_page_%s.tif'%(p,))     #create a temp file of current page of tif
            #print(p)
            current_page = Image.open('Temp_page_%s.tif'%(p,))      
            
            width, height = current_page.size
            page_list.append(height)



            #dst.paste(current_page, (0, im2.height * p))  #stitch temp file onto "dst" image. Y dimension depends on which page number the loop is currently on. X dimension always 0.  
            #print("Page",p+1, im2.height * p)
            #delete_file('Tempx_page_%s.tif'%(p,)) #cleans up temp file before moving on to next page.
 

        except EOFError:                        


            break    

    #print(page_list)
    total_height = 0
    for ele in range(0, len(page_list)):
        total_height = total_height + page_list[ele]
    #print(total_height)


    #dst = Image.new('RGB', (im2.width, im2.height * pages))  #new image that has height of all pages stacked on each other
    dst = Image.new('RGB', (im2.width, total_height))
    running_total = 0
    for p in range(pages):  #Goes through the Tif file page by page, saves each one as temp_page_1 and so on
                                                    #for i in range(pages)
        try:                
            #im2.seek(p)
            #im2.save('temp_page_%s.tif'%(p,))     #create a temp file of current page of tif
            current_page = Image.open('temp_page_%s.tif'%(p,))      
            

            if p == 0:
                dst.paste(current_page, (0, 0))

            #dst.paste(current_page, (0, im2.height * p))  #stitch temp file onto "dst" image. Y dimension depends on which page number the loop is currently on. X dimension always 0.  
            #print("Page",p+1, im2.height * p)


            if p > 0:
                running_total = running_total + page_list[p-1]
                dst.paste(current_page, (0, running_total))
                #print(page_list[p-1 ])
                

            delete_file('temp_page_%s.tif'%(p,))

        except EOFError:                        


            break


    return dst  #retuns combined image of multipage Tif


new_path = create_dir() #Make new directory for output files

filename = "index" #Create a variable for the file name.

infile = open(filename, 'r') #Open the file to read it

line=infile.readlines() 
s="C"      #search for string. "C" is marker for merging 2 lines.
i=0             #line counter, start a line 1

while i<len(line):  #look continues until it reaches the last line of the index file.
    if line[i].find(s)!=-1: #Search each line for string
             
        sline = line[i].split(',')  #If found, split that line into strings seprated by commas
        CheckFront= sline[8]            #grabs the 9th string in the line. Should be check front image file name. Assumes file name is always the 9th category in each line.
        CheckFront = CheckFront.rstrip("\n")  #Removes newline character "\n" from string
        CheckAmount = sline[10]
        CheckNumber = sline[11]
        Batch = sline[4]
        Item = sline[5]
        
        sline2 = line[i+1].split(',') #splits the next line under the one with the check image.
        List_length = len(sline2)      #Checks length of check info line. Lines with one check info should have 9 slots, two should have 10

        CheckInfo = sline2[8]         #grabs the 9th string in the line. Should be check front image file name. Assumes file name is always the 9th category in each line.
        CheckInfo = CheckInfo.rstrip("\n")  #Removes newline character "\n" from string

        im1 = Image.open(CheckFront)  #grabs file names to send to final concat function
        im2 = Image.open(CheckInfo)  #open CheckInfo file for manipulation 

        
        get_concat_pages(im2).save('Combined.tif') #function to save multipage Check Info to single page
        im3 = Image.open('Combined.tif')

        Final_Image = 'C' + CheckNumber + ' ' + 'Amt_' + CheckAmount.replace('.','_')+ ' ' + Batch + '_' + Item + '.tif'  #Final_Image is the file name of final ouput, displays file names of check front and info
        file_path = os.path.join(new_path, Final_Image) #creates path for new timestamped folder and file name of final output

        get_concat_v(im1, im3).save(file_path) #combine Check Front and single page Check Info
        delete_file('Combined.tif') #delete single page Check Info
        i+=1

    else:
        i+=1
