fruit = "pomme"
match fruit:
    case "pomme":
        print("j'aime les pommes")
    case "poire":
        print("J'aime les poires")
    case "banane":
        print("j'aime les bananes")
    case _:
        print("Je ne connais pas ce fruit")
