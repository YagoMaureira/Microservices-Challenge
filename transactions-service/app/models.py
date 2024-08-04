class Transaction:
    def __init__(self, sender_cvu, receiver_cvu, amount):
        self.sender_cvu = sender_cvu
        self.receiver_cvu = receiver_cvu
        self.amount = amount

    def __repr__(self):
        return f"Transaction({self.sender_cvu}, {self.receiver_cvu}, {self.amount})"
    
    def to_dict(self):
        return {
            "sender_cvu": self.sender_cvu,
            "receiver_cvu": self.receiver_cvu,
            "amount": self.amount
        }
    
    @staticmethod
    def from_dict(data):
        return Transaction(
            sender_cvu=data.get('sender_cvu'),
            receiver_cvu=data.get('receiver_cvu'),
            amount=data.get('amount')
        )