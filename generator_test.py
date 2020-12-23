# from poke53280 https://stackoverflow.com/questions/35640780/python-fastest-way-to-find-indexes-of-item-in-list


from random import shuffle, randint

def index_finder(lst, item):
    """A generator function, if you might not need all the indices"""
    start = 0
    while True:
        try:
            start = lst.index(item, start)
            yield start
            start += 1
        except ValueError:
            break

test_nums = list(range(0, 1000000))
shuffle(test_nums)
test_num = randint(0, 1000000)

print(*index_finder(test_nums, test_num))