import time
import sys
import os

def selection_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def read_input(file_path: str) -> list[int]:
    with open(file_path, 'r') as f:
        data = [int(line.strip().split(':')[-1]) for line in f if line.strip()]
    return data

def save_output(sorted_data: list[int], algorithm: str, input_filename: str) -> None:
    output_filename = f"sorted_{algorithm}_{os.path.basename(input_filename)}.txt"
    with open(output_filename, 'w') as f:
        for num in sorted_data:
            f.write(f"{num}\n")
    print(f"Arquivo gerado: {output_filename}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py caminho/arquivo.in")
        sys.exit(1)

    input_path = sys.argv[1]
    filename = os.path.basename(input_path)
    
    try:
        data = read_input(input_path)
        print(f"\nArquivo: {filename} | {len(data)} números lidos")

        # Selection Sort
        start_sel = time.time()
        sorted_sel = selection_sort(data.copy())
        time_sel = (time.time() - start_sel) * 1000  # ms
        save_output(sorted_sel, "selection", input_path)

        # Insertion Sort
        start_ins = time.time()
        sorted_ins = insertion_sort(data.copy())
        time_ins = (time.time() - start_ins) * 1000  # ms
        save_output(sorted_ins, "insertion", input_path)

        # Resultados
        print(f"\nTempo Selection Sort: {time_sel:.3f} ms")
        print(f"Tempo Insertion Sort: {time_ins:.3f} ms")

        if time_sel < time_ins:
            print("\nRESULTADO: Selection Sort foi mais rápido!")
        else:
            print("\nRESULTADO: Insertion Sort foi mais rápido!")

    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()