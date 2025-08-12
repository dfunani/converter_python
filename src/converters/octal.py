from enum import Enum
from typing import Any


class OctalConversions(Enum):
    DECIMAL = "decimal"
    HEXADECIMAL = "hexadecimal"
    BINARY = "binary"


class OctalConverter:
    def to(self, value: Any, convert_to: str) -> Any:
        match convert_to:
            case OctalConversions.DECIMAL.name:
                return self._to_decimal(value)
            case OctalConversions.HEXADECIMAL.name:
                return self._to_hexadecimal(value)
            case OctalConversions.BINARY.name:
                return self._to_binary(value)
            case _:
                raise ValueError("Unsupported conversion type")

    def _to_decimal(self, value: Any) -> Any:
        return int(value, 8)

    def _to_hexadecimal(self, value: Any) -> Any:
        return hex(self._to_decimal(value)).upper()

    def _to_binary(self, value: Any) -> Any:
        decimal_value = self._to_decimal(value)
        return bin(decimal_value).replace("0b", "").upper()
