#!/usr/local/bin/python36
from 
with open("/Users/epi/gmap.html") as file:
    htmlFile = file.read()
    soup = Soup(htmlFile) 
    headTag = soup.find('h1') 
    divTag = soup.new_tag('div') 
    divTag['class'] = "link" 
    headTag.insert_after(divTag)
    print(soup) #This should print the new, modified html