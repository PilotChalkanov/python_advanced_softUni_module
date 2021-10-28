def age_assignment(*args, **kwargs):
    dict ={}
    for name in args:
        first_letter = name[0]
        dict[name] = kwargs[first_letter]
    return dict


print(age_assignment("Peter", "George", G=26, P=19))