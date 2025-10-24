def list_roman_emperors(*args, **kwargs):
    successful = {}
    unsuccessful = {}

    for emperor, success in args:
        if success:
            successful[emperor] = kwargs[emperor]
        else:
            unsuccessful[emperor] = kwargs[emperor]

    successful = sorted(successful.items(), key=lambda x: (-x[1], x[0]))
    unsuccessful = sorted(unsuccessful.items(), key=lambda x: (x[1], x[0]))
    output = []
    output.append(f"Total number of emperors: {len(args)}")

    if successful:
        output.append("Successful emperors:")
        for emperor, years in successful:
            output.append(f"****{emperor}: {years}")

    if unsuccessful:
        output.append("Unsuccessful emperors:")
        for emperor, years in unsuccessful:
            output.append(f"****{emperor}: {years}")

    return "\n".join(output)


print(
    list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False),
                        ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19, ))
