wordlist=[]
displaywords=[]
while len(wordlist)==10:
    word=input("Enter a word: ")
    if word in wordlist:
        print("word already exist!!")
        continue
    else:
        wordlist.append(word)
if len(wordlist)==10:
    number=int(input("Enter number: "))
    for wordz in wordlist:
        if len(wordz)>=number:
            displaywords.appened(wordz)
        else:
            continue
    print(displaywords)