import multiprocessing

# Function to process data in parallel
def process_data(data_chunk):
    result = []
    for item in data_chunk:
        # Perform some computation on each item in the data chunk
        # Example: Calculate square of each number
        result.append(item ** 2)
    return result

if __name__ == "__main__":
    # Define the dataset
    dataset = list(range(1, 1000001))  # Example: List of numbers from 1 to 1 million

    # Split the dataset into chunks for parallel processing
    num_processes = multiprocessing.cpu_count()  # Get the number of CPU cores
    chunk_size = len(dataset) // num_processes
    data_chunks = [dataset[i:i+chunk_size] for i in range(0, len(dataset), chunk_size)]

# Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_processes)

    # Perform parallel processing on each data chunk
    results = pool.map(process_data, data_chunks)

    # Concatenate results from all processes
    final_result = []
    for result in results:
        final_result.extend(result)

    # Close the pool
    pool.close()
    pool.join()

    # Output the final result
    print("Final result:", final_result[:10], "...")
