#value init
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
Below shows the basic usage.

def basic_list():
    print("Count item in lists: ", fruits.count('apple'))
    print("Add new item. - 'papaya' ------ ", fruits.append('papaya'))
    print("Show all list after append.", fruits)
    print("Get first 'banana' 's index: ",fruits.index('banana'))
    print("Find next 'banana', starts by 4: ",fruits.index('banana', 4))
    print("Reverse list. ------ ",fruits.reverse())
    print("Show all list after reverse. ", fruits)
    fruits.append('grape')
    print("Sort the list: ",fruits.sort())
    print("Show Sorted. ", fruits)
    print("Delete one item, default from last: ",fruits.pop())
    print("Remove item 'banana'. ------ ", fruits.remove('banana'))
    print("Current list: ",fruits)
    print("Clean up list. ",fruits.clear())
    print("Shown list 'fruits' : ",fruits)

basic_list()

#First define an unpacker
def unpacker(name=None, food=None):
    return ["Hi, I'm {} and I love to eat {}!".format(name, food)]

#Define a function to unpack and reformat the result from extracting datas.
def string_factory(values):
    ans = []
    for value in values:
        template = unpacker(**value)
        ans.extend(template)
    return ans

if __name__ == "__main__":
    values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
    result = string_factory(values)
    print(result)

