class Celsius(object):
    def __init__(self, value=78):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)


celsius = Celsius()

#celsius = 5
print(celsius) #calls celsius.__get__