def lotto_winning_ticket_checker( ticket_numbers: list, winning_numbers: list):
    matching_number_count = 0

    for winning_number in winning_numbers:
        for ticket_number in ticket_numbers:
            if winning_number == ticket_number:
                matching_number_count += 1

    if matching_number_count == 2:
        return "You have won a lucky dip!"
    elif matching_number_count > 2 & matching_number_count < 5:
        return f'You have won moneys for matching ${matching_number_count} numbers!'
    elif matching_number_count == 6:
        return "YOU HAVE WON THE JACKPOT!"
    else:
        return "You get nothing! You lose! Good day sir!"