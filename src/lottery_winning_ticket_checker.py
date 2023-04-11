def lotto_winning_ticket_checker( ticket_numbers, winning_numbers):
    matching_number_count = 0
    bonus_ball = winning_numbers.pop() #Bonus Ball last number in the list
    non_matching_numbers = [] #To be used to check if they match the bonus ball
    matching_bonus_ball = False

    for number in ticket_numbers:
        if number in winning_numbers:
            matching_number_count += 1
        else:
            non_matching_numbers.append(number)

    
    for number in non_matching_numbers:
        if number == bonus_ball:
            matching_bonus_ball = True
            break

    if matching_number_count == 2:
        return "You have won a lucky dip!"
    elif matching_number_count > 2 and matching_number_count < 5:
        return f'You have won moneys for matching {matching_number_count} numbers!'
    elif matching_number_count == 6:
        return "YOU HAVE WON THE JACKPOT!"
    else:
        return "You get nothing! You lose! Good day sir!"