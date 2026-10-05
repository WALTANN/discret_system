clear;

% Период дискретизации
T_dist = 0.25;

% Коэффициенты характеристического полинома
a = 2 * exp(-T_dist) * cos(3 * T_dist);
b = exp(-2 * T_dist);

% p(z) = (z^2 - a*z + b)(z - 1)^2
%
% p(z) = z^4 + p3*z^3 + p2*z^2 + p1*z + p0

p3 = -(2 + a);
p2 = 1 + 2*a + b;
p1 = -(a + 2*b);
p0 = b;

% Матрица динамики генератора
Gamma_dist = [
     0,    1,    0,    0;
     0,    0,    1,    0;
     0,    0,    0,    1;
    -p0, -p1, -p2, -p3
];

% Внешнего входа у генератора нет
B_dist = [
    0;
    0;
    0;
    0
];

% g(k) = xi_1(k)
H_dist = [1, 0, 0, 0];

D_dist = 0;

% Исходное возмущение
g = @(k) 2 * exp(-k*T_dist) * sin(3*k*T_dist) ...
         + 0.5*k*T_dist;

% Начальные условия:
% xi(0) = [g(0); g(1); g(2); g(3)]
xi0_dist = [
    g(0);
    g(1);
    g(2);
    g(3)
];

% Вывод для проверки
disp('Gamma_dist =');
disp(Gamma_dist);

disp('H_dist =');
disp(H_dist);

disp('xi0_dist =');
disp(xi0_dist);

disp('eig(Gamma_dist) =');
disp(eig(Gamma_dist));