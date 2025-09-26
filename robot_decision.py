import logging

#Configure Logging
logging.basicConfig(
  filename='decision_log.txt',
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s'
)

def decide_movement(obstacle_front, obstacle_left, obstacle_right, obstacle_back):
  # Fully Surrounded
  if obstacle_front and obstacle_left and obstacle_right and obstacle_back:
    logging.error("Robot is surrounded")
    return "Blocked"

  # All sides blocked except for the back
  elif obstacle_front and obstacle_left and obstacle_right and not obstacle_back:
    logging.warning("All sides blocked except for behind")
    return "Backup"

  # Obstacle ahead and left
  elif obstacle_front and obstacle_left and not obstacle_right and not obstacle_back:
    logging.info("Obstacle ahead and left")
    return "Turn Right"

  # Obstacle ahead and right
  elif obstacle_front and not obstacle_left and obstacle_right and not obstacle_back:
    logging.ingo("Obstacle ahead and right")
    return "Turn Left"

  #Obstacle ahead but both sides are open
  elif obstacle_front and not obstacle_left and not obstacle_right:
    logging.ingo("Obstacle ahead, sides are open")
    return "Turn Left"

  # No obstacle in front - move forward
  elif not obstacle_front:
    logging.info("Path ahead is clear")
    return "Move Forward"

  #Default fallback case
  else:
    logging.warning("Unexpected sensor config. Stopping.")
    return "Stop"


# Testing Scenarios
if __name__ == "__main__":
  print("Scenario 1")
  print(decide_movement(True, False, True, False)) # turns left

  print("Scenario 2")
  print(decide_movement(False, False, False, False)) # moves forward

  print("Scenario 3")
  print(decide_movement(True, True, True, True)) # Fully blocked

  print("Scenario 4")
  print(decide_movement(True, True, True, False) # Backup

  print("Scenario 5")
  print(decide_movement(True, True, False, True)) # turns right
  
