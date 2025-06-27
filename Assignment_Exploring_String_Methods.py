# Task 1 - String Slicing and Indexing
original_string = "Python is amazing!"

first_word = original_string[:6]  
amazing_part = original_string[-8:-1] 
reversed_string = original_string[::-1] 

print("Original string:", original_string)
print("First word:", first_word)
print("Amazing part:", amazing_part)
print("Reversed string:", reversed_string)

words = original_string.split()
amazing_word = words[2][:-1] 
print("Amazing word (alternative method):", amazing_word)

# Task 2 - String Methods
messy_string = " hello, python world! "

stripped_string = messy_string.strip() 
capitalized_string = stripped_string.capitalize()  
replaced_string = stripped_string.replace("world", "universe")  
uppercase_string = stripped_string.upper()  

print("Original string:", repr(messy_string))  
print("After strip():", repr(stripped_string))
print("After capitalize():", capitalized_string)
print("After replace():", replaced_string)
print("After upper():", uppercase_string)

chained_result = messy_string.strip().capitalize().replace("world", "universe")
print("Chained methods:", chained_result)

# Task 3 - Check for Palindromes
word = input("Enter a word: ")

cleaned_word = word.lower().replace(" ", "")

reversed_word = cleaned_word[::-1]

if cleaned_word == reversed_word:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"No, '{word}' is not a palindrome.")
    
print(f"Original (cleaned): {cleaned_word}")
print(f"Reversed: {reversed_word}")