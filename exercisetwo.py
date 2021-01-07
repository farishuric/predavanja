
words = {
    "Hello":"Hallo",
    "Car":"Auto",
    "Day":"Tag"
}
class Dictionary:


    def get_word(self, userword):
        self.userword = userword




class English(Dictionary):
    def __init__(self, userword):
        super().get_word(userword)
        for i in words:
            if i == self.userword:
                translation = words.get(i)
        print (translation)

class German(Dictionary):
    def __init__(self, userword):
        super().get_word(userword)
        for i in words:
            if i == self.userword:
                translation = words.get(i)
        print (translation)

user_input = input("Enter: ")
faris = Dictionary
engleski = English(user_input)
njemacki = German(user_input)