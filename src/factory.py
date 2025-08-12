from enum import Enum
import re

from converters.binary import BinaryConversions, BinaryConverter
from converters.decimal import DecimalConversions, DecimalConverter
from converters.hexadecimal import HexadecimalConversions, HexadecimalConverter
from converters.octal import OctalConversions, OctalConverter


class Converters(Enum):
    BINARY = re.compile(r"^[01]+$"), BinaryConversions
    DECIMAL = re.compile(r"^\d+$"), DecimalConversions
    HEXADECIMAL = re.compile(r"^[0-9A-Fa-f]+$"), HexadecimalConversions
    OCTAL = re.compile(r"^[0-7]+$"), OctalConversions

class ConverterFactory:
    @staticmethod
    def get_converter(converter_type: str):
        print(converter_type)
        match converter_type:
            case "BINARY":
                return BinaryConverter()
            case "DECIMAL":
                return DecimalConverter()
            case "HEXADECIMAL":
                return HexadecimalConverter()
            case "OCTAL":
                return OctalConverter()
            case _:
                raise ValueError("Unknown converter type")