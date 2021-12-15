#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>

static int table[100 * 100];
static int cost[100 * 100] = { [0 ... 100 * 100 - 1] = INT_MAX };
static int w, h;

enum { N, E, S, W };

static void parse(void)
{
    char buffer[256];
    int i = 0;

    for (i = 0; !feof(stdin); i++) {
        int count = scanf("%256s\n", buffer);
        assert(count == 1);
        int len = strlen(buffer);
        assert(w == 0 || len == w);
        w = len;

        for (int j = 0; j < w; j++) {
            char digit_buffer[] = { buffer[j], 0 };
            table[w * i + j] = atoi(digit_buffer);
        }
    }

    h = i;
}

static void dump(int *t)
{
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++)
            printf("%d ", t[i * w + j]);

        printf("\n");
    }
}

static void visit(int i, int j, int acc, int dir)
{
    if (i < 0 || j < 0 || i >= h || j >= w)
        return;

    if (i != 0 || j != 0)
        acc += table[i * w + j];

    if (cost[i * w + j] >= 0 && cost[i * w + j] <= acc)
        return;

    cost[i * w + j] = acc;

    if (dir != S)
        visit(i - 1, j,     acc, N);

    if (dir != W)
        visit(i,     j + 1, acc, E);

    if (dir != N)
        visit(i + 1, j,     acc, S);

    if (dir != E)
        visit(i,     j - 1, acc, W);
}

int main(void)
{
    parse();

    visit(0, 0, 0, E);

    printf("%d\n", cost[(h - 1) * w + w - 1]);
}
