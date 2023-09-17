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

        self.innerExprOrg_ = innermost_expr_maker(expressionLi)
        if self.innerExprOrg_[0] == "(" and self.innerExprOrg_[-1] == ")":
            self.innerExpr_ = self.innerExprOrg_[1:-1]
        else:
            self.innerExpr_ = self.innerExprOrg_

        return self.innerExpr_

    def get_inner_expr_result(self, innerExpression: list = None):
        if innerExpression is None:
            innerExpression = self.innerExpr_

        self.result_ = str(expression_eval(innerExpression))
        return self.result_

    def get_replaced_expression(self, expression: list = None, innerExprOriginal: list = None, result: str = None):
        if expression is None:
            expression = self.expression_
        if innerExprOriginal is None:
            innerExprOriginal = self.innerExprOrg_
        if result is None:
            result = self.result_

        self.replaced_expression_ = list(" ".join(expression).replace(" ".join(innerExprOriginal), result).split(" "))
        return self.replaced_expression_

    def __len__(self):
        return len(self.expression_)


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
