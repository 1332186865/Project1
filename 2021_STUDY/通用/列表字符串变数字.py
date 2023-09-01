def convert_to_int(lists):
    return [int(i) if not isinstance(i, list) else convert_to_int(i) for i in lists]
