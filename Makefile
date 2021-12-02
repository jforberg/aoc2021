executables :=

# Day 1 - Numpy
executables += 1/a.py 1/b.py

# Day 2 - AWK
executables += 2/a.awk 2/b.awk

all: $(executables)

run: $(executables)
	echo; \
	echo --------------------; \
	echo; \
	for e in $(executables); do \
		name="$${e%%.*}"; \
		printf "$$name\t"; \
		"./$$e"; \
	done
