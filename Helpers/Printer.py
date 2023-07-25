class Printer:

    def __init__(self) -> None:

        self.colors = {
            "RESET": "\033[0m",
            "BLUE": "\033[1;34m",
            "CYAN": "\033[1;36m",
            "RESET": "\033[0;0m",
            "BOLD": "\033[;1m",
            "GREEN": "\033[0;32m",
            "RED": "\033[0;31m"
        }
    
    def get_colors(self, key):
        try:
            return self.colors[key]
        except:
            return self.colors["RESET"]

    def print_with_colors(self, msg, color):

        color_selected = self.get_colors(key=color)

        print("{} {} {}".format(color_selected, msg, self.colors["RESET"]))

    def print_start(self):
        print(f"{self.colors['CYAN']} {'*' * 20} RANDOM GAME {'*' * 20} {self.colors['RESET']}")