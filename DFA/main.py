import json
from DFA_validator import loadfile, valid

def run_dfa(input_elements, data):
    print("Starting DFA...")
    current_state = data['start']
    print(f"Initial state: {current_state}")

    for index, element in enumerate(input_elements, start=1):
        print(f"Step {index}: Processing element '{element}'...")
        transition_found = False
        
        # Search for a valid transition for the current element
        for from_state, transition_elements, to_state in data['delta']:
            if from_state == current_state and element in transition_elements:
                current_state = to_state
                print(f"Transitioned to {current_state}")
                transition_found = True
                break  # Found a valid transition, no need to continue checking
        
        if not transition_found:
            print(f"Error: No transition found from {current_state} on '{element}'")
            return "Invalid string: transition not found for current state and element"

    # Final state check
    if current_state in data['final']:
        print(f"Success: Ended in final state {current_state}")
        return "String is compatible"
    else:
        print(f"Failure: Ended in non-final state {current_state}")
        return "String is not compatible"

if __name__ == "__main__":
    # Load the DFA configuration
    config = loadfile("./config.json")
    
    # Validate the DFA configuration
    validation_result = valid(config)
    
    if validation_result is True:
        print("DFA configuration is valid.")
        
        # Get input sequence from user
        input_sequence = input("Enter the input sequence (comma separated): ").split(',')
        
        # Run the DFA with the input sequence
        result = run_dfa(input_sequence, config)
        
        # Print the result
        print(f"Result: {result}")
    else:
        print(f"DFA configuration error: {validation_result}")
