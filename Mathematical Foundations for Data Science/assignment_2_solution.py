import math
import sys


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 90)
    print(f" {title}")
    print("=" * 90 + "\n")


def print_row(headers, values):
    """Print one formatted table row for iterative optimizer output."""
    widths = [max(len(h), 12) for h in headers]
    row = " | ".join(f"{str(v):>{w}}" for v, w in zip(values, widths))
    print(row)


def print_table_header(headers):
    """Print iterative table header."""
    widths = [max(len(h), 12) for h in headers]
    header = " | ".join(f"{h:>{w}}" for h, w in zip(headers, widths))
    divider = "-+-".join("-" * w for w in widths)
    print(header)
    print(divider)


# ============================================================================
# PROBLEM 1: Gradient Descent with Adam Optimizer
# ============================================================================
def problem_1_adam():
    print_section("PROBLEM 1: Adam Optimizer for f(x, y) = x^2 + y^2")

    # Given settings
    x = -2.0
    y = 2.0
    alpha = 0.1
    beta1 = 0.9
    beta2 = 0.9
    eps = 1e-8
    max_epochs = 50

    # Adam state variables
    m_x = 0.0
    m_y = 0.0
    v_x = 0.0
    v_y = 0.0

    print("Initial settings:")
    print(f"x0 = {x}, y0 = {y}")
    print(f"alpha = {alpha}, beta1 = {beta1}, beta2 = {beta2}, eps = {eps}, epochs = {max_epochs}\n")

    headers = ["epoch", "x", "y", "f(x,y)", "grad_x", "grad_y"]
    print_table_header(headers)

    for t in range(1, max_epochs + 1):
        # Gradient for f(x, y) = x^2 + y^2
        g_x = 2.0 * x
        g_y = 2.0 * y

        # Update biased first moment estimate
        m_x = beta1 * m_x + (1.0 - beta1) * g_x
        m_y = beta1 * m_y + (1.0 - beta1) * g_y

        # Update biased second raw moment estimate
        v_x = beta2 * v_x + (1.0 - beta2) * (g_x ** 2)
        v_y = beta2 * v_y + (1.0 - beta2) * (g_y ** 2)

        # Bias correction
        m_x_hat = m_x / (1.0 - (beta1 ** t))
        m_y_hat = m_y / (1.0 - (beta1 ** t))
        v_x_hat = v_x / (1.0 - (beta2 ** t))
        v_y_hat = v_y / (1.0 - (beta2 ** t))

        # Parameter update
        x = x - alpha * m_x_hat / (math.sqrt(v_x_hat) + eps)
        y = y - alpha * m_y_hat / (math.sqrt(v_y_hat) + eps)

        f_val = x ** 2 + y ** 2

        # Print first 10, then every 5th epoch, and last epoch
        if t <= 10 or t % 5 == 0 or t == max_epochs:
            print_row(
                headers,
                [
                    t,
                    f"{x:.8f}",
                    f"{y:.8f}",
                    f"{f_val:.10f}",
                    f"{g_x:.8f}",
                    f"{g_y:.8f}",
                ],
            )

    print("\nFinal Adam result:")
    print(f"x* = {x:.10f}, y* = {y:.10f}")
    print(f"f(x*, y*) = {x ** 2 + y ** 2:.12f}")

    return x, y, x ** 2 + y ** 2


# ============================================================================
# PROBLEM 2: Gradient Descent with AdaGrad Optimizer
# ============================================================================
def problem_2_adagrad():
    print_section("PROBLEM 2: AdaGrad Optimizer for f(x, y) = x^2 + y^2")

    # Given settings
    x = -2.0
    y = 2.0
    alpha = 0.1
    eps = 1e-8
    max_epochs = 50

    # AdaGrad accumulators
    g2_x = 0.0
    g2_y = 0.0

    print("Initial settings:")
    print(f"x0 = {x}, y0 = {y}")
    print(f"alpha = {alpha}, eps = {eps}, epochs = {max_epochs}\n")

    headers = ["epoch", "x", "y", "f(x,y)", "acc_g2_x", "acc_g2_y"]
    print_table_header(headers)

    for t in range(1, max_epochs + 1):
        # Gradient for f(x, y) = x^2 + y^2
        g_x = 2.0 * x
        g_y = 2.0 * y

        # Accumulate squared gradients
        g2_x += g_x ** 2
        g2_y += g_y ** 2

        # Parameter update
        x = x - alpha * g_x / (math.sqrt(g2_x) + eps)
        y = y - alpha * g_y / (math.sqrt(g2_y) + eps)

        f_val = x ** 2 + y ** 2

        # Print first 10, then every 5th epoch, and last epoch
        if t <= 10 or t % 5 == 0 or t == max_epochs:
            print_row(
                headers,
                [
                    t,
                    f"{x:.8f}",
                    f"{y:.8f}",
                    f"{f_val:.10f}",
                    f"{g2_x:.8f}",
                    f"{g2_y:.8f}",
                ],
            )

    print("\nFinal AdaGrad result:")
    print(f"x* = {x:.10f}, y* = {y:.10f}")
    print(f"f(x*, y*) = {x ** 2 + y ** 2:.12f}")

    return x, y, x ** 2 + y ** 2


# ============================================================================
# PROBLEM 3: Lagrange Multipliers
# ============================================================================
def problem_3_lagrange():
    print_section("PROBLEM 3: Lagrange Multipliers for constrained minimization")

    print("Objective function: f(x, y) = x + 2y")
    print("Constraint: g(x, y) = x^2 + y^2 = 4")
    print("Initial guess (given): (0, 0)\n")

    print("Lagrangian:")
    print("L(x, y, lambda) = x + 2y + lambda(x^2 + y^2 - 4)\n")

    print("Stationary equations:")
    print("dL/dx = 1 + 2lambda x = 0  =>  x = -1/(2lambda)")
    print("dL/dy = 2 + 2lambda y = 0  =>  y = -1/lambda")
    print("dL/dlambda = x^2 + y^2 - 4 = 0\n")

    # Substitute x and y into constraint:
    # (1/(4*lambda^2)) + (1/lambda^2) = 4
    # (5/4) * (1/lambda^2) = 4
    # lambda^2 = 5/16
    lambda_abs = math.sqrt(5.0) / 4.0
    lambda_1 = lambda_abs
    lambda_2 = -lambda_abs

    # Candidate 1
    x1 = -1.0 / (2.0 * lambda_1)
    y1 = -1.0 / lambda_1
    f1 = x1 + 2.0 * y1

    # Candidate 2
    x2 = -1.0 / (2.0 * lambda_2)
    y2 = -1.0 / lambda_2
    f2 = x2 + 2.0 * y2

    print(f"lambda solutions: +sqrt(5)/4 = {lambda_1:.10f}, -sqrt(5)/4 = {lambda_2:.10f}\n")

    print("Candidate points and function values:")
    print(f"Point 1: (x, y) = ({x1:.10f}, {y1:.10f}), f = {f1:.10f}")
    print(f"Point 2: (x, y) = ({x2:.10f}, {y2:.10f}), f = {f2:.10f}\n")

    if f1 < f2:
        x_min, y_min, f_min = x1, y1, f1
        x_max, y_max, f_max = x2, y2, f2
    else:
        x_min, y_min, f_min = x2, y2, f2
        x_max, y_max, f_max = x1, y1, f1

    print("Conclusion:")
    print(f"Minimum value is f_min = {f_min:.10f} at (x, y) = ({x_min:.10f}, {y_min:.10f})")
    print(f"Maximum value is f_max = {f_max:.10f} at (x, y) = ({x_max:.10f}, {y_max:.10f})")

    return x_min, y_min, f_min


# ============================================================================
# MAIN EXECUTION
# ============================================================================
if __name__ == "__main__":
    print("\n" + "#" * 90)
    print(" " * 22 + "MATHEMATICAL FOUNDATIONS FOR DATA SCIENCE")
    print(" " * 33 + "ASSIGNMENT 2 SOLUTIONS")
    print("#" * 90)
    print("\nName: [Your Name]")
    print("ID: [Your ID]")
    print("Date: 11 April 2026")
    print("Due Date: 16 April 2026")

    try:
        adam_result = problem_1_adam()
        adagrad_result = problem_2_adagrad()
        lagrange_result = problem_3_lagrange()

        print_section("SUMMARY OF SOLUTIONS")
        print("Problem 1: Adam optimizer implemented for 50 epochs")
        print(f"  Final point: ({adam_result[0]:.10f}, {adam_result[1]:.10f})")
        print(f"  Final objective: {adam_result[2]:.12f}")

        print("Problem 2: AdaGrad optimizer implemented for 50 epochs")
        print(f"  Final point: ({adagrad_result[0]:.10f}, {adagrad_result[1]:.10f})")
        print(f"  Final objective: {adagrad_result[2]:.12f}")

        print("Problem 3: Lagrange multipliers solved analytically")
        print(f"  Minimum point: ({lagrange_result[0]:.10f}, {lagrange_result[1]:.10f})")
        print(f"  Minimum value: {lagrange_result[2]:.10f}")

        print("\n" + "#" * 90)
        print(" " * 31 + "ALL PROBLEMS COMPLETED")
        print("#" * 90 + "\n")

    except Exception as exc:
        print(f"\nError occurred: {exc}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        sys.exit(1)
