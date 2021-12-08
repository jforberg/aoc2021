executables :=

# Day 1 - Numpy
executables += 1/a.py 1/b.py

# Day 2 - AWK
executables += 2/a.awk 2/b.awk

# Day 3 - Numpy
executables += 3/a.py 3/b.py

# Day 4 - Numpy
executables += 4/a.py 4/b.py

# Day 5 - Numpy
executables += 5/a.py 5/b.py

# Day 6 - C
executables += 6/a 6/b

# Day 7 - Numpy
executables += 7/a.py 7/b.py

# Main rules
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

.PHONY: clean
clean:
	git clean -fdX

# Build rules for C code
CFLAGS := -O2 -Wall -Wno-unused-function

%: %.c Makefile

# Build rules for Haskell code
HSFLAGS := -O2

%: %.hs Makefile
	stack ghc -- $(HSFLAGS) $<
