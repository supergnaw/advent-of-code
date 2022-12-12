import re
import math
# import random
import operator

# Load sample data
sample_1 = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
sample_2 = """
sample_input_goes_here
"""
sinput_1 = sample_1.strip()
sinput_2 = sample_2.strip()

def parse_monkeys(input, print_monkey=False):
    matches = re.findall(r"[^\d]+(\d+):[^:]+:([,\d ]+)[^d]+(old\s.\s(\d+|old))[^y]+y\s(\d+)[^\d]+(\d+)[^\d]+(\d+)", input)
    monkeys = {}
    for monkey in matches:
        monkeys[int(monkey[0])] = {
            "inspect_count": 0
            , True: int(monkey[5])
            , False: int(monkey[6])
            , "test": int(monkey[4].strip())
            , "operation": parse_bonanza(monkey[2].strip())
            , "items": list(map(int, re.findall("\d+", monkey[1])))
        }

        if print_monkey:
            print(f"{monkey[0]}: {monkeys[int(monkey[0])]}")
    return monkeys

def parse_bonanza(operation):
    bananas = {
        "+": operator.add
        , "*": operator.mul
        # I mean, if you're gonna do one (two), you might as well do the rest
        , "-": operator.sub
        , "/": operator.truediv
        , "%": operator.mod
        , "^": operator.xor
    }

    if not re.findall("\d+", operation):
        return (lambda x: bananas[re.findall(r"[^\d\s\w]", operation)[0]](x, x))
    return (lambda x: bananas[re.findall(r"[^\d\s\w]", operation)[0]](x, int(re.findall("\d+", operation)[0])))

def monkey_around(monkeys, rounds = 20):
    turns = range(0, len(monkeys))
    for round in range(0, rounds):
        for turn in turns:
            items = monkeys[turn]["items"]
            for item in items:
                # inspect item
                item = monkeys[turn]["operation"](item) // 3
                monkeys[turn]["inspect_count"] += 1
                # test worry level
                monkeys[monkeys[turn][0 == item % monkeys[turn]["test"]]]["items"].append(item)
            monkeys[turn]["items"] = []
    return monkeys

def monkey_around_more(monkeys, rounds = 20):
    turns = range(0, len(monkeys))
    anxiety = math.lcm(*[monkeys[m]["test"] for m in monkeys])
    print(f"Critical anxiety level before total meltdown: {anxiety}")
    # a round is where all monkeys have a turn
    for round in range(0, rounds):
        # a turn is when a monkey inspects its items
        for turn in turns:
            for item in monkeys[turn]["items"]:
                # inspect item
                monkeys[turn]["inspect_count"] += 1
                # to worry is to suffer
                item = monkeys[turn]["operation"](item) % anxiety
                # throw to the next monkey
                monkeys[monkeys[turn][0 == item % monkeys[turn]["test"]]]["items"].append(item)
            # clear the inventory of the current turn's monkey
            monkeys[turn]["items"] = []
    return monkeys

def calculate_monkey_business(monkeys):
    monkey_businesses = sorted([monkeys[monkey]["inspect_count"] for monkey in monkeys], reverse=True)
    # support your local monkey-business
    return monkey_businesses[0] * monkey_businesses[1]

def log_simian_baffoonary(monkeys, round):
    print(f"\n== After round {round} ==")
    for m in monkeys:
        print(f"Monkey {m} inspected items {monkeys[m]['inspect_count']} times.")
    print("")

# Load input file
input = open("inputs/day-11.txt", 'r').read().strip()


print("########## start pt 1 ##########")
rounds = 20
monkeys = parse_monkeys(sinput_1.replace(r"\s+", "s"), False)
monkeys = monkey_around(monkeys, rounds)
log_simian_baffoonary(monkeys, rounds)
monkey_business = calculate_monkey_business(monkeys)
print(f"Monkey business after {rounds} rounds: {monkey_business}")
print("---------- wrong answers ----------")
print({})
print("========== end pt 1 ==========\n")

print("########## start pt 2 ##########")
monkeys = parse_monkeys(input.replace(r"\s+", "s"), False)
rounds = 10000
monkeys = monkey_around_more(monkeys, rounds)
log_simian_baffoonary(monkeys, rounds)
monkey_business = calculate_monkey_business(monkeys)
print(f"Monkey business after {rounds} rounds: {monkey_business}")
print("---------- wrong answers ----------")
print({})
print("========== end pt 2 ==========\n")
