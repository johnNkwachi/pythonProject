def fizzbuzz(num):
    three = num % 3
    five = num % 5
    match (three, five):
        case (0, 0):
            return "FIZZBUZZ"

        case (0, _):
            return "FIZZ"

        case (_, 0):
            return  "BUZZ"

        case _:
            return num