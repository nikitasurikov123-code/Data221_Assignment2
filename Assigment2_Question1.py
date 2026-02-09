#defined punctuation characters os that they can be removed
punctuation = "!?,.;:'\"()[]<>{}-_/..."
#open the file and read it
with open("sample-file.txt" , "r", encoding = "utf8") as f:
    tokens = f.read().split()
#list to store lowercase tokens
convert_tokens_to_lowercase = []
#go through every token in the file
for token in tokens:
    #convert to lowercase
    token = token.lower()
    token = token.strip(punctuation)
    count = 0
    #count how many alphabetic letters are inside the token
    for i in token:
        if i >= "a" and i <= "z":
            count += 1
    #makes sure that the tokens contain 2 characters
    if count >= 2:
        convert_tokens_to_lowercase.append(token)
#dictionary to store frequency
count_word_frequency = {}
#counts how often each word appears in the token list
for word_frequency in convert_tokens_to_lowercase:
    #if the word is repeated, add one to the count
    if word_frequency in count_word_frequency:
        count_word_frequency[word_frequency] += 1
    #if it's the first time seeing the word start the count at one
    else:
        count_word_frequency[word_frequency] = 1
#print 10 most frequent words
for i in range(10):
    word_in_text = ""
    word_count = 0
    #search for the dictionary to find the word with the highest count
    for word, count in count_word_frequency.items():
        if count > word_count:
            word_in_text = word
            word_count = count
    #print the most frequent word then delete it so that it goes onto the next most frequent, not counting a word most frequent twice
    print(word_in_text, "->", word_count)
    del count_word_frequency[word_in_text]
