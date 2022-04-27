
#To access to any command-line arguments via the sys.argv
import sys


updateHand = open("LastUpdate.txt","r") 

flashHand  = open("LastFlashed.txt","r")

fileToFlashHand =open("FileToFlash.txt","w")


#read last update in the file-first-line 
updatefile   = updateHand.readline()
#Read last-flashed
flashfile_1  = flashHand.readline()
#second file
flashfile_2  = flashHand.readline()
#Third file  Read older version before last-flashed
flashfile_3  = flashHand.readline()


'''
if updatefile== flashfile_1:
    print ("yes")

if flashfile_1 == updatefile :
    print ("yes2")
'''
#print (updatefile )
#print (flashfile_1)
#print (flashfile_2)

#get number of passed argurments
ArgNum = len(sys.argv)

#valid Argumrent as fileName(FileToFlashUpdater.py) is argumrnt 1
if ArgNum == 2 :

    #state is lastUpdate or  lastFlashed
    state = sys.argv

    #if Update version
    if state[1] == 'lastUpdate' :
        #--------------------------
        if (updatefile == flashfile_1) or  ( not( len(updatefile.strip()) ) ) :
            print ("noupdate",end ='' ) #end="" as the default is \n

        #last-update is in FileToFlash file 
        else :
            fileToFlashHand.write(updatefile)
            print ("oklastupdate", end ='')

    #if back to last update
    elif state[1] == 'lastFlashed' :
        #----------------------   not true   (empty)
        if ( not( len(flashfile_1.strip()) ) ) or ( not( len(flashfile_2.strip()) ) ) :
            print ("alreadyold" , end = '')

        #true (full)
        else :
             #compare
            if (flashfile_1 == flashfile_3)  :
                print ("alreadyold" , end = '')

            #last-update is in FileToFlash file 
            else :
                fileToFlashHand.write(flashfile_2)
                print ("oklastflashed" , end = '')


    #invalid state
    else :
        print ("Invalid State")


else :
    print ("Invalid Arguments")


#close files
updateHand.close()
flashHand.close()
fileToFlashHand.close()


