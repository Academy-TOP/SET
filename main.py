our_set = set()
our_set_2 = {0}

x = "Помидор"

our_set.add("Помидор")
our_set_2.add("Огурец")

our_set_3 = our_set.union(our_set_2)
our_set.update(our_set_2)

print(our_set_2.issubset(our_set_3))
print(our_set_3.issuperset(our_set_2))

our_products = {"Apple", "Tesla", "McDonald's"}
range_of_the_company_1 = {"Samsung", "Sony"}
range_of_the_company_2 = {"Apple", "IBM", "Tesla"}
range_of_the_company_3 = {"BMW", "Tesla", "Ferrari"}

print(our_products.intersection(range_of_the_company_1))
print(our_products.intersection(range_of_the_company_2))
print(our_products.intersection(range_of_the_company_3))
