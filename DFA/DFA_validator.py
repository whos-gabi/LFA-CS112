import json

def loadfile(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def valid(data):
    # Check the length of the components
    if len(data['sigma']) <= 1 or len(data['states']) <= 1 or len(data['final']) <= 1 or len(data['delta']) <= 1:
        return "Data length error"

    # Validate the start state
    if data['start'] not in data['states']:
        return "Start not in state's error"

    # Validate final states
    for e in data['final']:
        if e not in data['states']:
            return "Final state error"

    # Validate delta transitions
    for e in data['delta']:
        if e[0] not in data['states'] or e[2] not in data['states']:
            return "Delta error"
        for s in e[1]:
            if s not in data['sigma']:
                return "Sigma in delta error"

    return True
