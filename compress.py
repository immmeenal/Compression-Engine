import zlib, base64
data = open('demo.txt','r').read()
data_bytes=bytes(data,'utf-8')
compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
decode_data = compressed_data.decode('utf-8')
compressed_file = open('compress.txt','w')
compressed_file.write(decode_data)

decompress_data = zlib.decompress(base64.b64decode(compressed_data))
print(decompress_data)
