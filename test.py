class Class:

    def __init__(self):
        self.__prop = 114514
    
    @property
    def prop(self):
        return "prop1 is: %s" %  str(self.__prop.__repr__())
    
    @prop.setter
    def change(self, new):
        if not isinstance(int):
            raise ValueError("The value should be an integer !")
        else:
            self.__prop = new
    
obj = Class()
print(obj.prop)
obj.change(1919810)
print(obj.prop)