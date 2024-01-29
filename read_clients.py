def main():
    infile = open('clients.txt', 'r')

    rank = 0

    for line in infile:
        rank += 1
        print(f"{rank}) {line}")

    infile.close()

main()