from collections import Counter
import pylab as plt

with open('laba16.2.txt', 'r', encoding='utf-8') as file:
    text = file.read()

ukrainian_letters = [char for char in text.lower() if 'а' <= char <= 'я' or char == 'є' or char == 'і' or char == 'ї' or char == 'ґ']

letter_counts = Counter(ukrainian_letters)

letters, counts = zip(*sorted(letter_counts.items()))

plt.figure(figsize=(12, 6))
plt.bar(letters, counts, color='skyblue')
plt.xlabel('Літери')
plt.ylabel('Частота')
plt.title('Гістограма частот українських літер у тексті')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig(r"C:\Users\artem\OneDrive\Рабочий стол\лаби\лаб16\lab16.2\letter_histogram.jpg")
