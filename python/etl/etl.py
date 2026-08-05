def transform(legacy_data):

    letter_point_pairs = [(letter.lower(), point)for point, letters in legacy_data.items() for letter in letters]

    return dict(sorted(letter_point_pairs))