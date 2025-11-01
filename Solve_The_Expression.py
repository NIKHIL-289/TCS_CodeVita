def pattern_to_bin(p):
    return ''.join('1' if c != ' ' else '0' for row in p for c in row)

def read_pattern():
    return [input() for _ in range(3)]

n = int(input())
mapping = {}

for _ in range(n):
    pat = read_pattern()
    symbol = input().strip()   
    mapping[pattern_to_bin(pat)] = symbol

m = int(input())  
expr_rows = [input() for _ in range(3)]

expr = ""
for i in range(0, m * 3, 3):
    block = [r[i:i+3] for r in expr_rows]
    key = pattern_to_bin(block)
    expr += mapping[key]

result = eval(expr)

print(result)
