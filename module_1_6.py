my_dict = {
    'Elena': 1980,
    'Ilya': 1981,
    'Ivan': 1986
}
print(my_dict)

print('Existing value:', my_dict['Ilya'])
print('Not existing value:', my_dict.get('Sasha'))

my_dict.update({
    'Maria': 1984,
    'Nina': 1953
})

deleted_value = my_dict.pop('Ivan')
print('Deleted value:', deleted_value)
print(my_dict)

my_set = {1, 1, 2, 'meat', False, False}
print('Set:', my_set)
my_set.add('Elena')
my_set.add(12.5)
my_set.discard(2)
print('Modified set:', my_set)

