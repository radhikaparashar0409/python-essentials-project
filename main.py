# COURSE EVALUATION PROJECT: CORE ENGINE
# Built to align with Units 3, 4, and 5 syllabus
# ==========================================

def display_user_dashboard():
    print("\n" + "="*35)
    print(" CORE NUMERIC & ARRAY ANALYTICS ")
    print("="*35)
    print("1. Process Factorial Calculation")
    print("2. Construct Fibonacci Sequence")
    print("3. Convert Base (Decimal to Binary)")
    print("4. Find Greatest Common Divisor (GCD)")
    print("5. Filter Prime Numbers by Boundary")
    print("6. Execute Array Transformation Matrix")
    print("7. Terminate Application Workspace")
    print("="*35)

# --- UNIT 3 ALGORITHMS ---
def compute_integer_factorial(target_value):
    if target_value < 0:
        return "Operation error: Undefined for negative parameters."
    running_product = 1
    for current_multiplier in range(1, target_value + 1):
        running_product *= current_multiplier
    return running_product

def generate_fibonacci_series(total_elements):
    if total_elements <= 0:
        return []
    elif total_elements == 1:
        return [0]
    
    fibonacci_data_store = [0, 1]
    while len(fibonacci_data_store) < total_elements:
        next_summation = fibonacci_data_store[-1] + fibonacci_data_store[-2]
        fibonacci_data_store.append(next_summation)
    return fibonacci_data_store

def transform_decimal_to_binary(decimal_integer):
    if decimal_integer == 0:
        return "0"
    binary_string_buffer = ""
    temporary_register = decimal_integer
    while temporary_register > 0:
        binary_string_buffer = str(temporary_register % 2) + binary_string_buffer
        temporary_register = temporary_register // 2
    return binary_string_buffer

# --- UNIT 4 ALGORITHMS ---
def calculate_euclidean_gcd(first_param, second_param):
    while second_param:
        first_param, second_param = second_param, first_param % second_param
    return abs(first_param)

def filter_primes_in_range(lower_limit, upper_limit):
    validated_primes = []
    for candidate_number in range(max(2, lower_limit), upper_limit + 1):
        primality_flag = True
        for divisor in range(2, int(candidate_number ** 0.5) + 1):
            if candidate_number % divisor == 0:
                primality_flag = False
                break
        if primality_flag:
            validated_primes.append(candidate_number)
    return validated_primes

# --- UNIT 5 ALGORITHMS ---
def evaluate_array_metrics(raw_integer_list):
    if not raw_integer_list:
        return "System matrix payload is completely empty."
    
    # Peak Value Extraction
    peak_maximum = raw_integer_list[0]
    for element in raw_integer_list:
        if element > peak_maximum:
            peak_maximum = element
            
    # Redundant Element Stripping
    unique_element_registry = []
    for element in raw_integer_list:
        if element not in unique_element_registry:
            unique_element_registry.append(element)
            
    # Mirror Sequence Reversal
    inverted_sequence = raw_integer_list[::-1]
    
    return {
        "Raw Structural Input": raw_integer_list,
        "Peak Maximum Extracted": peak_maximum,
        "Processed Unique Registry": unique_element_registry,
        "Mirror Inverse Output": inverted_sequence
    }

# --- SYSTEM MAIN CONTROL LOOP ---
def runtime_orchestrator():
    while True:
        display_user_dashboard()
        user_selection = input("Select Workspace Action (1-7): ").strip()
        
        if user_selection == '1':
            try:
                input_val = int(input("Enter an integer parameter: "))
                print(f"Output Matrix: {input_val}! = {compute_integer_factorial(input_val)}")
            except ValueError:
                print("Formatting Fault: Provide integers exclusively.")
            
        elif user_selection == '2':
            try:
                element_count = int(input("Define length of sequence: "))
                print(f"Output Matrix: {generate_fibonacci_series(element_count)}")
            except ValueError:
                print("Formatting Fault: Provide integers exclusively.")
            
        elif user_selection == '3':
            try:
                base_val = int(input("Enter base-10 value to convert: "))
                if base_val < 0:
                    print("Constraint Fault: Input cannot be negative.")
                else:
                    print(f"Output Matrix: Binary code = {transform_decimal_to_binary(base_val)}")
            except ValueError:
                print("Formatting Fault: Provide integers exclusively.")
            
        elif user_selection == '4':
            try:
                val1 = int(input("First component input: "))
                val2 = int(input("Second component input: "))
                print(f"Output Matrix: Common Factor = {calculate_euclidean_gcd(val1, val2)}")
            except ValueError:
                print("Formatting Fault: Provide integers exclusively.")
            
        elif user_selection == '5':
            try:
                low_bound = int(input("Establish entry boundary index: "))
                high_bound = int(input("Establish exit boundary index: "))
                print(f"Prime Matrix: {filter_primes_in_range(low_bound, high_bound)}")
            except ValueError:
                print("Formatting Fault: Provide integers exclusively.")
            
        elif user_selection == '6':
            array_payload = input("Enter linear arrays split by a space character (e.g., 10 20 10 50): ")
            try:
                parsed_list = [int(item) for item in array_payload.split()]
                metric_results = evaluate_array_metrics(parsed_list)
                if isinstance(metric_results, str):
                    print(metric_results)
                else:
                    print("\n=== MATRIX METRIC RUNTIME BREAKDOWN ===")
                    for descriptor, data in metric_results.items():
                        print(f"-> {descriptor}: {data}")
            except ValueError:
                print("Parse Fault: Verify numbers are broken cleanly by spaces alone.")
                    
        elif user_selection == '7':
            print("Shutting down development workspace environments cleanly. Finalized.")
            break
        else:
            print("Selection Out of Range: Choose explicitly from index range 1 to 7.")

if __name__ == "__main__":
    runtime_orchestrator()
