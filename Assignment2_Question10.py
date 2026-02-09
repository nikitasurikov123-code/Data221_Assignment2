def find_lines_containing(filename, keyword):
    #store lines that contain the keyword
    matched_words = []
    file = open(filename, "r")
    #keep track of what line number it's on
    line_number = 1
    #loop through the file line by line and if the keyword appears, note that down and store both the line number and line text
    for line in file:
        #makes sure that evertything is lower case
        if keyword.lower() in line.lower():
            matched_words.append(line_number)
        line_number += 1
    file.close()
    return matched_words
#search for lines that contain lorem
result = find_lines_containing("sample-file.txt", "lorem")
print("Number of matched lines: " ,  len(result))
#print the first 3 matched lines
for line_number, line_text in result[:3]:
    print(str(line_number) + ":" + line_text)

