
import os #Imports the os module.

dirPath = os.listdir(path = 'C:\\Users\\asand\\Desktop\\School\\Python-Projects\\Page 180') #Lists all files inside of the path dir.
print(dirPath)


joinPath = os.path.join("C:\\Users\\asand\\Desktop\\School\\Python-Projects\\Page 180\\","Python.txt") #Concatenates the second path to the end of path1.
print(joinPath)


modTime = os.path.getmtime("C:\\Users\\asand\\Desktop\\School\\Python-Projects\\Page 180\\") #Grabs the time of last modification of the directory.
print(modTime)


