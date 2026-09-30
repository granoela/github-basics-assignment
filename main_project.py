#!/usr/bin/env python3
"""
Main Project File - GitHub Basics Assignment
Demonstrates core project functionality
"""

def greet(name):
    """Greet a user with a personalized message"""
    return f"Hello, {name}! Welcome to the GitHub Basics project."

def calculate_sum(a, b):
    """Calculate and return the sum of two numbers"""
    return a + b

def main():
    """Main function to demonstrate project functionality"""
    print(greet("Developer"))
    result = calculate_sum(10, 20)
    print(f"Sum of 10 and 20 is: {result}")

if __name__ == "__main__":
    main()
