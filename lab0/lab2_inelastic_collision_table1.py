import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Default values
pd.options.display.max_columns = 10

m1 = 1.0
v1_before = 1.0

print("\n=== LAB 3 — Elastic & Inelastic Collisions ===")
print("Automatic v_after tables version\n")

# =====================================================
# TABLE 3 – Graph A (β = −1)
# =====================================================
print("=== TABLE 3 (Graph A: β = −1) ===")

# You can edit these manually before each run
data3 = [
    # (m2, v_after)
    (1, 0.0),
    (2, -0.3),
    (3, -0.5),
    (4, -0.6),
    (5, -0.7),
    (6, -0.7),
    (7, -0.7),
    (8, -0.8),
    (9, -0.8),
    (10, -0.8),
]

table3 = []
for m2, v_after in data3:
    print(f"\n→ m₂ = {m2} kg, v_after = {v_after} m/s")
    E_before = float(input("   Enter E_k_before (J): "))
    E_after = float(input("   Enter E_k_after (J): "))

    ΔE = E_before - E_after
    δ_meas = ΔE / E_before if E_before else 0
    ξ = m1 / m2
    X = ξ / (1 + ξ)**2
    δ_theor = 4 * X

    table3.append({
        "m₂ (kg)": m2,
        "v_after (m/s)": v_after,
        "E_before (J)": E_before,
        "E_after (J)": E_after,
        "ΔE (J)": ΔE,
        "δ_meas": δ_meas,
        "ξ = m₁/m₂": ξ,
        "X = ξ/(1+ξ)²": X,
        "δ_theor = 4X": δ_theor
    })

df3 = pd.DataFrame(table3)
print("\n--- TABLE 3 RESULTS ---")
print(df3.round(4))

# Plot Graph A
Xvals = df3["X = ξ/(1+ξ)²"].values.reshape(-1, 1)
Yvals = df3["δ_meas"].values
regA = LinearRegression().fit(Xvals, Yvals)
kA, bA = regA.coef_[0], regA.intercept_

plt.figure(figsize=(7, 5))
plt.scatter(Xvals, Yvals, color="blue", label="Measured δ")
plt.plot(Xvals, regA.predict(Xvals), "r-", label=f"Fit Y={kA:.3f}X+{bA:.3f}")
plt.plot(Xvals, df3["δ_theor = 4X"], "g--", label="Theory Y=4X")
plt.title("Graph A – δ vs ξ/(1+ξ)²  (β = −1)")
plt.xlabel("ξ / (1 + ξ)²")
plt.ylabel("δ = ΔE / E_before")
plt.legend(); plt.grid(True); plt.show()

print(f"Experimental slope k_exp = {kA:.3f} (theoretical 4.000)\n")