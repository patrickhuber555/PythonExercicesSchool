def mod_cross_sum(I, J):
    for i in range(I):
        for j in range(J):
            if (i + j) % 2 == 0:
                print(f"I: {i} J: {j} := Gerade!")
            else:
                print(f"I: {i} J: {j} := Ungerade!")
        print("")


def main():
    I = 5
    J = 3
    mod_cross_sum(I, J)


if __name__ == "__main__":
    main()
