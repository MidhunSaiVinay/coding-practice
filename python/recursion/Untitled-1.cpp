#include <stdio.h>
#include <math.h>

#define L 40
#define c 1
#define time 20
#define n 2


#define nu 0.4


void lax_method(double *u, double dx, double nu, int n_x);
void apply_periodic_bc(double *u, int n_x);
void plot_wave(double *u, double dx, char *label, int n_x);

int main() {
    double dx_list[] = {1, 0.5, 0.1};

    for (int i = 0; i < sizeof(dx_list) / sizeof(dx_list[0]); i++) {
        double dx = dx_list[i];
        double dt = nu * dx / c;
        int n_t = time / dt;
        int n_x = L / dx + 1;

        double x[n_x];
        for (int j = 0; j < n_x; j++) {
            x[j] = j * dx;
        }

        double u[n_x];
        for (int j = 0; j < n_x; j++) {
            u[j] = sin(2 * n * M_PI * x[j] / L);
        }

        for (int t = 0; t < n_t; t++) {
            lax_method(u, dx, nu, n_x);
        }

        plot_wave(u, dx, "dx=", n_x);
    }

    return 0;
}

void lax_method(double *u, double dx, double nu, int n_x) {
    double u_new[n_x];
    for (int i = 1; i < n_x - 1; i++) {
        u_new[i] = 0.5 * (u[i + 1] + u[i - 1]) - nu / 2 * (u[i + 1] - u[i - 1]);
    }
    apply_periodic_bc(u_new, n_x);
    for (int i = 0; i < n_x; i++) {
        u[i] = u_new[i];
    }
}

void apply_periodic_bc(double *u, int n_x) {
    u[0] = u[n_x - 2];
    u[n_x - 1] = u[1];
}

void plot_wave(double *u, double dx, char *label, int n_x) {
    printf("%s\n", label);
    for (int i = 0; i < n_x; i++) {
        printf("%f\n", u[i]);
    }
}