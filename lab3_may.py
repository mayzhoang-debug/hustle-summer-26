# May | Lab 3 | Hustle
username = "mz.h"
print(len(username))
# predict it is 4 characters 
# comment it counted every character including the period

print(username[0])
print(username[3])
# predict it will print m and h. 
# comment it is always last index len(username) minus 1 because the first character actually starts at 0. 

print("Welcome to Loop, @" + "mz.h" + "!")
print(f"Welcome to Loop, @{"mz.h"}!")
# predict I think both will be the same
# comment I think method one is a bit easier writing 

#username[0]= "X"
# Predict I think it wil break but I don't know why it will
# comment Immutable means it can't change 

feed = ["I am a Larper", "Highschool went by fast", "Bigback activites"]
print(len(feed))
print(feed[0])
# comment I think 3 wil print out. I think "I am a larper" will print out first. 

feed.append("Playing minecraft this whole week")
#predict this index will be 4
#comment the fourth post sit at index 3 because it starts at 0

feed.pop(0)
#comment I dont understand this will ask for help later

profile = {
    "username": "mz.h",
    "followers": 225,
    "verified": False
}
print(profile["followers"])
#predict the number 225 prints i think because it looks for number 0 it cant find it and it breaks
#profile[0]
#explain dictionaries are for labled data and i think it got confused with the 0 and the amount of followers

profile["followers"] = profile["followers"] + 50
profile["bio"] = "On a sidequest"
print(profile)
print(profile.get("age"))
#predict I think it will give out a bunch of error sytanx
#explain I guess it's safer because it spits out none and my code will run still

print(f"@{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]}")
#predict it will give followers my username and my top post I think it will show highschool went by fast 
#explain we used dictionary and list 