#!/bin/python3

class Converter:

    @staticmethod
    def cels_to_fahr(cels: float) -> float:
        return cels * 9/5 + 32

    @staticmethod
    def fahr_to_cels(fahr: float) -> float:
        return 5/9 * (fahr - 32)
