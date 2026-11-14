# TI-84 Plus CE Python Math Toolkit

A collection of lightweight Python math utilities designed for the **Texas Instruments TI-84 Plus CE Python** graphing calculator.

These programs simplify common algebra problems by providing guided input, step-by-step result screens, and easy-to-read answers.

The toolkit is designed specifically for the TI-84 Plus CE Python's limited memory and small display.

## Programs

| Program | Description |
|---|---|
| **QUADUTIL** | Convert between quadratic equation forms and calculate important properties |
| **LINEUTIL** | Find equations of parallel and perpendicular lines |
| **QUADFORM** | Solve quadratic equations using the quadratic formula |

Each program operates independently, allowing users to install only the utilities they need.

---

## Installation

### Requirements

- TI-84 Plus CE Python Edition calculator
- TI Connect CE software
- USB cable for connecting the calculator to a computer

### Installing the programs

1. Download the Python program files from this repository.
2. Connect your TI-84 Plus CE Python to your computer using USB.
3. Open **TI Connect CE**.
4. Transfer the desired Python files to the calculator.
5. On the calculator, open the Python application.
6. Select the program you want to run.

**Note:** These utilities use the calculator's built-in Python environment and the `ti_system` module. They are not intended for the standard non-Python TI-84 Plus CE.

---

# 1. QUADUTIL — Quadratic Equation Utility

QUADUTIL calculates quadratic equations in multiple forms and displays their important properties.

It supports four methods of entering a quadratic function.

### Main menu

```text
QUADRATIC UTILITY
1 FROMSTD
2 FROMVERT
3 FROMINT
4 FROM3PTS
5 EXIT
```

### Option 1: FROMSTD

Enter a quadratic equation in standard form:

**y = ax² + bx + c**

Example:

```text
FROMSTD
a: 1
b: -6
c: 8
```

The program calculates:

- Standard form
- Vertex form
- Factored form (when real roots exist)
- Vertex coordinates
- X-intercepts
- Y-intercept
- Axis of symmetry
- Direction of opening
- Minimum or maximum value

### Option 2: FROMVERT

Construct a quadratic equation using its vertex and one additional point.

Required inputs:

- Vertex coordinates (h, k)
- Another point (x, y)

Example:

```text
FROMVERT
h: 2
k: -3
x: 4
y: 5
```

The program calculates the standard-form coefficients and all associated properties.

### Option 3: FROMINT

Construct a quadratic equation using its y-intercept and two x-intercepts.

Example:

```text
FROMINT
Y-int: 8
X1: 2
X2: 4
```

The resulting equation is:

**y = x² - 6x + 8**

Both x-intercepts must be nonzero for this input method to determine a unique quadratic.

### Option 4: FROM3PTS

Construct a quadratic equation using three points.

Example:

```text
FROM3PTS
X1: 0
Y1: 8
X2: 2
Y2: 0

X3: 4
Y3: 0
```

The program calculates the quadratic equation passing through all three points.

The three x-coordinates must be distinct, and the points must define a quadratic rather than a straight line.

### Output screens

QUADUTIL organizes its results into three screens.

**Screen 1 — Equations**

```text
=== EQUATIONS ===
STANDARD:
y=1x^2-6x+8
VERTEX:
y=1(x-3)^2-1
FACTORED:
y=1(x-2)(x-4)
```

**Screen 2 — Points**

```text
=== POINTS ===
VERTEX:
(3,-1)
Y-INTERCEPT:
(0,8)
X-INTERCEPTS:
(2,0)
(4,0)
```

**Screen 3 — Properties**

```text
=== PROPERTIES ===
AXIS: x=3
OPENS: UP
MIN: -1
```

Press ENTER to advance between screens.

---

# 2. LINEUTIL — Parallel and Perpendicular Lines

LINEUTIL calculates the equation of a line passing through a specified point that is either parallel or perpendicular to another line.

It supports integer, decimal, and fractional input.

### Main menu

```text
LINE UTILITY
--------------
1 PARALLEL
2 PERPENDICULAR
3 EXIT
```

### Option 1: PARALLEL

Find the equation of a line parallel to another line.

**Example problem:**

Find the equation of the line passing through (5, 15) that is parallel to:

**y = 4x - 1**

Enter:

```text
PARALLEL
POINT:
x: 5
y: 15
ORIGINAL LINE:
Slope: 4
```

Output:

```text
=== RESULT ===
SLOPE: 4
Y-INT: -5

SLOPE-INTERCEPT:
y=4x-5
```

Parallel lines have equal slopes.

### Option 2: PERPENDICULAR

Find the equation of a line perpendicular to another line.

**Example problem:**

Find the equation of the line passing through (35, 2) that is perpendicular to:

**y = -7x**

Enter:

```text
PERPENDICULAR
POINT:
x: 35
y: 2
ORIGINAL LINE:
Slope: -7
```

Output:

```text
=== RESULT ===
SLOPE: 1/7
Y-INT: -3

SLOPE-INTERCEPT:
y=1/7x-3
```

Perpendicular lines have slopes that are negative reciprocals of one another, except for horizontal and vertical lines.

### Fraction support

LINEUTIL accepts fractions directly:

```text
1/2
-3/4
7/8
```

Fractions are automatically converted for calculation and simplified for output.

For example:

| Input | Output |
|---|---|
| `2/4` | `1/2` |
| `-6/8` | `-3/4` |
| `8/2` | `4` |
| `-7` (perpendicular slope) | `1/7` |

The fraction formatter uses numerical approximation with denominators up to 1000. It is intended for typical algebra problems rather than arbitrary-precision symbolic mathematics.

### Additional output

LINEUTIL also provides the equation in point-slope form on a second screen.

**Current limitation:** The utility accepts the original line's slope, not the full equation. Vertical original lines are not directly supported as inputs.

---

# 3. QUADFORM — Quadratic Formula Solver

QUADFORM solves quadratic equations using the quadratic formula.

Given:

**ax² + bx + c = 0**

The program calculates:

**x = (-b ± √(b² - 4ac)) / (2a)**

### Features

- Integer input
- Decimal input
- Fraction input
- Discriminant calculation
- Two real roots
- Repeated real roots
- Detection of complex roots
- Simplified fractional output when possible
- Decimal approximations
- Paginated results

### Example 1: Two real roots

Solve:

**2x² - 7x + 3 = 0**

Enter:

```text
QUADRATIC FORMULA
ax^2+bx+c=0

a: 2
b: -7
c: 3
```

Output:

```text
=== RESULTS ===
DISCRIMINANT:
25

TWO REAL ROOTS:
x1=1/2
x2=3
```

### Example 2: Irrational roots

Solve:

**x² - 2 = 0**

Enter:

```text
a: 1
b: 0
c: -2
```

The mathematical solutions are:

**x = ±√2**

The current version calculates numerical approximations.

```text
DECIMAL VALUES:
x1=-1.414214
x2=1.414214
```

### Example 3: No real roots

Solve:

**x² + 4x + 8 = 0**

Enter:

```text
a: 1
b: 4
c: 8
```

Output:

```text
=== RESULTS ===
DISCRIMINANT:
-16

NO REAL ROOTS
Complex solutions
```

The current version identifies complex roots but does not calculate their values.

### Planned improvement: Exact radical formatting

A future version is intended to display simplified radical expressions such as:

```text
x1=(-3-sqrt(17))/4
x2=(-3+sqrt(17))/4
```

Rather than displaying only decimal approximations.

**Important:** Exact radical formatting and complex-number solutions are not yet implemented.

---

# Limitations

These utilities are intended primarily for introductory and intermediate algebra.

Current limitations include:

- QUADUTIL displays rounded decimal values rather than exact symbolic expressions.
- LINEUTIL's fraction conversion is approximate.
- LINEUTIL does not accept vertical original lines directly.
- QUADFORM does not yet simplify irrational solutions into exact radicals.
- QUADFORM does not yet calculate complex-number solutions.
- Input validation is basic.
- Extremely large or precise values may produce rounding errors.

These programs are educational tools and should not be considered full computer algebra systems.

---

# Future Development

Possible additions to the toolkit include:

- Exact radical simplification
- Complex-number solutions
- General linear equation solver
- Systems of linear equations
- Function composition and inverses
- Polynomial factoring
- Radical simplification
- Additional fraction utilities

The goal is to expand the toolkit while preserving compatibility with the TI-84 Plus CE Python's memory limitations.

---

**Built for students who want quick, straightforward algebra tools on their TI-84 Plus CE Python.**