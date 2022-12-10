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
    if _directory.parent_directory:
        add_size_to_parents(_directory.parent_directory, file_size_sum)
    if _directory.child_directories:
        for child_dir in _directory.child_directories.values():
            populate_directories_with_size(child_dir)


def find_sorted_directories(_directory: Directory, output_list: list) -> list[Directory]:
    output_list.append(_directory)
    for child_dir in _directory.child_directories.items():
        find_sorted_directories(child_dir[1], output_list)
    return output_list


def delete_dir(directory_name_to_delete, _directory: Directory) -> Directory:
    if directory_name_to_delete == _directory.name:
        add_size_to_parents(_directory.parent_directory, -_directory.size)
        _directory.size = 0
    else:
        for child_dir in _directory.child_directories.items():
            delete_dir(directory_name_to_delete, child_dir[1])


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

available_storage = 70000000
needed_storage = 30000000
used_storage = base_directory.size
deletion_needed = available_storage-used_storage-needed_storage

dirs = find_sorted_directories(base_directory, [])
dirs.sort(key=lambda x: x.size)

for _dir in dirs:
    if _dir.size >= -deletion_needed:
        print(f'Dir size = {_dir.size}')

print(f'Size before delete: {base_directory.size}')
print(f'Deleting {dirs[0].size}')
delete_dir(dirs[0].name, base_directory)
print(f'Size after delete: {base_directory.size}')
