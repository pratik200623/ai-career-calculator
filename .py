# ai career salery calculator 
 
print("welcome to ai carear calculator")

#step 1
skill = int(input("enter your skill level (1= biginner , 2 = intermedit , 3 = advance):"))

hours_per_day = int(input("how many hours do you study daily"))

#calculates

target_salery = 20000000 #2 cr
avg_salery_by_level = [400000,800000,1500000] #yearly estimate 

#step2:estimate years needee

current_estimated_salery = avg_salery_by_level[skill - 1]
growth_rate = 1 + (hours_per_day/10)  #learning speed factor


year_needed = 0 

salery = current_estimated_salery 

progress =(salery / target_salery)*100


while salery < target_salery:
    salery*= growth_rate
    year_needed += 1
    progress = (salery / target_salery)*100

#step 3 : weekly plain 
weekly_hours = hours_per_day * 7

topics = ["pythan","dsa ","project","github + linkedin ","elglish","logic","mini progect"]

daily_topic = topics[year_needed  % len(topics)]
#step 4:output

print(f"\n Estimeted time to reach 2 cr/year :{year_needed} years")

print(f"you started salery estimated: {current_estimated_salery}")

print  (f"progress towords gole {round(progress,2)} %")

print(f"\n weekly learning plain : ")

print(f" - total weekly studey : {weekly_hours} hours")

print(f"focuse more on : {daily_topic} this week")
