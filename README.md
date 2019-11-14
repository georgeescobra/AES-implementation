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
    - last round of encryption does not involve mix columns step
    - last round of decryption does not involve inverse mix columns step
    - algorithm is guaranteed to change every bit of the ciphertext
 
#### Substitution Bytes
    - subBytes
    - Byte for byte substitution
    - decryption process := inverseSubBytes
    - uses a rule that stays the same in all encryption rounds
    - different in decryption chain
    - x' = xin^-1 in GF(2^8) // xin => input bit
    - special constany byte c =0x63
    - xout = A(x') + c      // xout => output bit
    

#### Shift Rows
    - shifting the rows of the state array
    - decryption process := inverseShiftRows


### Mix Columns
    - decryption process := inverseMixColumns
    - mixes up the bytes in each column separately
   
### Add Round Key
    - adding the round key to the output
    - decryption process := inverseAddRoundKey
    



    - [AES overview pdf](https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture8.pdf)
    - [AES implementation](https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf)


