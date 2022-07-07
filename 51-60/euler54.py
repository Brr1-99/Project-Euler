"""
The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

converter = {
    "T": "10",
    "J": "11",
    "Q": "12",
    "K": "13",
    "A": "14"
}

points = {
    "High Card": 1,
    "One Pair": 2,
    "Two Pairs": 3,
    "Three of a Kind": 4,
    "Straight": 5,
    "Flush": 6,
    "Full House": 7,
    "Four of a Kind": 8,
    "Straight Flush": 9,
    "Royal Flush": 10
}

p1_counter = 0
p2_counter = 0
more_work = 0


def get_numbers(hand):
    temp = []
    for i in range(len(hand)//3+1):
        t = hand[i*3]
        if t in converter:
            t = converter[t]
        temp.append(int(t))
    temp.sort()
    return temp # [2, 7, 7, 13, 13]

def get_suits(hand):
    temp = []
    for i in range(len(hand)//3+1):
        temp.append(hand[i*3+1])
    temp.sort()
    return temp # ['C', 'D', 'H', 'S', 'S']

def check_consecutive(nums):
    # if consecutive returns True -> [2,3,4,5,6]
    for i in range(len(nums)-1):
        if nums[i] + 1 == nums[i+1]:
            pass
        else:
            return False
    return True

def check_main(hand):
    nums = get_numbers(hand)
    suits = get_suits(hand)

    # checkt, ob suits alle gleich sind
    if len(set(suits)) == 1:
        # checkt, ob nums consecutive sind
        if check_consecutive(nums):
            if nums[0] == 10:
                return("Royal Flush")
            else:
                return("Straight Flush")
        else:
            return("Flush")

    # checkt, ob nur zwei verschiede Werte vorhanden sind (four oder full house)
    if len(set(nums)) == 2:
        if nums.count(nums[0]) == 4 or nums.count(nums[1]) == 4:
            return("Four of a Kind")
        else:
            return("Full House")

    if check_consecutive(nums):
        return("Straight")

    # checkt, ob nur drei verschiede Werte vorhanden sind (Three oder Two Pairs)
    if len(set(nums)) == 3:
        if nums.count(nums[2]) == 3:
            return("Three of a Kind")
        else:
            return("Two Pairs")

    if len(set(nums)) == 4:
        return("One Pair")

    return("High Card")

def check_more(hand, points):
    nums = get_numbers(hand)
    suits = get_suits(hand)

    # one pair
    if points == 2:
        for num in nums:
            if nums.count(num) == 2:
                return num

    # high card
    if points == 1:
        return nums[4]

def find_winner(p1, p2):
    global p1_counter
    global p2_counter
    global more_work

    p1_points = points[check_main(p1)]
    p2_points = points[check_main(p2)]
    if p1_points > p2_points:
        p1_counter += 1
    elif p1_points < p2_points:
        p2_counter += 1
    else:
        p1_hc = check_more(p1, p1_points)
        p2_hc = check_more(p2, p2_points)
        if p1_hc > p2_hc:
            p1_counter += 1
        elif p1_hc < p2_hc:
            p2_counter += 1
        else:
            more_work += 1

def main(game):
    p1 = game[0:len(game)//2]
    p2 = game[len(game)//2+1:len(game)]
    find_winner(p1, p2)


with open('51-60\poker.txt') as file:
    games = file.read()
    # Split a string into a list where each line is a list item
    games = games.splitlines()
    # Remove spaces at the beginning and at the end of each element
    games = [e.strip() for e in games]
    for game in games:
        main(game)
    print("p1_counter:", p1_counter, "p2_counter:", p2_counter, "more_work:", more_work)