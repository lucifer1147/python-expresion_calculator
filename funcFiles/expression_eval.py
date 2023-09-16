from funcFiles.calc_func import sin, cos, tan, asin, acos, atan, fact, add, sub, mul, div, log, exp, toDeg, toRad, e

func_dict_oneVal = {"sin": sin, "cos": cos, "tan": tan, "asin": asin, "acos": acos, "atan": atan, "!": fact, "log": log}
func_dict_twoVal = {"^": exp, "/": div, "*": mul, "+": add, "-": sub}

innerExpr = ["log3", "(", "3", "*", "3", ")"]


def expression_eval(innerExpr: list):
    oneValExpr = {}
    for item in list(func_dict_oneVal.keys()):
        for item2 in innerExpr:
            if item in item2:
                oneValExpr.update({item: innerExpr.index(item2)})

    if len(oneValExpr) > 0:
        lIdx = innerExpr.index("(")
        rIdx = innerExpr.index(")")

        currExpr = innerExpr[lIdx+1:rIdx]
    else:
        currExpr = innerExpr

    while len(currExpr) > 1:
        for item in list(func_dict_twoVal.keys()):
            if item in currExpr:
                idx = currExpr.index(item)
                currExpr.insert(idx-1, func_dict_twoVal[item](float(currExpr[idx-1]), float(currExpr[idx+1])))
                for _ in range(3):
                    currExpr.pop(idx)

    res = currExpr[0]

    if len(oneValExpr) > 0:
        for oneValOpr in list(oneValExpr.keys()):
            if oneValOpr in ["sin", "cos", "tan"]:
                res = func_dict_oneVal[oneValOpr](toRad(float(res)))
            elif oneValOpr in ["asin", "acos", "atan"]:
                res = toDeg(func_dict_oneVal[oneValOpr](float(res)))
            elif oneValOpr in ['!']:
                res = func_dict_oneVal['!'](float(res))
            else:
                try:
                    base = float(innerExpr[oneValExpr["log"]][-1])
                except ValueError:
                    base = e
                res = func_dict_oneVal[oneValOpr](float(res), base)

    return res
