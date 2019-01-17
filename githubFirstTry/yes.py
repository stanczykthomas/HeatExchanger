#this is a test script of python code

print ('Hello there')
i = 2
for i in range(6):
    print(i)


words = ["antidisestablishmentarianism", "monarchies", "socialism"]
for w in words:
    print(w, len(w))
    if(len(w)==3*len(words)):
        print('YES')
