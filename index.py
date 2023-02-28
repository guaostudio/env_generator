import sys
import json
from os.path import exists

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def env_file(data):
  try:
    f = open(".env", "w")
    f.write(data)
    f.close()
  except ValueError:
    return print('A problem occurred when creating the .env file')

def env_exists():
  file_exists = exists('.env')
  return file_exists

def env_data():
  try:
    if len(sys.argv) == 1: raise ValueError('You must send a parameter with json format')

    arguments = sys.argv[1]

    if is_json(arguments) == False: raise ValueError('Please verify that you sent the json correctly')
    if env_exists() == True: raise ValueError('.env file already exists')

    arr_env = json.loads(arguments)
    env_data = ""

    for var in arr_env:
      var_key = list(var.keys())
      env_data += f"{var_key[0]}={var[var_key[0]]}\n"

    env_file(env_data)

    print('SUCCESS: .env file was created successfully')
  except ValueError as e:
    return print('ERROR: ',e)

env_data()