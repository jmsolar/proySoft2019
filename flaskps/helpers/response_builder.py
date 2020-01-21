def build_response(data, total, page=1, request=None):
    response = {
        "status": 200,
        "data": data,
        "recordsTotal": total,
        "recordsFiltered": total,
        "page": page
    }
    return response


def error_response(code, error):
    response = {
        "status": code,
        "message": error
    }
    return response


def success_response(msg=""):
    return {
        "status": 200,
        "message": msg
    }
