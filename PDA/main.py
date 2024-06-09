import json
from PDA_validator import loadfile, valid as valid_pda

def run_pda(pda, input_string):
    current_state = pda['start_state']
    stack = pda['stack'][:]

    for symbol in input_string:
        transition_found = False
        for transition in pda['transitions']:
            (from_state, input_symbol, stack_symbol, to_state, stack_action) = transition
            if (current_state == from_state and
                (input_symbol == symbol or input_symbol == 'ε') and
                stack and stack[-1] == stack_symbol):
                current_state = to_state
                if stack_action == ['ε']:
                    stack.pop()
                else:
                    stack.pop()
                    stack.extend(reversed(stack_action))
                transition_found = True
                break
        
        if not transition_found:
            return False

    # Check for epsilon transitions after input is exhausted
    while True:
        epsilon_transition_found = False
        for transition in pda['transitions']:
            (from_state, input_symbol, stack_symbol, to_state, stack_action) = transition
            if (current_state == from_state and
                input_symbol == 'ε' and
                stack and stack[-1] == stack_symbol):
                current_state = to_state
                if stack_action == ['ε']:
                    stack.pop()
                else:
                    stack.pop()
                    stack.extend(reversed(stack_action))
                epsilon_transition_found = True
                break
        if not epsilon_transition_found:
            break

    if current_state in pda['accept_states']:
        return True
    return False

if __name__ == "__main__":
    # Load the configuration
    config = loadfile("config.json")
    
    # Validate the PDA configuration
    validation_result = valid_pda(config)
    
    if validation_result is True:
        print("PDA configuration is valid.")
        
        # Read the input string from the command line
        input_string = input("Enter the string to validate: ")
        
        # Validate the input string against the PDA
        if run_pda(config, input_string):
            print(f"The string '{input_string}' is valid according to the PDA.")
        else:
            print(f"The string '{input_string}' is NOT valid according to the PDA.")
    else:
        print(f"PDA configuration error: {validation_result}")
