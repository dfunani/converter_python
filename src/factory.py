from enum import Enum
import re

from converters.binary import BinaryConversions, BinaryConverter


class Converters(Enum):
    BINARY = re.compile(r"^[01]+$"), BinaryConversions
    DECIMAL = re.compile(r"^\d+$"), BinaryConversions
    HEXADECIMAL = re.compile(r"^[0-9A-Fa-f]+$"), BinaryConversions
    OCTAL = re.compile(r"^[0-7]+$"), BinaryConversions

class ConverterFactory:
    @staticmethod
    def get_converter(converter_type: str):
        if converter_type == Converters.BINARY.name:
            return BinaryConverter()
        raise ValueError("Unknown converter type")