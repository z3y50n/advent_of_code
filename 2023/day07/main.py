from enum import IntEnum
from collections import Counter
from functools import cmp_to_key


class Rank(IntEnum):
    HIGH = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_KIND = 3
    FULL_HOUSE = 4
    FOUR_KIND = 5
    FIVE_KIND = 6


card_strength = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

card_strength_joker = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


def read_data(filename: str):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    return [(row.split()[0], int(row.split()[1])) for row in data]


def get_hand_rank(hand: str) -> Rank:
    counter = Counter(hand)
    count_set = set(counter.values())
    if 5 in count_set:
        return Rank.FIVE_KIND
    if 4 in count_set:
        return Rank.FOUR_KIND
    if 3 in count_set:
        if 2 in count_set:
            return Rank.FULL_HOUSE
        return Rank.THREE_KIND
    if 2 in count_set:
        if counter.most_common(2)[1][1] == 2:
            return Rank.TWO_PAIRS
        return Rank.ONE_PAIR
    return Rank.HIGH


def sort_cmp(hand1: tuple[str, int], hand2: tuple[str, int]):
    rank1 = get_hand_rank(hand1[0])
    rank2 = get_hand_rank(hand2[0])
    if rank1 == rank2:
        for c1, c2 in zip(hand1[0], hand2[0]):
            s1 = card_strength[c1]
            s2 = card_strength[c2]
            if s1 == s2:
                continue
            if s1 > s2:
                return 1
            return -1
    if rank1 > rank2:
        return 1
    return -1


def part1(cards: list[tuple[str, int]]) -> int:
    sorted_cards = sorted(cards, key=cmp_to_key(sort_cmp))
    return sum([(idx + 1) * card[1] for (idx, card) in enumerate(sorted_cards)])


def get_hand_rank_joker(hand: str) -> Rank:
    counter = Counter(hand)
    joker_count = counter["J"]
    count_set = set(counter.values())

    if 5 in count_set:
        return Rank.FIVE_KIND
    if 4 in count_set:
        if joker_count == 1 or joker_count == 4:
            return Rank.FIVE_KIND
        return Rank.FOUR_KIND
    if 3 in count_set:
        if 2 in count_set:
            if joker_count == 2 or joker_count == 3:
                return Rank.FIVE_KIND
            return Rank.FULL_HOUSE
        if joker_count == 1 or joker_count == 3:
            return Rank.FOUR_KIND
        return Rank.THREE_KIND
    if 2 in count_set:
        if counter.most_common(2)[1][1] == 2:
            if joker_count == 2:
                return Rank.FOUR_KIND
            if joker_count == 1:
                return Rank.FULL_HOUSE
            return Rank.TWO_PAIRS
        if joker_count == 2 or joker_count == 1:
            return Rank.THREE_KIND
        return Rank.ONE_PAIR
    if joker_count == 1:
        return Rank.ONE_PAIR
    return Rank.HIGH


def sort_cmp_joker(hand1: tuple[str, int], hand2: tuple[str, int]):
    rank1 = get_hand_rank_joker(hand1[0])
    rank2 = get_hand_rank_joker(hand2[0])
    if rank1 == rank2:
        for c1, c2 in zip(hand1[0], hand2[0]):
            s1 = card_strength_joker[c1]
            s2 = card_strength_joker[c2]
            if s1 == s2:
                continue
            if s1 > s2:
                return 1
            return -1
    if rank1 > rank2:
        return 1
    return -1


def part2(cards: list[tuple[str, int]]) -> int:
    sorted_cards = sorted(cards, key=cmp_to_key(sort_cmp_joker))
    return sum([(idx + 1) * card[1] for (idx, card) in enumerate(sorted_cards)])


if __name__ == "__main__":
    test_cards = read_data("test_input")
    cards = read_data("input")
    assert part1(test_cards) == 6440
    print(part1(cards))

    assert part2(test_cards) == 5905
    print(part2(cards))
