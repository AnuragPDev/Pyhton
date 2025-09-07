# @staticmethod 

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self,owner, balance):
        self.owner=owner
        self._balance= balance

    def deposite(self, amount ):
        if self._is_valid_amount(amount):
            self._balance+=amount
            self.__log_transaction("Deposite",amount)
        else:
            print("Deposite amount must be positve")

    def _is_valid_amount(self,amount):
        return amount>0
    
    @staticmethod
    def  is_valid_interest_rate(rate):  # utility function 
        return    0<=rate<=5  # chained comparision works as and operator if both true than return true else retirn false
    def __log_transaction(self, trasaction_type, amount):
        print(f'Logging {trasaction_type} of ${amount}. New balance: ${self._balance}')

account =BankAccount("Peter", 500) 
account.__log_transaction("Withdraw", 3444)

account.deposite(43002442)
# we dont need object to check if interest rate is valid or not 

    