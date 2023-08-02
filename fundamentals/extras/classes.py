# Class names are singular nouns an in PascalCase
class Guitar:
    # constructor function (dunder init)
    def __init__(self, brand, model, num_strings):
        self.brand = brand
        self.model = model
        self.num_strings: int = num_strings
        self.is_Playing = False


    def __str__(self): 
        return f"<Guitar: {self.brand}, Brand: {self.model}, Playing: {self.is_Playing}>"
    
    # Instance methods always take self as the first parameter
    def play(self):
        self.is_Playing = True
        print (f"The {self.brand} {self.model} is being played!")
        return self

    def stop_playing(self):
        self.is_Playing = False
        print (f"The {self.brand} {self.model} has stopped playing.")
        return self

    def change_strings(self, new_num_strings) -> int:
        self.num_strings = new_num_strings
        print (f"Changed to {self.num_strings} strings.")
        return self.num_strings

# Instantiating an object of type Guitar

fender = Guitar("Fender", "Stratocaster", 6)

# accessing values using . notation
# print(fender)
# print(fender.play())
# print(fender)
# fender.stop_playing()
# print(fender)
# print(fender.change_strings(12))
# print(fender)

# To chain you must return self
fender.play().stop_playing()
# If a method is already returning a value it cannot be chained.