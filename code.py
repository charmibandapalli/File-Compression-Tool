import zlib

def compress_file(file):
    with open(file, 'rb') as f:
        data = f.read()
    compressed = zlib.compress(data)
    with open(file + ".zlib", 'wb') as f:
        f.write(compressed)

compress_file("example.txt")
