# Constants 
SECONDS_IN_A_MINUTE = 60
SECONDS_IN_A_HOUR = 3600
SECONDS_IN_A_DAY = 86400

# Prompt
total_seconds = int(input("Enter the number of seconds: "))

# Calculations
days = total_seconds // SECONDS_IN_A_DAY # 17 // 3 = 5
remaining_seconds = total_seconds % SECONDS_IN_A_DAY

hours = remaining_seconds // SECONDS_IN_A_HOUR
remaining_seconds %= SECONDS_IN_A_HOUR

minutes = remaining_seconds // SECONDS_IN_A_MINUTE
remaining_seconds %= SECONDS_IN_A_MINUTE

seconds = remaining_seconds

print(f"{total_seconds} seconds is equals to")
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

#Enter the number of seconds: 105310
#105310 seconds is equals to
#1 days, 5 hours, 15 minutes, 10 seconds