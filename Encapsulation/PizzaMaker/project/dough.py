class DoughGetersSetters:
    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, string):
        if not string:
            raise ValueError("The flour type cannot be an empty string")
        self.__flour_type = string

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, stringa):
        if not stringa:
            raise ValueError("The baking technique cannot be an empty string")
        self.__baking_technique = stringa

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, string):
        if not string:
            raise ValueError("The baking technique cannot be an empty string")
        self.__weight = string


class Dough(DoughGetersSetters):
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        super().__init__()
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

