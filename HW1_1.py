"""Exercise 1a
Import the string library.
Create a variable alphabet that consists of the lowercase 
and uppercase letters in the English alphabet using the 
ascii_letters data attribute of the string library."""

import string
alphabet = string.ascii_letters

"""Exercise 1b
The lower and upper case letters of the English alphabet should
stored as the string variable alphabet. Consider the sentence
'Jim quickly realized that the beautiful gowns are expensive'.
Create a dictionary count_letters with keys consisting of each
unique letter in the sentence and values consisting of the
number of times each letter is used in this sentence. Count 
upper case and lower case letters separately in the dictionary."""

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
for letter in sentence:
    if letter in alphabet:
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1

"""Exercise 1c
Rewrite your code from 1b to make a function called counter
that takes a string input_string and returns a dictionary 
of letter counts count_letters. Use your function to call 
counter(sentence)."""

def counter(input_string):
    count_letters = {}
    for letter in input_string:
        if letter in alphabet:
            if letter in count_letters:
                count_letters[letter] += 1
            else:
                count_letters[letter] = 1
    return(count_letters)

counter(sentence)

"""{'J': 1,
 'i': 5,
 'm': 1,
 'q': 1,
 'u': 3,
 'c': 1,
 'k': 1,
 'l': 3,
 'y': 1,
 'r': 2,
 'e': 8,
 'a': 4,
 'z': 1,
 'd': 1,
 't': 4,
 'h': 2,
 'b': 1,
 'f': 1,
 'g': 1,
 'o': 1,
 'w': 1,
 'n': 2,
 's': 2,
 'x': 1,
 'p': 1,
 'v': 1}

Exercise 1d
Abraham Lincoln was a president during the American Civil War.
His famous 1863 Gettysburg Address has been stored as address.
Use the counter function from 1c to return a dictionary
consisting of the count of each letter in this address and
save it as address_count."""

address = """Four score and seven years ago our fathers brought forth on this continent, a new nation, 
conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a 
great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. 
We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final 
resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper 
that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- 
this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add 
or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. 
It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so 
nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored 
dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here 
highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of 
freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""   

address_count = counter(address)

print(address_count)

max_value = 0
desired_key = ""
for key in address_count: 
    if (max_value < address_count[key]):
        max_value = address_count[key]
        desired_key = key

print(desired_key, max_value)