# ATM Withdrawal Validation
# Create a simple ATM withdrawal program.
# Ask the user for:
#  Account balance
#  Withdrawal amount
#  PIN
# The transaction should be successful only when:
#  PIN is correct
#  Withdrawal amount is greater than 0
#  Withdrawal amount is less than or equal to the balance
# Use and to combine the conditions.
# If the withdrawal is successful, calculate and display the remaining balance.
# Handle different cases such as:
#  Invalid PIN
#  Invalid withdrawal amount
#  Insufficient balance
#  Withdrawal successful


# ATM Withdrawal Validation
account_balance = float(input("Enter account balance: Rs. "))
withdrawal_amount = float(input("Enter withdrawal amount: Rs. "))
pin = input("Enter PIN: ")

correct_pin = "1234"

if pin == correct_pin and withdrawal_amount > 0 and withdrawal_amount <= account_balance:
	remaining_balance = account_balance - withdrawal_amount
	print(f"Withdrawal successful. Remaining balance: Rs. {remaining_balance:.2f}")
elif pin != correct_pin:
	print("Invalid PIN.")
elif withdrawal_amount <= 0:
	print("Invalid withdrawal amount. Enter an amount greater than 0.")
else:
	print("Insufficient balance.")
