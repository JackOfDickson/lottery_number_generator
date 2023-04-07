from random import *

def lotto_number_generator():
    generated_lotto_numbers = []

    while len(generated_lotto_numbers) < 6:
        lotto_number = randint(1,60)
        if lotto_number not in generated_lotto_numbers:
            generated_lotto_numbers.append(lotto_number)
        
    
    generated_lotto_numbers.sort()

    return generated_lotto_numbers


def hold_johns_bags():
    john_looking_for_keys = True
    while john_looking_for_keys:
        user_input = input("Has john found keys?")
        if user_input == "yes":
            john_looking_for_keys = False
