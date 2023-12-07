from functools import cmp_to_key

file_path = "input.txt"
lines = []
cards=[]
bids={}
with open(file_path, "r") as file:
    for line in file:
        cards.append(line.strip().split(" ")[0])
        bids[line.strip().split(" ")[0]]=int(line.strip().split(" ")[1])

print(cards)

def count_number_of_jokers_in_cards(cards):
    count = 0
    for card in cards:
        if 'J' in card:
            count += 1
    return count

def find_five_same_cards(cards):
    result = []
    for card in cards:
        orig=card
        counts = {}
        jokers=count_number_of_jokers_in_cards(card)
        card = card.replace('J', '')
        # print("Jokers: ", jokers, "in cards ", card)
        for char in card:
            counts[char] = counts.get(char, 0) + 1
        if 5 in counts.values() or (4 in counts.values() and jokers == 1):
            result.append(orig)
        # two jokers and three same cards
        elif jokers == 2 and 3 in counts.values():
            result.append(orig)
        elif jokers == 3 and 2 in counts.values():
            result.append(orig)
        elif jokers == 4 and 1 in counts.values():
            result.append(orig)
        elif jokers == 5:
            result.append(orig)
    return result

def find_four_same_cards(cards):
    result = []
    for card in cards:
        orig=card
        counts = {}
        jokers=count_number_of_jokers_in_cards(card)
        card = card.replace('J', '')
        for char in card:
            counts[char] = counts.get(char, 0) + 1
        if 4 in counts.values() or (3 in counts.values() and jokers == 1):
            result.append(orig)
        elif jokers == 2 and (2 in counts.values()):
            # print("4 SAME CARDS! Jokers: ", jokers, "in cards ", card, "counts: ", counts)
            # readline = input()
            result.append(orig)
        elif jokers == 3:
            result.append(orig)
    return result

def find_full_house(cards):
    result = []
    for card in cards:
        orig=card
        counts = {}
        jokers=count_number_of_jokers_in_cards(card)
        card = card.replace('J', '')
        for char in card:
            counts[char] = counts.get(char, 0) + 1
        if 3 in counts.values() and (2 in counts.values()):
            result.append(orig)
        elif (len(counts) == 2 and list(counts.values()).count(2) == 2) and jokers == 1:
            result.append(orig)        
    return result
                
def find_three_same_cards(cards):
    result = []
    for card in cards:
        orig=card
        counts = {}
        jokers=count_number_of_jokers_in_cards(card)
        card = card.replace('J', '')
        for char in card:
            counts[char] = counts.get(char, 0) + 1
        if 3 in counts.values() or (2 in counts.values() and jokers == 1):
            result.append(orig)
        elif jokers == 2:
            result.append(orig)
        elif jokers == 3:
            result.append(orig)
    return result

def find_two_pair(cards):
    result = []
    for card in cards:
        orig=card
        counts = {}
        jokers=count_number_of_jokers_in_cards(card)
        card = card.replace('J', '')
        for char in card:
            counts[char] = counts.get(char, 0) + 1
        if len(counts) == 3 and list(counts.values()).count(2) == 2:
            result.append(orig)
        elif len(set(card)) == 3 and jokers == 1:
            result.append(orig)
    return result

def find_one_pair(cards):
    result = []
    for card in cards:
        orig=card
        counts = {}
        jokers=count_number_of_jokers_in_cards(card)
        card = card.replace('J', '')
        for char in card:
            counts[char] = counts.get(char, 0) + 1
        print("FIND ONE PAIR: Jokers: ", jokers, "in cards ", card, "counts.values(): ", counts.values())
        if 2 in counts.values():
            result.append(orig)
        elif jokers == 1:
            result.append(orig)
    return result

def find_all_distinct(cards):
    result = []
    for card in cards:
        if len(set(card)) == 5 and 'J' not in card:
            result.append(card)
    return result

def compare_cards(card1, card2):
    order = "AKQT98765432J"
    for char1, char2 in zip(card1, card2):
        print("Comparing c1:",char1, " and c2:", char2, " in ", card1, " and ", card2)
        rank1 = order.index(char1)
        rank2 = order.index(char2)
        if rank1 == rank2:
            continue
        if rank1 > rank2:
            return 1
        elif rank1 < rank2:
            return -1
    return 0


def sort_card_decks(cards):
    sorted_cards = sorted(cards, key=cmp_to_key(compare_cards) )
    print("Sorted cards: ", sorted_cards)
    return sorted_cards
    

def create_winning_cards_order(cards):
    result = []
    result.append(find_five_same_cards(cards))
    print("Five same cards", result)
    # remove all five same cards from cards
    for card in result[0]:
        cards.remove(card)                
    result.append(find_four_same_cards(cards))
    print("Four same cards", result)
    input()
    # remove all four same cards from cards
    for card in result[1]:
        cards.remove(card)
    result.append(find_full_house(cards))
    print("Full house", result)
    input()
    # remove all full house cards from cards
    for card in result[2]:
        cards.remove(card)
    result.append(find_three_same_cards(cards))
    print("Three same cards", result)
    input()
    # remove all three same cards from cards
    for card in result[3]:
        cards.remove(card)
    result.append(find_two_pair(cards))
    print("Two pair", result)
    input()
    # remove all two pair cards from cards
    for card in result[4]:
        cards.remove(card)
    result.append(find_one_pair(cards))
    print("Two same cards", result)
    input()
    # remove all two same cards from cards
    for card in result[5]:
        cards.remove(card)
    result.append(find_all_distinct(cards))
    print("All distinct", result)
    # remove all all distinct cards from cards
    for card in result[6]:
        cards.remove(card)
    print("Cards left", cards)
    return result

total=0
rank=len(cards)
result = create_winning_cards_order(cards)
for i in range(len(result)):
    if len(result[i]) > 0:
        for cards in sort_card_decks(result[i]):
            print(cards)
            print(bids[cards])
            total += int(bids[cards])*rank
            print("Rank: ", rank, "Total: ", total, "Bid: ", bids[cards])
            rank -= 1
            print(total)

print("Total: ", total)
        
        