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

# def spam():
#     eggs = 99;
#     bacon();
#     print(eggs);

# def bacon():
#     ham = 101;
#     eggs = 0;

# spam();

# error handling


# def spam(divideBy):
#     try:
#         return 42 / divideBy;
#     except:
#         print('Error: Invalid argument');

# print(spam(2));
# print(spam(12));
# print(spam(0));
# print(spam(1));


# print('How many cats do you have?');

# numCats = input();
# if int(numCats) >= 4:
#     print('That is a lot of cats');
# else:   
#     print('That is not that many cats');

# with error handling

# try:
#     print('How many cats do you have?');
#     numCats = input();
#     if int(numCats) >= 4:
#         print('That is a lot of cats');
#     else:   
#         print('That is not that many cats');
# except ValueError:
#     print('You did not enter a number');


# import random

# print('Hello! What is your name?');
# name = input();

# print('Well, ' + name + ', I am thinking of a number between 1 and 20');

# secretNumber = random.randint(1, 20);

# for guessesTaken in range(1, 7):
#     print('Take a guess');
#     guess = int(input());

#     if guess < secretNumber:
#         print('Your guess is too low');
#     elif guess > secretNumber:
#         print('Your guess is too high');
#     else:
#         break;

# if guess == secretNumber:
#     print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses');
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber));


# array = ['cal', 'cat', 'bat', 'rat', 'mat', 'fat', 'sat', 'pat', 'hat'];
# print(array[0:3]);


# arrayInsideArray = [['cal', 'cat', 'bat'], ['rat', 'mat', 'fat'], ['sat', 'pat', 'hat']];
# print(arrayInsideArray[1][1]);

# del arrayInsideArray[1];

# print(arrayInsideArray);

# res = 'howdy' in ['hello', 'hi', 'howdy', 'hey'];
# print(res);

# res2 = 'howsdy' not in ['hello', 'hi', 'howdy', 'hey'];
# print(res2);


# for i in range(4):
#     print(i);

# for i in [0, 1, 2, 3]:
#     print(i);

# supplies = ['pens', 'staplers', 'flame-throwers', 'binders'];

# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i]);

# cat = ['fat', 'orange', 'loud'];

# size = cat[0];
# color = cat[1];
# disposition = cat[2];

# print(size);

# size, color, disposition = cat;


# a = 'AAA';
# b = 'BBB';

# a, b = b, a;

# print(a);
# print(b);

# spam = ['hello', 'hi', 'howdy', 'hey'];

# spam.append('yo');

# print(spam);

# spam.insert(1, 'yo');

# print(spam);

# spam.remove('yo');

# print(spam);

# spam.sort();

# spam.sort(reverse=True);

# print(spam);


list('hello');

print(list('hello'));

spam = [0, 1, 2, 3, 4, 5];

cheese = spam;

cheese[1] = 'Hello';

print(spam);