import sympy

def calculate_derivative(expr, var, order=1):
    """
    Calculate the derivative of an expression.
    
    Parameters:
        expr (str): The mathematical expression as a string.
        var (str): The variable with respect to which to differentiate.
        order (int): The order of the derivative (default is 1).
    
    Returns:
        str: The derivative as a string.
    """
    try:
        x = sympy.symbols(var)
        parsed_expr = sympy.sympify(expr)  # Convert string to sympy expression
        derivative = sympy.diff(parsed_expr, x, order)  # Compute the derivative
        return str(derivative)
    except Exception as e:
        return f"Error: {e}"


def maclaurin_series(expr, var, terms=5):
    """
    Compute the Maclaurin series (Taylor series at x=0).
    
    Parameters:
        expr (str): The mathematical expression as a string.
        var (str): The variable in the expression.
        terms (int): The number of terms in the series (default is 5).
    
    Returns:
        str: The Maclaurin series as a string.
    """
    try:
        x = sympy.symbols(var)
        parsed_expr = sympy.sympify(expr)
        series = sympy.series(parsed_expr, x, 0, terms)  # Maclaurin series
        return str(series)
    except Exception as e:
        return f"Error: {e}"


def taylor_series(expr, var, point, terms=5):
    """
    Compute the Taylor series around a specific point.
    
    Parameters:
        expr (str): The mathematical expression as a string.
        var (str): The variable in the expression.
        point (float): The point around which to expand the series.
        terms (int): The number of terms in the series (default is 5).
    
    Returns:
        str: The Taylor series as a string.
    """
    try:
        x = sympy.symbols(var)
        parsed_expr = sympy.sympify(expr)
        series = sympy.series(parsed_expr, x, point, terms)  # Taylor series at a point
        return str(series)
    except Exception as e:
        return f"Error: {e}"
