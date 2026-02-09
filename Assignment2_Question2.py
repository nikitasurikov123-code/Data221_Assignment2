#same as question 1
punctuation = "!?,.;:'\"()[]<>{}-_/..."
with open("sample-file.txt" , "r", encoding = "utf8") as f:
    tokens = f.read().split()
convert_tokens_to_lowercase = []
for token in tokens:
    token = token.lower()
    token = token.strip(punctuation)
    count = 0
    for i in token:
        if i >= "a" and i <= "z":
            count += 1
    if count >= 2:
        convert_tokens_to_lowercase.append(token)
#create a dictionary of bigrams count
bigrams_count = {}
#goes through the cleaned list of tokens and builds bigrams
for i in range(len(convert_tokens_to_lowercase)):
    if i + 1 < len(convert_tokens_to_lowercase):
        #creates a bigram using the two adjacent words
        bigrams = convert_tokens_to_lowercase[i] + " " + convert_tokens_to_lowercase[i+1]
        #update the counts for the bigram
        if bigrams in bigrams_count:
            bigrams_count[bigrams] += 1
        else:
            bigrams_count[bigrams] = 1
#print 5 most frequent bigrams
for j in range(5):
    most_frequent_bigrams = []
    frequent_bigrams_count = 0
    #finds the bigram with the largest count
    for bigram, count in bigrams_count.items():
        if count > frequent_bigrams_count:
            most_frequent_bigrams = bigram
            frequent_bigrams_count = count
    #output most frequent bigram and deletes it so it isn't counted twice.
    print(most_frequent_bigrams, " " , frequent_bigrams_count)
    del bigrams_count[most_frequent_bigrams]