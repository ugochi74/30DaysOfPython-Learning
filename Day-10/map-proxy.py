from types import MappingProxyType

d = {"a": 1}
readonly = MappingProxyType(d)
d["a"] = 51



print("Read-only view contents:", readonly)

# 2. Test reading a value
print(f"Reading key 'a': {readonly['a']}")

# 3. Test its read-only protection using a try/except block
try:
    readonly["a"] = 42
except TypeError as e:
    print(f"Write blocked as expected! Error: {e}")