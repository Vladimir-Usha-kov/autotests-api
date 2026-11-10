import logging

def get_logger(name: str):
    loger = logging.getLogger(name)
    loger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    loger.addHandler(handler)

    return loger


