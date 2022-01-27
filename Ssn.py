class Ssn:
    def __init__(self, num_secu):
        self.num_secu = num_secu

    def is_valid(self):
        b = int(self.num_secu[:-2]) % 97
        c = 97 - b
        key = int(self.num_secu[-2:])
        print(key, c)
        return c == int(self.num_secu[-2:])

