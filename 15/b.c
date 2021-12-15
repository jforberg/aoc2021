/*
 * Problem is identical to Project Euler #83 so I re-use my solution to that problem. It is quite
 * inefficent due to using glib's crappy queue that is based on linked lists. Would be much better
 * with a proper priority queue. But it's more than fast enough for this data set.
 */
#include <assert.h>
#include <glib.h>
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>

#define SIZE 100

static int sub_matrix[SIZE][SIZE];
static int sub_w, sub_h;

static int matrix[5 * SIZE][5 * SIZE];
static int w, h;

typedef struct node {
    int i;
    int j;
    int dist;
    bool visited;
    bool in_queue;
} Node;

static Node nodes[5 * SIZE][5 * SIZE];
static GQueue *queue;

static int compare(const void *av, const void *bv, void *_)
{
    const Node *a = av, *b = bv;
    return a->dist - b->dist;
}

static void sub_queue(Node *from, Node *to)
{
    to->dist = MIN(to->dist, from->dist + matrix[to->i][to->j]);

    if (!to->visited && !to->in_queue) {
        g_queue_insert_sorted(queue, to, compare, NULL);
        to->in_queue = true;
    }
}

static void dijkstra(void)
{
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            Node *n = &nodes[i][j];
            n->i = i, n->j = j, n->dist = INT_MAX, n->visited = false, n->in_queue = false;

            if (i == 0 && j == 0)
                n->dist = 0;
        }
    }

    queue = g_queue_new();
    g_queue_insert_sorted(queue, &nodes[0][0], compare, NULL);
    nodes[0][0].in_queue = true;

    while (!g_queue_is_empty(queue)) {
        Node *from = g_queue_pop_head(queue);

        from->in_queue = false;
        from->visited = true;

        if (from->i != 0)
            sub_queue(from, &nodes[from->i - 1][from->j]);
        if (from->j != 0)
            sub_queue(from, &nodes[from->i][from->j - 1]);
        if (from->i != h - 1)
            sub_queue(from, &nodes[from->i + 1][from->j]);
        if (from->j != w - 1)
            sub_queue(from, &nodes[from->i][from->j + 1]);
    }

    g_queue_free(queue);
}

static void parse(void)
{
    char buffer[256];
    int i = 0;

    for (i = 0; !feof(stdin); i++) {
        int count = scanf("%256s\n", buffer);
        assert(count == 1);
        int len = strlen(buffer);
        assert(sub_w == 0 || len == sub_w);
        sub_w = len;

        for (int j = 0; j < sub_w; j++) {
            char digit_buffer[] = { buffer[j], 0 };
            sub_matrix[i][j] = atoi(digit_buffer);
        }
    }

    sub_h = i;
}

static void tile(void)
{
    w = 5 * sub_w;
    h = 5 * sub_h;

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            for (int k = 0; k < sub_h; k++) {
                for (int l = 0; l < sub_w; l++) {
                    int scale = i + j;
                    int val = (sub_matrix[k][l] + scale - 1) % 9 + 1;
                    matrix[sub_h * i + k][sub_w * j + l] = val;
                }
            }
        }
    }
}

static void dump(void)
{
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++)
            printf("%d ", matrix[i][j]);

        printf("\n");
    }
}

int main(void)
{
    parse();
    tile();
    //dump();
    dijkstra();

    printf("%u\n", nodes[h - 1][w - 1].dist);
}
