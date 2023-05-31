# ATM_2.0
This code appears to be an implementation of an ATM (Automated Teller Machine) simulation for the Bank of India. It seems to import a module named `atmTool` that likely contains various functions related to ATM operations.

The code runs a loop that iterates 100 times, simulating 100 different interactions with the ATM. Each iteration begins with a welcome message and prompts the user to enter their PIN (Personal Identification Number). The code then calls the `check_pin` function from the `atmTool` module to verify the entered PIN.

If the entered PIN matches the one returned by the `check_pin` function, the code proceeds to display the user's account details using the `detail` function from `atmTool`. It then enters an inner loop that allows the user to perform multiple transactions within the same session.

The user is presented with a menu of transaction options, including withdrawal, balance inquiry, fast cash, and credit amount. Based on the user's input, the code performs the corresponding operation using functions from the `atmTool` module.

For withdrawals, the code checks if the withdrawal amount is valid (either equal to or less than the available balance) and if it is a multiple of 100. If the conditions are met, it updates the account balance using the `update_bal` function, prints a success message, and prompts the user to collect cash and their debit card. If the withdrawal amount is not valid, an appropriate error message is displayed.

For balance inquiry, the code retrieves the current balance using the `balance` function from `atmTool` and displays it to the user.

The "fast cash" option allows the user to choose predefined amounts (1-1000, 2-500, 3-2000, 4-5000) for withdrawal. The code checks if the chosen amount is less than the available balance and updates the balance accordingly. If the chosen amount is not valid, an error message is displayed.

The "credit amount" option allows the user to add funds to their account. The code prompts the user to enter the amount, updates the balance using the `update_bal` function, and displays the credited amount and the new available balance.

After each transaction, the code gives the option to continue or exit the session. If the user chooses to exit, the inner loop breaks, and the program goes back to the outer loop to simulate another interaction.

If the entered PIN does not match the one returned by the `check_pin` function, an error message is displayed, indicating an incorrect PIN.

Once the outer loop completes 100 iterations, a message is displayed indicating that today's transactions are over.

Overall, this code simulates an ATM interface, allowing users to perform various banking transactions such as withdrawals, balance inquiries, and fund credits.
