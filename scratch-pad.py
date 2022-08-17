## Range ##
# print(list(range(10)))


## Mod ##
for num in range(5):
    if num % 2 == 0:
        print("even", num)
    else:
        print("odd", num)

print("hello")


## Tuples ##
fruits = (
    "apple", # 0, if in a loop - first iteration ... "off by 1 errrors" bc of 0 indexing
    "banana", # 1
    "orange", # 2
    "mango", # 3 # comma at end of list is a style thing
)

# print(fruits[2])

# fruits[2] = "pineapple"
# print(fruits[2])

print(type(fruits))

for fruit in fruits: # variable names are for us, not the computer
    print("loopin", fruit)


## Lists ##
# lists contain elements ("the element at index 1 is banana")

fruits = [
    "apple", # 0, if in a loop - first iteration ... "off by 1 errrors" bc of 0 indexing
    "banana", # 1
    "orange", # 2
    "mango", # 3 # comma at end of list is a style thing
]

print(fruits[2])

fruits[2] = "pineapple"
print(fruits[2])

# fruits[4] = "watermelon" # returns list assignment out of range ... need to use append instead

fruits.append("watermelon") # can't append tuples, can't append multiple things at once

# numbers = [1,2,3,4,5,6,7]

# misc = ["apple", 12, True, [1,2,3,4]]

for fruit in fruits: # variable names are for us, not the computer
    print("loopin", fruit)
