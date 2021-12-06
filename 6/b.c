#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define MAX_DAYS 256

#define BINS 9
#define CHILD_TIMER 8
#define MOTHER_TIMER 6

typedef int64_t s64;

static int days;
static s64 counts[BINS];

static void parse(void)
{
    char *line;

    assert(scanf("%m[^\n]", &line) == 1);

    char *token = strtok(line, ",");

    while (token) {
        int x = atoi(token);
        assert(x && x < BINS);
        counts[x]++;
        token = strtok(NULL, ",");
    }

    free(line);
}

static s64 count_fish(void)
{
    s64 c = 0;

    for (int i = 0; i < BINS; i++)
        c += counts[i];

    return c;
}

static void sim_step(void)
{
    s64 births = 0;

    for (int i = 0; i < BINS; i++) {
        if (i == 0)
            births = counts[i];
        else
            counts[i - 1] += counts[i];

        if (i == CHILD_TIMER)
            counts[i] = births;
        else if (i == MOTHER_TIMER)
            counts[i] = births;
        else
            counts[i] = 0;
    }

    days++;
}

int main(void)
{
    parse();

    for (int i = 0; i < MAX_DAYS; i++)
        sim_step();

    printf("%lld\n", (long long) count_fish());
}
