import random

# Задание №1: Генерация последовательностей случайных чисел
M = 1000
a_TZ = 39
a_TS = 39
b = 1
x0 = 1
n = 50  # Количеm :- div(m,10) b := mod(m,10) m := div(m,10) m := b*100+s*10+m ство заявок

def generate_linear_sequence(a, b, M, x0, n, min_val, max_val):
    random_numbers = []
    for _ in range(n):
        x0 = (a * x0 + b) % M
        value = min_val + (max_val - min_val) * (x0 / M)
        random_numbers.append(value)
    return random_numbers

TZmin, TZmax = 4, 12  # Для входного потока заявок
TSmin, TSmax = 0, 15  # Для времени обработки заявок сервером

tz_sequence = generate_linear_sequence(a_TZ, b, M, x0, n, TZmin, TZmax)

# Определение параметров буфера
buffer_size = 2
buffer = []

# Определение параметров серверов
num_servers = 3
server_limits = [15, 15, 15]  # Ограничения времени обработки для каждого сервера

# Лимит времени в буфере
buffer_time_limit = 5

# Списки для отслеживания обработанных и необработанных заявок
processed_requests = []
unprocessed_requests = []

# Задание №2: Определение времен прихода заявок и времени обработки на серверах
print("Времена прихода заявок и времена обработки на серверах:")
for i, tz_time in enumerate(tz_sequence, start=1):
    print(f"\nЗаявка {i} пришла в {tz_time:.2f} сек")

    # Проверка доступных серверов
    available_servers = [j for j, time_left in enumerate(server_limits) if time_left >= 0]

    # Проверка буфера
    if not available_servers and len(buffer) < buffer_size:
        buffer.append((i, tz_time))
        print(f"Заявка {i} добавлена в буфер")
    elif available_servers:
        # Обработка заявок серверами
        server_num = random.choice(available_servers)
        ts_time = random.uniform(TSmin, min(TSmax, server_limits[server_num]))

        if ts_time <= server_limits[server_num]:
            print(f"Заявка {i} обработана сервером {server_num + 1} за {ts_time:.2f} сек")
            processed_requests.append((i, tz_time, ts_time, server_num + 1))
            server_limits[server_num] -= ts_time
        else:
            buffer.append((i, tz_time))
            print(f"Заявка {i} добавлена в буфер из-за превышения лимита времени сервера")

# Задание №3: Обработка заявок из буфера
print("\nОбработка заявок из буфера:")
for i, tz_time in buffer:
    available_servers = [j for j, time_left in enumerate(server_limits) if time_left >= 0]

    if available_servers:
        server_num = random.choice(available_servers)
        ts_time = random.uniform(TSmin, min(TSmax, server_limits[server_num]))

        if ts_time <= server_limits[server_num]:
            print(f"Заявка {i} из буфера обработана сервером {server_num + 1} за {ts_time:.2f} сек")
            processed_requests.append((i, tz_time, ts_time, server_num + 1))
            server_limits[server_num] -= ts_time
        else:
            unprocessed_requests.append((i, tz_time, "Превышение лимита времени сервера"))
            print(f"Заявка {i} из буфера не обработана из-за превышения лимита времени сервера")
    else:
        unprocessed_requests.append((i, tz_time, "Нет доступных серверов"))
        print(f"Заявка {i} из буфера не обработана из-за отсутствия доступных серверов")

# Вывод результатов
print("\nРезультаты:")
print(f"Обработанные заявки: {len(processed_requests)}")
print("Детали обработанных заявок:")
for i, tz_time, ts_time, server_num in processed_requests:
    print(f"Заявка {i} пришла в {tz_time:.2f} сек, обработана сервером {server_num} за {ts_time:.2f} сек")

print(f"\nНеобработанные заявки: {len(unprocessed_requests)}")
print("Детали необработанных заявок:")
for i, tz_time, reason in unprocessed_requests:
    print(f"Заявка {i} пришла в {tz_time:.2f} сек, причина необработки: {reason}")
