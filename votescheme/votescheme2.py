import sys


def candidates(ballots):
    candidate_list = []
    for ballot in ballots:
        for level2_ballot in ballot:
            if level2_ballot not in candidate_list:
                candidate_list.append(level2_ballot)
    return candidate_list


def voteCount(candidate, votes):
    first_place_votes = 0
    for x in votes:
        try:
            if candidate in x[0]:
                first_place_votes += 1
        except IndexError:
            pass
    return first_place_votes


def eliminate(candidate, ballots):
    for ballot in ballots:
        try:
            ballot.remove(candidate)
        except ValueError:
            pass
    return ballots


def remove_empty_ballot(ballots):
    for _ in range(10):
        for ballot in ballots:
            if not ballot:
                ballots.remove(ballot)
    return ballots


def rank_first_preferences(ballots):
    ranks = []
    for candidate in candidates(ballots):
        ranks.append((voteCount(candidate, ballots), candidate))
    return sorted(ranks)


def find_lowest(ranks):
    loser = ranks[0]
    all_losers = [x[1] for x in ranks if loser[0] in x]
    return all_losers


def single_or_no_candidate(ballots):
    if len(candidates(ballots)) <= 1:
        return True
    else:
        return False


def main():
    with open(str(sys.argv[1]), 'r') as f:
        ballots = []
        ballots2 = (f.read()).split('\n')
        for x in ballots2:
            ballots.append(x.split(','))
    print('Ballots:', ballots)

    while not len(candidates(ballots)) <= 1:
        ranks = rank_first_preferences(ballots)
        for x in find_lowest(ranks):
            winners = find_lowest(ranks)
            eliminate(x, ballots)
            remove_empty_ballot(ballots)

    if not ballots:
        for winner in winners:
            print('Winner:', winner)
    else:
        print('Winner:', candidates(ballots)[0])


main()
