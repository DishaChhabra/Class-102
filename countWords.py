sentence = input('enter a sentence: ')
count = 0
wordCount = 1

for i in sentence :
    count=count+1
    if i == ' ':
        count=count-1
        wordCount= wordCount+1
print(count)
print(wordCount)