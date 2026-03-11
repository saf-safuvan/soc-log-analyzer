log_file = input("Enter log file path: ")

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:
    if "failed" in line.lower():
        print("Suspicious login detected:", line)
