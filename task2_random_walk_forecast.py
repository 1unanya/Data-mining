import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# --- Генеруємо випадкове блукання з напрямом ---
n = 50
trend = 0.05  # сталий тренд (зростання активності)
noise = np.random.normal(0, 0.2, n)  # випадкові коливання
Y = np.zeros(n)
Y[0] = 1.0  # початкова активність
for t in range(1, n):
    Y[t] = Y[t-1] + trend + noise[t]  # випадкове блукання з трендом

# --- Побудова графіка ---
plt.figure(figsize=(10,5))
plt.plot(Y, color='blue', marker='o')
plt.title('Випадкове блукання активності користувачів з трендом')
plt.xlabel('Період (день)')
plt.ylabel('Активність користувачів')
plt.grid(True)
plt.show()

# --- Прогнозування y(t+τ) ---
tau = 5  # прогноз на 5 днів уперед
y_t = Y[-1]
forecast = y_t + trend * tau
print(f"Прогноз активності через {tau} днів: y(t+{tau}) = {forecast:.3f}")

# --- Прогнозна помилка (mean forecast error) ---
# У випадку випадкового блукання з трендом:
# прогнозна помилка має дисперсію, що зростає з τ
sigma2 = np.var(noise)
forecast_error_var = tau * sigma2
rmse = np.sqrt(forecast_error_var)
print(f"Середньоквадратична похибка прогнозу (RMSE) = {rmse:.3f}")