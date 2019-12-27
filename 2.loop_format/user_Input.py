def weather_condition(temp):
    if temp > 18:
        return "warm"
    else:
        return "cold"

user_input = input("Enter temperture:")
print(weather_condition(user_input))
print(type(user_input))