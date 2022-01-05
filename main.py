from typing import Union
import math, logging

logger = logging.getLogger("LOGGER")
file_handler = logging.FileHandler("dvidesimtos_uzduoties_logai.log", encoding="UTF-8")
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.info("LOG")

def get_amount(*args: Union[int, float]) -> Union[int, float]:
    numbers = [*args]
    amount = sum(numbers)
    logger.info(f"Skaičių {args} suma yra lygi: {amount}")
    return amount


def get_root_from_number(number: Union[int, float]) -> Union[int, float]:
    try:
        root = math.sqrt(number)
    except TypeError as e:
        logger.exception(f"KLAIDA: vartotojo įvestis nėra skaičius, įvesta: {number}")
    else:
        logger.info(f"Skaičiaus {number} šaknis yra: {root}")
        return root

def get_sentence_length(sentence: str) -> Union[int, float]:
    sentence_length = len(sentence)
    logger.info(f"Sakinį sudaro {sentence_length} simboliai")
    return sentence_length

def division(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    try:
        quotient = a / b
    except ZeroDivisionError as e:
        logger.exception(f"KLAIDA: vartotojas bandė {a} dalinti iš 0")
    else:
        logger.info(f"Skaičių {a} padalinus iš skaičiaus {b} dalmuo yra: {quotient}")
        return quotient

if __name__ == '__main__':
    get_amount(15, 10, 6, 89)
    get_root_from_number("81")
    get_sentence_length("cia yra net 24 simboliai")
    division(72, 0)

