from ast import pattern
import re
from nltk.tokenize import word_tokenize;

text = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure 7558313179 Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem +91-7558313179Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) 9022231583 by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first 7218462529 line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32"

# Here we will be finding the phone number from the given text using the text matching technique

pattern = '\+\d{2}-\d{10}|\d{10}'

ans = re.findall(pattern,text);
print(ans)


text = '''note-1: Ram had empire\n Contrary to 19 BC popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure 7558313179 Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem +91-7558313179Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) 9022231583 by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first 7218462529 line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32 \n
note-2: Chhatrapati shivaji Maharaj had empire\n Contrary to 19 BC popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure 7558313179 Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem +91-7558313179Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) 9022231583 by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first 7218462529 line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32\n
note-3: I will be having the empire\n Contrary to 19 BC popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure 7558313179 Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem +91-7558313179Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) 9022231583 by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first 7218462529 line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32'''

pattern = 'note\-\d\:'

result = re.findall(pattern, text)
print(result)


# To print any character except the character that we want to specify we give the ^ symbol

pattern = '[^n]' #Here we have left the value of  from the text file
print(re.findall(pattern, text))

# Now we will be having only the header of each of the topic
# To match this type of character pattern we will be having the character sequence as the pattern as given and then only till we find the new line

pattern = "note-\d:[^\n]*"
print(re.findall(pattern, text))

#Now we want to print the data where number is follwed by BC
pattern = '\d\d BC'
print(re.findall(pattern, text))

#if we want our data to have any range of data from any digit then the numbers can be put into the square brackets
#Here only data values between the range of [1-2]follwed by any numbers is accepted
pattern = '[1-2][0-9] BC'
print(re.findall(pattern, text))

pattern = "([1-2][0-9]) BC"
print("Years of the BC",re.findall(pattern, text, flags=re.IGNORECASE))

text ="""FY2021 Q1 $4.85
FY2020 Q4 $3.00"""

pattern1 = "FY[\d{4}]*"
pattern2 = '\$[\d\.\d\d]*'

print(re.findall(pattern1, text), " has the money of ", re.findall(pattern2,text))

# We can even find the email address of the person by using the client's information it can be done using pattern matching

text = "I have my personal email id as mahdikrs512@gmail.com and college has given me the email address as radhakrushna.mahadik122020@gcoeara.ac.in"

pattern = '[a-zA-Z0-9\._]*@[a-z]*\.[a-z\.]*'

# If you want to retrieve the particular data in the code then that data only can be extracted using the ()

text = "codebasics: My order 412889912 is having an issue, I was charged 300$ when online it says 280$. codebasics: I have a problem with my order number 412889912 codebasics: Hello, I am having an issue with my order # 412889912"

pattern = 'order[^0-9]*(\d*)'
print(re.findall(pattern, text))

print(re.findall(pattern, text))


# Here we will get only name elon musk with functions such as as strip and all.
text = """Born	Elon Reeve Musk
June 28, 1971 (age 51)
Pretoria, Transvaal, South Africa
Citizenship	
South AfricanCanadianAmerican
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Founder of The Boring Company and X.com (now part of PayPal)
Co-founder of Neuralink, OpenAI, and Zip2
President of Musk Foundation
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2022)[1]
Children	10[a][3]
Parents	
Errol Musk (father)
Maye Musk (mother)
Relatives	
Kimbal Musk (brother)
Tosca Musk (sister)
Lyndon Rive (cousin)
Family	Musk family
Awards	List of honors and awards
Signature"""

pattern = 'Born([^\n]*)'
ans = re.findall(pattern, text)

print(ans[0].strip())

# To get the date of birth only from above data we can use the following pattern 
pattern = 'Born.*\n(.*)\('
print(re.findall(pattern, text))

# To get the birth place only examine the pattern given over there and we can then use the pattern to find the birthplace after it.
pattern = "age.*\n(.*)\n"
print(re.findall(pattern, text))

def get_Information(text):
    age = 'age(.*)\)'
    name = 'Born(.*)\n'
    date = 'Born.*\n(.*)\('
    place = 'age.*\n(.*)\n'
    return {
        "Age: ": re.findall(age, text),
        "Name: ": re.findall(name, text),
        "Birth date: ": re.findall(date, text),
        "Birth Place: ": re.findall(place, text)
    }

print(get_Information(text))
