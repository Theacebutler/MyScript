#! /usr/bin/env python3
# FullFlask.py
from os import makedirs, chdir, getcwd, path
from sys import argv

def main():
    if len(argv) != 2:
        return print('\nUsage:\n  MF.py [Name of new folder]')

    # make a parent dir for the whole project
    makedirs(argv[1], exist_ok=True)
    chdir(argv[1])
    # in thet dir 
        # create a file file named 'run.py'
    with open('run.py', 'w') as run:
        run.write('''from app import app \n\n\n
                    if __name__ == "__main__": \n
                        app.run(debug=True)''')
        # create a requirements.txt file for pip install
    with open('requirements.txt', 'w') as req:
        req.write('flask')
        # create a dir called 'app'
    makedirs('app', exist_ok=True)
    chdir('app')
    # in the app folder create a static and templates folder
    makedirs('templats', exist_ok=True)
    makedirs('static', exist_ok=True)

    allpath = [str(getcwd()), 'templats']
    chdir(path.join(*allpath))
    # create a layout and index files in the templates folder
    with open ('layout.html', 'w') as layout:
        pass
    with open ('index.html', 'w') as index:
        index.write('{% extends "layout.html" %} \n {% block body %} \n\n\n {% endblock %}')





if __name__ =='__main__':
    main()