def http_status(status: int) -> str:
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
        
print(http_status(200))      # Output -> OK
# print(http_status(404))    # Output -> Not Found
# print(http_status(500))    # Output -> Internal Server Error
# print(http_status(69))     # Output -> Unknown Status