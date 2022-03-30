def check_instance(obj, cls):
    return check_subclasses(type(obj), cls)


def check_subclasses(child, base):
    if child == base:
        return True
    for direct_base in child.__bases__:
        if base == direct_base:
            return True
        return check_subclasses(direct_base, base)


print(check_subclasses(bool, str))
print(check_instance(bool, str))
