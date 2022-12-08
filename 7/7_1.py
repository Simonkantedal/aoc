from __future__ import annotations


import csv
from dataclasses import dataclass


@dataclass
class File:
    size: int
    name: str


@dataclass
class Directory:
    name: str
    child_directories: dict[str:Directory]
    parent_directory: Directory | None
    files: list[File]
    size: int


def add_size_to_parents(_directory: Directory, size: int):
    _directory.size += size
    if _directory.parent_directory:
        add_size_to_parents(_directory.parent_directory, size)


def populate_directories_with_size(_directory: Directory):
    file_size_sum = 0
    for _file in _directory.files:
        file_size_sum += _file.size
    _directory.size += file_size_sum
    if _directory.child_directories:
        for child_dir in _directory.child_directories.values():
            populate_directories_with_size(child_dir)
    else:
        add_size_to_parents(_directory.parent_directory, file_size_sum)


def find_small_directories(_directory: Directory, small_directories: list):
    if _directory.size <= 100000:
        print(f'{_directory.name}: {_directory.size}')
        small_directories.append(_directory.size)
    for child_dir in _directory.child_directories.values():
        find_small_directories(child_dir, small_directories)

    return small_directories


def traverse_tree(_directory: Directory, size_sum: int, small_dir_sum: int):
    file_size_sum = 0
    for _file in _directory.files:
        file_size_sum += _file.size
    if _directory.child_directories:
        for child_dir in _directory.child_directories.values():
            size_sum += file_size_sum
            traverse_tree(child_dir, size_sum + file_size_sum, small_dir_sum)
        if size_sum <= 100000:
            small_dir_sum += size_sum
        print(f"Size of {_directory.name}: {size_sum}")
    else:
        return
    print(f"Small dir sum = {small_dir_sum}")


base_directory = Directory("/", {}, None, [], 0)
current_directory = base_directory
last_directory = base_directory
num_cds = 0
with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        inputs = row[0].split(" ")
        if inputs[0] == "$":
            if inputs[1] == "cd":
                num_cds += 1
                if inputs[2] == "..":
                    current_directory = current_directory.parent_directory
                else:
                    last_directory = current_directory
                    current_directory = current_directory.child_directories[inputs[2]]
                    current_directory.parent_directory = last_directory
            elif inputs[1] == "ls":
                pass

        elif inputs[0].isdigit():
            file = File(size=int(inputs[0]), name=inputs[1])
            current_directory.files.append(file)
        elif inputs[0] == "dir":
            directory = Directory(
                name=inputs[1],
                child_directories={},
                parent_directory=current_directory,
                files=[],
                size=0,
            )
            current_directory.child_directories[directory.name] = directory

populate_directories_with_size(base_directory)

small_directories = find_small_directories(base_directory, [])

print(sum(small_directories))
