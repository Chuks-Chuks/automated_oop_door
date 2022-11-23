class EncryptDecrypt:
    step = 2  # 242236

    def __init__(self):
        self.new_alphabet_list = []
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.new_list = self.steps_for_determining_hashed_password()

    def steps_for_determining_hashed_password(self):
        """This takes the entered password and encrypts or decrypts it with a random given step."""

        for copy in range(0, self.step):
            for letters in self.alphabet:
                self.new_alphabet_list.append(letters)
        return self.new_alphabet_list

    def encrypt_integers(self, password):
        new_word = ""
        for number in password:
            index_position = int(number) + self.step
            if index_position > 26:
                new_letter = self.alphabet[index_position % len(self.alphabet)]
            else:
                new_letter = self.alphabet[index_position]
            new_word += new_letter
        return new_word

    def decrypt_integers(self, hashed_password):
        password = ""
        for letter in hashed_password:
            new_index = str(self.alphabet.index(letter) - self.step % len(self.alphabet))
            password += new_index
        return password
