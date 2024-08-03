class Account:
    def __init__(self, cvu, username, email, balance):
        self.cvu = cvu
        self.username = username
        self.email = email
        self.balance = balance

    def __repr__(self):
        return f"Account({self.cvu}, {self.username}, {self.email}, {self.balance})"
    
    def to_dict(self):
        return {
            "cvu": self.cvu,
            "username": self.username,
            "email": self.email,
            "balance": self.balance
        }
    
    @staticmethod
    def from_dict(data):
        return Account(
            cvu=data.get('cvu'),
            username=data.get('username'),
            email=data.get('email'),
            balance=data.get('balance')
        )