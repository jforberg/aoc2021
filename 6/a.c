#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_DAYS 80

#define BINS 9
#define CHILD_TIMER 8
#define MOTHER_TIMER 6

static int days;
static int counts[BINS];

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

static int count_fish(void)
{
    int c = 0;

    for (int i = 0; i < BINS; i++)
        c += counts[i];

    return c;
}

static void debug_print(void)
{
    printf("After %2d days: ", days);

    for (int i = 0; i < BINS; i++)
        for (int j = 0; j < counts[i]; j++)
            printf("%d,", i);

    putchar('\n');
}

static void sim_step(void)
{
    int births = 0;

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

    printf("%d\n", count_fish());
}
