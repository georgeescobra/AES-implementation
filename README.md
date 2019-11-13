For option 2, upload your code and project report (Which algorithm/protocol, how does your code work, your project input, your project output.)

## Notes on AES (block cipher)
    - using 128 bit keys
    - Encription consists of 10 rounds
    - Processing:
        - single-byte based substition
        - row-wise permutation
        - column-wise mixing
        - addition of round key
        - (order of these steps are executed depending if enc or decry)
    - Need to have a state array => statearray = [[0 for x in range(4)] for x in range(4)]
    - Each round of processing works on the input state array and produces output state array
        - output state array produced by the lasr round is rearranged into 128-bit output block
    - AES uses a substitution permutation network



## [link to AES  pdf] (https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture8.pdf)
