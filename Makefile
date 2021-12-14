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

# Day 8 - Numpy
executables += 8/a.py 8/b.py

# Day 9 - Numpy
executables += 9/a.py 9/b.py

# Day 10 - Haskell
executables += 10/a 10/b

# Day 11 - Numpy
executables += 11/a.py 11/b.py

# Day 12 - Haskell
executables += 12/a 12/b

# Day 13 - Numpy
executables += 13/a.py 13/b.py

# Day 14 - Haskell
executables += 14/a 14/b

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

# Build rules for Haskell codes
HSFLAGS := -O2

%: %.hs Makefile
	stack ghc -- $(HSFLAGS) $<
