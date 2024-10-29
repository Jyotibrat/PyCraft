import random

def get_cpu_move():
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_move():
    opts = ['rock', 'paper', 'scissors']
    plyr_ipt = input("What's your choice? Rock, Paper, or Scissors: ").lower()
    
    if plyr_ipt not in opts:
        print("\nHmm, that's not a valid choice! Let's try that again.")
        return get_player_move()
    return plyr_ipt

def find_winner(plyr_mv, cpu_mv):
    if plyr_mv == cpu_mv:
        return "It's a tie! Looks like we're on the same wavelength."
    
    win_mvs = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    if win_mvs[plyr_mv] == cpu_mv:
        return "Awesome! You win this round!"
    else:
        return "Oh no! The computer took the victory this time."

def start_game():
    print("\n🌟 Welcome to the Rock, Paper, Scissors Showdown! 🌟\n")
    
    cpu_mv = get_cpu_move()
    plyr_mv = get_player_move()
    
    print(f"\nYou chose: {plyr_mv.capitalize()}")
    print(f"Computer chose: {cpu_mv.capitalize()}")
    
    rslt = find_winner(plyr_mv, cpu_mv)
    print(f"\n{rslt}\n")

if __name__ == "__main__":
    start_game()
