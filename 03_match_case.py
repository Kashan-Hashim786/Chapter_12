def http_status(status):
    match status:
        case  200:
            return "ok"
        case 404:
            return "Not Found"
        case 500:
            return "internal Server Error"
        case _:
            return "Unknown Status"


print(http_status(200))  # ok
print(http_status(404))  # Not Found
print(http_status(500))  # internal Server Error
print(http_status(789))  # Unknown Status