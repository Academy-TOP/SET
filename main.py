our_set = set()
our_set_2 = {0}

x = "Помидор"

our_set.add("Помидор")
our_set_2.add("Огурец")

print(x in our_set)
print(x in our_set_2)

print(our_set.isdisjoint(our_set_2))
