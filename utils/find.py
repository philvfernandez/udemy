from utils.file_operations import save_to_file
# another way to make the above import is: from .file_operations import save_to_file
# However, if you run just this py file, it will not work, resulting in a runtime error.
#

# Note the '.' means inside the current folder.

def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFoundError(f'{expected} not found in provided iterable')

class NotFoundError(Exception):
    pass