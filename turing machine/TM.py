import sys


def construct_tm_dictionary(fname):
    newlist = []
    with open(str(fname), 'r') as f:
        file = (f.read()).split('\n')
    # remove comments in beginning of file
    for line in file:
        if line[0] != '%':
            newlist.append(line.split(','))
    # determine the highest value the first dictionary is created to
    highest_state_list = newlist[-1]
    highest_state = int(highest_state_list[0])

    # constructor for first dictionary
    tm_dictionary = {}

    for x in range(highest_state):
        dict2 = {}
        # constructor for second dictionary
        for string in newlist:
            if string[0] == str(x + 1):
                dict2[string[2]] = (string[1], string[3], string[4])
        tm_dictionary[x + 1] = dict2

    return tm_dictionary


def print_tape(tape, state):
    print(tape[0], state)
    print((tape[1]) * ' ' + '^')


# if state == h, then break out of while loop, or if state has no number for it
# if there's another state where the arrows come in with no exit, then break out
# Also, if there's no arrow going out for the value you are reading, then break out
# ^^ just use these as basic if statements in beginning of while loop


def run_TM(tm_dictionary, state, tape, debug):
    accept = False
    while True:
        current_tape = tape[0]
        position = tape[1]

        if position < 0:
            current_tape = '#' + current_tape
            position = 0
            tape = (current_tape, position)

        if position > len(current_tape) - 1:
            current_tape = current_tape + '#'
            # position -= 1
            tape = (current_tape, position)

        if debug:
            print_tape(tape, state)
            input()

        if state == 'h':
            accept = True
            break

        if int(state) not in tm_dictionary:
            break

        second_dict = tm_dictionary[int(state)]
        current_character = current_tape[position]

        if current_character not in second_dict:
            break

        operating = second_dict[current_character]

        temp_tape = ''
        for x in range(len(current_tape)):
            if x == position:
                temp_tape += operating[1]
            else:
                temp_tape += current_tape[x]

        if operating[2] == 'l':
            movement = -1
        else:
            movement = +1

        tape = (temp_tape, (position + movement))
        state = operating[0]

    return tape, state, accept

    # state is the key to the 1st dictionary, then you operate based on instructions inside 2nd dictionary

    # if debug, then print every step and take input() so that you see every step at a time

    # needs to execute 1 step of TM
    # this depends on state and the position of the head(second part of t)
    # state

    # tape[0][read/write] = symbol (assigned as a symbol)
    # basically find index of content where position of read/write head is at
    # before you do step below, check if state in dictionary
    # if not, then break
    # then check if symbol in dictionary[state]
    # if not, then break
    # dictionary[state][symbol] tells you what to do: this is a tuple

    # find way to change states and modify the tape
    # check for edge cases of if the direction cannot go further left or right
    # check for edge cases of write issues

    # tape has two parts: content (whole thing as a string) and read/write (head position)


def main():
    if sys.argv[1] == '-d':
        debug = True
        initial_tape_content = sys.argv[3]
        tm_dictionary = construct_tm_dictionary(sys.argv[2])
    else:
        file = sys.argv[1]
        debug = False
        initial_tape_content = sys.argv[2]
        tm_dictionary = construct_tm_dictionary(file)

    state = 1
    tape = (initial_tape_content, 0)
    print('Initial Tape:')

    if not debug:
        print_tape(tape, state)

    final_tape = run_TM(tm_dictionary, state, tape, debug)

    print('Final Tape:')

    state = final_tape[1]
    tape = final_tape[0]
    accept = final_tape[2]
    print_tape(tape, state)
    if accept:
        print('ACCEPT')
    else:
        print('REJECT')


main()
