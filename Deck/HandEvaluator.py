from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    if len(hand) == 0:
        return "High Card"
    #Rank and suits count
    rank_counts = {}
    suit_counts = {}
    for card in hand:
        rank = card.rank.value
        suit = card.suit
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
        suit_counts[suit] = suit_counts.get(suit, 0) + 1
    #Sorting ranks
    counts_sorted = sorted(rank_counts.values(), reverse=True)

    #Hand checking
    #1:Flush
    flush_suit = None
    for suit, count in suit_counts.items():
        if count >= 5:
            flush_suit = suit
            break

    #2:Straight, ace counts as 1, so add one

    unique_ranks = sorted(set(rank_counts.keys()))
    if 14 in unique_ranks:
        unique_ranks.append(1)
    unique_ranks = sorted(unique_ranks)

    straight = False

    for i in range(len(unique_ranks)-4):
        seq = unique_ranks[i:i+5]
        if seq == list(range(seq[0], seq[0]+5)):
            straight = True
            break

    #3:Straight Flush
    if flush_suit:
        flush_cards = [card.rank.value for card in hand if card.suit == flush_suit]
        #same as straight but with flush
        unique_flush_ranks = sorted(set(flush_cards))

        if 14 in unique_flush_ranks:
            unique_flush_ranks.append(1)
        unique_flush_ranks = sorted(unique_flush_ranks)

        for x in range(len(unique_flush_ranks)-4):
            seq = unique_flush_ranks[x:x+5]
            if seq == list(range(seq[0], seq[0]+5)):
                return "Straight Flush"

#Checking other hand's rank cards
    if counts_sorted[0]==4:
        return "Four of a Kind"
    if len(counts_sorted) >= 2 and counts_sorted[0] == 3 and counts_sorted[1] == 2:
        return "Full House"
    if flush_suit:
        return "Flush"
    if straight:
        return "Straight"
    if counts_sorted[0]==3:
        return "Three of a Kind"
    if len(counts_sorted) > 1 and counts_sorted[0] == 2 and counts_sorted[1] == 2:
        return "Two Pair"
    if counts_sorted[0]==2:
        return "One Pair"

    return "High Card"