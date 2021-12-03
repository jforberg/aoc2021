#!/usr/bin/gawk -f

$1 == "forward" {
    horiz += $2
}

$1 == "down" {
    depth += $2
}

$1 == "up" {
    depth -= $2
}

END {
    print horiz * depth
}
