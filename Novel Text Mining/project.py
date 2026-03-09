#Student Name: Duy Bao Khang Nguyen
#Student ID: 185000239



#This program reads a text file and counts word frequencies using hash tables (dictionaries).
#It preprocesses the text by converting to lowercase and removing punctuation, then counts
#occurrences of each word and displays the top 20 most frequent words in a formatted table.
#It also includes a bonus feature that counts and displays the top 10 most frequent bigrams 
#(consecutive word pairs).



import string
file_name = 'c:/Users/Admin\Downloads/adventures_of_huckleberry_finn.txt'
file = open(file_name,'r') # Open the file in read mode ('r') and assign it to the variable 'file'
text = file.read() # Read the entire content of the file and store it in the 'text' variable
file.close() # Close the file to free up system resources

text = text.lower() # Convert all characters in the text to lowercase
for p in string.punctuation: # Loop through each punctuation mark (like !, ?, ., etc.)
    text = text.replace(p," ") # Replace each punctuation mark with a space to separate words
words = text.split() # Split the text into a list of individual words using whitespace as delimiter
words_freq={} #create a blank dictionary for word frequencies
for word in words: # for word in set of words
    if word in words_freq:  #Check if the word already exists in the dictionary
        words_freq[word] +=1 # If yes, increment its count by 1
    else:
        words_freq[word] = 1 # If no, add the word to the dictionary with initial count of 1
    
sorted_words = sorted(words_freq.items(),key = lambda x: x[1],reverse=True) #key=lambda x: x[1] means sort by the second element (frequency count) of each tuple, reverse=True sorts from highest to lowest
print("Top 20 Word Frequencies")
for word, freq in sorted_words[:20]:# Loop through only the first 20 items in sorted list
    print(word,freq) # Print each word and its frequency
print("--------------------------------------------")
print("--------------------------------------------")


bigram_freq = {} # Create an empty dictionary to store bigram (two-word pair) frequencies
for i in range(len(words)-1):
    bigram = words[i] + " " + words[i+1] # Create a bigram by combining the current word and the next word with a space
    if bigram in bigram_freq:  # Check if the bigram already exists in the dictionary
        bigram_freq[bigram] +=1 # If yes, increment its count by 1
    else:
        bigram_freq[bigram] = 1 # If no, add the bigram to the dictionary with initial count of 1

sorted_bigram = sorted(bigram_freq.items(),key = lambda x: x[1], reverse= True)  #key=lambda x: x[1] means sort by the second element (frequency count) of each tuple, reverse=True sorts from highest to lowest
print("Top 10 Bigram Word Frequencies")# Loop through only the first 10 items
for bigram, freq in sorted_bigram[:10]:
    print(bigram,freq)
