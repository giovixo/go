import sys
import os
import yaml

with open("/Users/giovanni/sw/scripts/dirs.yaml", 'r') as stream:
    try:
        options = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

if len(sys.argv) == 1:
    print("Usage: python go.py option")
    print("Example: 'python go.py ml'")
    print("To get the list of the options: 'python go.py list'")
    print("Configuration file: 'sw/script/dirs.yaml'")
    exit() 

if sys.argv[1] == 'list':
    print('Possible options:')
    for opt in options:
        print('Option: ', opt['opt'])
        print(opt['info'])
    exit()

try:
    my_option = [x for x in options if x['opt'] == sys.argv[1]][0]
    os.chdir(my_option['dir'])
    print(my_option['info'])
    if my_option['notes'] != None:
        print("Notes: ", my_option['notes'])
    print("Working dir: {}".format(my_option['dir']))
    os.system('zsh')
except:
    print("Wrong option. To get the list of the options: 'python go.py list'")