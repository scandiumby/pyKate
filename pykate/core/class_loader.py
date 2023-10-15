import importlib


def load_class(full_path: str):
    path_parts = full_path.split(".")
    path = ".".join(path_parts[:-1])
    class_name = path_parts[-1]
    print(f"{path=}, {class_name=}")
    if isinstance(path, str) and isinstance(class_name, str):
        module = importlib.import_module(path)
        _class = getattr(module, class_name)
    else:
        raise ValueError("Invalid data for class loading")
    return _class
