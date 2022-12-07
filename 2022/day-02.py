# Load input_02 file
input_02 = open("inputs/day-02.txt", 'r').read()

def parse_choice(input):
    associations = {
        "A": "rock"
        , "B" : "paper"
        , "C" : "scissors"
        , "X" : "rock"
        , "Y" : "paper"
        , "Z" : "scissors"
    }
    return associations[input]

def parse_end(input):
    outcome = {
        "X" : "loss"
        , "Y" : "draw"
        , "Z" : "win"
    }
    return outcome[input]

def pick_win_loss_tie(you, outcome):
    choices = {
        "win": {
            "rock": "paper"
            , "paper": "scissors"
            , "scissors": "rock"
        }
        , "loss": {
            "rock" : "scissors"
            , "paper": "rock"
            , "scissors": "paper"
        }
        , "draw" : {
            "rock" : "rock"
            , "paper": "paper"
            , "scissors": "scissors"
        }
    }
    return choices[outcome][you]

def choice_points(choice):
    if "rock" == choice:
        return 1
    if "paper" == choice:
        return 2
    return 3

def outcome_points(outcome):
    if "win" == outcome:
        return 6
    if "tie" == outcome:
        return 3
    return 0

def win_loss_tie(you, me):
    if "rock" == you:
        if "rock" == me:
            return "tie"
        elif "paper" == me:
            return "win"
        elif "scissors" == me:
            return "loss"
    elif "paper" == you:
        if "rock" == me:
            return "loss"
        elif "paper" == me:
            return "tie"
        elif "scissors" == me:
            return "win"
    elif "scissors" == you:
        if "rock" == me:
            return "win"
        elif "paper" == me:
            return "loss"
        elif "scissors" == me:
            return "tie"

def calculate_score(you, me):
    return outcome_points(win_loss_tie(you, me)) + choice_points(me)

total_score_1 = 0
for game in input_02.split("\n"):
    if 0 == len(game.strip()):
        continue
    you, me = game.split(" ")
    you = parse_choice(you)
    me = parse_choice(me)
    score = calculate_score(you, me)
    ch_pts = choice_points(me)
    outcome = win_loss_tie(you, me)
    print(f"{you:>8} x {me:<8} ({choice_points(me)}) | {outcome:^5} ({outcome_points(outcome)}) | {score}")
    total_score_1 += score
print("========== end pt 1 ==========")

total_score_2 = 0
for game in input_02.split("\n"):
    if 0 == len(game.strip()):
        continue
    you, me = game.split(" ")
    you = parse_choice(you)
    outcome = parse_end(me)
    me = pick_win_loss_tie(you, outcome)
    score = calculate_score(you, me)
    print(f"{you:>8} x {me:<8} ({choice_points(me)}) | {outcome:^5} ({outcome_points(outcome)}) | {score}")
    total_score_2 += score
print("========== end pt 2 ==========")

print(f"part 1 total_score: {total_score_1}")
print(f"part 2 total_score: {total_score_2}")
