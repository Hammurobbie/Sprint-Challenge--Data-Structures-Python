import time
from lru_cache import LRUCache

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# OG time complexity O(n^2)

lru = LRUCache(10000)

for name in names_1:
    lru.set(name, name)

for name2 in names_2:
    lru.get(name2, duplicates)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)


end_time = time.time()

print("\n", "\n")
print("Number of duplicates:", len(duplicates), "\n")
print("Duplicates:", "\n")
print(duplicates, "\n")
print("Runtime:", end_time - start_time, "seconds", "\n", "\n")
# print (f'{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n')
# print (f'runtime: {end_time - start_time} seconds')

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
