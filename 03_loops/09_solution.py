#My approach
items = ["apple", "banana", "orange", "apple", "mango"]
for i in items:
    if items.count(i) > 1:
        print(i)
        break

#Sir approach
items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)