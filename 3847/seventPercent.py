
''''
Input from input.txt
See problem description at 3847.pdf

'''
def seventPercent(sentence):

    codes= {' ': '%20', '!': '%21', '$': '%24','(': '%28', ')': '%29', '*': '%2a'}

    if '%' in sentence:
        sentence = sentence.replace('%', '%25')

    for x in codes:
        if x in sentence:
            sentence = sentence.replace(x, codes[x])

    return sentence

def main():
    f = open("input.txt", 'r')
    for line in f:
        l = line.strip().split(',')
        print ('Testing for: ' + l[1])
        if seventPercent(l[0]) == l[1]:
            print (True)
        else:
            print (False)


if __name__ == "__main__":
    main()
