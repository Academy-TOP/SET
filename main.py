#Знакомимся с методом вывода множества
our_set = set()
our_set_2 = {0}

print('Определяем тип множества:')
print(our_set, type(our_set))
print(our_set_2, type(our_set_2))

print('\nНаполняем множества:')
our_set.add("Помидор")
our_set_2.add("Огурец")

print(our_set)
print(our_set_2)

print('\nПроверяем наличие элемента во множестве:')
x = "Помидор"
print(x in our_set)
print(x in our_set_2)

print('\nОпределяем длину (размер) множества:')
print(len(our_set))
print(len(our_set_2))

print('\nУбедимся действительно ли массивы не содержат общие элементы:')
print(our_set.isdisjoint(our_set_2))

print('\nОбъединим и расширим наши множества:')
our_set_3 = our_set.union(our_set_2)
our_set.update(our_set_2)
print(our_set_3)
print(our_set)

print('\nПроверим содержит ли в себе множество 3 множество 2:')
print(our_set_2.issubset(our_set_3))

print('\nПроверим входит ли множество 2 в множестве 3:')
print(our_set_3.issuperset(our_set_2))

our_products = {"Apple", "Tesla", "McDonald's"}
range_of_the_company_1 = {"Samsung", "Sony"}
range_of_the_company_2 = {"Apple", "IBM", "Tesla"}
range_of_the_company_3 = {"BMW", "Tesla", "Ferrari"}

print(our_products.intersection(range_of_the_company_1))
print(our_products.intersection(range_of_the_company_2))
print(our_products.intersection(range_of_the_company_3))

print(our_products.difference(range_of_the_company_1))
print(our_products.difference(range_of_the_company_2))
print(our_products.difference(range_of_the_company_3))

print(our_products.symmetric_difference(range_of_the_company_2))

our_products.discard("Apple")
our_products.discard("Mercedes")
print(our_products)
our_products.remove("McDonald's")
print(our_products)

my_frozenset = frozenset()
print(type(my_frozenset))
my_tuple = tuple()
print(type(my_tuple))
my_tuple_2 = (0, )
print(type(my_tuple_2))
my_tuple_3 = 0,
print(type(my_tuple_3))
my_tuple_4 = (0)
print(type(my_tuple_4))
