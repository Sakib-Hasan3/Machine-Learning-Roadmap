# Understanding Exceptions

Exception handling in Python allows you to handle errors gracefully and take corrective actions without stopping the execution of the program. This lesson will cover the basics of exceptions, including how to use try, except, else, and finally blocks.

## What Are Exceptions?

Exceptions are events that disrupt the normal flow of a program. They occur when an error is encountered during program execution. Common exceptions include:

- **ZeroDivisionError**: Dividing by zero.
- **FileNotFoundError**: File not found.
- **ValueError**: Invalid value.
- **TypeError**: Invalid type.

## 1. Basic Exception Try-Except Block

```python
## Exception try ,except block

try:
    a=b
except:
    print("The variable has not been assigned")
```

**ব্যাখ্যা:** এই কোডটি মৌলিক try-except ব্লক দেখায়। `try` ব্লকে `a=b` কোডটি NameError দেবে কারণ `b` ভেরিয়েবল define করা নেই। `except` ব্লক যেকোনো ধরনের error catch করে একটি custom message প্রিন্ট করে।

## 2. Code Without Exception Handling

```python
a=b
```

**ব্যাখ্যা:** এই লাইনটি exception handling ছাড়া সরাসরি error দেবে এবং program crash করবে।

## 3. Specific Exception Handling with NameError

```python
try:
    a=b
except NameError as ex:
    print(ex)
```

**ব্যাখ্যা:** এখানে নির্দিষ্টভাবে `NameError` catch করা হয়েছে এবং `as ex` ব্যবহার করে error object কে একটি ভেরিয়েবলে store করা হয়েছে।

## 4. Handling ZeroDivisionError

```python
try:
    result=1/0
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than 0")
```

**ব্যাখ্যা:** শূন্য দিয়ে ভাগ করার কারণে যে `ZeroDivisionError` হয় তা catch করে system error message এবং custom message দুটোই প্রিন্ট করা হয়।

## 5. Multiple Exception Handling

```python
try:
    result=1/2
    a=b
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than 0")
except Exception as ex1:
    print(ex1)
    print('Main exception got caught here')
```

**ব্যাখ্যা:** একাধিক except ব্লক ব্যবহার করে বিভিন্ন ধরনের error handle করা হয়। এখানে `ZeroDivisionError` এর জন্য specific handler এবং অন্য সব error এর জন্য general `Exception` handler আছে।

## 6. User Input Exception Handling

```python
try:
    num=int(input("Enter a number"))
    result=10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than 0")
except Exception as ex:
    print(ex)
```

**ব্যাখ্যা:** User input নিয়ে কাজ করার সময় `ValueError` (invalid input) এবং `ZeroDivisionError` (zero input) handle করা হয়েছে।

## 7. Try-Except-Else Block

```python
## try,except,else block
try:
    num=int(input("Enter a number:"))
    result=10/num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"the result is {result}")
```

**ব্যাখ্যা:** `else` ব্লক তখনই execute হয় যখন `try` ব্লকে কোনো error হয় না। এটি successful execution এর ক্ষেত্রে result প্রিন্ট করে।

## 8. Try-Except-Else-Finally Block

```python
## try,except,else and finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"The result is {result}")
finally:
    print("Execution complete.")
```

**ব্যাখ্যা:** `finally` ব্লক সবসময় execute হয়, error হোক বা না হোক। এটি cleanup operations এর জন্য ব্যবহৃত হয়।

## 9. File Handling with Exception Handling

```python
### File handling and Exception HAndling

try:
    file=open('example1.txt','r')
    content=file.read()
    a=b
    print(content)

except FileNotFoundError:
    print("The file does not exists")
except Exception as ex:
    print(ex)

finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print('file close')
```

**ব্যাখ্যা:** File handling এর সাথে exception handling এর combination। `FileNotFoundError` handle করা হয়েছে এবং `finally` ব্লকে file properly close করা হয়েছে।

## 10. Checking Local Variables

```python
if 'file' in locals():
    print(True)
```

**ব্যাখ্যা:** `locals()` function ব্যবহার করে current scope এর local variables check করা হয়।

## 11. File Status Check

```python
not file.closed()
```

**ব্যাখ্যা:** File open আছে কিনা check করার জন্য `file.closed()` method ব্যবহার করা হয়।

## Exception Handling Best Practices

1. **Specific Exceptions**: সবসময় specific exception catch করার চেষ্টা করুন
2. **Finally Block**: Resource cleanup এর জন্য finally ব্লক ব্যবহার করুন
3. **Error Messages**: Clear এবং helpful error messages দিন
4. **Logging**: Production code এ proper logging করুন
5. **Graceful Degradation**: Error হলেও program যেন gracefully handle করতে পারে

Exception handling Python programming এর একটি গুরুত্বপূর্ণ অংশ যা robust এবং user-friendly applications তৈরি করতে সাহায্য করে।
