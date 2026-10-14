#include <stdio.h>

/* GATE EC 2025 Q45 verification harness.
   The PDF figure's circuit and timing diagram must be transcribed first.
   At each positive clock edge T0..T3, enter the selected D input:
     SEL=0 selects P0=0; SEL=1 selects P1=1.
   If the circuit has additional S/reset/enable logic, incorporate it in
   next_y() after reading the diagram. The generic mux-only version below
   intentionally does not pretend to recover unseen diagram details. */

static int next_y(int sel, int p0, int p1) {
    return sel ? p1 : p0;
}

int main(void) {
    int sel[4], y[4];
    int p0 = 0, p1 = 1;
    int i;
    puts("Enter SEL sampled at positive edges T0, T1, T2, T3 (0 or 1).");
    for (i = 0; i < 4; ++i) {
        printf("SEL[T%d] = ", i);
        if (scanf("%d", &sel[i]) != 1 || (sel[i] != 0 && sel[i] != 1)) {
            puts("Invalid input."); return 1;
        }
        y[i] = next_y(sel[i], p0, p1);
    }
    printf("Y sequence (mux-only baseline): ");
    for (i = 0; i < 4; ++i) printf("%d", y[i]);
    puts("");
    puts("Verification note: apply the exact S/flip-flop logic from the Q45 figure before treating this as the paper answer.");
    return 0;
}
