"""
- Removes extra spaces
- Replaces spaces to hyphens
- Makes lowercase
- ignores dotfiles
- ignore directories and is not RECURSIVE
python renaming.py
"""
import os

path =  os.getcwd()



def remove_extra_spaces():
    for filename in filenames:
        if os.path.isfile(filename) and filename[0]!='.':
            for i in range(1,10):
                os.rename(filename, filename.replace(i*' ',' '))
            if filename[-1]!=' ': filename[0]!=''
            os.rename(filename, filename.replace(' .','.'))


def spaces_to_hyphens_lowercaser():
    for filename in filenames:
        if os.path.isfile(filename) and filename[0]!='.':
            os.rename(filename, filename.replace(" ","-"))
            os.rename(filename, filename.lower())


filenames = os.listdir(path)
print('Before',filenames)

remove_extra_spaces()
spaces_to_hyphens_lowercaser()

filenames = os.listdir(path)
print('After',filenames)
