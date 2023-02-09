input = "ahhll@ahllh.cz"
reg_expression = "&&*@&&*.$$$*"


# input = "745"
# reg_exp = "###"


def parse(reg_exp):
    start_state = "q0"
    set_of_states = []
    transition = []
    final_state = []
    alphabet = []
    current_state = 0
    index = 0
    alpha_short = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # zkracena abeceda aby me to nevypisovalo tisic prechodovych funkci
    alpha_long = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(reg_exp)):
        tmp = []
        if reg_exp[i] == '|':
            current_state -= 1
            continue

        if reg_exp[i] == '#':  #pro cisla
            # print(index)
            for i in range(9):
                tmp = []
                tmp.append("q" + str(current_state))
                tmp.append(str(i))
                tmp.append("q" + str(current_state + 1))
                transition.append(tmp)
            index += 1
            current_state += 1
            continue
        elif reg_exp[i] == '&':  # cisla a znaky
            for i in range(len(alpha_short)):
                tmp = []
                tmp.append("q" + str(current_state))
                tmp.append(alpha_short[i])
                tmp.append("q" + str(current_state + 1))
                transition.append(tmp)
                # print(tmp)
            index += 1
            current_state += 1
            continue
        elif reg_exp[i] == "$":
            for i in range(len(alpha_long)):
                tmp = []
                tmp.append("q" + str(current_state))
                tmp.append(alpha_long[i])
                tmp.append("q" + str(current_state + 1))
                transition.append(tmp)
            current_state += 1
            index += 1
            continue
        elif reg_exp[i] == "*":
            if reg_exp[i - 1] == "&":
                for c in range(len(alpha_short)):
                    last = transition[-c - 1]
                    last[2] = last[0]
                current_state -= 1
            if reg_exp[i - 1] == "$":
                for c in range(len(alpha_short)):
                    last = transition[-c - 1]
                    last[2] = last[0]
                current_state -= 1
            last = transition[-1]
            last[2] = last[0]
            current_state -= 1
            continue

        tmp = []
        if "$" in reg_exp and "&" in reg_exp:
            current_state += 1

        tmp.append("q" + str(current_state))
        tmp.append((reg_exp[i]))
        tmp.append("q" + str(current_state + 1))
        transition.append(tmp)
        current_state += 1
        index += 1
    # final state
    final_state.append(transition[-1][2])

    # alphabet
    if "&" in reg_exp and "$" in reg_exp and "#" in reg_exp:
        alphabet.append(alpha_long)
    elif "$" in reg_exp:
        alphabet.append(alpha_long)
    elif "&" in reg_exp:
        alphabet.append(alpha_short)
    elif "#" in reg_exp:
        alphabet.append("0123456789")

    for char in reg_exp:
        if char.isalpha() and "&" not in reg_exp and "$" not in reg_exp:
            alphabet.append(char)
        if char.isalpha() == False and char != "$" and char != "&" and char != "*":
            alphabet.append(char)

    string_alphabet = "".join(["".join(row) for row in alphabet])
    # print(string_alphabet)

    # setOfStates

    for i in range(len(transition)):
        set_of_states.append(transition[i][2])

    set_of_states = set(set_of_states)

    return transition, final_state, string_alphabet, start_state, set_of_states


#####################################################

result_of_parse = parse(reg_expression)

transition = result_of_parse[0]
print("Přechodové funkce: ", transition)
final_state = result_of_parse[1]
print("Konečný stav: ", final_state)
alphabet = result_of_parse[2]
print("Abeceda: ", alphabet)
start_state = result_of_parse[3]
print("Počáteční stav: ", start_state)
set_of_states = result_of_parse[4]
print("Stavy automatu: ", set_of_states)


######################################################################


def final_automata(input, start_state, transition_state, final_state, alpha, set_of_states):
    state_count = len(transition_state)

    switch = ""  ## PRO UCELY TESTOVANI &* a $* a z duvodu neosetreni abecedy ( to uz je asi jednodussi ) zakomentovano
    for char in input:
        if char in alpha:
            switch = "1"
        else:
            switch = "0"
            break
    if switch == "1":  # start_state in set_of_states and
        state = start_state
        for char in input:
            for i in range(0, state_count):
                if state == transition_state[i][0]:
                    # print(prechodove_stavy[i])
                    if char == transition_state[i][1]:
                        # print(prechodove_stavy[i])
                        state = transition_state[i][2]
                        break
            else:

                return False
        # print(state)
        if state in final_state:
            return True
        else:
            return False
    else:
        return False


print(final_automata(input, start_state, transition, final_state, alphabet, set_of_states))


"""
Věřím, že regulární výrazy jsou nesmírně důležité. Například se používají
k filtraci vstupů od uživatele. Všeobecně se totiž věří, že na uživatele
nemůže být spoleh. Proto je důležitá kontrola a sanitace vstupů.

But - “I haven’t cried this hard since Toy Story 3.” — Raj, Big Bang Theory...
"""