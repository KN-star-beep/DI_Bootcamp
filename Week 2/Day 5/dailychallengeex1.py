1. What is a class?

A class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that the objects created from it will have.

👉 Example: A Car class can define properties like color and speed.

✅ 2. What is an instance?

An instance is a specific object created from a class.

👉 Example:
If Car is a class, then my_car = Car() is an instance of that class.

✅ 3. What is encapsulation?

Encapsulation is the concept of bundling data and methods together and restricting direct access to some of the object's components.

👉 It helps protect data using private/protected attributes.

✅ 4. What is abstraction?

Abstraction means hiding complex implementation details and showing only the essential features.

👉 Example: You drive a car without knowing how the engine works.

✅ 5. What is inheritance?

Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

👉 Example:
A Dog class can inherit from an Animal class.

✅ 6. What is multiple inheritance?

Multiple inheritance is when a class inherits from more than one parent class.

👉 Example:

class A:
    pass

class B:
    pass

class C(A, B):
    pass
✅ 7. What is polymorphism?

Polymorphism means "many forms" — it allows the same method to behave differently in different classes.

👉 Example:
Different classes can have a make_sound() method, but each produces a different sound.

✅ 8. What is Method Resolution Order (MRO)?

MRO is the order in which Python looks for methods and attributes in a class hierarchy, especially in multiple inheritance.

👉 Python follows a specific order (C3 linearization) to determine which method to use.

👉 You can view it using:

ClassName.__mro__

If you want, I can give you:

real-world examples for each concept
or a quick summary table to memorize faster 📚