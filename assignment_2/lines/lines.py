import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few/Too many command-line arguments")
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r") as f:
            count = 0
            for line in f:
                stripped = line.lstrip()
                # se, depois de remover espaços à esquerda, a linha começa por '#', ignorar
                if stripped.startswith("#"):
                    continue
                # se, sem espaços e quebras de linha, a linha está vazia, ignorar
                if stripped.strip() == "":
                    continue
                # caso contrário, é uma linha de código
                count += 1
            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()