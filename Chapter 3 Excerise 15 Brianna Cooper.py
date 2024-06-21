# Get a number of seconds from the user
total_seconds = int(input("Enter the number of seconds: "))

#Get the number of days
days = total_seconds // 86400
remaining_seconds = total_seconds % 86400

#Get the number of hours
hours = remaining_seconds // 3600
remaining_seconds = remaining_seconds % 3600

#Get the number of minutes
minutes = remaining_seconds // 60

#Get the number of seconds
seconds = remaining_seconds % 60

if total_seconds < 60:
        print('Seconds', seconds)
elif total_seconds >= 60 and total_seconds < 3600:
        print('Minutes', minutes)
        print('Seconds', seconds)
elif total_seconds >= 3600 and total_seconds < 86400:
        print('Hours', hours)
        print('Minutes', minutes)
        print('Seconds', seconds)
else:
        print('Days', days)
        print('Hours', hours)
        print('Minutes', minutes)
        print('Seconds',seconds)
