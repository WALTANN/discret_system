T = 0.2;
A_sig = -1.24;
omega = 0.09;

Gamma_d = [cos(T*omega),  sin(T*omega);
          -sin(T*omega),  cos(T*omega)];

B_gen = [0; 0];
H = [A_sig, 0];
D_gen = 0;

xi0 = [0; 1];