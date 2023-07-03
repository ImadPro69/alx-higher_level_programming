#!/usr/bin/python3
"""Module to multiply two matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function to multiply two matrices using NumPy
    Args:
        m_a: First matrix (list of lists of integers or floats)
        m_b: Second matrix (list of lists of integers or floats)
    Returns:
        The resulting matrix (list of lists of integers or floats)
    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists
                  If m_a or m_b contains elements that are not integers or floats
                  If m_a or m_b is not a rectangle (rows have different sizes)
        ValueError: If m_a or m_b is empty
                    If m_a and m_b cannot be multiplied
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")
    if len(m_a) == 0 or len(m_b) == 0 or any(len(row) == 0 for row in m_a) or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a can't be empty and m_b can't be empty")
    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size and each row of m_b must be of the same size")

    m_a_np = np.array(m_a)
    m_b_np = np.array(m_b)

    if len(m_a_np[0]) != len(m_b_np):
        raise ValueError("m_a and m_b can't be multiplied")

    result_np = np.dot(m_a_np, m_b_np)

    result = result_np.tolist()

    return result

