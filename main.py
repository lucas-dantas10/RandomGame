from random import randint
import time
from Helpers.Printer import Printer

def main():
    printer = Printer()
    printer.print_start()

    printer.print_with_colors("Computador Pensando em um Número...", "BOLD")
    time.sleep(2)
    printer.print_with_colors("Pronto!!!", "BOLD")
    option = 's'

    while option == 's':
        computerNumber = randint(1, 100)
        userNumber = int(input("\033[1;36mDigite um número entre 1 e 100: \033[0m"))

        if computerNumber == userNumber:
            printer.print_with_colors(f"Você acertou o número que o computador escolheu!!! foi {computerNumber}", "GREEN")
        else:
            printer.print_with_colors(f"Você Errou o número era {computerNumber}", "RED")

        option = str(input("Deseja Continuar? [\033[0;32m S\033[0m/\033[0;31mN \033[0m]: ")).lower()

    



if __name__ == '__main__':
    main()