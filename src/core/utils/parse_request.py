from flask import Request


def parse_request(request: Request) -> dict[str, str]:
    try:
        return request.get_json(force=True)
    except Exception:
        return request.form
