our_set = set()
our_set_2 = {0}

x = "Помидор"

our_set.add("Помидор")
our_set_2.add("Огурец")

our_set_3 = our_set.union(our_set_2)
our_set_2.update(our_set)

print(our_set_3)
print(our_set_2)
