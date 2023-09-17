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

    def get_inner_expr(self, expressionLi: list = None):
        if expressionLi is None:
            expressionLi = self.expression_

        self.innerExprOrg = innermost_expr_maker(expressionLi)
        if self.innerExprOrg[0] == "(" and self.innerExprOrg[-1] == ")":
            self.innerExpr = self.innerExprOrg[1:-1]
        else:
            self.innerExpr = self.innerExprOrg

        return self.innerExpr

    def __len__(self):
        return len(self.expression_)


while True:
    exprMade = Expression(exprMade)
    innerExpr = exprMade.get_inner_expr(exprMade.expression_)

    res = str(expression_eval(innerExpr))
    if len(exprMade) > 1:
        exprMade = list(" ".join(exprMade.expression_).replace(" ".join(exprMade.innerExprOrg), str(res)).split(" "))
    else:
        break

print("Result:", innerExpr[0])
