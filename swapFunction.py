def swapFiles():
    file1= input('enter file1 name: ')
    file2= input('enter file2 name: ')
    f1 = open(file1, 'r')
    f1text = f1.read()
    f2 = open(file2, 'r')
    f2text = f2.read()
    #w to write
    f1write = open(file1, 'w')
    f1write.write(f2text)
    f2write = open(file2, 'w')
    f2write.write(f1text)

swapFiles()