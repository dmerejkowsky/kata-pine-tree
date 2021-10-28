width = 9


def display_triangle():
    display_line(5, 6)
    display_line(4, 7)


def display_leg():
    display_line(5, 6)
    display_line(5, 6)


def display_line(start, end):
    print(" " * start, end="")
    print("#" * (end - start))


def display_tree():
    display_triangle()
    display_leg()


display_tree()
