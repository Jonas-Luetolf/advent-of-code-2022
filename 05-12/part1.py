import helper

data = helper.read_inp("input.txt", sep="""\n\n""")

# format field
inp_field, steps = data[0], data[1]
inp_field = inp_field.split("\n")[:-1]

field = []
for x in range(0, len(inp_field[0]), 4):
    field.append(
        list(
            [
                inp_field[y][x : x + 3]
                for y in range(0, len(inp_field))
                if inp_field[y][x : x + 3] != "   "
            ]
        )
    )

# format steps
steps = steps.replace("move", "").replace("from", "").replace("to", "").split("\n")
steps = [i.split(" ") for i in steps]
steps = list(
    map(lambda step: list(map(int, list(filter(lambda i: i != "", step)))), steps)
)

# move cartes
for i in steps:
    to_move = field[i[1] - 1][: i[0]]
    field[i[2] - 1] = list(reversed(to_move)) + field[i[2] - 1]
    field[i[1] - 1] = (field[i[1] - 1])[i[0] :]

# print top cartes
for i in field:
    print(i[0])
