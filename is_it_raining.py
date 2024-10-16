import random

def is_it_raining():
    if random.choice([True, False]):
        return "Yes it's raining"
    else:
        return "No it's not raining"

print(is_it_raining())