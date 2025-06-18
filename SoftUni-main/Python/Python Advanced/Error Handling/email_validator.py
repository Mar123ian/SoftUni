import re


class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    command = input()
    if command == "End":
        break
    pattern = r"([a-z]+)@[a-z]+(\.[a-z]+)"
    matches = re.search(pattern, command)
    if not "@" in command:
        raise MustContainAtSymbolError("Email must contain @")
    name, domain = matches.groups()
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if domain not in [".com", ".bg", ".org", ".net"]:
        raise InvalidDomainError(
            "Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")
