def main():
    f = open("text.txt", 'r')
    word = input("введіть слово -> ").split()
    outPut = wordFilter(f.read(), word[0])
    for x in outPut:
        print(x)

def wordFilter(text, inputWord):
    massParagraph = text.split("    ")
    outputMass = []
    for x in massParagraph:
        for j in x.split():
            if inputWord == str(j):
                outputMass.append(x)
    return outputMass

if __name__ == '__main__':
    main()
