from src.lottery_number_generator import *
from src.lottery_winning_ticket_checker import *

my_numbers = lotto_number_generator()
print(my_numbers)

winning_lotto_numbers = [4, 18, 29, 30, 39, 52, 46]
result = lotto_winning_ticket_checker(my_numbers, winning_lotto_numbers)
print(result)