"""
Author: Paul Sommers
Date written: 11/20/2024
Assignment: Module 05 Programming Assignment 1
Short Desc: This program prompts the user for total sales for the month, and then calculates the county, state, and total sales tax.
"""

# Function to calculate and display sales tax
def calculateTax():
    
    # Input: Ask the user to enter the total sales for the month
    totalSales = float(input("Enter the total sales for the month: "))

    # Calculate the county and state sales tax
    countyTax = totalSales * 0.025  # 2.5% county tax
    stateTax = totalSales * 0.05  # 5% state tax

    # Calculate the total sales tax
    totalTax = countyTax + stateTax

    # Display the county, state, and total sales tax
    print(f"The county sales tax is: ${countyTax:.2f}")
    print(f"The state sales tax is: ${stateTax:.2f}")
    print(f"The total sales tax is: ${totalTax:.2f}")

# Call the function
calculateTax()