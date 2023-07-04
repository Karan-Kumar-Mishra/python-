import zlib
import sys
str=b'a'*45
print("size of string =>",sys.getsizeof(str))
cstr=zlib.compress(str)
print("size after compression",sys.getsizeof(cstr))
dstr=zlib.decompress(cstr)
print("Size after decompression ",sys.getsizeof(dstr))