import json

def loadfile(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def valid(pda):
    states = pda.get('states', [])
    input_alphabet = pda.get('input_alphabet', [])
    stack_alphabet = pda.get('stack_alphabet', [])
    transitions = pda.get('transitions', [])
    start_state = pda.get('start_state', '')
    accept_states = pda.get('accept_states', [])
    stack = pda.get('stack', '')

    # Check for required keys
    if not states or not input_alphabet or not stack_alphabet or not transitions or not start_state or not accept_states or not stack:
        return "PDA error: missing components"

    # Validate the start state
    if start_state not in states:
        return "PDA error: start state not in states"

    # Validate that accept states are in states
    if not set(accept_states).issubset(set(states)):
        return "PDA error: accept states not a subset of states"

    # Validate transitions
    for transition in transitions:
        if len(transition) != 5:
            return "PDA error: each transition must have 5 elements"
        current_state, input_symbol, stack_symbol, next_state, stack_action = transition
        if current_state not in states or next_state not in states:
            return "PDA error: transition states must be in states"
        if input_symbol not in input_alphabet + ['ε']:
            return "PDA error: input symbol must be in input alphabet or ε"
        if stack_symbol not in stack_alphabet:
            return "PDA error: stack symbol must be in stack alphabet"
        for action in stack_action:
            if action not in stack_alphabet + ['ε']:
                return "PDA error: stack action symbols must be in stack alphabet or ε"

    return True
