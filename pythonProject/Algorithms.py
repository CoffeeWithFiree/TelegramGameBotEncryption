
class Algorithms:

    def __init__(self, word, lang):
        self.word = word
        self.lang = lang

    def CaesarCipher(self):
        word_lst = list(self.word)

        shift_ascii = []
        min_char = 97 if self.lang == "ENG" else 1072
        max_char = 122 if self.lang == "ENG" else 1103
        for i in word_lst:
            ascii_char = ord(i) + 3
            if ascii_char > max_char:
                ascii_char = min_char + (ascii_char - (max_char + 1))  #a = 97; z = 122
            shift_ascii.append(ascii_char)

        result = [chr(j) for j in shift_ascii]
        return "".join(result)

