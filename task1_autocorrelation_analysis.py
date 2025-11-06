import numpy as np
import matplotlib.pyplot as plt

# Дані: кількість відвідувань користувачами електронної бібліотеки за 16 днів
y = np.array([1.6, 0.8, 1.2, 0.5, 0.9, 1.1, 1.1, 0.6, 1.5, 0.8, 0.9, 1.2, 0.5, 1.3, 0.8, 1.2])

# --- (а) Побудова графіка часового ряду ---
plt.figure(figsize=(10,5))
plt.plot(y, marker='o', linestyle='-', color='purple')
plt.title('Активність користувачів електронної бібліотеки (часовий ряд)')
plt.xlabel('Період (день)')
plt.ylabel('Кількість відвідувань')
plt.grid(True)
plt.show()

# --- (б) Наближене визначення коефіцієнта автокореляції 1-го порядку ---
# Для наближення можна візуально оцінити коливання навколо середнього.
# Але ми обчислимо точно нижче, щоб порівняти.

# --- (в) Побудова графіка залежності y(t+1) від y(t) ---
y_t = y[:-1]   # поточні значення
y_t1 = y[1:]   # наступні значення

plt.figure(figsize=(6,6))
plt.scatter(y_t, y_t1, color='darkviolet')
plt.title('Залежність y(t+1) від y(t)')
plt.xlabel('y(t)')
plt.ylabel('y(t+1)')
plt.grid(True)
plt.show()

# --- Точне обчислення коефіцієнта автокореляції 1-го порядку ---
def autocorr_first_order(series):
    y_mean = np.mean(series)
    numerator = np.sum((series[:-1] - y_mean)*(series[1:] - y_mean))
    denominator = np.sum((series - y_mean)**2)
    return numerator / denominator

r1 = autocorr_first_order(y)
print(f"Коефіцієнт автокореляції першого порядку r₁ = {r1:.3f}")