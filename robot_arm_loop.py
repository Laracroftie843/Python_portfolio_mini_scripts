# Define Leg Movement
Leg = 0
kneel = 45
stand = 180
point = 225

# Simulates a robot arm repeating a movement

for i in range(5):
  print(f"Cycle {i + 1}:")
  print("Arm moving to pickup position")
  print("Grabbing object")
  print("Arm moving to placement position")
  print("Releasing object")
  print("Returning to idle position)


# While loop version
print("Starting while loop simulation...\n")
while Leg <= point:
    print(f"Leg position: {Leg}")
    
    if Leg == 0:
        print("Arm in idle position")
        Leg = kneel  # Move to kneeling next
    
    elif Leg == kneel:
        print("Arm moving to kneeling position")
        Leg = stand  # Move to standing next

    elif Leg == stand:
        print("Leg is moving to standing position")
        Leg = point  # Move to pointing next

    elif Leg == point:
        print("Leg is in pointing position")
        Leg = point + 1  # End the loop
    
    else:
        print("Leg offline")
        break  # safety exit
