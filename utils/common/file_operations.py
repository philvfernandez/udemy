from utils.find import NotFoundError
## from ..find import NotFoundError  ## imports parent

def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

print(__name__) ## __main__  Note: This will generate error using ..find import NotFoundError
# as there is no other top level package to import
## This file will run w/o errors if run as module instead of a script.