#match statement is like --> switch case statement to used for multiple cases and print the results


def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not found"
        case 500:
            return "Internal Server Found"
        case _:   #this acts like other than any number from above cases
            return "Unknown status"


#if we print the function by passing the values , it will execute --> 
print(http_status(200))

print(http_status(404))

print(http_status(500))


print(http_status(402))


# Ok
# Not found
# Internal Server Found
# Unknown status