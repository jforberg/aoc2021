executables :=

# Day 1
executables += 1/a.py 1/b.py

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
