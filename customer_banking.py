# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Please enter the starting balance of the savings account: $"))
    savings_interest = float(input("Please enter the interest rate for the savings account: "))
    savings_maturity = int(input("Please enter the number of months: "))
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    # Print out the interest earned and updated saving account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The starting balance is: ${savings_balance}")
    print(f"The interest earned over {savings_maturity} months is: ${interest_earned}")
    print(f"The updated account balance is: ${updated_savings_balance}")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Please enter the balance of the CD account: $"))
    cd_interest = float(input("Please enter the interest rate of the account: "))
    cd_maturity = int(input("Please enter the number of months: "))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your starting balance is: ${cd_balance}")
    print(f"The interest earned over {cd_maturity} months is: ${interest_earned}") 
    print(f"The updated balance is: ${updated_cd_balance}")
if __name__ == "__main__":
    # Call the main function.
    main()