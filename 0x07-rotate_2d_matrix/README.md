Rotate 2D Matrix
Description
This project implements an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. The rotation is done directly on the matrix without creating a copy, optimizing the space complexity. The solution is written in Python and involves matrix manipulation using nested loops to achieve the desired transformation.

Requirements
The solution must be written in Python 3.8.10.
The rotation must be performed in-place, meaning the original matrix is modified.
No external libraries or modules are allowed.
The matrix is guaranteed to be non-empty and 2-dimensional.
The implementation must comply with pycodestyle (version 2.8.0).
Prototype
python
Copy code
def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): 2D matrix to be rotated.
    """
How It Works
The algorithm is based on two main steps:

Transpose the matrix: This involves swapping elements such that rows become columns.
Reverse each row: After transposing, the rows are reversed to complete the 90-degree clockwise rotation.
Example
Given the matrix:

csharp
Copy code
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
After the rotation, the matrix becomes:

csharp
Copy code
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
Usage
To use the function, simply call rotate_2d_matrix(matrix) with an n x n matrix as the argument. Here's a sample usage:

python
Copy code
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
Sample Output:
lua
Copy code
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Files
0-rotate_2d_matrix.py: Contains the implementation of the rotate_2d_matrix function.
main_0.py: Sample script to test the rotation function.
Installation and Setup
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/alx-interview.git
Navigate to the project directory:
bash
Copy code
cd 0x07-rotate_2d_matrix
Ensure you have Python 3.8.10 installed:
bash
Copy code
python3 --version
Run the test script:
bash
Copy code
./main_0.py
Constraints
The matrix will always be a square matrix (n x n).
The matrix will always contain integers.
Author
Ima-obong Akinwumi Olabiyi
GitHub: Imaolabiyi


