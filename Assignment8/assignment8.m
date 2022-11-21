close all; clear all;

syms theta1 theta2 theta4 theta5

%% known parameters
% Known joint lengths (cm)
S1 = 6; S2 = 4.5; S4 = 7.5; S6 = 3.9;
% Known twist angles (deg)
alpha12 = 47.5; alpha23 = 221; alpha34 = 115; 
alpha45 = 38.5; alpha56 = 295; alpha61 = 45;
% known joint offsets (cm)
a12 = 5.5; a23 = 3.6; a34 = 7.2; 
a45 = 2.8; a56 = 3.8; a61 = 6.2;
% known joint angles (deg)
theta3 = 90; theta6 = 220;

% sine and cosine terms
s12 = sind(alpha12);
s23 = sind(alpha23);
s34 = sind(alpha34);
s45 = sind(alpha45);
s56 = sind(alpha56);
s61 = sind(alpha61);
c12 = cosd(alpha12);
c23 = cosd(alpha23);
c34 = cosd(alpha34);
c45 = cosd(alpha45);
c56 = cosd(alpha56);
c61 = cosd(alpha61);
s3  = sind(theta3);
s6  = sind(theta6);
c3  = cosd(theta3);
c6  = cosd(theta6);

%% solve for theta1 and theta2
X6 = s56*s6;
Y6 = -(s61*c56+c61*s56*c6);
Z6 = c61*c56 - s61*s56*c6;

A1 = s34 * (Y6 * c12 * c23 * c3 + X6 * s3) + c34 * s23 * c12 * Y6;
B1 = s34 * (X6 * c12 * c23 * c3 - Y6 * s3) + c34 * s23 * c12 * X6;
D1 = -s12 * Z6 * (c23 * c3 * s34 + c34 * s23);
E1 = s34 * (c23 * X6 * c3 - c12 * Y6 * s3) + c34 * s23 * X6;
F1 = s34 * (-c12 * X6 * s3 - c23 * Y6 * c3) - c34 * s23 * Y6;
G1 = Z6 * s12 * s3 * s34;
H1 = -Y6 * c3 * s12 * s23 * s34 + Y6 * c23 * c34 * s12;
I1 = -X6 * c3 * s12 * s23 * s34 + X6 * c23 * c34 * s12;
J1 = -Z6 * (c3 * s23 * s34 - c23 * c34) * c12 - c45;


A2 = S6 * s56 * c12 * c61 * s23 * s6 + S1 * X6 * c12 * s23 + S2 * s23 * X6 + a56 * (-c12 * c56 * c6 * c61 * s23 + c12 * s23 * s56 * s61) + a61 * (c12 * c6 * s23 * s56 * s61 - c12 * c56 * c61 * s23) - a12 * s23 * s12 * Y6 + a23 * c12 * Y6 * c23 - S4 * s34 * (-Y6 * c12 * c23 * s3 + X6 * c3) + a34 * (Y6 * c12 * c23 * c3 + X6 * s3) - a45 * s23 * c12 * Y6 * c45 / s45;
B2 = S6 * s56 * c12 * s23 * c6 - S1 * Y6 * c12 * s23 - S2 * s23 * Y6 + a56 * c56 * c12 * s23 * s6 - a12 * s23 * s12 * X6 + a23 * c12 * X6 * c23 - S4 * s34 * (-X6 * c12 * c23 * s3 - Y6 * c3) + a34 * (X6 * c12 * c23 * c3 - Y6 * s3) - a45 * s23 * c12 * X6 * c45 / s45;
D2 = (((((-S6 * s6 * s61 + c61 * (a61 * c6 + a56)) * s56 + c56 * s61 * (a56 * c6 + a61)) * s23 - c23 * Z6 * (S4 * s3 * s34 + a34 * c3 + a23)) * s12 - c12 * s23 * Z6 * a12) * s45 + Z6 * a45 * c45 * s12 * s23) / s45;
E2 = S6 * s56 * c6 * s23 - S1 * s23 * Y6 - S2 * s23 * c12 * Y6 + a56 * c56 * s23 * s6 + a23 * c23 * X6 - S4 * s34 * (-X6 * c23 * s3 - Y6 * c12 * c3) + a34 * (X6 * c23 * c3 - Y6 * c12 * s3) - a45 * s23 * X6 * c45 / s45;
F2 = -S6 * s56 * c61 * s23 * s6 - S1 * s23 * X6 - S2 * s23 * c12 * X6 + a56 * (c56 * c6 * c61 * s23 - s23 * s56 * s61) + a61 * (-c6 * s23 * s56 * s61 + c56 * c61 * s23) - a23 * c23 * Y6 - S4 * s34 * (-X6 * c12 * c3 + Y6 * c23 * s3) + a34 * (-X6 * c12 * s3 - Y6 * c23 * c3) + a45 * s23 * Y6 * c45 / s45;
G2 = Z6 * s12 * (-S4 * c3 * s34 + S2 * s23 + a34 * s3);
H2 = S6 * s56 * c23 * c61 * s12 * s6 + S1 * X6 * c23 * s12 + a56 * (-c23 * c56 * c6 * c61 * s12 + c23 * s12 * s56 * s61) + a61 * (c23 * c6 * s12 * s56 * s61 - c23 * c56 * c61 * s12) + a12 * c12 * Y6 * c23 - a23 * s23 * s12 * Y6 - S4 * s34 * s23 * s12 * Y6 * s3 - a34 * s23 * s12 * Y6 * c3 - a45 * c23 * s12 * Y6 * c45 / s45;
I2 = S6 * s56 * c23 * s12 * c6 - S1 * Y6 * c23 * s12 + a56 * c56 * c23 * s12 * s6 + a12 * c12 * X6 * c23 - a23 * s23 * s12 * X6 - S4 * s34 * s23 * s12 * X6 * s3 - a34 * s23 * s12 * X6 * c3 - a45 * c23 * s12 * X6 * c45 / s45;
J2 = (((((S6 * s6 * s61 - c61 * (a61 * c6 + a56)) * s56 - c56 * s61 * (a56 * c6 + a61)) * c23 - s23 * Z6 * (S4 * s3 * s34 + a34 * c3 + a23)) * c12 - c23 * s12 * Z6 * a12) * s45 - a45 * (Z6 * c12 * c23 * c45 - c34)) / s45;

% eq2 = vpa(cosd(theta2)*(A1*cosd(theta1)+B1*sind(theta1)+D1) + sind(theta2)*(E1*cosd(theta1)+F1*sind(theta1)+G1) + (H1*cosd(theta1)+I1*sind(theta1)+J1),4);
% eq3 = vpa(cosd(theta2)*(A2*cosd(theta1)+B2*sind(theta1)+D2) + sind(theta2)*(E2*cosd(theta1)+F2*sind(theta1)+G2) + (H2*cosd(theta1)+I2*sind(theta1)+J2),4);

a1 = A1-D1-H1+J1;
b1 = 2*(I1-B1);
d1 = -A1-D1+H1+J1;
e1 = 2*(G1-E1);
f1 = 4*F1;
g1 = 2*(G1+E1);
h1 = -A1+D1-H1+J1;
i1 = 2*(I1+B1);
j1 = A1+D1+H1+J1;

a2 = A2-D2-H2+J2;
b2 = 2*(I2-B2);
d2 = -A2-D2+H2+J2;
e2 = 2*(G2-E2);
f2 = 4*F2;
g2 = 2*(G2+E2);
h2 = -A2+D2-H2+J2;
i2 = 2*(I2+B2);
j2 = A2+D2+H2+J2;


[ x1 , x2 ] = solve_bi_quadratics( a1, b1, d1, e1, f1, g1, h1, i1, j1, ...
    a2, b2, d2, e2, f2, g2, h2, i2, j2 ) ;

x1 = real(x1);
x2 = real(x2);
theta1 = zeros(numel(x1),1);
theta2 = zeros(numel(x2),1);
theta4 = zeros(numel(x1),1);
theta5 = zeros(numel(x1),1);
for i = 1:numel(x1)
    theta1(i) = get_angle(x1(i));
    theta2(i) = get_angle(x2(i));
    
    % solve for theta4
    
    c1     = cosd(theta1(i));
    s1     = sind(theta1(i));
    c2     = cosd(theta2(i));
    s2     = sind(theta2(i));
    X_61   = X6*c1 - Y6*s1;
    Y_61   = c12*(X6*s1+Y6*c1) - s12*Z6;
    Z_61   = s12*(X6*s1+Y6*c1) + c12*Z6;
    X_612  = X_61*c2 - Y_61*s2;
    Y_612  = c23*(X_61*s2+Y_61*c2)-s23*Z_61;
    Z_612  = s23*(X_61*s2+Y_61*c2)+c23*Z_61;
    X_6123 = X_612*c3 - Y_612*s3;
    Y_6123 = c34*(X_612*s3 + Y_612*c3) - s34*Z_612;
    %X_astrik_6123 = X_612*s3 + Y_612*c3; 
    s4 = X_6123/s45;
    c4 = Y_6123/s45;
    theta4(i) = atan2d(s4,c4);
    
    X_1    = s61*s1;
    Y_1    = -(s12*c61+c12*s61*c1);
    Z_1    = c12*c61 - s12*s61*c1;
    X_12   = X_1*c2 - Y_1*s2;
    Y_12   = c23*(X_1*s2+Y_1*c2) - s23*Z_1;
    Z_12   = s23*(X_1*s2+Y_1*c2) + c23*Z_1;
    X_123  = X_12*c3 - Y_12*s3;
    Y_123  = c34*(X_12*s3+Y_12*c3)-s34*Z_12;
    Z_123  = s34*(X_12*s3+Y_12*c3)+c34*Z_12;
    X_1234 = X_123*c4 - Y_123*s4;
    Y_1234 = c45*(X_123*s4 + Y_123*c4) - s45*Z_123;
    s5     = X_1234/s56;
    c5     = Y_1234/s56;
    theta5(i) = atan2d(s5,c5);
end


S1 * (X_65 ) + a12 * (W_165 )+ S2 * (X_34 )+ a_23 * (W_34 ) + S3 * (X_4 )+ a34 * (c4 )...
+ a45 + a56 * (c5 ) + S6 * (X_5_bar) + a61 * (W_65)== 0;

% h = 6; i = 1; j = 2; k = 3;


% X_h     = s_gh*s_h;
% Y_h     = -(s_hi*c_gh+c_hi*s_gh*c_h);
% Z_h     = c_hi*c_gh - s_hi*s_gh*c_h;
% X_hi   = X_h*c_i - Y_h*s_i;
% Y_hi   = c_ij*(X_h*s_i+Y_h*c_i) - s_ij*Z_h;
% Z_hi   = s_ij*(X_h*s_i+Y_h*c_i) + c_ij*Z_h;
% X_hij  = X_hi*c_j - Y_hi*s_j;
% Y_hij  = c_jk*(X_hi*s_j+Y_hi*c_j)-s_jk*Z_hi;
% Z_hij  = s_jk*(X_hi*s_j+Y_hi*c_j)+c_jk*Z_hi;
% X_hijk = X_hij*c_k - Y_hij*s_k;
% Y_hijk = c_kl*(X_hij*s_k + Y_hij*c_k) - s_kl*Z_hij;


%S = vpasolve([ eq2 == 0, eq3 == 0],[theta1,theta2]);

% %% solve for theta4
% theta1 = double(vpa(S.theta1,4));
% theta2 = double(vpa(S.theta2,4));
% c1 = cosd(theta1);
% s1 = sind(theta1);
% c2 = cosd(theta2);
% s2 = sind(theta2);
% 
% 
% X_61   = X6*c1 - Y6*s1;
% Y_61   = c12*(X6*s1+Y6*c1) - s12*Z6;
% Z_61   = s12*(X6*s1+Y6*c1) + c12*Z6;
% X_612  = X_61*c2 - Y_61*s2;
% Y_612  = c23*(X_61*s2+Y_61*c2)-s23*Z_61;
% Z_612  = s23*(X_61*s2+Y_61*c2)+c23*Z_61;
% 
% X_6123 = X_612*c3 - Y_612*s3;
% Y_6123 = c34*(X_612*s3 + Y_612*c3) - s34*Z_612;
% %X_astrik_6123 = X_612*s3 + Y_612*c3; 
% 
% s4 = X_6123/s45;
% c4 = Y_6123/s45;
% theta4 = atan2d(s4,c4);










%S = vpasolve([X_6123 == s45*sind(theta4), Y_6123 == s45*cosd(theta4)],[theta4,theta4]);


% eq1    = -S4*(s34*X_6123)+a34*(X_astrik_6123)-a45*((-c34+c45*Z_612)/s45);
% vpa(eq1,4)


% Y4     = (-c34+c45*Z_612) / s45;

function theta = get_angle(x)

s = 2*x./(1+x.^2);
c = (1-x.^2)./(1+x.^2);

theta = atan2d(s,c);
end