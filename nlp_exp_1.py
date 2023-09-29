#Tokenization:

import re

def regex_tokenizer(text):
    # Tokenizes a string by spaces and removes punctuation
    # The pattern looks for sequences of alphanumeric characters (\w+)
    tokens = re.findall(r'\w+', text.lower())
    
    return tokens

# Get input from user
user_input = input("Enter a text to tokenize: ")

tokens = regex_tokenizer(user_input)
print("Tokenized text:", tokens)


#Regional Lnaguage Filtration:

import re

def filter_hindi(text):
    hindi_text = ','.join(re.findall(r'[\u0900-\u097F]+',text))
    return hindi_text
user_input = input("Enter your text: ")

filtered_text = filter_hindi(user_input)
print("Extracted Hindi text:", filtered_text)

#Stop Word Filtration:

import re 

stop_words = set(["and","the","is""in", "of", "to", "a", "an", "for", "by", "on", "with", "as", "that", "this", "it"
])


def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def filter_stop_words(tokens):
    return [token for token in tokens if token not in stop_words]

user_input = input("Enter your text: ")
tokens = tokenize(user_input)
filtered_tokens = filter_stop_words(tokens)
print ("Orignal Tokens:", tokens)
print ("Tokens after stop word filtration:", filtered_tokens)

#Punctuation Filtration 

import string 

def remove_punctuation(text):
    no_punct = ''.join([char for char in text if char not in string.punctuation])
    return no_punct

user_input = input("Enter your text: ")
filtered_text = remove_punctuation(user_input)
print("Text after punctutation filtration:",filtered_text)


#Email, Phone number and Name Validation 

import re 

def validate_name(name):
    if re.match(r'^[a-zA-Z\s]+$', name):
        return True
    return False

def validate_phone(phone):
    if re.match(r'^\d{10}$',phone):
        return True
    return False

def validate_email(email):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return True 
    return False

name = input("Enter your Name: ")
phone = input("Enter your Phone Number: ")
email = input("Enter your Email: ")

# Validating user input
invalid_fields = []

if not validate_name(name):
    invalid_fields.append("Name")
if not validate_phone(phone):
    invalid_fields.append("Phone Number")
if not validate_email(email):
    invalid_fields.append("Email")

if invalid_fields:
    print("Invalid fields:", ", ".join(invalid_fields))
else:
    print("All details entered are valid!")

