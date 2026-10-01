# ==========================================
# DAY 19 - CUSTOM DATA STRUCTURES
# Min Stack
# ==========================================

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            print("Stack is empty!")
            return None

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def get_min(self):
        if not self.min_stack:
            return None

        return self.min_stack[-1]


# Create Min Stack
min_stack = MinStack()

# Test values
temperatures = [32, 28, 35, 25, 30, 22]

print("======================================")
print("          TEMPERATURE MIN STACK")
print("======================================")

print("\nPushing temperatures:")

for temperature in temperatures:
    min_stack.push(temperature)
    print(
        f"Pushed: {temperature}°C | "
        f"Minimum: {min_stack.get_min()}°C"
    )

print("\nCurrent Minimum:", min_stack.get_min(), "°C")

print("\nPopping:", min_stack.pop(), "°C")
print("Minimum after pop:", min_stack.get_min(), "°C")

print("\nPopping:", min_stack.pop(), "°C")
print("Minimum after pop:", min_stack.get_min(), "°C")