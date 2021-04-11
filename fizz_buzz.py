print("Fizz & Buzz igra...")
broj = int(input("unesi broj između 1-100: "))

if broj > 1 and broj < 100:
    for x in range(broj + 1):
        if x == 0:
            pass
        elif x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        else:
            print(x)
else:
    print("koji dio ne razumiješ, pokreni ponovno program ako želiš unijeti broj između 1-100...")
