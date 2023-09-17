from funcFiles.expression_maker import expr_maker, innermost_expr_maker
from funcFiles.expression_eval import expression_eval

inp = str(input("Enter The Expression: "))
expr = f"({inp})"
exprMade = expr_maker(expr, oprLi=["+", "-", "/", "*", "(", ")", "^"])
print("The Expression you inputted:", "".join(exprMade)[1:-1])


class Expression:
    def __init__(self, expression: list):

        for i in range(len(expression)):
            try:
                expression.remove("")
            except ValueError:
                break

        self.expression_ = expression

    def get_expression_list(self):
        return self.expression_

    def __len__(self):
        return len(self.expression_)


while True:
    exprMade = Expression(exprMade)
    innerExpr = innermost_expr_maker(exprMade.get_expression_list())

    if innerExpr[0] == "(" and innerExpr[-1] == ")":
        innerExprN = innerExpr[1:-1]
    else:
        innerExprN = innerExpr

    res = str(expression_eval(innerExprN))
    if len(exprMade) > 1:
        exprMade = list(" ".join(exprMade.get_expression_list()).replace(" ".join(innerExpr), str(res)).split(" "))
    else:
        break

print("Result:", innerExprN[0])
