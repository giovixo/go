import sys
import os
import yaml
# print("This is the name of the script:", sys.argv[0])
# print("Number of arguments:", len(sys.argv))
# print("The arguments are:" , str(sys.argv))

#file = open('dirs.txt', 'r') 
#dirs = file.readlines() 

with open("/Users/giovanni/sw/scripts/dirs.yaml", 'r') as stream:
    try:
        options = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

if len(sys.argv) == 1:
    print("Usage example: go.py ml")
    print("List of the options: /Users/giovanni/sw/scripts/dirs.yaml")
    exit() 

# if sys.argv[1] == "1":
#     print(options[0]['info'])
#     print("New dir: {}".format(dirs[0]))
#     #os.chdir(dirs[0].strip())
#     os.chdir(options[0]['dir'])
#     os.system('zsh')
# else:
#     print('Wrong argument')

[x for x in options if x['opt'] == 1] 

#index = int(sys.argv[1])
try:
    my_option = [x for x in options if x['opt'] == sys.argv[1]][0]
    os.chdir(my_option['dir'])
    print(my_option['info'])
    print("Working dir: {}".format(my_option['dir']))
    os.system('zsh')
except:
    print('Wrong option')
