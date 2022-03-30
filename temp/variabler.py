
# fuction that cecks variable type
def variable_type(variable):
    if isinstance(variable, int):
        return "int"
    elif isinstance(variable, float):
        return "float"
    elif isinstance(variable, str):
        return "string"
    else:
        return "unknown"
