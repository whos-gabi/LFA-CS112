import json
from CFG_validator import loadfile, valid as valid_cfg

def validate_string(cfg, string):
    def match(symbols, string):
        if not symbols and not string:
            return True
        if not symbols or not string:
            return False
        symbol = symbols[0]
        if symbol in cfg['sigma']:
            if string[0] == symbol:
                return match(symbols[1:], string[1:])
            else:
                return False
        if symbol in cfg['variables']:
            for rule in cfg['rules'][symbol]:
                if match(rule + symbols[1:], string):
                    return True
        return False

    start_symbol = cfg['start']
    return match([start_symbol], string)

if __name__ == "__main__":
    import sys
    
    # Load the configuration
    config = loadfile("config.json")
    
    # Validate the CFG configuration
    validation_result = valid_cfg(config)
    
    if validation_result is True:
        print("CFG configuration is valid.")
        
        # Read the input string from the command line
        input_string = input("Enter the string to validate: ")
        
        # Validate the input string against the CFG
        if validate_string(config, input_string):
            print(f"The string '{input_string}' is valid according to the CFG.")
        else:
            print(f"The string '{input_string}' is NOT valid according to the CFG.")
    else:
        print(f"CFG configuration error: {validation_result}")
