import datetime


class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.bank_total_money = 100
        self.can_loan = True
        self.bank_total_loan = 0
        self.admin = None
        self.users = {}

    def add_user(self, user):
        if user.email in self.users:
            print("User with this email already exists.")
        else:
            self.users[user.email] = user
            print("Account created! Login now.")

    def add_money(self, sign, amount):
        if amount > 0:
            if sign == "+":
                self.bank_total_money += amount
            else:
                self.bank_total_money -= amount


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.password = password
        self.email = email
        self.total_money = 0
        self.loan = False
        self.loan_money = 0
        self.transection_history = []

    def __repr__(self) -> str:
        welcoming_message = f"*** Welcome {user.name.upper()} ***"
        balance_maessage = f"Your account got balance {self.total_money} Rm."
        # print()
        press_digit = f"Press Digit\n\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Tranfer Money\n5. Check Transaction History\n6. Want Loan\n7. Log out"
        if self.loan_money is not None:
            loan_maessage = f"You have a loan of {self.loan_money} Rm."
            return f"\n{welcoming_message}\n{balance_maessage}\n{loan_maessage}\n\n{press_digit}"
        else:
            return f"\n{welcoming_message}\n{balance_maessage}\n\n{press_digit}"

    def deposit(self, amount, transaction):
        if amount > 0:
            self.total_money += amount
            self.transection_history.append(transaction)
            # self.transection_history()
            print(
                f"Succesfully {amount} Rm deposit to account and balance is {self.total_money} Rm."
            )
            return True

        else:
            print("Something Wrong!")

    def withdraw(self, amount, transaction):
        if amount > self.total_money:
            # self.total_money-=amount
            # self.transection_history.append(transaction)
            print(
                f"You have balance {self.total_money} Rm.Your withdrawal amount can not exceeded than that."
            )
        elif amount <= self.total_money:
            self.total_money -= amount
            self.transection_history.append(transaction)
            print(
                f"Succesfully {amount} Rm withdraw from account and balance is {self.total_money} Rm."
            )
            return True
            # self.total_money-=amount
            # self.transection_history.append(transaction)
            # self.transection_history()
        else:
            print("Sorry to say, You are bankrupt!")

    def check_balance(self):
        print(f"Your total balance is: {self.total_money} Rm.")

    def transfer_money(self, amount, reciever_name, transaction):
        if amount <= self.total_money and amount > 0:
            self.total_money -= amount
            self.transection_history.append(transaction)
            print(
                f"Succesfully {amount} Rm tranfer to {reciever_name} and balance is {self.total_money} Rm."
            )
            # self.transection_history()
        else:
            print("Sorry to say, You are bankrupt! Something Wrong.")

    # def transaction_history_keeper(self,story_name,amount_plus_minus,time,before_balance,after_balance):
    #     story={'name':story_name,'amountAdOrDed':amount_plus_minus,'time':time,'before_balance':before_balance,'now_balance':after_balance}
    #     self.transection_history.append(story)

    def take_loan(self):
        # if self.loan_money>0:
        if self.loan:
            print("You have loan !")
        else:
            # self.loan = True
            if user.total_money != 0:
                self.loan = True
                self.loan_money = self.total_money * 2
                print("Congrats! Your loan accapted.")
                return True
            else:
                print("You have 0 balance can not approve loan.")

    def transaction_history(self):
        print("*** Your Transaction History ***")
        index = 1
        for transaction in self.transection_history:
            print(index)
            print("--------------------")
            print()
            print(f"Time: {transaction.time}")
            if transaction.trans_name == "deposit":
                print(f"Deposited Amount: {transaction.amount} RM")
            elif transaction.trans_name == "withdraw":
                print(f"Withdrawn Amount: {transaction.amount} RM")
            elif transaction.trans_name == "transfer":
                print(
                    f"Transferred Amount: {transaction.amount} RM to {transaction.to}"
                )
            elif transaction.trans_name == "recieve":
                print(f"Recieved Amount: {transaction.amount} RM from {transaction.to}")
            elif transaction.trans_name == "loan":
                print(f"Loaned Amount: {transaction.amount} RM ")
            print(f"Balance After Transaction: {transaction.after_add_total_money} RM")
            print()
            index += 1
            # print('--------------------')
        # index+=1

    def logout(self):
        print("Logged out successfully.")
        return False

    # def is_succes(self):
    #     return True


class Transaction:
    def __init__(self, transaction_name, amount, to_who, after_add_total_money) -> None:
        self.trans_name = transaction_name
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.amount = amount
        self.to = to_who
        self.after_add_total_money = after_add_total_money


class Admin:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

    # def bank_total_loan(self):
    #     return self.bank_total_loan

    # def on_of_loan_feature(self,sign):
    #     if sign==1:
    #         if

    def __repr__(self) -> str:
        # print(f'*** Welcome Admin {admin.name} ***')
        # print(f'Press Digit\n1. Total Available Balance\n2. Total Loan\n3. On Or Off Loan Feature')
        welcome_mesaage = f"*** Welcome Admin {admin.name} ***"
        user_input = f"Press Digit\n1. Total Available Balance\n2. Total Loan\n3. On Or Off Loan Feature\n4. Log out"
        return f"{welcome_mesaage}\n{user_input}"

    def logout(self):
        print("Logged out successfully.")
        return False


# Create Bank
my_bank = Bank("Monday Bank")
# Create User
user_1 = User("Money man", "money_man@mail.com", "123")
user_2 = User("Money man2", "money_man2@mail.com", "123")
# Add user to Bank
my_bank.add_user(user_1)
my_bank.add_user(user_2)
# Add admin
admin = Admin("Admin", "admin@mail.com", "a123")
my_bank.admin = admin
# print(my_bank.admin.name)

logged_in = False
while not logged_in:
    print("---- Welcome To Monday Bank ----")
    print(f"1. New to Bank? Signup\n2. Login")
    # a = int(input("Plesase type digit: "))
    a = input("Plesase type digit: ")
    if a == "1":
        name = input("Please Enter your name: ")
        email = input("Please Enter your email: ")
        password = input("Please Enter your password: ")
        if email in my_bank.users:
            print("User with this email already exists!")
        else:
            user = User(name, email, password)
            my_bank.add_user(user)
    elif a == "2":
        # logged_in = True
        email = input("Please Enter your email: ")
        password = input("Please Enter your password: ")
        # while logged_in:
        if email in my_bank.users:
            # print(email)
            user = my_bank.users[email]
            # print(user.loan_money)
            if user.password == password:
                logged_in = True

                while logged_in:
                    print(user)
                    # u_a = int(input("Please type digit: "))
                    u_a = input("Please type digit: ")
                    if u_a == "1":
                        amount = int(input("Please enter your amount: "))
                        transaction = Transaction(
                            "deposit", amount, user.name, user.total_money + amount
                        )

                        is_success = user.deposit(amount, transaction)
                        if is_success:
                            my_bank.add_money("+", amount)

                    elif u_a == "2":
                        amount = int(input("Please enter your amount: "))
                        transaction = Transaction(
                            "withdraw", amount, user.name, user.total_money - amount
                        )

                        is_succes = user.withdraw(amount, transaction)
                        if is_succes:
                            my_bank.add_money("-", amount)
                    elif u_a == "3":
                        user.check_balance()
                    elif u_a == "4":
                        reciever = input("Please input reciever email: ")
                        if reciever in my_bank.users:
                            reciever_name = input("Please input reciever name: ")
                            amount = int(input("Please enter your amount:  "))
                            reciever_user = my_bank.users[reciever]
                            if reciever_user.name != reciever_name:
                                print("Name does not match !")
                            #   elif reciever.name  in my_bank.users[reciever]:
                            #       user.transfer_money(amount)
                            else:
                                transaction_user = Transaction(
                                    "transfer",
                                    amount,
                                    reciever_user.name,
                                    user.total_money - amount,
                                )
                                reciever_user.total_money += amount

                                transaction_reciever = Transaction(
                                    "recieve",
                                    amount,
                                    user.name,
                                    reciever_user.total_money,
                                )
                                # reciever_user.total_money += amount
                                reciever_user.transection_history.append(
                                    transaction_reciever
                                )
                                user.transfer_money(
                                    amount, reciever_user.name, transaction_user
                                )

                        else:
                            print("User not Exists in the bank")
                    elif u_a == "5":
                        user.transaction_history()
                    elif u_a == "6":
                        can = my_bank.can_loan
                        if can == True:
                            if my_bank.bank_total_money >= user.total_money * 2:
                                is_succes = user.take_loan()
                                if is_succes:
                                    my_bank.bank_total_loan += user.loan_money
                                    my_bank.bank_total_money -= user.loan_money
                                    transaction=Transaction('loan',user.total_money*2,user.name,user.total_money)
                                    user.transection_history.append(transaction)
                            else:
                                print(f"Bank do not have enough money!")
                        else:
                            print("At this moment can not take loan!Be patient.")

                    elif u_a == "7":
                        logged_in = user.logout()
                        # if not logged_in:
                        #     break
                    else:
                        print("Wrongly pressed!!!")
                        continue
            else:
                print("Wrong Password!Try again.")
        elif email == admin.email:
            if password == admin.password:
                # print(admin)
                logged_in = True
            while logged_in:
                print(admin)
                a_i = input("Please type digit: ")
                if a_i == "1":
                    print(
                        f"{my_bank.name} have total balance:", my_bank.bank_total_money
                    )
                elif a_i == "2":
                    print(f"{my_bank.name} have total loan:", my_bank.bank_total_loan)
                elif a_i == "3":
                    print(f"Press Digit\n1.On\n2. Off")
                    on_of_i = int(input("Please press digit: "))
                    if on_of_i == 1:
                        if my_bank.can_loan == True:
                            print("Bank loan feature already on!")
                        else:
                            my_bank.can_loan = True
                            print("Successfully on feature")
                    if on_of_i == 2:
                        if my_bank.can_loan == False:
                            print("Bank loan feature already off!")
                        else:
                            my_bank.can_loan = False
                            print("Successfully off feature!")
                elif a_i == "4":
                    logged_in = admin.logout()
                    # if not logged_in:
                    #     break
                else:
                    print("Wrongly Pressed admin !!!")
                    continue
            else:
                print("Wrong Password!Try again.")
        else:
            print("User not found. Please sign up.")

    else:
        print("Wrongly press!!!")
        continue
