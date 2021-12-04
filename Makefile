executables :=

# Day 1 - Numpy
executables += 1/a.py 1/b.py

# Day 2 - AWK
executables += 2/a.awk 2/b.awk

# Day 3 - Numpy
executables += 3/a.py 3/b.py

# Day 4 - Numpy
executables += 4/a.py 4/b.py

.PHONY: all
all: $(executables)

.PHONY: run
run: $(executables)
	echo; \
	echo --------------------; \
	echo; \
	for e in $(executables); do \
		number="$$(dirname $$e)"; \
		name="$${e%%.*}"; \
		printf "$$name\t"; \
		"./$$e" <"$$number"/input.txt; \
	done
