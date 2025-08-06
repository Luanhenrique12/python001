import csv 
file= open("file.csv")
reader =  csv.reader(file)
data =  list(reader)
data