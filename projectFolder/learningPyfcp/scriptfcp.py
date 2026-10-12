# food_total = 100
# drink_total = 40
# meal_total = food_total + drink_total
# print(meal_total)

morning = "food"
afternoon = "nap"
night = "sleep"

plan_for_the_day = "my plan for today is: " + \
    morning + ", " + afternoon + ", and " + night

# print(plan_for_the_day)

first_name = "Tobi"
evnt = "birthday"
number = 10
noun = "cake"
verb = "eat"

excuse = f"I can't come to your  {evnt} because I have to {verb} {number} {noun} for {first_name}'s {evnt}."

# print(excuse)
event_name = "Molabat"
cost = int(input("Enter the cost of the event: "))
service_charge = cost * 0.1
group_size = int(input("Enter the number of people in the group: "))
grand_total = cost + service_charge
total_per_person = round(grand_total / group_size, 2)

Output = f"Welcome to Payup! \n \n Here is the breakdowm for dinner at {event_name}: \n \n Cost of the event: {cost} \n \n Service charge: {service_charge} \n \n Grand total: {grand_total} \n \n Total per person: {total_per_person}"

print(Output)
