def fill_the_box(*args):
    size = args[0] * args[1] * args[2]
    finish_index = args.index("Finish")
    boxes = sum(args[3:finish_index])
    result = size - boxes

    output = f"No more free space! You have {abs(result)} more cubes." if result < 0 else f"There is free space in the box. You could put {result} more cubes."

    return (output)


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
