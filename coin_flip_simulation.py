from random import randint
from statistics import mode


def flip_coin(flip_count_per_flip, best_of=None):
    winnings = []
    total_heads_wins = 0
    total_tails_wins = 0
    for num in range(best_of):
        print(f'Flip {num + 1} ({flip_count_per_flip} flips)...')
        outcomes = [randint(0, 1) for _ in range(flip_count_per_flip)]

        heads_count = outcomes.count(0)
        tails_count = outcomes.count(1)
        total_heads_wins += outcomes.count(0)
        total_tails_wins += outcomes.count(1)

        winnings.append(0 if heads_count > tails_count else 1)

    return {'winner': "Heads" if mode(winnings) == 0 else "Tails", "total_heads": total_heads_wins,
            "total_tails": total_tails_wins, 'total_flips': best_of * flip_count_per_flip}


winners = []
while True:
    flip_count = input('\nEnter flip count (integer) or type "quit": ')
    if flip_count == "quit":
        print(f"\nQuitting...\nTotal Overall Wins: Heads - {winners.count('Heads')} | Tails - {winners.count('Tails')}")
        break
    best_of_input = input('Best of (integer)? ')

    coinflip_results = flip_coin(flip_count_per_flip=int(flip_count), best_of=int(best_of_input))
    winners.append(coinflip_results['winner'])
    print(f"Coinflip Results:\n"
          f"Heads: {coinflip_results['total_heads']}\n"
          f"Tails: {coinflip_results['total_tails']}\n"
          f"{coinflip_results['winner']} won by {abs(coinflip_results['total_heads'] - coinflip_results['total_tails'])} flips out of {coinflip_results['total_flips']} total.")
    if len(winners) > 2:
        print(f"\nTotal Overall Wins: Heads - {winners.count('Heads')} | Tails - {winners.count('Tails')}")
