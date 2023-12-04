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
    print("Here is your scrapbook! " + contents)


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
    print("Here is your scrapbook! " + contents)
