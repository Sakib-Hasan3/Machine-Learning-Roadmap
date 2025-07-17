# 🔹 Python OOP টিউটোরিয়াল  
## ক্লাস, অবজেক্ট, ভ্যারিয়েবল ও মেথড ব্যাখ্যাসহ

---

# 🔸 OOP কী?

OOP বা Object-Oriented Programming হলো এমন একটি প্রোগ্রামিং পদ্ধতি যেখানে বাস্তব জীবনের বস্তু (Object) ও তাদের বৈশিষ্ট্য (Properties) এবং আচরণ (Behaviors) অনুযায়ী কোড লেখা হয়।

---

# 🔸 OOP-এর মূল উপাদানসমূহ

- `Class` — ব্লুপ্রিন্ট বা ছক
- `Object` — ক্লাস থেকে তৈরি বস্তু
- `Instance Variable` — অবজেক্ট অনুযায়ী আলাদা ভ্যারিয়েবল
- `Class Variable` — সব অবজেক্টের জন্য অভিন্ন ভ্যারিয়েবল
- `Instance Method` — অবজেক্ট ব্যবহার করে কল করা যায়
- `Static Method` — ক্লাস বা অবজেক্ট ছাড়াই কল করা যায়
- `Class Method` — পুরো ক্লাসকে রিপ্রেজেন্ট করে

---

# 🔸 ১. ক্লাস ও অবজেক্ট

```python
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display_info(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

student1 = Student("Rahim", 101)
student2 = Student("Karim", 102)

student1.display_info()
student2.display_info()
✅ __init__() হচ্ছে constructor
✅ self দ্বারা বোঝানো হয় নিজস্ব অবজেক্ট

🔸 ২. ক্লাস ভ্যারিয়েবল বনাম ইনস্ট্যান্স ভ্যারিয়েবল
python
Copy code
class School:
    school_name = "Green Valley School"  # class variable

    def __init__(self, student_name):
        self.student_name = student_name  # instance variable

    def show(self):
        print(f"Student: {self.student_name}, School: {School.school_name}")

s1 = School("Amina")
s2 = School("Jahid")

s1.show()
s2.show()
✅ class variable সব অবজেক্টে এক
✅ instance variable প্রতিটি অবজেক্টে আলাদা

🔸 ৩. Static Method
python
Copy code
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(Calculator.add(5, 7))
print(Calculator.multiply(4, 3))
✅ @staticmethod কোনো self বা cls ছাড়া কাজ করে
✅ সাধারণ utility function হিসাবে ব্যবহৃত হয়

🔸 ৪. Class Method
python
Copy code
class Circle:
    pi = 3.1416

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def area(self):
        return Circle.pi * (self.radius ** 2)

c1 = Circle(5)
print("Area from radius:", c1.area())

c2 = Circle.from_diameter(10)
print("Area from diameter:", c2.area())
✅ @classmethod পুরো ক্লাস নিয়ে কাজ করে
✅ বিকল্প constructor হিসেবে কাজ করতে পারে

🔸 ৫. পূর্ণাঙ্গ উদাহরণ: Employee System
python
Copy code
class Employee:
    company = "TechSoft Ltd"

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_details(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Company: {Employee.company}")

    @staticmethod
    def company_policy():
        print("Working hours: 9AM - 5PM, Off: Friday")

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

emp1 = Employee("Sadia", "Manager", 50000)
emp2 = Employee("Arif", "Developer", 40000)

emp1.get_details()
emp2.get_details()

Employee.company_policy()

Employee.change_company("NextGen Tech")

emp1.get_details()
emp2.get_details()