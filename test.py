#Python3 code to demonstrate 
#to extract words from string
#using regex() + string.punctuation
import re
import string

#initializing string
test_string = "Rias and Akeno are the baddest waifus in HS DxD!! FACTS!"

#printing original string 
print("The Original string is: " + test_string)

#using regex() + string.punctuation
#to extract words from string 
res = re.sub('[+string.punctuation+]', '', test_string).split()

#printing result
print ("The result of words is: " + str(res))

