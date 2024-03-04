# Turing Machine Simulator

This project simulates a Turing Machine using Python, allowing for the execution of specified Turing Machine (TM) algorithms on given inputs. The simulation reads a "tape" or "memory," processes the contents based on a set of instructions, and performs actions such as reading, writing, and moving the read/write head left or right.

## Features

- **Tape Manipulation:** Simulates the reading and writing operations of a Turing Machine on a tape.
- **Flexible Movement:** Allows the read/write head to move left or right, simulating the movement mechanism of a Turing Machine.
- **State Transitions:** Supports transitions between different states based on the current symbol under the read/write head and the instructions provided.
- **Debug Mode:** Offers a debug mode that displays each step of the Turing Machine's execution, helping users understand the process in detail.

## Instructions Format

The TM instruction files (`.tm`) contain instructions with five components:
1. **From State:** The current state of the Turing Machine.
2. **Read Symbol:** The symbol read by the machine at the current position on the tape.
3. **Write Symbol:** The symbol to be written to the current position on the tape.
4. **Move Direction:** The direction in which the read/write head should move next (`L` for left, `R` for right).
5. **To State:** The state to transition to after the current instruction is executed.

## Usage

To run the Turing Machine simulator, execute the `tm.py` script with the TM instruction file and the initial tape content as arguments. Additionally, you can enter debug mode to see the execution step by step.

### Examples

- **Standard Mode:** `python tm.py equal.tm abaab`
- **Debug Mode:** `python tm.py -d equal.tm abaab`

In debug mode, the program will pause after each step, allowing you to press Enter to continue to the next step. This mode provides a detailed view of the Turing Machine's operations.

## Sample Instruction Files

This project includes several `.tm` files demonstrating different Turing Machine algorithms:
- **anbnan.txt:** Accepts strings of `n` a's followed by `n` b's followed by `n` a's.
- **equal.tm:** Accepts strings with an equal number of a's and b's.
- **mul.tm:** For input in the form `sa*ma*e`, places `n1*n2` a's after `e`, where `n1` is the number of a's between `s` and `m` and `n2` is the number of a's between `m` and `e`.
