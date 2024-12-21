class Algorithms:

    def __init__(self, word, lang):
        self.word = word
        self.lang = lang

    def CaesarCipher(self):
        word_lst = list(self.word)

        shift_ascii = []
        min_char = ord("a") if self.lang == "ENG" else ord("а")
        max_char = ord("z") if self.lang == "ENG" else ord("я")
        for i in word_lst:
            ascii_char = ord(i) + 3
            if ascii_char > max_char:
                ascii_char = min_char + (ascii_char - (max_char + 1))
            shift_ascii.append(ascii_char)

        result = [chr(j) for j in shift_ascii]
        return "".join(result)

    def AtbashCipher(self):
        word_lst = list(self.word)

        min_char = ord("a") if self.lang == "ENG" else ord("а")
        max_char = ord("z") if self.lang == "ENG" else ord("я")
        result = []
        for i in word_lst:
            new_char = chr(max_char - (ord(i) - min_char))

            result.append(new_char)
        return "".join(result)
