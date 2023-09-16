expr = "sin(1*2*3*4)"
oprLi = ["+", "-", "/", "*", "(", ")"]


def expr_maker(expr, oprLi):
    oprIdx = []
    for idx, item in enumerate(expr):
        if item in oprLi:
            oprIdx.append(idx)

    exprNew = list(expr)

    idx = 0
    forbiddenIdx = []
    while len(oprIdx) > 0:
        if exprNew[idx] in oprLi and idx not in forbiddenIdx:
            forbiddenIdx.append(idx+1)
            oprIdx.pop(0)

            exprNew.insert(idx, " ")
            exprNew.insert(idx+2, " ")

        idx += 1

    for idx, item in enumerate(exprNew):
        try:
            if exprNew[idx] == " " and exprNew[idx+1] == " ":
                exprNew.pop(idx)
        except IndexError:
            break

    exprStr = "".join(exprNew)
    finExpr = exprStr.split(" ")

    return finExpr


def innermost_expr_maker(exprLi):
    rBrIdx = []
    lBrIdx = []

    for idx, item in enumerate(exprLi):
        if item == "(":
            lBrIdx.append(idx)
        elif item == ")":
            rBrIdx.append(idx)

    if len(lBrIdx) > 0:
        rBrIdx = exprLi.index(")", lBrIdx[-1])
        lBrIdx = lBrIdx[-1]

        if exprLi[lBrIdx-1] in ["sin", "cos", "tan", "asin", "acos", "atan"]:
            lBrIdx -= 1
        if "log" in exprLi[lBrIdx-1]:
            lBrIdx -= 1
        try:
            if exprLi[rBrIdx+1] == "!":
                rBrIdx += 1
        except IndexError:
            rBrIdx = rBrIdx

        return exprLi[lBrIdx:rBrIdx + 1]
    else:
        return exprLi
