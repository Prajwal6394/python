# print('Hello man');
# print('what is your name');

# name = input();

# print('Hello ' + name);
# print('length of your name is ' + str(len(name)));

# print('what is your age');
# age = input();
# print('you will be ' + str(int(age) + 1) + ' in a year');



# i = 1
# for i in range(1, 11):
#     print(i)
#     i += 1


# name = 'Prajwal';

# if name == 'Praj1wal':
#     print('Hello Prajwal');
# else:
#     print('Hello stranger');

# print('Done');

# print('Please enter your name');

# name = input();

# if name:
#     print('Thank you for entering your name '+ name);
# else:    
#     print('You did not enter your name' );

# name = '';

# while name != 'your name':
#     print('Please type your name');
#     name = input();

# print('Thank you!');

# total = 5;

# for num in range(101, 102):
#     total = total + num;
# print(total);

# def hello():
#     print('Hello');
#     print('How are you?');

# hello();

# def call(name):
#     print('Hello ' + name);

# def calculator(num1, num2, operator):
#     if operator == '+':
#         print(num1 + num2);
#     elif operator == '-':
#         print(num1 - num2);
#     elif operator == '*':
#         print(num1 * num2);
#     elif operator == '/':
#         print(num1 / num2);
#     else:
#         print('Invalid operator');

# input1 = input('Enter first number: ');
# input2 = input('Enter second number: ');
# input3 = input('Enter operator: ');
# calculator(int(input1), int(input2), input3);


# hello = 10; # global variable

# def hello():
#    hello = 5; # local variable
#    print(int(hello));

# hello();
# print(hello);

# local scope cannnot be accessed from another local scope

def spam():
    eggs = 99;
    bacon();
    print(eggs);

def bacon():
    ham = 101;
    eggs = 0;

spam();