
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

X6 = s56*s6;
Y6 = -(s61*c56+c61*s56*c6);
Z6 = c61*c56 - s61*s56*c6;

Y4     = ((-s45)^2*c34-s45*c45*s34*c4+c45^2*c34-c45^2*c34)/s45;
X_61   = X6*c1 - Y6*s1;
Y_61   = c12*(X6*s1+Y6*c1) - s12*Z6;
Z_61   = s12*(X6*s1+Y6*c1) + c12*Z6;
X_612  = X_61*c2 - Y_61*s2;
Y_612  = c23*(X_61*s2+Y_61*c2)-s23*Z_61;
X_6123 = X_612*c3 - Y_612*s3;
eq1    = -S4*(s34*X_6123)+a34*(X_astrik_6123)-a45*((-c34+c45*Z612)/s45);



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
