import json
from NFA_validator import loadfile, valid
from concurrent.futures import ThreadPoolExecutor, as_completed

def epsilon_closure(state, data):
    closure = {state}
    stack = [state]
    while stack:
        current_state = stack.pop()
        for from_state, transition_elements, to_states in data['delta']:
            if from_state == current_state and '*' in transition_elements:
                for to_state in to_states:
                    if to_state not in closure:
                        closure.add(to_state)
                        stack.append(to_state)
    return closure

def run_nfa_step(current_states, element, data):
    next_states = set()
    for state in current_states:
        for from_state, transition_elements, to_states in data['delta']:
            if from_state == state and element in transition_elements:
                for to_state in to_states:
                    next_states.update(epsilon_closure(to_state, data))
    return next_states

def run_nfa(input_elements, data):
    print("Starting NFA...")
    current_states = epsilon_closure(data['start'], data)
    print(f"Initial states: {current_states}")

    for index, element in enumerate(input_elements, start=1):
        print(f"Step {index}: Processing element '{element}'...")
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(run_nfa_step, current_states, element, data)]
            current_states = set()
            for future in as_completed(futures):
                current_states.update(future.result())
        if not current_states:
            print(f"Error: No transition found from states {current_states} on '{element}'")
            return "Invalid string: transition not found for current states and element"
        print(f"Current states: {current_states}")

    # Final state check
    if any(state in data['final'] for state in current_states):
        print(f"Success: Ended in final states {current_states}")
        return "String is compatible"
    else:
        print(f"Failure: Ended in non-final states {current_states}")
        return "String is not compatible"

if __name__ == "__main__":
    # Load the NFA configuration
    config = loadfile("config.json")
    
    # Validate the NFA configuration
    validation_result = valid(config)
    
    if validation_result is True:
        print("NFA configuration is valid.")
        
        # Get input sequence from user
        input_sequence = input("Enter the input sequence (comma separated): ").split(',')
        
        # Run the NFA with the input sequence
        result = run_nfa(input_sequence, config)
        
        # Print the result
        print(f"Result: {result}")
    else:
        print(f"NFA configuration error: {validation_result}")
