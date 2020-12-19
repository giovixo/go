import sys
import os
import yaml

with open("/Users/giovanni/Software/scripts/go/dirs.yaml", 'r') as stream:
    try:
        options = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

if len(sys.argv) == 1:
    print("Usage: python go.py option")
    print("Example: 'python go.py gammapy'")
    print("To get the list of the options: 'python go.py list'")
    print("Configuration file: 'Software/scripts/go/dirs.yaml'")
    exit() 

if sys.argv[1] == 'list':
    print('Possible options:')
    for opt in options:
        print('Option: \033[92m', opt['opt'], '\033[0m')
        print('\033[96m' + opt['info'] + '\033[0m')
    exit()

try:
    my_option = [x for x in options if x['opt'] == sys.argv[1]][0]
    os.chdir(my_option['dir'])
    print('\033[96m' + my_option['info'] + '\033[0m')
    if my_option['notes'] != None:
        print("Notes: ", my_option['notes'])
    print("Working dir: {}".format(my_option['dir']))
    if os.path.isfile('info.txt'):
        os.system('cat info.txt')
    os.system('zsh')
    os.system('source .zshrc')
except:
    print("Wrong option. To get the list of the options: 'python go.py list'")
