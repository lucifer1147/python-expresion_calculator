from funcFiles.expression_maker import expr_maker
from funcFiles.expressionClass import Expression

inp = str(input("Enter The Expression: "))
expr = f"({inp})"
exprMade = expr_maker(expr, oprLi=["+", "-", "/", "*", "(", ")", "^"])
print("The Expression you inputted:", "".join(exprMade)[1:-1])

while True:
    exprMade = Expression(exprMade)
    exprMade.get_inner_expr()
    exprMade.get_inner_expr_result()

    exprMadeReplaced = exprMade.get_replaced_expression()
    exprMade = exprMadeReplaced

    result = exprMadeReplaced[0]

    if len(exprMadeReplaced) > 1:
        continue
    else:
        break

print("Result:", result)
