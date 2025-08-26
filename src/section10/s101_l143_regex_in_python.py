import re

email = "jose@tecladocode.com"
expression = "[a-z\.]+"

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = matches[1]

print(name)
print(domain)

# Not using regex
email_address = "jose@tecladocode.com"
parts = email.split("@")
name = parts[0]
domain = parts[1]
print(name)
print(domain)

price = 'Price: $18649.50'

# expression = 'Price: \$(189.50)'
expression = 'Price: \$([0-9]*\.[0-9]*)' # 9384394839483.934839483
matches = re.search(expression, price)

print(matches.group(0)) # entire match
print(matches.group(1)) # first parenthesized (thing) subgroup
price = float(matches.group(1))
print(price)