import gzip

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            f_out.writelines(f_in)

input_file = 'example.txt'
compressed_file = 'example.txt.gz'

compress_file(input_file, compressed_file)
print(f"Compression successful. Compressed file saved as {compressed_file}")




