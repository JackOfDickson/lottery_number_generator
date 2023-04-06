from random import *

def lotto_number_generator():
    generated_lotto_numbers = []

    while len(generated_lotto_numbers) < 6:
        lotto_number = randint(1,60)
        if generated_lotto_numbers.count(lotto_number) != 1:
            generated_lotto_numbers.append(lotto_number)
        
    
    generated_lotto_numbers.sort()

    return generated_lotto_numbers

