
# Euler's F + V = E + 2 formula
def EulerFormula(F, V):
    E = int(F) + int(V) - 2
    print(f"\nthe shape have {E} edges")
    print("Formula: Faces + Vertices = Edges + 2(F + V = E + 2)\n")

# Newton's f = ma formula
def NewtonFormula(M, A):
    F = float(M) * float(A)
    print(f"\nAnswer: {F} newtons")
    print("Formula: Force = Mass * Acceleration(f = ma)\n")

# Formula for measuring gravitational force
def GravityFormula(M1, M2, D):
    G = 0.0000000000667
    F = G * float(M1) * float(M2) / (float(D) ** 2)
    print(f"\nAnswer: {F} newtons")
    print("Formula: Force = Gravitational constant * (M1 * M2) / Distance(F = G * (M1 * M2) / D)\n")

# Einstein's E = mc ^ 2 formula
def EinsteinFormula(M):
    C = 299792458
    E = float(M) * float(C) ** 2
    print(f"\nThe amount of energy is {E}")
    print("Formula: Energy = Mass * Speed of Light ** 2(E = mc^2)\n")

# Examples:
GravityFormula(M1 = 10, M2 = 8, D = 5) # should output 2.1344e-10 newtons
EinsteinFormula(M = 34) # should output 3.0557676077051796e+18
NewtonFormula(M = 15, A = 2.5) # should output 37.5 newtons
EulerFormula(F = 4, V = 4) # should output 6 edges
