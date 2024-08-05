[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15506683&assignment_repo_type=AssignmentRepo)
# Additional Basic String Exercises

Welcome to the additional basic string exercises assignment! This exercise will help you further practice working with strings in Python by implementing a few more functions. Follow the instructions below to complete the assignment.

## Instructions

1. **Fill in the Code:**
   - You will complete the functions provided in the `string2.py` file.
   - Each function has a description of what it should do. Your task is to write the code inside each function to achieve the described behavior.
   - The `main()` function is already set up to call these functions with various inputs and print `'OK'` when a function is correct.

2. **Function Descriptions:**
   - **Verbing:**
     - Given a string, if its length is at least 3, add 'ing' to its end. Unless it already ends in 'ing', in which case add 'ly' instead. If the string length is less than 3, leave it unchanged. Return the resulting string.
     - Example: `verbing('hail')` should return `'hailing'` and `verbing('swiming')` should return `'swimingly'`.
   - **Not_bad:**
     - Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'. Return the resulting string.
     - Example: `not_bad('This dinner is not that bad!')` should return `'This dinner is good!'`.
   - **Front_back:**
     - Consider dividing a string into two halves. If the length is even, the front and back halves are the same length. If the length is odd, the extra char goes in the front half.
     - Given 2 strings, `a` and `b`, return a string of the form `a-front + b-front + a-back + b-back`.
     - Example: `front_back('abcde', 'xyz')` should return `'abcxydez'`.

3. **Testing Your Code:**
   - The `main()` function includes test cases that will help you verify if your implementations are correct.
   - The `test()` function compares the output of your function with the expected result and prints `'OK'` if they match, otherwise it prints `'X'`.

## Submission

- Complete as many functions as you can.
- Ensure your code runs without errors.
- Submit your completed `string2.py` file by pushing your repo to GitHub and it will auto grade. 

Happy coding!
