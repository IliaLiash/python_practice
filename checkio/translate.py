def translate(phrase):
    phrase_list = phrase.split()
    vowels = 'aeioyu'
    non_vowels = 'bcdfghjklmnpqrstvwxz'
    final = ''
    for word in phrase_list:
        i = 0
        while i <= len(word) - 1:
            if word[i] in vowels:
                final += word[i]
                i += 3
            elif word[i] in non_vowels:
                final += word[i]
                i += 2
        final += ' '        
    return final.strip()

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")