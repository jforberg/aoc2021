/*
 * Problem is identical to Project Euler #83 so I re-use my solution to that problem. It is quite
 * inefficent due to using glib's crappy queue that is based on linked lists. Would be much better
 * with a proper priority queue. But it's more than fast enough for this data set.
 */
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <glib.h>

#define SIZE 100

static int matrix[SIZE][SIZE];
static int w, h;

typedef struct node {
    int i;
    int j;
    int dist;
    int pos;
    bool visited;
} Node;

static Node nodes[SIZE][SIZE];
static GQueue *queue;

static int compare(const void *av, const void *bv, void *_)
{
    const Node *a = av, *b = bv;
    return a->dist - b->dist;
}

static void sub_queue(Node *from, Node *to)
{
    to->dist = MIN(to->dist, from->dist + matrix[to->i][to->j]);

    if (!to->visited) {
        g_queue_remove(queue, to);
        g_queue_insert_sorted(queue, to, compare, NULL);
    }
}

static void dijkstra(void)
{
    queue = g_queue_new();

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            Node *n = &nodes[i][j];
            n->i = i, n->j = j, n->dist = INT_MAX, n->visited = false;

            if (i == 0 && j == 0)
                n->dist = 0;

            g_queue_insert_sorted(queue, n, compare, NULL);
        }
    }

    while (!g_queue_is_empty(queue)) {
        Node *from = g_queue_pop_head(queue);
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
        assert(w == 0 || len == w);
        w = len;

        for (int j = 0; j < w; j++) {
            char digit_buffer[] = { buffer[j], 0 };
            matrix[i][j] = atoi(digit_buffer);
        }
    }

    h = i;
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
    dijkstra();

    printf("%u\n", nodes[h - 1][w - 1].dist);
}
