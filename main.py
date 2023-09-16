from expression_maker import expr_maker, innermost_expr_maker
from expression_eval import expression_eval

input = str(input("Enter The Expression: "))
expr = f"({input})"
exprMade = expr_maker(expr, oprLi=["+", "-", "/", "*", "(", ")", "^"])
print("The Expression you inputted:", "".join(exprMade)[1:-1])

for i in range(len(exprMade)):
    try:
        exprMade.remove("")
    except ValueError:
        break

while True:
    innerExpr = innermost_expr_maker(exprMade)

    if innerExpr[0] == "(" and innerExpr[-1] == ")":
        innerExprN = innerExpr[1:-1]
    else:
        innerExprN = innerExpr

    res = str(expression_eval(innerExprN))
    if len(exprMade) > 1:
        exprMade = list(" ".join(exprMade).replace(" ".join(innerExpr), str(res)).split(" "))
    else:
        break

print("Result:", innerExprN[0])
