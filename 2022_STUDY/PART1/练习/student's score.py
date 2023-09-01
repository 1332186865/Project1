def get_score():
    s = input("input grade:")
    try:
        i = int(s)
    except ValueError as err:
        print(err)
        return 0

    if 0 <= i <= 100:
        return i
    return 0


score = get_score()
print("student's grade:", score)
