# Instance variable : Name, Amount, Address, Account No
# Instance method : CreateAccount(), DisplayAccountInfo(), DisplayBankName or Interest()

class Bank_Account:

    Bank_Name = "HDFC Bank PVT LTD"
    ROI_ON_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter your initial amount : ")
        self.Amount = int(input())

        print("Enter your Address : ")
        self.Address = input()

        print("Enter your AccountNo : ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("------------Your Account information is as below----------")
        print("Name of Account Holder : ",self.Name)
        print("Account Number : ",self.AccountNo)
        print("Address of Account Holder : ",self.Address)
        print("Current Amount in account : ",self.Amount)


def main():

    print("Name of Bank : ",Bank_Account.Bank_Name)
    print("Rate of Intrest on Fixed Deposit : ",Bank_Account.ROI_ON_FD)

    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the first account")
    User1.CreateAccount()

    print("Creating the second account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__ == "__main__":
    main()