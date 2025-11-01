def evaluate(expr, vars_):
    try:
        return eval(expr, {}, vars_)
    except:
        return vars_.get(expr, int(expr))

def run(lines, vars_):
    i = 0
    while i < len(lines):
        parts = lines[i].split()
        cmd = parts[0]
        if cmd == "print":
            val = parts[1]
            print(vars_.get(val, val) if not val.isdigit() else int(val))
            i += 1
        elif '=' in lines[i]:
            var, expr = lines[i].split('=', 1)
            vars_[var.strip()] = evaluate(expr.strip(), vars_)
            i += 1
        elif cmd == "if":
            cond = " ".join(parts[1:])
            cond_result = bool(evaluate(cond.replace("==", "==").replace("!=", "!="), vars_))
            block, yes_block, no_block = [], [], []
            depth = 0
            i += 1
            branch = None
            while i < len(lines):
                if lines[i].startswith("if") or lines[i].startswith("for"):
                    depth += 1
                if lines[i] == "end":
                    if depth == 0:
                        break
                    else:
                        depth -= 1
                if depth == 0 and lines[i] == "Yes":
                    branch = "Yes"
                elif depth == 0 and lines[i] == "No":
                    branch = "No"
                elif branch == "Yes":
                    yes_block.append(lines[i])
                elif branch == "No":
                    no_block.append(lines[i])
                i += 1
            run(yes_block if cond_result else no_block, vars_)
            i += 1
        elif cmd == "for":
            var, start, end = parts[1], parts[2], parts[3]
            start, end = evaluate(start, vars_), evaluate(end, vars_)
            block, depth = [], 0
            i += 1
            while i < len(lines):
                if lines[i].startswith("for") or lines[i].startswith("if"):
                    depth += 1
                if lines[i] == "end":
                    if depth == 0:
                        break
                    else:
                        depth -= 1
                block.append(lines[i])
                i += 1
            for val in range(start, end + 1):
                vars_[var] = val
                run(block, vars_)
            i += 1

        else:
            i += 1

n = int(input())
lines = [input().strip() for _ in range(n)]
run(lines, {})
