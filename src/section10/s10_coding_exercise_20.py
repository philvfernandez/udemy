import re
"""
Our definition of a secure filename is:
- The filename must start with an English letters or a number (a-zA-Z0-9)
- The filename can **only** contain English letters, numbers and '-_()'.
- The filename must end with a proper file extension among '.jpg', 'jpeg', '.png', and '.gif'
"""

def is_filename_safe(filename):
    # you only need to change the regular expression (regex) below
    regex = r'^[a-zA-Z0-9][a-zA-Z0-9_-]*[\(a-zA-Z0-9]*[\)]*\.(jpg|jpeg|png|gif)$'
    return re.match(regex, filename) is not None

print(is_filename_safe('a1-a_2(1).jpg'))
print(is_filename_safe('05645com'))




