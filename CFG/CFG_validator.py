import json

def loadfile(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def valid(cfg):
    vars = cfg.get('variables', [])
    sigma = cfg.get('sigma', [])
    rules = cfg.get('rules', {})
    start = cfg.get('start', '')

    # Check for required keys
    if not vars or not sigma or not rules or not start:
        return "CFG error: missing components"

    # Validate the start symbol
    if start not in vars:
        return "CFG error: start symbol not in variables"

    # Validate that vars and sigma are disjoint sets
    if not set(vars).isdisjoint(set(sigma)):
        return "CFG error: variables and alphabet are not disjoint"

    # Validate production rules
    for lhs, rhs_list in rules.items():
        if lhs not in vars:
            return "CFG error: LHS of production rule not in variables"
        for rhs in rhs_list:
            for symbol in rhs:
                if symbol not in vars and symbol not in sigma:
                    return "CFG error: RHS of production rule contains unknown symbol"

    return True
