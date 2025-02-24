short_tuple = "Rolf", "Bob" # Notice no square brackets
a_bit_clearer = ("Rolf", "Bob") # Brackets no required but it's clearer
tuple_in_list = [("Rolf", "Bob")] # Here brackets are required for adding a tuplet to a list.

# short_tuple.append("Jen") # Add Jen to tuple which you can append to it.
short_tuple = short_tuple + ("Jen",) # Correct way to add Jen to a tuple
print(short_tuple)

#Note: Difference between lists and tuples: With lists you can add/remove elements but with tuples you can't
