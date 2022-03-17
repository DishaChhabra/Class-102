def sum(a,b):
    print(a+b)

sum(2,3)

sentence = 'disha siddhant, ishita pari '
print(sentence.split(','))

# def is used to define a function
def countWords():
    file = input('enter the file name- ')
    count = 0
    #r means in reading format
    #open is used to open a file
    f = open(file, 'r')
    for i in f :
        #split is to seperate using any separator
        words = i.split(' ')
        #len is to count in list
        count=count+len(words)
    print(count)

countWords()