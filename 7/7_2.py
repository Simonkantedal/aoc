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


def find_all_directories(_directory: Directory, directories: list):
    directories.append(_directory.size)
    for child_dir in _directory.child_directories.values():
        find_all_directories(child_dir, directories)
    return directories


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

directories = find_all_directories(base_directory, [])

sum_of_directories = sum(directories)

print(f'Sum of all directories = {sum(directories)}')