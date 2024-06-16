import random

test_descriptions = {
    "Performance": [
        "Check temperature of room", 
        "Response time",
        "User navigation", 
        "standalone component check",
        "Fluid levels",
        "Component wear testing",
        "Burn-in timing",
        "Knob and dial sensitivity",
        "Crash test",
    ],
    "Functional": [
        "Check for gas leakage",
        "Delays at specific components",
        "Pipe fit test",
        "Electronics cosmic ray robustness",
        "Diode current capacity",
        "Rain check",
        "Fuzz testing",
        "Regression test",
        "Weight check",
        ],
    "System": [
        "End to end flow to check all components",
        "New components integration",
        "End to end integration",
        "Lifecycle use test",
        "User walkthrough",
        "Animal testing",
        ],
}

def generate_result():
    test_type = random.choice(["Performance", "Functional", "System"]) 
    result = random.choice(["PASS", "FAIL"])
    description = random.choice(test_descriptions[test_type]) 
    return f"Test Type: {test_type} Result: {result} Description: {description}"


k = random.randint(3, 100)
count = random.randint(5, k * k)
for i in range(count):
    print(generate_result())

