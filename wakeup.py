start = '''
You've a rough night and you're in deep sleep.
Your alarm goes off at 7am.
Do you either snooze or get up?'''


print(start)


print("Type 'snooze' to snooze or 'get up' to go get up.")
user_input = input()
if user_input == "snooze":
    print("You decide to snooze and accidently falls asleep for an hour...")
print("The alarm goes off again. Do you keep on sleeping or get up now and get ready?")
 print("Type 'get up now' and get ready or 'keep sleeping' to continue to dream on.")
user_input = input()
if user_input == "get up now":
    print("You are currently getting ready and will be running late.")
    exit()
elif user_input == "keep sleeping":
    print("Missed the whole day and never arrived.. you also got fired.")
    exit()

elif user_input == "get up":
    print("You choose to get up and get ready for the day...") # finished the story writing what happens
    print("You leave house early")
    print("Type 'eat' to stop by 7/11 or 'take bus' to arrive early and not eat")
user_input = input()
if user_input == "eat":
    print("You have decided to go to the nearest 7/11 and get yourself some coffee :D... and arrived perfectly on time via bus.")
    exit() # finished the story by writing what happens
elif user_input == "take bus":
    print("You have decided to wait for the nearest bus and arrive to your destination early...")
    exit()
# finished the story by writing what happens
    print("The alarm goes off again. Do you keep on sleeping or get up now and get ready?")
    print("Type 'get up now' and get ready or 'keep sleeping' to continue to dream on.")
user_input = input()
if user_input == "get up now":
    print("You are currently getting ready and will be running late.")
    exit()
elif user_input == "keep sleeping":
    print("Missed the whole day and never arrived.. you also got fired.")
    exit()
elif user_input == "get up":
    print("You choose to get up and get ready for the day...") # finished the story writing what happens
    print("You leave house early")

user_input = input()
if user_input == "eat":
    print("You have decided to go to the nearest 7/11 and get yourself some coffee :D... and arrived perfectly on time via bus.")
    exit() # finished the story by writing what happens
elif user_input == "take bus":
    print("You have decided to wait for the nearest bus and arrive to your destination early...")
    exit()
