import random


def xor(a, b):
    if a == b:
        return 1
    elif a != b:
        return 0


class OneTimePad:
    def __init__(self, word):
        self.word = word
        self.word_bin = []
        self.key = []

    def gen(self):
        word_ascii = [ord(l) for l in self.word]
        self.word_bin = [bin(i)[2:] for i in word_ascii]

        self.key = []
        for letter in self.word_bin:
            string = ''
            for i in range(len(letter)):
                string += str(random.randint(0, 1))
            self.key.append(string)

    def encrypt(self):
        self.gen()
        c = []
        for l in range(0, len(self.word_bin)):
            string = ''
            for i in range(0, len(self.word_bin[l])):
                string += str(xor(self.word_bin[l][i], self.key[l][i]))
            c.append(string)
        return [c, self.key]

    @staticmethod
    def decrypt(c, k):
        w = []
        for l in range(0, len(c)):
            string = ''
            for i in range(0, len(c[l])):
                string += str(xor(c[l][i], k[l][i]))
            w.append(string)
        return w

    @staticmethod
    def bin_to_word(bin_list):
        wint = [int(l, 2) for l in bin_list]
        w_list = [chr(l) for l in wint]
        w = ''
        for l in w_list:
            w += l
        return w

    @staticmethod
    def word_to_bin(word):
        word_ascii = [ord(l) for l in word]
        return [bin(i)[2:] for i in word_ascii]


class Hash:
    def __init__(self, word):
        self.word = word

    def get_hash(self):
        word = self.word
        if len(word) % 2 != 0:
            word += 'y'
        word_bin = [ord(l) for l in word]
        p1 = word_bin[0:int(len(word) / 2)]
        p2 = word_bin[int(len(word) / 2):]
        ret = ''
        for i in range(len(p1)):
            if p1[i] > p2[i]:
                ret += str(p1[i] % p2[i])
            else:
                ret += str(p2[i] % p1[i])
        return ret
