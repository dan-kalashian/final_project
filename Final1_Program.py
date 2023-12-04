#Program
#Develop a Word Scrapbook File using words from other files to make a story!

with open("WordCollection1.txt", "r") as collection:
    part1=collection.read()
with open("WordScrapbook.txt", "w") as Scrapbook:
    Scrapbook.write(part1)

with open("WordCollection2.txt", "r") as collection:
    part2=collection.read()
with open("WordScrapbook.txt", "a") as Scrapbook:
    Scrapbook.write(part2)

with open ("WordScrapbook.txt", "r") as file:
    contents = file.read()
    print("Here is first scrapbook! " + contents)


#Alternativeley, the scrapbook can lead to a story with a differnet ending using words from differnt files
with open("WordCollection1.txt", "r") as collection:
    part1=collection.read()
with open("WordScrapbook.txt", "w") as Scrapbook:
    Scrapbook.write(part1)

with open("WordCollection3.txt", "r") as collection:
    part2=collection.read()
with open("WordScrapbook.txt", "a") as Scrapbook:
    Scrapbook.write(part2)

with open ("WordScrapbook.txt", "r") as file:
    contents = file.read()
    print("Here is the second scrapbook! " + contents)


#Here, the user can choose how to end the story
end = input("Choose which file to use to end the story: (WordCollection2.txt or WordCollection3.txt): ")
with open("WordCollection1.txt", "r") as collection:
    part1=collection.read()
with open("WordScrapbook.txt", "w") as Scrapbook:
    Scrapbook.write(part1)

a=0
while a==0:
        try:
            with open(end, "r") as collection:
                part2=collection.read()
            break
        except FileNotFoundError:
            print("file not found. Please type 'WordCollection2.txt' or 'WordCollection3.txt' or 'quit': ")
            end = input()
            if end== "quit":
                part2= "then went home and cries because you quit"
                a=1
with open("WordScrapbook.txt", "a") as Scrapbook:
    Scrapbook.write(part2)

with open ("WordScrapbook.txt", "r") as file:
    contents = file.read()
    print("Here is your scrapbook! " + contents)

#Also here is the gramatic structure of the words explained inside tuples. 
words = ("the", "man", "went", "to", "the", "store")
(article, subject, verb, preposition, preposition_article, object_of_the_preposition) = ("the", "man", "went", "to", "the", "store")
print("I want to find out what the verb of this sentence is, so I will use the tuple!")
print("The verb is: " + verb)
print("Now I want to find out what the subject is")
print("The subject is: "+ subject)

# We can add to the story using words from webscraping!
# Here I am webscaping a website explaining what a grocery store is. I want the first section only, so I will 
#find the first section, and get just the text.
import requests
from bs4 import BeautifulSoup 
URL = "https://dbpedia.org/page/Grocery_store"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib') 
print("After a trip to the store, I now love grocery stores. Here is some information about grocery stores online!")
grocery=soup.find("section")
print(grocery.get_text())
#print("Here is your scrapbook! " + contents + "Then the man thought of the quote: " + new)

#API English class?
