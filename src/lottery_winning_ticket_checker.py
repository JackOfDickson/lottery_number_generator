def lotto_winning_ticket_checker( ticket_numbers, winning_numbers):
    matching_number_count = 0

    for winning_number in winning_numbers:
        if winning_number in ticket_numbers:
            matching_number_count += 1

    if matching_number_count == 2:
        return "You have won a lucky dip!"
    elif matching_number_count >= 2 and matching_number_count < 5:
        return f'You have won moneys for matching ${matching_number_count} numbers!'
    elif matching_number_count == 6:
        return "YOU HAVE WON THE JACKPOT!"
    else:
        return "You get nothing! You lose! Good day sir!"