#shabang
#!/bin/bash

#search for file then sort files then write
#currentDir='pwd' 

cd  /var/www/html/codenext/uploadfile/files 


ls  project_[0-9]*.hex | sort -r -t'_' -n -k2 >~/Desktop/Gradution-Project/HeadUnit_GUI/LastUpdate.txt


cd ~/Desktop/Gradution-Project/HeadUnit_GUI/ 

#cd $("currentDir") 


