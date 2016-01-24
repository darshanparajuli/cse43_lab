from collections import defaultdict

import prompt


def read_voter_preferences(file: open):
    result = defaultdict(list)
    for line in file:
        line = line.rstrip('\n').split(';')
        result[line[0]] = line[1:]
    return dict(result)


def dict_as_str(d: {None: None}, key: callable = None, reverse: bool = False) -> str:
    return ''.join(['  {} -> {}\n'.format(k, d[k]) for k in sorted(d.keys(), key=key, reverse=reverse)])


def evaluate_ballot(vp: {str: [str]}, cie: {str}) -> {str: int}:
    result = defaultdict(int)
    for k in vp.keys():
        for c in vp[k]:
            if c in cie:
                result[c] += 1
                break
    return dict(result)


def remaining_candidates(vd: {str: int}) -> {str}:
    min_vote_count = min(vd.values())
    return set([k for k in vd.keys() if vd[k] > min_vote_count])


def run_election(vp_file: open) -> {str}:
    vp = read_voter_preferences(vp_file)
    cie = set([j for i in vp.keys() for j in vp[i]])
    ballot_count = 1
    while True:
        ballot = evaluate_ballot(vp, cie)

        print('Vote count on ballot #{} with candidates (alphabetical order): remaining candidates = {}'.format(
                ballot_count, cie))
        print(dict_as_str(ballot, key=lambda x: x))

        print('Vote count on ballot #{} with candidates (numerical order): remaining candidates = {}'.format(
                ballot_count, cie))
        print(dict_as_str(ballot, key=lambda x: ballot[x], reverse=True))

        ballot_count += 1
        cie = remaining_candidates(ballot)
        if len(cie) <= 1:
            break

    if len(cie) == 1:
        print('Winner is {}'.format(cie))
    else:
        print('No winner: election is a tie among the candidates remaining on the last ballot')
    print()

    return cie


if __name__ == '__main__':
    # Write script here
    while True:
        name = prompt.for_string('Enter the name of a file with voter preferences', is_legal=lambda x: len(x) > 0)
        try:
            with open(name, 'r') as file:
                vp = read_voter_preferences(file)
                print('Voter Preferences')
                print(dict_as_str(vp))

            with open(name, 'r') as file:
                run_election(file)
            break
        except Exception as e:
            print(str(e))

    # For running batch self-tests
    print()
    import driver

    driver.default_file_name = "bsc2.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
