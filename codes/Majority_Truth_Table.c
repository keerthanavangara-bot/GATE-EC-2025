#include <stdio.h>

/* GATE EC 2025 Q23: majority output F = XY + YZ + ZX.
   Truth-table verification is performed by comparing the expression with
   the definition "1 iff at least two inputs are 1". */

int main(void) {
    int x, y, z;
    puts("X Y Z | F(expression) F(definition) | VERIFIED");
    for (x = 0; x <= 1; ++x) {
        for (y = 0; y <= 1; ++y) {
            for (z = 0; z <= 1; ++z) {
                int expr = (x & y) | (y & z) | (z & x);
                int defn = (x + y + z >= 2);
                printf("%d %d %d |      %d           %d      | %s\n",
                       x, y, z, expr, defn, expr == defn ? "YES" : "NO");
            }
        }
    }
    return 0;
}
