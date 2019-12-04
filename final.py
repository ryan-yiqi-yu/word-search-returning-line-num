def index(fileName, wordslist):
    
    
    file = open(fileName)
    sentenceslist = file.readlines()
    for word in wordslist:
        lst = []    
        for num, sentence in enumerate(sentenceslist):
            if word.lower() in sentence.lower():
                lst.append(num + 1)
        print(word, end=": ")
        print(lst)
       
        
    file.close()


if __name__ == "__main__":
    

    index('raven.txt', ['ghost', 'raven', 'dying', 'ghastly', 'evil', 'demon', 'hi'])
