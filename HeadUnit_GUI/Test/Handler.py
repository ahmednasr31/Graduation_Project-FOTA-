Handler = open("text.txt" , "r+")

name= "nasoura" +'\n'

file_list=[name]

for line in Handler :
    file_list.append(line)
    #Handler.write("Project_2.hex")
Handler.close()
writeHandler = open("text.txt" , "w+")

for iterator in file_list :
    writeHandler.write(iterator)

print (file_list)

#print (file_list)
writeHandler.close()


