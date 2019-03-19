class Ass:
    def manipulate(self, some_fucking_object):
        return some_fucking_object


list1 = [x for x in range(10)]
print(list1)
temp = Ass.manipulate
print(temp(Ass(), list1))  # This is without making an instance of Ass

booty = Ass()
b = booty.manipulate(list1)
print(b)