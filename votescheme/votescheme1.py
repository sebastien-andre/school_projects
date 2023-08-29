import sys


def candidates(ballots):
    candidate_list = []
    for ballot in ballots:
        if ballot not in candidate_list:
            candidate_list.append(ballot)
    return candidate_list


def voteCount(candidate, ballots):
    votes = 0
    for x in ballots:
        if x == candidate:
            votes += 1
    return votes


def voteCounts(candidates, ballots):
    list = []
    for candidate in candidates:
        tuple = (voteCount(candidate, ballots), candidate)
        list.append(tuple)
    return list


def winners(voteCounts):
    voteCounts.sort(reverse=True)
    winner = voteCounts[0]
    all_winners = [x for x in voteCounts if winner[0] in x]
    for x in all_winners:
        print('Winner:', x[1])



def main():
    with open(str(sys.argv[1]), 'r') as f:
        contents = (f.read()).split('\n')
        print('Votes:', contents)

    winners(voteCounts(candidates(contents), contents))


main()
