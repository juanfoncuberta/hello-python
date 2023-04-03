### File handling ###

import os, json, csv



###---txt file---###
file = open("my_file.txt","w+")
#file = open("my_file2.txt","w+")

#writing
# print("writing file")
file.write("Juan\nFoncuberta\n1986\nBarcelona\nPython")
print("reading file","w+")

#reading 10 positions/chars
# print(file.read(10))

#reading line by line
# print(file.readline())

#'exploding' lines in array
# print(file.readlines())

file.write("\nhello this is a writed line")
print(file.readline())
for line in file.readlines():
  print(line)


#close file
file.close()

#delete file
#os.remove("my_file2.txt")

###---END txt file---###


###---json file---###
json_file = open("my_json_file.json","w+")

json_test =  {
                "Name":'Juan', 
                "Lastname": 'Foncuberta',
                "Birth": "8/5/1986",
                "Languages" :["Python", "Javascript"] 

           }
#writing json (dictionary) in a file
json.dump(json_test,json_file,indent=3)
json_file.close()
#reading a json file
json_file_content = json.load(open("my_json_file_to_read.json"))
print(json_file_content)


###---END json file---###



###---csv file---###
csv_file = open("my_csv_file.csv", "w+")
csv_writer = csv.writer(csv_file)

csv_writer.writerow(["name","lastname","birth","languages"])
csv_writer.writerow([json_test["Name"],json_test["Lastname"],json_test["Birth"],json_test["Languages"]])
csv_file.close()

###---END csv file---###
