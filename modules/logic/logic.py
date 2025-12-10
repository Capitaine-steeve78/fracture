# module/logic/logic.py

class Logic:
    def __init__(self):
        self.skip = False
        self.stack = []

    @staticmethod
    def eval_expr(expr, variables):
        """
        Évalue une expression simple : =, >, <, !
        variables : dictionnaire des variables
        """
        # Remplacer les variables par leurs valeurs
        for var_name, value in variables.items():
            expr = expr.replace(var_name, f"'{value}'")

        # Transformations simples pour ton langage
        expr = expr.replace("=", "==")  # = devient ==
        expr = expr.replace("!==", "!=")  # sécurité pour !=
        expr = expr.replace("!=", "!=")  # laisse passer !=

        # Utilisation de eval pour évaluer la condition
        try:
            return bool(eval(expr))
        except (NameError, SyntaxError, TypeError, ValueError):
            return False

    def if_(self, expr, variables):
        result = self.eval_expr(expr, variables)
        self.stack.append(result)
        self.skip = not result

    def else_(self):
        if self.stack:
            last = self.stack[-1]
            self.skip = last  # inverse le skip

    def end(self):
        if self.stack:
            self.stack.pop()
            self.skip = False


logic = Logic()
