homework_minutes = int(input("Homework time in minutes: "))

if homework_minutes >= 60:
    print("That is a long homework session.")
else:
    print("That is a short homework session.")

free_time = input("Is there free time after homework? (yes/no): ").strip().lower()

if free_time == "yes":
    print("Reminder: pick a hobby for your free time!")

print("===== DAILY PLAN =====")
print("Homework minutes:", homework_minutes)

if homework_minutes >= 60:
    print("Plan: start homework now")
else:
    print("Plan: finish homework quickly")

print("Free time:", free_time)