import json

def loadfile(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def valid(data):
    # Check the length of the components
    if len(data['sigma']) <= 0 or len(data['states']) <= 1 or len(data['final']) <= 1 or len(data['delta']) <= 1:
        return "Data length error"

    # Validate the start state
    if data['start'] not in data['states']:
        return "Start state error"

    # Add '*' to sigma if it's not already present
    if '*' not in data['sigma']:
        data['sigma'].append('*')

    # Validate final states
    for e in data['final']:
        if e not in data['states']:
            return "Final state error"

    # Validate delta transitions
    for e in data['delta']:
        if e[0] not in data['states'] or not all(state in data['states'] for state in e[2]):
            return "Delta error"
        for s in e[1]:
            if s not in data['sigma']:
                return "Sigma in delta error"

    return True
