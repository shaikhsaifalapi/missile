import os

ROOT = os.path.dirname(os.path.abspath(__file__))  # project root
IGNORE = {"node_modules", ".git", "dist", "build"}  # skip these


def walk_dir(root):
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        # filter ignored directories (in-place modification prevents descending)
        dirnames[:] = [d for d in dirnames if d not in IGNORE]

        for d in dirnames:
            results.append(os.path.join(dirpath, d))
        for f in filenames:
            if f not in IGNORE:
                results.append(os.path.join(dirpath, f))
    return results


def print_tree(files):
    print("=== PROJECT STRUCTURE ===\n")
    for f in files:
        print(f)


def print_contents(files):
    print("\n=== FILE CONTENTS ===\n")
    for file_path in files:
        if os.path.isdir(file_path):
            continue
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"my {file_path} is as \n{content}\n")
        except Exception as e:
            print(f"# Could not read {file_path}: {e}\n")


if __name__ == "__main__":
    all_paths = walk_dir(ROOT)
    print_tree(all_paths)
    print_contents(all_paths)
