import importlib
import os
from pathlib import Path


def import_from_folder(folder):
    modules = []
    for root, dirs, file in os.walk(folder):
        for f in file:
            if f.endswith(".py"):
                path = Path(root) / f
                path_name = path.with_suffix("").as_posix().replace("/", ".")
                module_name = importlib.import_module(path_name)
                modules.append({"path_name": path.with_suffix("").as_posix(), "handler": module_name})
    return modules


