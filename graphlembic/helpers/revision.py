from uuid import uuid4


def get_revision() -> str:
    return str(uuid4())[-12:]
