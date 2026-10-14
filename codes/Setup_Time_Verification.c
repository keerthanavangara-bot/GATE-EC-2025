#include <stdio.h>

/* GATE EC 2025 Q62 setup-time calculation.
   Given: AND gate delay=1 ns, FF setup=2 ns, FF clock-to-Q=2 ns.
   Add the combinational path delay from the actual figure (AND gate and any
   other gates on the register-to-register path). For a single AND path:
   Tclk_min = t_cq + t_comb + t_setup = 2 + 1 + 2 = 5 ns.
   Include skew/extra gates only if the diagram specifies them. */

int main(void) {
    double tcq = 2.0, tsetup = 2.0, tand = 1.0;
    double extra;
    printf("Extra combinational delay on the critical path beyond the stated AND gate (ns; enter 0 if none): ");
    if (scanf("%lf", &extra) != 1 || extra < 0) {
        puts("Invalid delay."); return 1;
    }
    double tmin = tcq + tand + extra + tsetup;
    double fmax_mhz = 1000.0 / tmin; /* 1 ns period -> 1000 MHz */
    printf("Minimum clock period = %.3f ns\n", tmin);
    printf("Maximum clock frequency = %.0f MHz (unrounded %.6f MHz)\n", fmax_mhz, fmax_mhz);
    return 0;
}
