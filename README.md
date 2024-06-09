# LFA CS112 Theory of Computation Homework

This repository contains homework assignments for CS112 Theory of Computation. Each subfolder represents a different computational model, with code to simulate and validate configurations described in JSON format.

---

## PDA (Pushdown Automaton)
### Instructions
1. Place your PDA configuration in `config.json`.
2. Run the main program using `python main.py`.

### JSON Configuration
- **states**: List of states.
- **input_alphabet**: List of input symbols.
- **stack_alphabet**: List of stack symbols.
- **transitions**: List of transition rules `[current_state, input, stack_top, new_state, stack_operation]`.
- **start_state**: Initial state.
- **accept_states**: List of accept states.
- **stack**: Initial stack configuration.

### CLI Examples
- Correct: `()`
- Incorrect: `(()`

## NFA (Nondeterministic Finite Automaton)
### Instructions
1. Place your NFA configuration in `config.json`.
2. Run the main program using `python main.py`.

### JSON Configuration
- **sigma**: List of input symbols.
- **states**: List of states.
- **start**: Initial state.
- **final**: List of final states.
- **delta**: Transition function as `[current_state, input, [new_states]]`.

### CLI Examples
- Correct: `1,0,0`
- Incorrect: `1,1,1,0,1`

## DFA (Deterministic Finite Automaton)
### Instructions
1. Place your DFA configuration in `config.json`.
2. Run the main program using `python main.py`.

### JSON Configuration
- **sigma**: List of input symbols.
- **states**: List of states.
- **start**: Initial state.
- **final**: List of final states.
- **delta**: Transition function as `[current_state, input, new_state]`.

### CLI Examples
- Correct: `1,0,1,0`
- Incorrect: `1,1,0,0,0`

## CFG (Context-Free Grammar)
### Instructions
1. Place your CFG configuration in `config.json`.
2. Run the main program using `python main.py`.

### JSON Configuration
- **sigma**: List of terminal symbols.
- **variables**: List of non-terminal symbols.
- **start**: Start symbol.
- **rules**: Production rules as `{variable: [[production]]}`.

### CLI Examples
- Correct: `aabb`
- Incorrect: `ababa`
