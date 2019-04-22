def cost_of_ground_shipping(weight):
  if weight <= 2:
    cost = (1.50 * weight) + 20
  elif weight > 2 and weight <= 6:
    cost = (3.00 * weight) + 20
  elif weight > 6 and weight <= 10:
    cost = (4.00 * weight) + 20
  elif weight > 10:
    cost = (4.75 * weight) + 20
  return cost

print(cost_of_ground_shipping(8.4))

premium_ground_shipping = 125.00

def cost_of_drone_shipping(weight):
  if weight <= 2:
    cost = (4.50 * weight)
  elif weight > 2 and weight <= 6:
    cost = (9.00 * weight)
  elif weight > 6 and weight <= 10:
    cost = (12.00 * weight)
  elif weight > 10:
    cost = (14.25 * weight)
  return cost

print(cost_of_drone_shipping(1.5))


def best_shipping(weight):
    if cost_of_ground_shipping(weight) < cost_of_drone_shipping(weight) and cost_of_ground_shipping(weight) < premium_ground_shipping:
        print("Ground Shipping is the cheapest and will cost " + str(cost_of_ground_shipping(weight)))
        
    elif cost_of_drone_shipping(weight) < cost_of_ground_shipping(weight) and cost_of_drone_shipping(weight) < premium_ground_shipping:
        print("Drone Shipping is the cheapest and will cost " + str(cost_of_drone_shipping(weight)))
        
    elif premium_ground_shipping < cost_of_drone_shipping(weight) and cost_of_ground_shipping(weight) > premium_ground_shipping:
        print("Premium Shipping is the cheapest and will cost " + str(premium_ground_shipping))
        
print(best_shipping(1))
print(best_shipping(2))
print(best_shipping(3))
print(best_shipping(4))
print(best_shipping(5))
print(best_shipping(10))
print(best_shipping(50))
print(best_shipping(100))
print(best_shipping(500))
