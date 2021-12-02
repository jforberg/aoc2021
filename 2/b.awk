#!/usr/bin/gawk -f

BEGIN {
    sprintf("dirname %s", (ENVIRON["_"])) | getline dir
    ARGV[1] = sprintf("%s/input.txt", dir)
    ARGC = 2
}

$1 == "forward" {
    horiz += $2
    depth += aim * $2
}

$1 == "down" {
    aim += $2
}

$1 == "up" {
    aim -= $2
}

END {
    print horiz * depth
}
