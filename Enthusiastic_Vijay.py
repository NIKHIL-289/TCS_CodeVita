digits = {
    " _ | ||_|": "0",
    "     |  |": "1",
    " _  _||_ ": "2",
    " _  _| _|": "3",
    "   |_|  |": "4",
    " _ |_  _|": "5",
    " _ |_ |_|": "6",
    " _   |  |": "7",
    " _ |_||_|": "8",
    " _ |_| _|": "9"
}

# Input
rows = [input() for _ in range(3)]
n = int(input())  # number of digits

# Decode
res = ""
for i in range(0, n * 3, 3):
    key = rows[0][i:i+3] + rows[1][i:i+3] + rows[2][i:i+3]
    res += digits.get(key, "?")

print(int(res))
