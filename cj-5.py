import math

def generate_sin_table(start, end, num_points):
    """Generates and prints a table of x and sin(x)."""
    print(f"{'x':>10} | {'sin(x)':>10}")
    print("-" * 25)

    # We use num_points - 1 to ensure we hit the 'end' value exactly
    step = (end - start) / (num_points - 1)

    for i in range(num_points):
        x = start + (i * step)
        sin_x = math.sin(x)
        
        # Formatting to 5 decimal places for a clean table
        print(f"{x:10.5f} | {sin_x:10.5f}")

def main():
    # Define our parameters
    lower_bound = 0.0
    upper_bound = 2.0
    total_entries = 1000
    
    # Execute the table generation
    generate_sin_table(lower_bound, upper_bound, total_entries)

if __name__ == "__main__":
    main()