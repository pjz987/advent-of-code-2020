import time

list1 = list(range(1000000))
list2 = list(range(1000000))
list3 = list(range(1000000))

var1 = 500000
var2 = 500000
var3 = 500000

start_loop = time.time()
for i in list1:
  if i == var2:
    print(i)
    break
end_loop = time.time()
loop_time = end_loop - start_loop
print(loop_time)
print()

start_index = time.time()
i = list2.index(var2)
print(i)
end_index = time.time()
index_time = end_index - start_index
print(index_time)
print()

dict1 = {}
for num in list3:
  dict1[num] = num
start_dict = time.time()
i = dict1[var3]
print(i)
end_dict = time.time()
dict_time = end_dict - start_dict
print(dict_time)
print()

start_set = time.time()
set1 = set(list1)
end_set = time.time()
set_time = end_set - start_set 
print(set_time)
print()

start_in = time.time()
print(1000001 in list1)
end_in = time.time()
in_list_time = end_in - start_in
print(in_list_time)
print()

start_in_set = time.time()
print(1000001 in set1)
end_in_set = time.time()
in_set_time = end_in_set - start_in_set
print(in_set_time)
print()

print(set_time + in_set_time)