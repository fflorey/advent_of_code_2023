from functools import cmp_to_key

file_path = "input.txt"
lines = []
cards=[]
bids={}
with open(file_path, "r") as file:
    for line in file:
        cards.append(line.strip().split(" ")[0])
        bids[line.strip().split(" ")[0]]=line.strip().split(" ")[1]


print(cards)

def find_five_same_cards(cards):
    result = []
    for card in cards:
        if len(set(card)) == 1:
            result.append(card)
    return result

def find_four_same_cards(cards):
    result = []
    for card in cards:
        counts = {}
        for char in card:
            counts[char] = counts.get(char, 0) + 1
        if 4 in counts.values():
            result.append(card)
    return result

def find_full_house(cards):
    result = []
    for card in cards:
        counts = {}
        for char in card:
            counts[char] = counts.get(char, 0) + 1
        if 3 in counts.values() and 2 in counts.values():
            result.append(card)
    return result

def find_three_same_cards(cards):
    result = []
    for card in cards:
        counts = {}
        for char in card:
            counts[char] = counts.get(char, 0) + 1
        if 3 in counts.values():
            result.append(card)
    return result

def find_two_pair(cards):
    result = []
    for card in cards:
        counts = {}
        for char in card:
            counts[char] = counts.get(char, 0) + 1
        if len(counts) == 3 and list(counts.values()).count(2) == 2:
            result.append(card)
    return result


def find_two_same_cards(cards):
    result = []
    for card in cards:
        if len(set(card)) == 4:
            result.append(card)
    return result

def find_all_distinct(cards):
    result = []
    for card in cards:
        if len(set(card)) == 5:
            result.append(card)
    return result

def compare_cards(card1, card2):
    order = "AKQJT98765432"
    for char1, char2 in zip(card1, card2):
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
    return sorted_cards
    # order is: A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2
    # A is the highest, 2 is the lowest
    # return 1 if card1 is higher than card2
    # return -1 if card1 is lower than card2
    # return 0 if card1 is equal to card2
    # print(card1, card2)
    

def create_winning_cards_order(cards):
    result = []
    result.append(find_five_same_cards(cards))
    print("Five same cards", result)
    # remove all five same cards from cards
    for card in result[0]:
        cards.remove(card)                
    result.append(find_four_same_cards(cards))
    print("Four same cards", result)
    # remove all four same cards from cards
    for card in result[1]:
        cards.remove(card)
    result.append(find_full_house(cards))
    print("Full house", result)
    # remove all full house cards from cards
    for card in result[2]:
        cards.remove(card)
    result.append(find_three_same_cards(cards))
    print("Three same cards", result)
    # remove all three same cards from cards
    for card in result[3]:
        cards.remove(card)
    result.append(find_two_pair(cards))
    print("Two pair", result)
    # remove all two pair cards from cards
    for card in result[4]:
        cards.remove(card)
    result.append(find_two_same_cards(cards))
    print("Two same cards", result)
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
# print(result)
for i in range(len(result)):
    if len(result[i]) > 0:
        for cards in sort_card_decks(result[i]):
        # for cards in result[i]:
            print(cards)
            print(bids[cards])
            total += int(bids[cards])*rank
            print("Rank: ", rank, "Total: ", total, "Bid: ", bids[cards])
            rank -= 1
            print(total)

print("Total: ", total)
        
        