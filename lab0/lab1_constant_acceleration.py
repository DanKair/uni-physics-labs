import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=== LAB: Motion with Constant Acceleration ===\n")

    # 1. Input parameters
    h0 = float(input("Enter initial height h0 (m): "))
    alpha_deg = float(input("Enter launch angle α (degrees): "))
    alpha = math.radians(alpha_deg)
    sin2 = math.sin(alpha) ** 2

    print("\nEnter 5 initial speeds v0 (m/s):")
    v0_values = [float(input(f"  v0[{i+1}]: ")) for i in range(5)]

    # 2. Measurements for each speed
    all_ymax_means = []
    all_ymax_stdevs = []

    for i, v in enumerate(v0_values, 1):
        print(f"\nMeasurements for v0 = {v} m/s:")
        y_values = [float(input(f"  y{i} = ")) for i in range(1, 6)]

        y_mean = np.mean(y_values)
        deviations = [y - y_mean for y in y_values]
        sq_sum = sum(d**2 for d in deviations)
        sigma = math.sqrt(sq_sum / (5 * 4))  # n=5
        t = 2.78  # 95% confidence
        abs_err = sigma * t

        print(f"  Mean ymax = {y_mean:.3f} m")
        print(f"  σ = {sigma:.4f}, AbsErr = {abs_err:.4f}")

        all_ymax_means.append(y_mean)
        all_ymax_stdevs.append(abs_err)

    # 3. Calculate gravity for each trajectory
    g_values = []
    print("\n=== Gravity calculations ===")
    for v, y_mean in zip(v0_values, all_ymax_means):
        g = (v**2 * sin2) / (2 * (y_mean - h0))
        g_values.append(g)
        print(f"  v0={v:>4.1f} m/s → g = {g:.3f} m/s²")

    g_mean = np.mean(g_values)
    g_deltas = [g_mean - g for g in g_values]
    sigma_g = math.sqrt(sum(d**2 for d in g_deltas) / (5 * 4))
    abs_err_g = sigma_g * t

    print(f"\n⟨g⟩ = {g_mean:.3f} ± {abs_err_g:.3f} m/s²")

    # 4. Plot graph <ymax> vs v0^2
    v2 = [v**2 for v in v0_values]
    coeffs = np.polyfit(v2, all_ymax_means, 1)  # linear regression y = kx + b
    k, b = coeffs
    y_fit = np.polyval(coeffs, v2)

    plt.figure(figsize=(8, 6))
    plt.scatter(v2, all_ymax_means, color='blue', label='Measured ⟨ymax⟩')
    plt.plot(v2, y_fit, color='red', label=f'Fit: y = {k:.4f}x + {b:.4f}')
    plt.xlabel('v₀² (m²/s²)')
    plt.ylabel('⟨ymax⟩ (m)')
    plt.title('Dependence of ⟨ymax⟩ on v₀²')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"\nRegression line: y = {k:.5f}x + {b:.5f}")
    print(f"Experimental g (from slope): g = 0.5 * sin²α * (1/k)")
    g_exp = 0.5 * sin2 * (1 / k)
    print(f"  g_exp = {g_exp:.3f} m/s²")

if __name__ == "__main__":
    main()
