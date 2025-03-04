def generate_number_table():
    numbers = list(range(1, 32))  # Generate numbers from 1 to 31
    
    # Print numbers in two columns, first 1-15 on the left, 16-31 on the right
    for i in range(15):
        col1 = f"{numbers[i]}_" + "_" * 25
        col2 = f"{numbers[i+15]}_" + "_" * 25 if i+15 < len(numbers) else ""
        print(f"{col1:<30} {col2}")

    print(f"{numbers[30]}_" + "_" * 25)

if __name__ == "__main__":
    generate_number_table()