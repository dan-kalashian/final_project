#Program developes a Word Scrapbook File using words from other files to make a story!
# Opens word collection one file, and writes that as 'WordScrapbook.txt' file. 
with open("WordCollection1.txt", "r") as collection:
    part1=collection.read()
with open("WordScrapbook.txt", "w") as Scrapbook:
    Scrapbook.write(part1)

#Opens the second word collection, and appends that to add to 'WordScrapbook.txt' file. 
with open("WordCollection2.txt", "r") as collection:
    part2=collection.read()
with open("WordScrapbook.txt", "a") as Scrapbook:
    Scrapbook.write(part2)

#Opens "WordScrapbook.txt" file and prints it
with open ("WordScrapbook.txt", "r") as file:
    contents = file.read()
    print("Here is first scrapbook! " + contents)


#Alternativeley, the scrapbook can lead to a story with a differnet ending using words from differnt files
#Same as previous except for files being used
with open("WordCollection1.txt", "r") as collection:
    part1=collection.read()
with open("WordScrapbook.txt", "w") as Scrapbook:
    Scrapbook.write(part1)

#Only difference is word collection 3 is not being read and appended
with open("WordCollection3.txt", "r") as collection:
    part2=collection.read()
with open("WordScrapbook.txt", "a") as Scrapbook:
    Scrapbook.write(part2)

with open ("WordScrapbook.txt", "r") as file:
    contents = file.read()
    print("Here is the second scrapbook! " + contents)


#Here, the user can choose how to end the story
#User inputs which file they want to use to complete the story 
end = input("Choose which file to use to end the story: (WordCollection2.txt or WordCollection3.txt): ")

#same for the first part
with open("WordCollection1.txt", "r") as collection:
    part1=collection.read()
with open("WordScrapbook.txt", "w") as Scrapbook:
    Scrapbook.write(part1)

#for the second part of story: program reads from user inputted file name
#while loop
a=0
while a==0:
        try: # tried to read file with name user inputted, if succesful reads it
            with open(end, "r") as collection:
                part2=collection.read()
            break
        except FileNotFoundError: # if error user will get to try again by selecting one or the other files. They can also quit
            print("file not found. Please type 'WordCollection2.txt' or 'WordCollection3.txt' or 'quit': ")
            end = input()
            if end== "quit": # if user inputted one of the files correctly, program will have read it. If they quit, the story continues as such.
                part2= "then went home and cries because you quit"
                a=1

#appends to add either words from user selected file or the "quit" endind
with open("WordScrapbook.txt", "a") as Scrapbook:
    Scrapbook.write(part2)

#opens WordScrapbook.txt to show user their story
with open ("WordScrapbook.txt", "r") as file:
    contents = file.read()
    print("Here is your scrapbook! " + contents)

#Grammar of the sentence is explained
#tuple of words
words = ("the", "man", "went", "to", "the", "store")
#tuple assigned variables
(article, subject, verb, preposition, preposition_article, object_of_the_preposition) = ("the", "man", "went", "to", "the", "store")
print("I want to find out what the verb of this sentence is, so I will use the tuple!")
#using tuple assigned definition of variable verb
print("The verb is: " + verb)
#can be done for any of the variables assigned with the words tuple
print("Now I want to find out what the subject is")
print("The subject is: "+ subject)

# We can add to the story using words from webscraping!
# Here I am webscaping a website explaining what a grocery store is. I want the first section only, so I will 
#find the first section, and get just the text.
import requests
from bs4 import BeautifulSoup 
#chosen website to webscrape with first paragraph explaining what grocery stores are
URL = "https://dbpedia.org/page/Grocery_store"
#bs4 and requests to scrape wesite and get it as Python objects?
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib') 
print("After a trip to the store, I now love grocery stores. Here is some information about grocery stores online!")
#Find the first instance of section, which is the first sectionin the website, which is the paragraph about grocery stores I wish to scrape
grocery=soup.find("section")
print(grocery.get_text())

#Using API to get English classes at UMD
print("still interested in learning about grammar and writing? Take a look at the UMD Enlgish courses below!")
import json
import requests
import re
#obtain API data and get it as python object
umd_request = requests.get("https://api.umd.io/v1/courses?dept_id=ENGL")
umd_data=json.loads(umd_request.content)
# for the courses in the API, if the dept id is ENGL, then print the Course ID and the name
#this step became redundant as it was easiest for me to only obtain ENGL courses from the API given the API's contraints. 
#However, this code still shows data extraction and what should be done if the API included all courses, so can be left. 
for course in umd_data:
    course_id = course["course_id"]
    dept_id = course["dept_id"]
    if dept_id=='ENGL':
        print(f"{course['course_id']}: {course['name']}")
