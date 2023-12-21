from pathlib import Path
import sys

IGNORE_PODS = [
    "global/main",
    "usw2/analytics",
    "cac1/s-cac1-jitsi1",
    "cac1/s-cac1-rudder1",
    "apse/apse2-rudder4",
    "apse/apse2-j4",
    "cac1/cac1-j1",
    "cac1/cac1-j5",
    "cac1/cac1-rudder1",
    "euw2/euw2-j3",
    "euw2/euw2-rudder3",
    "usw2/usw2-j2",
    "usw2/usw2-rudder2",
]


def get_all_module_paths(root_dir):
    parent_dir = Path(root_dir)
    all_pods = []

    for first_level in parent_dir.iterdir():
        if first_level.is_dir():
            for second_level in first_level.iterdir():
                rel_path = str(second_level.relative_to(parent_dir))
                if second_level.is_dir() and (rel_path not in IGNORE_PODS):
                    all_pods.append(rel_path)
    return sorted(all_pods)


if __name__ == "__main__":
    print(get_all_module_paths(sys.argv[1]))
