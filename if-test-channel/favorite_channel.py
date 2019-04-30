#!/usr/bin/env python3
message = 'Based on your favorite channel number, we recommend '
print('What is your favorite channel number?')
channel_input = float(input())
if channel_input >= 1 and  channel_input <= 10:
    message = message + 'Basic package.'
elif channel_input >= 1 and channel_input <= 40:
    message = message + 'Standard package.'
elif channel_input >= 1 and channel_input <= 100:
    message = message + 'Premiun package.'
elif channel_input >= 101 and channel_input <= 200:
    message = message + 'HD package,'
else:
    message = message + 'Expensive extras.'
print(message)    


    
#elif connection >= 5:
 #   message = message + 'setting video to 1080p.'
#elif connection >= 2:
#    message = message + 'setting video to 720p.'
#else:
 #   message = message + 'finding another access network.'
#print(message)

