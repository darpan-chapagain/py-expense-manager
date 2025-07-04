from abc import ABC, abstractmethod

class ExpenseEntry(ABC):
    def __init__(self, description, amount, category):
        self.__description = description
        self.__amount = amount
        self.__category = category

    def get_description(self):
        return self.__description
    
    def get_amount(self):
        return self.__amount
    
    def get_category(self):
        return self.__category
    
    def set_description(self, desc):
        self.__description = desc

    def set_amount(self, amt):
        if amt < 0:
            print("Amount cant be negative")
        else:
            self.__amount = amt
    
    def set_category(self, cat):
        self.__category = cat

    @abstractmethod
    def describe(self):
        pass
    