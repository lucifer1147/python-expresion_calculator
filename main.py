from funcFiles.expression_maker import expr_maker
from funcFiles.expressionClass import Expression

inp = str(input("Enter The Expression: "))
expr = f"({inp})"
exprMade = expr_maker(expr, oprLi=["+", "-", "/", "*", "(", ")", "^"])
print("The Expression you inputted:", "".join(exprMade)[1:-1])

while True:
    exprMade = Expression(exprMade)
    innerExpr = exprMade.get_inner_expr()
    res = exprMade.get_inner_expr_result()
    exprMadeReplaced = exprMade.get_replaced_expression()

    if len(exprMadeReplaced) > 1:
        exprMade = exprMadeReplaced
        continue
    else:
        result = exprMadeReplaced[0]
        break

print("Result:", result)
