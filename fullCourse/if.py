is_male = True
is_tall = False

if is_male or is_tall:
    print("You're a male or tall or both.")
else:
    print("You're neither male or tall.")

if is_male and is_tall:
    print("You're a male or tall or both.")
elif is_male and not(is_tall):
    print("You're a short male")
elif not(is_male) and is_tall:
    print("You're not male but are tall")
else:
    print("You're neither male or tall.")