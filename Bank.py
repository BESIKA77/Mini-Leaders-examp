# Bank System:

# 1.create account
# 2.Deposit
# 3.Withdraw
# 4.Exit

# თქვენი დავალება იქნება გააკეთოთ ბანკის სისტემა მოცემული სექციებით პითონში,რაც აქამდე ისწავლეთ გააკეთეთ იმ მასალით გამოიყენეთ თქვენი მაქსიმალური ცოდნა,მერე კი ჩვენ შევამოწმეთ თუ რა დონის ცოდნა გამოიყენეთ და იმის მიხედვით შეიგიმოწმებთ!!!
# როდესაც დააამთავრებთ გამოცდას გააკეთეთ ახალი რეპოზიტორია და ატვირთეთ იქ თქვენი ნაშრომი და შემდეგ მოცემულ doc-ში ჩასვით თქვენი გით ჰაბი!!!

# creating acc.
print("please create a account:")
name = input("please enter your name: ")
surname = input('please enter your surname: ')
age = int(input('please enter your age: '))
while age < 18:
    print("you are not adult to have bank account")
    age = int(input('please enter your age again: '))
while age > 99:
        print("please enter the real age")
        age = int(input('please enter your age again: '))
tel_num = int(input('please enter your telephone number: '))
private_num = int(input('please enter your private number: '))
print('hello ' + name + " " + surname + "!")

# choosing
while True:
    choose = input("do u want to do deposit or withdraw?: ")
    choose_1 = "deposit"
    choose_2 = "withdraw"
    balance = 0
    
    if choose == choose_1:
        deposit = int(input("enter how much $ do u want to deposit? "))
        if deposit >= 1:
            balance = balance + deposit
            print('your balance:↓')
            print(balance)
        elif deposit <= 0:
           print("you can't deposit that")
    elif choose == choose_2:
             withdraw = int(input("enter how $ money do u want to withdraw? "))
             if balance > withdraw:
                 print(balance - withdraw)
                 print("withdrawed sucsessful, on balance, you have:↓")
                 print(balance)

    else:
        print("you can't enter that")

