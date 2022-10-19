# Way Too Long Words problem, second solution

for i in [0]*int(input()):
    word = input()
    print([word,word[0]+str(len(word)-2)+word[-1]][len(word)>10])