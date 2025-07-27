# Inheritance In Python

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a class to inherit attributes and methods from another class. This lesson covers single inheritance and multiple inheritance, demonstrating how to create and use them in Python.

## 1. Single Inheritance - Parent Class (Car)

```python
## Inheritance (Single Inheritance)
## Parent class
class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype 
    
    def drive(self):
        print(f"The person will drive the {self.enginetype} car ")
```

**লাইন বাই লাইন ব্যাখ্যা:**
- `class Car:` - Car নামে parent/base class define করা হচ্ছে
- `def __init__(self,windows,doors,enginetype):` - Constructor method যা তিনটি parameter নেয়
- `self.windows=windows` - windows এর সংখ্যা instance variable হিসেবে store করা
- `self.doors=doors` - doors এর সংখ্যা instance variable হিসেবে store করা  
- `self.enginetype=enginetype` - engine এর type (petrol/diesel/electric) store করা
- `def drive(self):` - drive method define করা যা car চালানোর functionality দেয়
- `print(f"The person will drive the {self.enginetype} car ")` - f-string দিয়ে engine type সহ message print করা

## 2. Parent Class Object তৈরি

```python
car1=Car(4,5,"petrol")
car1.drive()
```

**ব্যাখ্যা:**
- `car1=Car(4,5,"petrol")` - Car class থেকে object তৈরি: 4 windows, 5 doors, petrol engine
- `car1.drive()` - car1 object এর drive method call করা
- **Output:** "The person will drive the petrol car"

## 3. Single Inheritance - Child Class (Tesla)

```python
class Tesla(Car):
    def __init__(self,windows,doors,enginetype,is_selfdriving):
        super().__init__(windows,doors,enginetype)
        self.is_selfdriving=is_selfdriving

    def selfdriving(self):
        print(f"Tesla supports self driving : {self.is_selfdriving}")
```

**লাইন বাই লাইন ব্যাখ্যা:**
- `class Tesla(Car):` - Tesla class যা Car class থেকে inherit করছে (parentheses এ Car লেখা)
- `def __init__(self,windows,doors,enginetype,is_selfdriving):` - Tesla এর constructor যা Car এর সব parameter + একটি নতুন parameter নেয়
- `super().__init__(windows,doors,enginetype)` - Parent class (Car) এর constructor call করা
- `self.is_selfdriving=is_selfdriving` - Tesla এর নিজস্ব additional attribute
- `def selfdriving(self):` - Tesla এর নিজস্ব method যা parent class এ নেই
- `print(f"Tesla supports self driving : {self.is_selfdriving}")` - Self-driving capability এর message

## 4. Child Class Object এবং Method Usage

```python
tesla1=Tesla(4,5,"electric",True)
tesla1.selfdriving()
```

**ব্যাখ্যা:**
- `tesla1=Tesla(4,5,"electric",True)` - Tesla object তৈরি: 4 windows, 5 doors, electric engine, self-driving enabled
- `tesla1.selfdriving()` - Tesla এর নিজস্ব selfdriving method call করা
- **Output:** "Tesla supports self driving : True"

## 5. Inherited Method Call

```python
tesla1.drive()
```

**ব্যাখ্যা:**
- `tesla1.drive()` - Parent class (Car) থেকে inherited drive method call করা
- Tesla object parent class এর method ব্যবহার করতে পারে
- **Output:** "The person will drive the electric car"

## 6. Multiple Inheritance - Base Classes

### Base Class 1 - Animal

```python
### Multiple Inheritance
## When a class inherits from more than one base class.
## Base class 1
class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Subclass must implement this method")
```

**ব্যাখ্যা:**
- `class Animal:` - Animal নামে প্রথম base class
- `def __init__(self,name):` - Animal constructor যা name parameter নেয়
- `self.name=name` - Animal এর name attribute
- `def speak(self):` - speak method define করা (generic implementation)
- `print("Subclass must implement this method")` - Message যা বলে যে subclass এ override করতে হবে

### Base Class 2 - Pet

```python
## BAse class 2
class Pet:
    def __init__(self, owner):
        self.owner = owner
```

**ব্যাখ্যা:**
- `class Pet:` - Pet নামে দ্বিতীয় base class
- `def __init__(self, owner):` - Pet constructor যা owner parameter নেয়
- `self.owner = owner` - Pet এর owner attribute

## 7. Multiple Inheritance - Derived Class

```python
##Derived class
class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)

    def speak(self):
        return f"{self.name} say woof"
```

**লাইন বাই লাইন ব্যাখ্যা:**
- `class Dog(Animal,Pet):` - Dog class যা Animal এবং Pet দুটি class থেকে inherit করছে
- `def __init__(self,name,owner):` - Dog constructor যা দুটি parameter নেয়
- `Animal.__init__(self,name)` - Animal class এর constructor manually call করা
- `Pet.__init__(self,owner)` - Pet class এর constructor manually call করা
- `def speak(self):` - Animal class এর speak method override করা
- `return f"{self.name} say woof"` - Dog specific speak behavior

## 8. Multiple Inheritance Object Usage

```python
## Create an object
dog=Dog("Buddy","Krish")
print(dog.speak())
print(f"Owner:{dog.owner}")
```

**ব্যাখ্যা:**
- `dog=Dog("Buddy","Krish")` - Dog object তৈরি: name="Buddy", owner="Krish"
- `print(dog.speak())` - Dog এর overridden speak method call করা
  - **Output:** "Buddy say woof"
- `print(f"Owner:{dog.owner}")` - Pet class থেকে inherited owner attribute access করা
  - **Output:** "Owner:Krish"

## Key Inheritance Concepts (মূল ধারণাসমূহ):

### 1. **Single Inheritance (একক উত্তরাধিকার)**
- একটি child class একটি parent class থেকে inherit করে
- `class ChildClass(ParentClass):` syntax ব্যবহার করা হয়
- `super()` function ব্যবহার করে parent constructor call করা হয়
- Child class parent এর সব methods এবং attributes পায়

### 2. **Multiple Inheritance (বহু উত্তরাধিকার)**
- একটি child class একাধিক parent class থেকে inherit করে
- `class ChildClass(Parent1, Parent2):` syntax ব্যবহার করা হয়
- Manual constructor calling করতে হয় প্রতিটি parent class এর জন্য
- সব parent class এর features একসাথে পাওয়া যায়

### 3. **Method Overriding (মেথড ওভাররাইডিং)**
- Child class parent class এর method কে নিজের মতো করে redefine করতে পারে
- `Dog.speak()` method `Animal.speak()` কে override করেছে
- Child class এর implementation parent class এর implementation কে replace করে

### 4. **super() Function**
- Parent class এর methods এবং constructor access করতে ব্যবহৃত হয়
- Code duplication এড়াতে সাহায্য করে
- Parent class এর functionality reuse করতে দেয়

## Benefits of Inheritance (উত্তরাধিকারের সুবিধাসমূহ):

1. **Code Reusability** - Parent class এর code বার বার ব্যবহার করা যায়
2. **Hierarchical Structure** - Logical class hierarchy তৈরি করা যায়
3. **Method Overriding** - Parent class এর behavior customize করা যায়
4. **Polymorphism** - Same interface দিয়ে different behaviors achieve করা যায়
5. **Maintainability** - Code maintenance সহজ হয়

## Best Practices (সর্বোত্তম অনুশীলন):

1. **Use super()** - Single inheritance এ super() ব্যবহার করুন
2. **Method Overriding** - Child class এ parent method override করার সময় সাবধান থাকুন
3. **Multiple Inheritance** - সাবধানে ব্যবহার করুন, complexity বাড়তে পারে
4. **Clear Hierarchy** - Logical এবং clear inheritance hierarchy maintain করুন

## Conclusion

Inheritance is a powerful feature in OOP that allows for code reuse and the creation of a more logical class structure. Single inheritance involves one base class, while multiple inheritance involves more than one base class. Understanding how to implement and use inheritance in Python will enable you to design more efficient and maintainable object-oriented programs.

উত্তরাধিকার হলো OOP এর একটি শক্তিশালী feature যা code reusability বাড়ায় এবং maintainable software তৈরি করতে সাহায্য করে।
