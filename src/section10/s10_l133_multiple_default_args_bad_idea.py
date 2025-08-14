def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }

a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Jen')

"""
This prints "{'name': 'savings', 'main_account_holder': 'Jen', 'account_holders': ['Rolf', 'Jen']}"
because the list is created at the time it is declared.  So because the third parameter is the same list
and is pointed to by the same id, Rolf and Jen are added to the same list.
You can solve this by not having a default argument when declaring the method.  But pass in an empty list
when the method is called.  For example,
a1 = create_account('checking', 'Rolf', [])
a2 = create_account('savings', 'Jen', [])
You can also use None as the third argument when declaring the method.  You will then need to check for an empty list
within the body of the method before appending to the list.
For example, 
def create_account(name: str, holder: str, account_holders = None):
 if not account_holders:
   account_holders = []
 account_holders.append(holder)
"""
print(a2)