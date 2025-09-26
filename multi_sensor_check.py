import logging

# Configures Logging to write to sensor_log.txt
Logging.basicConfig(
  filename="sensor_log.txt',
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_multiple_sensors(sensor_data, threshold = 75):
  results = {}

for sensor_name, reading in sensor_data.items():
  try:
    value = float(reading)

    if value > threshold:
      logging.warning(f"[{sensor_name}] {value} exceeds threshold of {threshold}.")
      results[sensor_name} = "Alert"
    else:
      logging.infor(f"[{sensor_name}] {value} is within safe range.")
      results[sensor_name} = "OK"

except (ValueError, TypeError):
  logging.error(f"[{sensor_name}] Invalid reading '{reading}' must be a number.")
  results[sensor_name] = "Error"
return results

# Sensor name and usage examples
if __name__ == "__main__":
  sensor_inputs = {
    "temp_sensor": 80,
    "object_sensor": 65,
    "infrared_sensor": "hot",
    "pressure_sensor": None
  }

  results = check_multiple_sensors(sensor_inputs)
  print("Sensor Check Results:", results)
  
