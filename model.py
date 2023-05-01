class User:
    def __init__(self, user_id, name, email, password):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"User: {self.name} - {self.email} - {self.password}"


class Account:
    def __init__(self, account_id, account_number, routing_number, balance, user_id, account_type):
        self.id = account_id
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance
        self.user_id = user_id
        self.type = account_type

    def __str__(self):
        return f"Account: {self.account_number} - {self.balance} - {self.user_id} - {self.type}"