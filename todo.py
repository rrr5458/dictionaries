import json


with open('todo.json', 'r') as file_handle:
    to_do_list = json.load(file_handle)
    to_do_list[1]['belt'] = 'black'
    print(to_do_list)


with open('todo.json', 'w') as file_handle:
    json.dump(to_do_list, file_handle)
