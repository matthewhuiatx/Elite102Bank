from help import create_new_account_helper, create_new_user_helper, get_account_helper, deposit_into_account_helper

if __name__ == '__main__':
    banking_choice = input('What would you like to do?\n\n'
                           '1: Create an User\n'
                           '2: Create an Account\n'
                           '3: Check  Your Account Balance\n'
                           '4: Deposit Your Money\n')

    if banking_choice == '1':
        name = input('Name: ')
        email = input('Email: ')
        password = input('Password: ')

        create_new_user_helper(name, email, password)
    elif banking_choice == '2':
        user_email = input('What is your email? ')
        account_type = input('What type of account is this?')

        create_new_account_helper(user_email, account_type)
    elif banking_choice == '3':
        user_email = input('What is your email? ')
        account_type = input('Which account do you want to check?')

        account = get_account_helper(user_email, account_type)
        print(f"Your balance for account {account.type} is: {account.balance}")
    elif banking_choice == '4':
        user_email = input('What is your email? ')
        account_type = input('Which account do you want to deposit to?')
        deposit_amount = float(input('How much do you want to deposit?'))

        deposit_into_account_helper(user_email, account_type, deposit_amount)
