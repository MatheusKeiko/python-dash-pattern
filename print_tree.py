import os


def tree(root="."):
    for dirpath, dirnames, filenames in os.walk(root):
        # ignore virtualenvs/ocultos comuns (ajuste se precisar)
        parts = dirpath.split(os.sep)
        if any(
            p
            in {
                ".git",
                ".venv",
                "_lixeira",
                "venv",
                "__pycache__",
                ".mypy_cache",
            }
            for p in parts
        ):
            continue
        indent = "│  " * (dirpath.count(os.sep))
        print(f"{indent}├─ {os.path.basename(dirpath) or dirpath}")
        for f in sorted(filenames):
            print(f"{indent}│  └─ {f}")


if __name__ == "__main__":
    tree(".")
