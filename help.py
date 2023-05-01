import random

from database import get_user_by_email, create_user_account, add_user, get_user_account, update_account_balance
from model import Account, User

def create_new_user_helper(user_name, user_email, user_password):
    # create a new User model
    new_user = User(None, user_name, user_email, user_password)

    # persist new user in the database
    add_user(new_user)

    print(f"Created new user: {new_user}")


def create_new_account_helper(user_email, account_type):
    # get user from the database by calling db.get_user_by_email
    user = get_user_by_email(user_email)

    # create randomized account and routing numbers
    new_account_number = str(random.randint(100000000, 999999999))
    new_routing_number = str(random.randint(100000000, 999999999))

    # create a new Account model representing the user's new account
    new_account = Account(None, new_account_number, new_routing_number, 0, user.id, account_type)

    create_user_account(user, new_account)

    print(f"Created new account: {new_account}")


def get_account_helper(user_email, account_type) -> Account:

    # get user from the database by calling db.get_user_by_email
    user = get_user_by_email(user_email)

    # get account from database for the given user and account type
    return get_user_account(user, account_type)


def deposit_into_account_helper(user_email, account_type, deposit_amount):

    # get account from database for the given user and account type
    account = get_account_helper(user_email, account_type)

    # update account balance
    new_balance = account.balance + deposit_amount

    # update account in database
    update_account_balance(account.id, new_balance)

    print(f"Deposited ${deposit_amount} into account {account.account_number}")