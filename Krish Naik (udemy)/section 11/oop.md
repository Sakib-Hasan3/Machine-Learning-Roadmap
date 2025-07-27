# Classes and Objects - Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. OOP allows for modeling real-world scenarios using classes and objects. This lesson covers the basics of creating classes and objects, including instance variables and methods.

## 1. Basic Class Creation (মৌলিক Class তৈরি)

```python
### A class is a blue print for creating objects. Attributes,methods
class Car:
    pass

audi=Car()
bmw=Car()

print(type(audi))
```

**ব্যাখ্যা:** 
- `class Car:` - Car নামে একটি class define করা হচ্ছে যা object তৈরির blueprint
- `pass` - কোনো functionality না থাকলে pass keyword ব্যবহার করতে হয়
- `audi=Car()` এবং `bmw=Car()` - Car class থেকে দুটি আলাদা object তৈরি করা হচ্ছে
- `print(type(audi))` - object এর type প্রিন্ট করবে `<class '__main__.Car'>`

## 2. Printing Objects (Object প্রিন্ট করা)

```python
print(audi)
print(bmw)
```

**ব্যাখ্যা:** এই কোডগুলো প্রতিটি object এর memory address প্রিন্ট করবে। প্রতিটি object এর আলাদা memory location থাকে।

## 3. Adding Attributes to Objects (Object এ Attribute যোগ করা)

```python
audi.windows=4

print(audi.windows)
```

**ব্যাখ্যা:** 
- `audi.windows=4` - audi object এ windows নামে একটি attribute যোগ করা হচ্ছে
- এই attribute শুধুমাত্র audi object এর জন্য, অন্য object এর জন্য নয়

## 4. Attribute Access Error Example

```python
tata=Car()
tata.doors=4
print(tata.windows)  # This will cause an error
```

**ব্যাখ্যা:** 
- `tata` object এ শুধু `doors` attribute আছে, `windows` নেই
- তাই `print(tata.windows)` AttributeError দেবে

## 5. Viewing Object Methods (Object এর Methods দেখা)

```python
dir(tata)
```

**ব্যাখ্যা:** `dir()` function object এর সব available attributes এবং methods এর list return করে।

## 6. Constructor and Instance Variables (Constructor এবং Instance Variables)

```python
### Instance Variable and Methods
class Dog:
    ## constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age

## create objects
dog1=Dog("Buddy",3)
print(dog1)
print(dog1.name)
print(dog1.age)
```

**ব্যাখ্যা:**
- `def __init__(self,name,age):` - Constructor method, object তৈরি হওয়ার সময় automatically call হয়
- `self.name=name` - instance variable তৈরি করা
- `self.age=age` - প্রতিটি object এর নিজস্ব age variable
- `dog1=Dog("Buddy",3)` - "Buddy" name এবং 3 age দিয়ে object তৈরি

## 7. Creating Multiple Objects (একাধিক Object তৈরি)

```python
dog2=Dog("Lucy",4)
print(dog2.name)
print(dog2.age)
```

**ব্যাখ্যা:** একই class থেকে ভিন্ন parameters দিয়ে আরেকটি object তৈরি করা। প্রতিটি object এর নিজস্ব instance variables থাকে।

## 8. Instance Methods (Instance Methods)

```python
## Define a class with instance methods
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def bark(self):
        print(f"{self.name} says woof")

dog1=Dog("Buddy",3)
dog1.bark()
dog2=Dog("Lucy",4)
dog2.bark()
```

**ব্যাখ্যা:**
- `def bark(self):` - instance method define করা
- `self` parameter দিয়ে current object এর reference পাওয়া যায়
- `dog1.bark()` - "Buddy says woof" প্রিন্ট করবে
- `dog2.bark()` - "Lucy says woof" প্রিন্ট করবে

## 9. Practical Example - Bank Account Class

```python
### Modeling a Bank Account

## Define a class for bank account
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited. New balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds!")
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn. New Balance is {self.balance}")

    def get_balance(self):
        return self.balance
    
## create an account
account=BankAccount("Krish",5000)
print(account.balance)
```

**ব্যাখ্যা:**
- `def __init__(self,owner,balance=0):` - Constructor with default balance value
- `def deposit(self,amount):` - টাকা জমা দেওয়ার method
- `def withdraw(self,amount):` - টাকা তোলার method with balance checking
- `def get_balance(self):` - Current balance return করার method
- Real-world banking scenario এর practical implementation

## 10. Using Bank Account Methods

```python
## Call instance methods
account.deposit(100)
```
**Output:** "100 is deposited. New balance is 5100"

```python
account.withdraw(300)
```
**Output:** "300 is withdrawn. New Balance is 4800"

```python
print(account.get_balance())
```
**Output:** 4800

## Key OOP Concepts (মূল OOP ধারণাসমূহ):

### 1. **Class (ক্লাস)**
- Object তৈরির blueprint বা template
- Attributes এবং methods define করে

### 2. **Object (অবজেক্ট)**
- Class এর instance বা real-world entity
- Class থেকে তৈরি হওয়া actual entity

### 3. **Constructor (`__init__`)**
- Object initialization এর জন্য special method
- Object তৈরি হওয়ার সময় automatically call হয়

### 4. **Instance Variables**
- প্রতিটি object এর নিজস্ব data/attributes
- `self.variable_name` format এ define করা হয়

### 5. **Instance Methods**
- Object এর behavior define করে
- `self` parameter অবশ্যই থাকতে হবে

### 6. **self Parameter**
- Current object এর reference
- Instance variables এবং methods access করতে ব্যবহৃত হয়

## Benefits of OOP (OOP এর সুবিধাসমূহ):

1. **Code Reusability** - একবার class তৈরি করে বার বার ব্যবহার করা যায়
2. **Modularity** - Code আলাদা আলাদা class এ organize করা যায়
3. **Maintainability** - Code maintenance সহজ হয়
4. **Real-world Modeling** - Real-world scenarios easily model করা যায়
5. **Data Security** - Data encapsulation এর মাধ্যমে data security

## Conclusion

Object-Oriented Programming (OOP) allows you to model real-world scenarios using classes and objects. In this lesson, you learned how to create classes and objects, define instance variables and methods, and use them to perform various operations. Understanding these concepts is fundamental to writing effective and maintainable Python code.

OOP হলো modern programming এর একটি গুরুত্বপূর্ণ paradigm যা clean, organized এবং scalable code লিখতে সাহায্য করে।
