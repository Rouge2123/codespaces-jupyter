# Generate a quote for shipping a package based on weight

weight = input("What is the weight of the package?")

# Ground Shipping
print("Ground Shipping Cost")
flat_charge_ground = 20
if weight <= 2:
  print(1.50 * weight + flat_charge_ground)
elif weight > 2 and weight <= 6:
  print(3.00 * weight + flat_charge_ground)
elif weight > 6 and weight <= 10:
  print(4.00 * weight + flat_charge_ground)
else:
  print(4.75 * weight + flat_charge_ground)

# Premium Ground Shipping
print("Premium Ground Shipping Cost")
premium_ground_shipping = 125.00

print(premium_ground_shipping)

# Drone Shipping
print("Drone Shipping Cost")
if weight <= 2:
  print(4.50 * weight)
elif weight > 2 and weight <= 6:
  print(9.00 * weight)
elif weight > 6 and weight <= 10:
  print(12.00 * weight)
else:
  print(14.25 * weight)