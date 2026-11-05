"""Week 1: Ask for personal details and print an introduction."""

name = input("Enter your name: ").strip()
age = input("Enter your age: ").strip()
city = input("Enter your city: ").strip()
course = input("Enter your course: ").strip()
hobby = input("Enter your hobby: ").strip()

print("\n--- My Introduction ---")
print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")
print(f"I am studying {course}.")
print(f"My hobby is {hobby}.")
