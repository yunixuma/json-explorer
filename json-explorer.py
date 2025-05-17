import my_common
import json
import os, sys

def dig_data(data, keys):
    try:
        if len(keys) == 0:
            return data
        datum = data
        for key in keys:
            datum = datum[key]
        return datum
    except KeyError:
        print(f"KeyError: {key} not found in data")
        return data

def list_keys(data, keys, arg):
    datum = dig_data(data, keys)
    text = ""
    for key in datum.keys():
        text += key + " "
    print(text)

def change_layer(data, keys, arg):
    datum = dig_data(data, keys)
    try:
        if arg == '':
            pass
        elif arg == '.':
            keys.pop()
        elif datum.get(arg) is not None:
            keys.append(arg)
        else:
            print("key {arg} not found")
        print(keys)
    except KeyError:
        print(f"KeyError: {arg} not found in data")
    return keys

def explore_json(data, keys=[]):
    while True:
        cmd = input("Please enter a command (q to quit): ")
        if len(cmd) == 0:
            continue
        c = cmd[0]
        arg = cmd.split(' ')
        if len(arg) > 1:
            arg = arg[1]
        else:
            arg = ''

        if cmd == '':
            continue
        elif c == 'q':
            return
        elif c == 'l':
            list_keys(data, keys, arg)
        elif c == 'c':
            keys = change_layer(data, keys, arg)
        else:
            print("Invalid command")
    # for key, value in data.items():
    #     # Print the key and value
    #     print(f"{key}: {value}")

if __name__ == "__main__":
    # # Load environment variables from .env file
    # my_common.load_dotenv()
    # Set the path to the JSON file
    if len(sys.argv) < 2:
        curr_path = os.path.dirname(os.path.abspath(__file__))
        print(f"Current path: {curr_path}", end='\n')
        tmp_path = input("Please enter the path of the JSON file: ")
        if tmp_path[0] == '/':
            file_path = tmp_path
        else:
            file_path = os.path.join(curr_path, tmp_path)
    else:
        file_path = sys.argv[1]
    # Read the JSON file
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON: {file_path}")
        exit(1)
    explore_json(data)
