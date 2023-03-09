def read_inp(filename, dtype=str, sep="\n"):
    with open(filename, "r") as f:
        inp = f.read().strip().split(sep)
    return list(map(dtype, inp))


def binary_search(item, sorted_list):
    lower = 0
    upper = len(sorted_list)
    middel = int(lower + upper // 2)

    if sorted_list[middel] == item:
        return middel
    elif item < sorted_list[middel] and item >= sorted_list[lower]:
        return binary_search(item, sorted_list[lower:middel])
    elif item > sorted_list[middel] and item <= sorted_list[upper - 1]:
        return binary_search(item, sorted_list[middel + 1 : upper]) + middel + 1
    else:
        raise ValueError(f"{item} not in list")


def seperate_by_k(l, k=0):
    if k not in l:
        l.append(k)
    l.sort()
    l_lower = l[: binary_search(k, l)]
    l_upper = l[binary_search(k, l) + 1 :]
    return l_lower, l_upper
