available_topping = ['mushrooms','olives','peppers','pineapple']
requested_toppings = ['bacon']
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_topping:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry we don't have {requested_topping}.")
    print("\nFinishing making your pizza!")
else:
    print("Are you sure you want a plain pizza")