import mysql.connector as mysql

from model import User, Account

# setup connection to database
db = mysql.connect(user='root', \
                   database='banking', \
                    password='matthew123')

def add_user(user: User):
    # create cursor
    cursor = db.cursor()

    # execute query
    query = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
    query_parameters = [user.name, user.email, user.password]
    cursor.execute(query, \
                   query_parameters)

    # commit changes
    db.commit()

    # close cursor
    cursor.close()


def get_user_by_email(email: str) -> User:
    # create cursor
    cursor = db.cursor()

    # execute query
    query = "SELECT * FROM user WHERE email = %s"
    cursor.execute(query, [email])

    # get results
    result = cursor.fetchone()

    # close cursor
    cursor.close()

    # return result
    return User(result[0], result[1], result[2], result[3])

def create_user_account(user: User, new_account: Account):
    # insert the new account into our database
    cursor = db.cursor()

    # execute query
    query = "INSERT INTO account (account_number, routing_number, balance, user_id, type) VALUES (%s, %s, %s, %s, %s)"
    query_parameters = [new_account.account_number, new_account.routing_number, new_account.balance, user.id, new_account.type]
    cursor.execute(query, \
                   query_parameters)

    # commit changes
    db.commit()

    # close cursor
    cursor.close()


def get_user_account(user: User, accountType: str) -> Account:
    # create cursor
    cursor = db.cursor()

    # execute query
    query = "SELECT * FROM account WHERE user_id = %s AND type = %s"
    query_parameters = [user.id, accountType]
    cursor.execute(query, \
                   query_parameters)

    # get results
    result = cursor.fetchone()

    # close cursor
    cursor.close()

    # return result
    return Account(result[0], result[1], result[2], result[3], result[5], result[4])


def update_account_balance(accountID, newBalance):
    # create cursor
    cursor = db.cursor()

    # execute query
    query = "UPDATE account SET balance = %s WHERE id = %s"
    query_parameters = [newBalance, accountID]
    cursor.execute(query, \
                   query_parameters)

    # commit changes
    db.commit()

    # close cursor
    cursor.close()