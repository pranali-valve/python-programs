




tests = ["pass", "pass", "pass", "fail", "pass"]

for test in tests:
    if test == "fail":
        print("Failed test found")
        break