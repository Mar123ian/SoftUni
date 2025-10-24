import re

destinations = [match.group(2) for match in re.finditer(r"([=\/])([A-Z][a-zA-Z][a-zA-Z]+)\1", input())]
points = len("".join(destinations))

print("Destinations: " + ", ".join(destinations) + f"\nTravel Points: {points}")
