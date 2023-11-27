from uuid import uuid4


def generate_revision() -> str:
    return str(uuid4())[-12:]
