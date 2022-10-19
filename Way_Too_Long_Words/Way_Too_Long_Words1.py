# Way Too Long Words problem, first solution

# Replacing abbreviation of a word
def abbreviation(word: str) -> str:
    return word[0]+str(len(word)-2)+word[len(word)-1]

words_number = int(input())
words = list()
for i in range(words_number):
    words.append(input())
for i in range(words_number):
    print(abbreviation(words[i])) if len(words[i])>10 else print(words[i]) 

