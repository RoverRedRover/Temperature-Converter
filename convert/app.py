#!/bin/python3

import sys, enum, rich, command_line, temp


class ConversionType(enum.Enum):
    FAHR_TO_CELS = 1
    CELS_TO_FAHR = 2


class App:
    def __init__(self) -> None:
        self.user_input = command_line.arguments()  # type = argparse.Namespace
        self.run()

    def _process_input(self):
        """Choose and perform the conversion calculation that is appropriate
        for the subcommand the user entered on the command line:
            - 'f' (i.e., convert from Fahrenheit to Celsius), or
            - 'c' (i.e., convert from Celsius to Fahrenheit).
        """
        if hasattr(self.user_input, "ftemp"):
            self.flag = ConversionType.FAHR_TO_CELS
            self.result = temp.Converter.fahr_to_cels(self.user_input.ftemp)
        elif hasattr(self.user_input, "ctemp"):
            self.flag = ConversionType.CELS_TO_FAHR
            self.result = temp.Converter.cels_to_fahr(self.user_input.ctemp)
        else:
            rich.print(
                "[red bold]Error:[/] Please enter 'f <n>' at the command line "
                "to convert a temperature from Fahrenheit to Celsius, or "
                "'c <n>' to convert from Celsius to Fahrenheit."
            )
            sys.exit()

    def _print_output(self):
        degree = "\N{DEGREE SIGN}"
        if self.flag == ConversionType.FAHR_TO_CELS:
            rich.print(
                f"{self.user_input.ftemp}{degree}[italic]f[/] = {self.result:.2f}{degree}[italic]c[/]"
            )
        elif self.flag == ConversionType.CELS_TO_FAHR:
            rich.print(
                f"{self.user_input.ctemp}{degree}[italic]c[/] = {self.result:.2f}{degree}[italic]f[/]"
            )
        else:
            raise AttributeError("I... don't know what I'm doing... I'm sorry...")

    def run(self):
        self._process_input()
        self._print_output()
        print()
