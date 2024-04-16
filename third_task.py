import re


def normalize_phone(phone_number: str) -> str:
    '''
    Delete redundant symbols from the phone number and extend the last one with
    the country code if needed.

    :param phone_number: string

    :return: string
    '''
    phone_number = re.sub(r'[^+\d]', '', phone_number)
    return '+38'[:13 - len(phone_number)] + phone_number
