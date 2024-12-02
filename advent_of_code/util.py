#!/usr/bin/env python

def read_input(filepath):
    with open(filepath, "r") as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped