#different separators for differnet type of document -markdown text, -code

from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = '''
    class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

'''

splitter = RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON,
    chunk_size = 250,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks[0])