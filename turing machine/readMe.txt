Turing machine simulated using Python program. Based on the contents of a "tape" or "memory", the read/write head reads the contents of a cell and can move left/right or replace the symbol in a cell. 

The instructions provided are the .tm files and contain five components:
1. From state
2. Read symbol
3. Write symbol
4. Move direction (L or R)
5. To state

Sample input: equal.tm abaab

Can do input like this: -d equal.tm abaab
	This will enter debug mode and show you step by step what the machine is doing
