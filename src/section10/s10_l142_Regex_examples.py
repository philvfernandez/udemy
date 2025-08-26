"""
Testing Regex Testing website: www.regexr.com
1) Given text "charlie"
Regex: /charlie/g
Regex: /.*/g --> matches zero or more of anything.
Regex: /[abc]/gm --> matches any characters in the bracket.
Regex: /[abc]+/gm --> Matches one or more characters in the bracket.  As a single thing.
Regex: /[a-z]/gm --> Matches any characters in the bracket.
Regex: /[A-z]/gm --> Matches any characters in the bracket including capital letters.
Warning: There are 26 letters in the alphabet, but [A-z] contains char codes 65 to 122...
There are a few extra characters in this range.

Example given an email jose@tecladocde.com:
Regex: /[A-z\.]+@/gm -> matches one or more characters before the @ symbol.  Then matches one ore more characters
after the @ symbol.
Here is another example which includes matching one more characters and digits before and after the @ symbol.
Regex: /[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+/gm



"""