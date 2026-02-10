tea_values = ("green tea", "black tea", "masala chai")
print(tea_values)

print(tea_values[0])
print(tea_values[-1])
print(tea_values[0:2])
print(len(tea_values))

more_tea = ("ginger tea", "harbel tea")
print(more_tea)

all_tea = tea_values + more_tea
print(tea_values + more_tea)

if "green" in all_tea:
    print("i have green tea")

print(more_tea.count("herbal"))
