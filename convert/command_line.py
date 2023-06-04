#!/bin/python3

import argparse


def arguments() -> argparse.Namespace:
    """Get command-line arguments and return argparse.Namespace object"""

    parser = argparse.ArgumentParser(
        prog="Temperature Converter",
        description="Convert from Fahrenheit to Celsius or vice-versa.",
    )
    subparsers = parser.add_subparsers()

    subcommand_ftoc = subparsers.add_parser("f", help="Convert Fahrenheit to Celsius")
    subcommand_ftoc.add_argument(
        "ftemp", help="Temperature in Fahrenheit degrees", type=float
    )
    subcommand_ctof = subparsers.add_parser("c", help="Convert Celsius to Fahrenheit")
    subcommand_ctof.add_argument(
        "ctemp", help="Temperature in Celsius degrees", type=float
    )

    return parser.parse_args()
