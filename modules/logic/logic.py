# 2025 Copyright, FractureV1 By Capitaine-steeve78 official repo : https://github.com/Capitaine-steeve78/fracture

# modules/logic/logic.py

class Logic:
    
    def __init__(self):
        self.stack = []
        
        self.skip = False

    # ======================
    # Evaluation d'expression
    # ======================

    def eval_expr(self, expr, variables):
        """
        Évalue une expression du type:
        'x < 10'
        'value != 3'
        'a = b'
        """

        tokens = expr.split()
        if len(tokens) != 3:
            return False

        left, op, right = tokens

        if left in variables:
            left = variables[left]

        if right in variables:
            right = variables[right]

        left = self._convert_value(left)
        right = self._convert_value(right)

        match op:
            case "<":  return left < right
            case ">":  return left > right
            case "=":  return left == right
            case "!=": return left != right

        return False

    @staticmethod
    def _convert_value(value):
        """Convertit en nombre si possible, sinon retourne la chaîne."""
        try:
            return float(value)
        except ValueError:
            return str(value)

    # ======================
    # IF
    # ======================
    def if_(self, expr, variables):
        result = self.eval_expr(expr, variables)
        self.stack.append(result)

        self.skip = not result

    # ======================
    # ELSE
    # ======================
    def else_(self):
        if not self.stack:
            return

        last = self.stack[-1]

        self.skip = last

    # ======================
    # END
    # ======================
    def end(self):
        if self.stack:
            self.stack.pop()

        self.skip = False


logic = Logic()
