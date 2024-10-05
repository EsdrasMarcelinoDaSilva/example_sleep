import time


count = 0
while count < 20:
    count += 1
    if count == 13:
        continue
    print(count)
    time.sleep(1)

# com for

for count in range(20, 0, -1):
    if count == 13:
        continue
    print(count)
    time.sleep(1)

# simulando a garantia da primeira execução do loop assim como o do while

count = 21
while True:
    count -= 1
    if count == 13:
        continue
    print(count)
    time.sleep(1)
    if not (count > 1):
        break
