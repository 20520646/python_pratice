import math
a = 6378137
e_2 = 0.0067
X_P = float(input("Nhap toa do X: "))
Y_P = float(input("Nhap toa do Y: "))
Z_P = float(input("Nhap toa do Z: "))
#buoc 1 tính Dp
D_P = math.sqrt(X_P ** 2 + Y_P ** 2)

#buoc 2 tính kinh đô
lambda_P = 2 * math.atan((D_P - X_P) / Y_P)
print(lambda_P)
#bươc 3 tính vĩ độ
pi_0 = math.atan(Z_P/(D_P*(1 - e_2)))
print(pi_0)
#buoc 4: tinh ba kinh
R_NP = a / (math.sqrt(1 - e_2 * math.sin(pi_0) ** 2))
#Buoc 5: tinh vi do
pii = math.atan((Z_P + e_2 * R_NP * math.sin(pi_0)) / D_P)
#buoc 7: tinh  do cao
if pii < 45 :
    h_P = D_P / math.cos(pii) - R_NP
else :
    h_P = (Z_P / math.sin(pii)) - R_NP * (1 - e_2)
print(h_P)