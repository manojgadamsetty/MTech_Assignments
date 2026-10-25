"""
Mathematical Foundations for Data Science - Assignment 1
Name: [Your Name]
ID: [Your ID]
Date: 27 February 2026

This script solves all 5 problems from Assignment 1 using Python.
Each problem includes detailed steps and intermediate solutions.
"""

import numpy as np
import sys

# Set print options for better readability
np.set_printoptions(precision=4, suppress=True, linewidth=100)

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*80)
    print(f" {title}")
    print("="*80 + "\n")

def print_matrix(matrix, label="Matrix"):
    """Print a matrix with label"""
    print(f"{label}:")
    print(matrix)
    print()


# ============================================================================
# PROBLEM 1: Find the Reduced Row-Echelon Form (RREF)
# ============================================================================
def problem_1():
    print_section("PROBLEM 1: Reduced Row-Echelon Form (RREF)")
    
    # Define the matrix
    A = np.array([
        [0, 1, 3, -1, 2, 1],
        [0, -2, -5, 3, 0, 2],
        [0, 0, 0, 1, -1, 7],
        [0, 2, 6, -2, 2, 0],
        [0, 3, 9, -2, 4, 7]
    ], dtype=float)
    
    print_matrix(A, "Original Matrix A")
    
    # Manual RREF implementation to show steps
    def rref(matrix):
        """Compute RREF with step-by-step display"""
        M = matrix.copy()
        rows, cols = M.shape
        current_row = 0
        
        print("Step-by-step RREF computation:\n")
        
        for col in range(cols):
            # Find pivot
            pivot_row = None
            for row in range(current_row, rows):
                if abs(M[row, col]) > 1e-10:
                    pivot_row = row
                    break
            
            if pivot_row is None:
                continue
            
            # Swap rows if needed
            if pivot_row != current_row:
                M[[current_row, pivot_row]] = M[[pivot_row, current_row]]
                print(f"Step: Swap row {current_row} with row {pivot_row}")
                print(M)
                print()
            
            # Scale pivot to 1
            pivot_val = M[current_row, col]
            if abs(pivot_val) > 1e-10:
                M[current_row] = M[current_row] / pivot_val
                print(f"Step: Scale row {current_row} by 1/{pivot_val:.4f}")
                print(M)
                print()
            
            # Eliminate column entries above and below pivot
            for row in range(rows):
                if row != current_row and abs(M[row, col]) > 1e-10:
                    factor = M[row, col]
                    M[row] = M[row] - factor * M[current_row]
                    print(f"Step: R{row} = R{row} - ({factor:.4f}) * R{current_row}")
            
            if any(abs(M[row, col]) > 1e-10 for row in range(rows) if row != current_row):
                print(M)
                print()
            
            current_row += 1
            if current_row >= rows:
                break
        
        # Clean up near-zero values
        M[np.abs(M) < 1e-10] = 0
        return M
    
    rref_matrix = rref(A)
    
    print_matrix(rref_matrix, "Final RREF")
    
    return rref_matrix


# ============================================================================
# PROBLEM 2: Matrix Inverse using Gauss Elimination
# ============================================================================
def problem_2():
    print_section("PROBLEM 2: Matrix Inverse using Gauss Elimination")
    
    # Define the matrix
    A = np.array([
        [0, 1, -1, 1],
        [2, 2, 0, -2],
        [1, 1, -2, 0],
        [0, 1, 2, 0]
    ], dtype=float)
    
    print_matrix(A, "Original Matrix A")
    
    # Check if matrix is invertible
    det = np.linalg.det(A)
    print(f"Determinant of A: {det:.4f}")
    
    if abs(det) < 1e-10:
        print("Matrix is singular (not invertible)!")
        return None
    
    print("Matrix is invertible.\n")
    
    # Gauss-Jordan elimination for inverse
    def gauss_jordan_inverse(matrix):
        """Compute inverse using Gauss-Jordan elimination"""
        n = matrix.shape[0]
        # Create augmented matrix [A | I]
        augmented = np.hstack([matrix.copy(), np.eye(n)])
        
        print("Augmented matrix [A | I]:")
        print(augmented)
        print()
        
        # Forward elimination with partial pivoting
        for col in range(n):
            # Find pivot
            pivot_row = col + np.argmax(np.abs(augmented[col:, col]))
            
            # Swap rows
            if pivot_row != col:
                augmented[[col, pivot_row]] = augmented[[pivot_row, col]]
                print(f"Step: Swap row {col} with row {pivot_row}")
                print(augmented)
                print()
            
            # Scale pivot row
            pivot_val = augmented[col, col]
            augmented[col] = augmented[col] / pivot_val
            print(f"Step: Scale row {col} by 1/{pivot_val:.4f}")
            print(augmented)
            print()
            
            # Eliminate column
            for row in range(n):
                if row != col:
                    factor = augmented[row, col]
                    augmented[row] = augmented[row] - factor * augmented[col]
            
            print(f"Step: Eliminate column {col}")
            print(augmented)
            print()
        
        # Extract inverse from augmented matrix
        inverse = augmented[:, n:]
        inverse[np.abs(inverse) < 1e-10] = 0
        
        return inverse
    
    A_inv = gauss_jordan_inverse(A)
    
    print_matrix(A_inv, "Inverse of A")
    
    # Verify: A * A_inv should be I
    verification = A @ A_inv
    verification[np.abs(verification) < 1e-10] = 0
    print_matrix(verification, "Verification: A * A^(-1) (should be Identity)")
    
    return A_inv


# ============================================================================
# PROBLEM 3: Check if vectors form a basis for R^3
# ============================================================================
def problem_3():
    print_section("PROBLEM 3: Check if vectors form a basis for R^3")
    
    # Define the vectors
    v1 = np.array([0, 3, 1])
    v2 = np.array([1, 0, 1])
    v3 = np.array([-3, 0, 5])
    
    print("Given vectors:")
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v3 = {v3}")
    print()
    
    # Create matrix with vectors as columns
    V = np.column_stack([v1, v2, v3])
    print_matrix(V, "Matrix V with vectors as columns")
    
    # Check 1: Number of vectors must equal dimension
    num_vectors = 3
    dimension = 3
    print(f"Number of vectors: {num_vectors}")
    print(f"Dimension of R^3: {dimension}")
    print(f"Condition 1 (count): {'PASS' if num_vectors == dimension else 'FAIL'}\n")
    
    # Check 2: Vectors must be linearly independent (det ≠ 0)
    det = np.linalg.det(V)
    print(f"Determinant of V: {det:.4f}")
    is_independent = abs(det) > 1e-10
    print(f"Condition 2 (linear independence): {'PASS' if is_independent else 'FAIL'}\n")
    
    # Check 3: Rank must equal 3
    rank = np.linalg.matrix_rank(V)
    print(f"Rank of V: {rank}")
    print(f"Condition 3 (rank): {'PASS' if rank == 3 else 'FAIL'}\n")
    
    # Final conclusion
    is_basis = (num_vectors == dimension) and is_independent and (rank == dimension)
    
    print("="*50)
    if is_basis:
        print("CONCLUSION: YES, the vectors form a basis for R^3")
    else:
        print("CONCLUSION: NO, the vectors do NOT form a basis for R^3")
    print("="*50)
    
    return is_basis


# ============================================================================
# PROBLEM 4: Find the rank of a matrix
# ============================================================================
def problem_4():
    print_section("PROBLEM 4: Find the Rank of Matrix A")
    
    # Define the matrix
    A = np.array([
        [1, 2, 0, 1, 1],
        [2, 4, 1, 3, 0],
        [3, 5, 2, 4, 1],
        [-4, -3, 1, -2, 1]
    ], dtype=float)
    
    print_matrix(A, "Original Matrix A")
    
    # Method 1: Using numpy
    rank_numpy = np.linalg.matrix_rank(A)
    print(f"Rank (using numpy): {rank_numpy}\n")
    
    # Method 2: Row echelon form to count pivots
    def compute_rank_via_ref(matrix):
        """Compute rank by counting pivots in REF"""
        M = matrix.copy()
        rows, cols = M.shape
        current_row = 0
        pivot_count = 0
        
        print("Computing row echelon form:\n")
        
        for col in range(cols):
            # Find pivot
            pivot_row = None
            for row in range(current_row, rows):
                if abs(M[row, col]) > 1e-10:
                    pivot_row = row
                    break
            
            if pivot_row is None:
                continue
            
            pivot_count += 1
            
            # Swap rows
            if pivot_row != current_row:
                M[[current_row, pivot_row]] = M[[pivot_row, current_row]]
            
            # Scale pivot
            M[current_row] = M[current_row] / M[current_row, col]
            
            # Eliminate below
            for row in range(current_row + 1, rows):
                if abs(M[row, col]) > 1e-10:
                    M[row] = M[row] - M[row, col] * M[current_row]
            
            current_row += 1
            if current_row >= rows:
                break
        
        M[np.abs(M) < 1e-10] = 0
        print("Row Echelon Form:")
        print(M)
        print()
        
        return pivot_count, M
    
    rank_ref, ref_matrix = compute_rank_via_ref(A)
    print(f"Rank (counting pivots in REF): {rank_ref}\n")
    
    # SVD analysis
    U, s, Vt = np.linalg.svd(A)
    print("Singular values:", s)
    rank_svd = np.sum(s > 1e-10)
    print(f"Rank (from SVD - non-zero singular values): {rank_svd}\n")
    
    print("="*50)
    print(f"FINAL ANSWER: Rank of A = {rank_numpy}")
    print("="*50)
    
    return rank_numpy


# ============================================================================
# PROBLEM 5: Singular Value Decomposition (SVD)
# ============================================================================
def problem_5():
    print_section("PROBLEM 5: Singular Value Decomposition (SVD)")
    
    # Define the matrix
    A = np.array([
        [3, 1, 1, 0],
        [1, 2, -2, -1]
    ], dtype=float)
    
    print_matrix(A, "Original Matrix A")
    print(f"Matrix shape: {A.shape[0]} × {A.shape[1]}\n")
    
    # Compute SVD: A = U * Σ * V^T
    U, s, Vt = np.linalg.svd(A, full_matrices=True)
    
    # Create full Sigma matrix
    Sigma = np.zeros(A.shape)
    Sigma[:len(s), :len(s)] = np.diag(s)
    
    print_matrix(U, "U matrix (left singular vectors)")
    print(f"U shape: {U.shape}")
    print(f"U is orthogonal: {np.allclose(U @ U.T, np.eye(U.shape[0]))}\n")
    
    print_matrix(Sigma, "Σ matrix (singular values)")
    print(f"Singular values: {s}\n")
    
    print_matrix(Vt, "V^T matrix (right singular vectors transposed)")
    print(f"V^T shape: {Vt.shape}")
    print(f"V is orthogonal: {np.allclose(Vt @ Vt.T, np.eye(Vt.shape[0]))}\n")
    
    # Verification: Reconstruct A from SVD
    A_reconstructed = U @ Sigma @ Vt
    A_reconstructed[np.abs(A_reconstructed) < 1e-10] = 0
    
    print_matrix(A_reconstructed, "Reconstructed A (U * Σ * V^T)")
    
    # Check if reconstruction matches original
    reconstruction_error = np.linalg.norm(A - A_reconstructed)
    print(f"Reconstruction error: {reconstruction_error:.10f}")
    print(f"Reconstruction successful: {reconstruction_error < 1e-10}\n")
    
    # Additional analysis
    print("Additional SVD Analysis:")
    print(f"Rank of A: {np.sum(s > 1e-10)}")
    print(f"Condition number: {s[0] / s[-1]:.4f}")
    print(f"Frobenius norm: {np.linalg.norm(A, 'fro'):.4f}")
    
    return U, s, Vt


# ============================================================================
# MAIN EXECUTION
# ============================================================================
if __name__ == "__main__":
    print("\n" + "█"*80)
    print(" "*15 + "MATHEMATICAL FOUNDATIONS FOR DATA SCIENCE")
    print(" "*30 + "ASSIGNMENT 1 SOLUTIONS")
    print("█"*80)
    print("\nName: [Your Name]")
    print("ID: [Your ID]")
    print("Date: 27 February 2026")
    print("Due Date: 7 March 2026")
    
    try:
        # Solve all problems
        result_1 = problem_1()
        result_2 = problem_2()
        result_3 = problem_3()
        result_4 = problem_4()
        result_5 = problem_5()
        
        # Summary
        print_section("SUMMARY OF SOLUTIONS")
        print("Problem 1: RREF computed successfully")
        print("Problem 2: Matrix inverse computed successfully")
        print(f"Problem 3: Vectors {'DO' if result_3 else 'DO NOT'} form a basis for R^3")
        print(f"Problem 4: Rank of matrix = {result_4}")
        print("Problem 5: SVD computed successfully")
        
        print("\n" + "█"*80)
        print(" "*25 + "ALL PROBLEMS COMPLETED")
        print("█"*80 + "\n")
        
    except Exception as e:
        print(f"\nError occurred: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
