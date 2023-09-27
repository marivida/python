import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) # search the string to see if it starts with 'The' and ends with 'Spain'
print(x)

x = re.findall("ai", txt) # returns a list containing all matches
print(x)
x = re.findall("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt) # search for the first white-space character in the string
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.split("\s", txt) # split at each white-space character
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt) #replace every white-space character with the number 9
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2) # replace the first 2 occurrences
print(x)

x = re.search("ai", txt) # do a search tha will return a Match Object
print(x) #this will print an object

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
'''  Print the position (start- and end-position) of the first match occurrence.
The regular expression looks for any words that starts with an upper case "S": '''
print(x.span())

x = re.search(r"\bS\w+", txt) #print the string passes into the function
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())