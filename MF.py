#! /usr/bin/env python3
# MF.py
from os import makedirs, chdir, getcwd, path
from sys import argv

def main():
    if len(argv) < 2:
        return print('\nUsage:\n  MF [Name of new folder]')
    
    try:
        # make a dir with the name from the user 
        makedirs(argv[1], exist_ok=True)
        chdir(argv[1])
        # create an app.py file
        with open('app.py', 'w') as app:
            app.write('from flask import Flaks')
        # create a requirements.txt file for pip install
        with open('requirements.txt', 'w') as req:
            req.write('flask')
        chdir(getcwd())
        # create templates and static folders
        makedirs('templats', exist_ok=True)
        makedirs('static', exist_ok=True)


        allpath = [str(getcwd()), 'templats']
        chdir(path.join(*allpath))
        # create a layout and index files in the templates folder
        with open ('layout.html', 'w') as layout:
            layout.write('!')
        with open ('index.html', 'w') as index:
            index.write('{% extends layout.html %} \n {% block body %} \n\n\n {% endblock %}')

        # chdir(getcwd())
        # create a styels.css file in the static folder
        allpath = [str(getcwd()), '../', 'static']
        chdir(path.join(*allpath))
        with open ('styles.css', 'w') as css:
            pass

    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
            