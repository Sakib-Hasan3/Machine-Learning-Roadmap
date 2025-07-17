# 🔹 Python OOP টিউটোরিয়াল (Bangla Comments সহ)

# 🔸 ১. ক্লাস ও অবজেক্ট
class Student:
    def __init__(self, name, roll):  # constructor
        self.name = name            # instance variable
        self.roll = roll

    def display_info(self):         # instance method
        print(f"Name: {self.name}, Roll: {self.roll}")

student1 = Student("Rahim", 101)
student2 = Student("Karim", 102)

student1.display_info()
student2.display_info()

# ✅ __init__() হচ্ছে constructor
# ✅ self দ্বারা বোঝানো হয় নিজস্ব অবজেক্ট


# 🔸 ২. ক্লাস ভ্যারিয়েবল বনাম ইনস্ট্যান্স ভ্যারিয়েবল
class School:
    school_name = "Green Valley School"  # class variable (সব object এর জন্য এক)

    def __init__(self, student_name):
        self.student_name = student_name  # instance variable

    def show(self):
        print(f"Student: {self.student_name}, School: {School.school_name}")

s1 = School("Amina")
s2 = School("Jahid")

s1.show()
s2.show()

# ✅ class variable সব অবজেক্টে এক
# ✅ instance variable প্রতিটি অবজেক্টে আলাদা


# 🔸 ৩. Static Method
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(Calculator.add(5, 7))       # Output: 12
print(Calculator.multiply(4, 3))  # Output: 12

# ✅ @staticmethod → self বা cls ছাড়াই কাজ করে
# ✅ utility function হিসেবে ব্যবহৃত হয়


# 🔸 ৪. Class Method
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

# ✅ @classmethod পুরো class নিয়ে কাজ করে
# ✅ এটি বিকল্প constructor হিসেবে কাজ করে


# 🔸 ৫. পূর্ণাঙ্গ উদাহরণ: Employee System
class Employee:
    company = "TechSoft Ltd"  # class variable

    def __init__(self, name, position, salary):
        self.name = name              # instance variable
        self.position = position
        self.salary = salary

    def get_details(self):            # instance method
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Company: {Employee.company}")

    @staticmethod
    def company_policy():             # static method
        print("Working hours: 9AM - 5PM, Off: Friday")

    @classmethod
    def change_company(cls, new_name):  # class method
        cls.company = new_name

emp1 = Employee("Sadia", "Manager", 50000)
emp2 = Employee("Arif", "Developer", 40000)

emp1.get_details()
emp2.get_details()

Employee.company_policy()

Employee.change_company("NextGen Tech")

emp1.get_details()
emp2.get_details()

# ✅ Static, Class এবং Instance method এখানে একত্রে ব্যবহার করা হয়েছে
