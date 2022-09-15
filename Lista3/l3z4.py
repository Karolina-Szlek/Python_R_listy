import random



def simplify(text, word_length, words_number):

    for word in text.split():
        word = word.strip(",.")
        if len(word) > word_length:
            text = text.replace(word,"")


    current_number = len(text.split())
    while len(text.split()) > words_number:
        words_tab = text.split()
        rand_word = random.choice(words_tab)
        text = text.replace(rand_word,"", 1)
    text = " ".join(text.split())
    return text





# jak działa replace?
# problem z kropką 
tekst = 'aa aa aa aa aa aa aa aa aa aa b'
#tekst = "Podział peryklinalny inicjałów wrzecionowatych kambium, charakteryzuje się ścianą podziałową inicjowaną w płaszczyźnie maksymalnej "
print(simplify(tekst, 10, 5))