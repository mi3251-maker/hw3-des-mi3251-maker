# HW3: DES

**Deadline:** 12:00 PM, Friday, 2/6/2026

---

## Files and Tasks

### 1. `DES_Simulation.py`
- Main simulation engine  
- **Status:** Completed

### 2. `Conversion.py`
- Provides utility functions for conversion between a string of characters and a binary string  
- **Status:** Completed

### 3. `DES.py`
- Includes encryption and decryption algorithms  
- **Task:** Complete `decrypt()`

### 4. `IP.py`
- Initial permutation  
- **Task:** Complete `permute()`

### 5. `Rounds.py`
- Implements the 16 rounds of DES  
- **Task:** Complete all methods declared in the module

### 6. `IP_inverse.py`
- Final permutation  
- **Task:** Complete `permute()`

### 7. `Key_schedule.py`
- Includes key scheduling algorithms for both encryption and decryption  
- **Task:** Complete `pc_1()`, `pc_2()`, and `generate_subkey_encryption()`

---

## Running the Program

To run the `DES_Simulation` class, type:

```bash
python DES_Simulation.py plaintext.txt key.txt
```

Once you complete the implementation, **uncomment the `assert` statements** in the `main` function.

### Expected Output

```
ciphertext: 1101001111100010001000011001111011010111100110110111111000000111
recovered Text: Hi World
```

---

## Input Files

- `plaintext.txt`
  - Contains **8 characters**
- `key.txt`
  - Contains a **64-bit key**
- You may test with different plaintexts and keys.

---

## Submission

Submit your solutions to your **GitHub repository** before the deadline.
