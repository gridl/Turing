# -*- coding: utf-8 -*-

from maths.evaluator import Evaluator
from maths.lib import basic, trig
from tests.framework import expect

tests = [
    # basic parsing
    ("42", 42, "42"),
    ("-42", -42, "-42"),

    # basic operators
    ("2+2", 4, "2 + 2"),
    ("3*3", 9, "3 * 3"),
    ("142        -9   ", 133, "142 - 9"),
    (" 50/10", 5, "50 / 10"),
    ("72+  15", 87, "72 + 15"),
    (" 12*  4", 48, "12 * 4"),
    ("4*2.5 + 8.5+1.5 / 3.0", 19, "4 * 2.5 + 8.5 + 1.5 / 3"),
    (" 2-7", -5, "2 - 7"),
    ("2 -4 +6 -1 -1- 0 +8", 10, "2 - 4 + 6 - 1 - 1 - 0 + 8"),
    (" 2*3 - 4*5 + 6/3 ", -12, "2 * 3 - 4 * 5 + 6 / 3"),
    ("10/4", 2.5, "10 / 4"),

    # unary edge cases
    ("--5", 5, "--5"),
    ("0--5", 5, "0 - -5"),

    # basic functions
    ("ceil(pi)", 4, "ceil(pi)"),
    ("floor(e)", 2, "floor(e)"),
    ("sqrt(49)", 7, "sqrt(49)"),
    ("sqrt(2)^2", 2, "sqrt(2) ^ 2"),
    ("cos(0)", 1, "cos(0)"),
    ("sin(pi)", 0, "sin(pi)"),
    ("deg(2pi)", 360, "deg(2 * pi)"),
    ("round(asin(acos(atan(tan(cos(sin(0.5)))))),5)", 0.5, "round(asin(acos(atan(tan(cos(sin(0.5)))))), 5)"),
    ("sign(-5)", -1, "sign(-5)"),

    ("binomial(3,2)", 3, "binomial(3, 2)"),
    ("binomial(3 , 0)", 1, "binomial(3, 0)"),

    ("average([12,82,74,36,14,94])", 52, "average([12, 82, 74, 36, 14, 94])"),
    ("sum([1,8,9,6,24,54,354])", 456, "sum([1, 8, 9, 6, 24, 54, 354])"),
    ("[8,5,42,96,31,84,35] [-4]", 96, "[8, 5, 42, 96, 31, 84, 35][-4]"),
    ("[1,2,3,4][2]", 3, "[1, 2, 3, 4][2]"),
    ("[42,{x,y,z}(x*abs({x, y}(x - y)(y, z))),38][1](4,3,5)", 8,
     "[42, {x, y, z}(x * abs({x, y}(x - y)(y, z))), 38][1](4, 3, 5)"),

    ("(2+2)==4", True, "2 + 2 == 4"),
    ("vrai xor true", False, "TRUE XOR TRUE"),
    ("\"abc\"+\"def\"", "abcdef", "\"abc\" + \"def\""),

    # list operators
    ("[1,2,3]+[3,4,5]", [1, 2, 3, 3, 4, 5], "[1, 2, 3] + [3, 4, 5]"),
    ("[1,2,3]-[3,4,5]", [1, 2], "[1, 2, 3] - [3, 4, 5]"),
    ("-[1,2,3]", [3, 2, 1], "-[1, 2, 3]"),
    ("3*[1,2,3]", [1, 2, 3, 1, 2, 3, 1, 2, 3], "3 * [1, 2, 3]"),
    ("[1,2,3]&[2,3,4]", [2, 3], "[1, 2, 3] AND [2, 3, 4]"),
    ("[1,2,3]|[2,3,4]", [1, 2, 3, 4], "[1, 2, 3] OR [2, 3, 4]"),
    ("[1,2,3]xor[3,4,5]", [1, 2, 4, 5], "[1, 2, 3] XOR [3, 4, 5]"),

    # complex lambda tests
    ("map({a}({a,b}(b*a)(2,a)),[1,2,3,4,5,6])", [2, 4, 6, 8, 10, 12],
     "map({a}({a, b}(b * a)(2, a)), [1, 2, 3, 4, 5, 6])"),
    ("-filter({a}(a<0),[-2,-1,0,1,2])", [-1, -2], "-filter({a}(a < 0), [-2, -1, 0, 1, 2])"),

    # leo
    ("gcd(248,4584)", 8, "gcd(248, 4584)"),
    ("lcm(904,1356)", 2712, "lcm(904, 1356)"),

    ("slice([1,2,3,4,5,6,7,8],2,6)", [3, 4, 5, 6], "slice([1, 2, 3, 4, 5, 6, 7, 8], 2, 6)"),

    ("round(variance([2.75,1.75,1.25,0.25,0.5,1.25,3.5]),2)", 1.18,
     "round(variance([2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]), 2)"),
    ("round(variance_sample([2.75,1.75,1.25,0.25,0.5,1.25,3.5]),2)", 1.37,
     "round(variance_sample([2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]), 2)"),
    ("harmonic_mean([2.5,3,10])", 3.6, "harmonic_mean([2.5, 3, 10])"),

    ("5e+99/2e45", 2.5e54, "5e99 / 2e45"),
    ("5e-99/2e-45", 2.5e-54, "5e-99 / 2e-45"),

    # complex
    ("3sqrt(-4)", 6j, "3 * sqrt(-4)"),

    ("(2+3i)+(4+5i)", 6 + 8j, "(2 + 3i) + (4 + 5i)"),
    ("(2+3i)*(4+5i)", -7 + 22j, "(2 + 3i) * (4 + 5i)"),
    ("(2+3i)^2", -5 + 12j, "(2 + 3i) ^ 2"),
    ("arg(2+3i) == atan(3/2)", True, "arg(2 + 3i) == atan(3 / 2)"),
    ("asin(2) == pi/2 + i*ln(2+sqrt(3))", True, "asin(2) == pi / 2 + i * ln(2 + sqrt(3))"),
    ("rect(sqrt(2),rad(45)) == 1+i", True, "rect(sqrt(2), rad(45)) == 1 + i"),
    ("polar(1+i)", [basic.sqrt(2), trig.c_pi / 4], "polar(1 + i)"),

    ("gcd(*-[4584, 248])", 8, "gcd(*-[4584, 248])"),

    ("re(5+4i)", 5, "re(5 + 4i)"),
    ("im(8-9i)", -9, "im(8 - 9i)"),
    ("conj(5+4i)", 5 - 4j, "conj(5 + 4i)"),

    ("euler(10)", 50521, "euler(10)"),
    ("fact(5)", 120, "fact(5)"),
    ("gamma(6)", 120, "gamma(6)"),
    ("beta(18,2)==1/342", True, "beta(18, 2) == 1 / 342"),
    ("{x}(2x^2+3x+4)(8)", 156, "{x}(2 * x ^ 2 + 3 * x + 4)(8)"),
    ("gradient({x}(2x^2+3x+4),8)", 35, "gradient({x}(2 * x ^ 2 + 3 * x + 4), 8)"),
    ("{x}(2x^2+3x+4)(8+1e-5)", 156.0003500002, "{x}(2 * x ^ 2 + 3 * x + 4)(8 + 1e-5)"),
    ("round(deriv(gamma)(5),4)", 36.1468, "round(deriv(gamma)(5), 4)"),
    ("integ({x}(4x^3-2x^2+3x-4),-7,4)", -2509.8 - 1 / 30, "integ({x}(4 * x ^ 3 - 2 * x ^ 2 + 3 * x - 4), -7, 4)"),
    ("integ(sin,0,pi)", 2, "integ(sin, 0, pi)"),
    ("round(integ({x}(root(x,3)),-19,71),1)", 239.5 + 32.9j, "round(integ({x}(root(x, 3)), -19, 71), 1)"),
    ("fib(400)", 176023680645013966468226945392411250770384383304492191886725992896575345044216019675, "fib(400)"),
    ("map(derivative(ln),[1,2,4,8])==map({x}(1/x),[1,2,4,8])", True,
     "map(derivative(ln), [1, 2, 4, 8]) == map({x}(1 / x), [1, 2, 4, 8])"),
    ("map(derivative(sin),[0,pi/2,pi])==map(cos,[0,pi/2,pi])", True,
     "map(derivative(sin), [0, pi / 2, pi]) == map(cos, [0, pi / 2, pi])"),
    ("2+2==4 and 3+3==6", True, "2 + 2 == 4 AND 3 + 3 == 6"),

    ("2+2>=1+1", True, "2 + 2 >= 1 + 1"),
    ("3+3<=12/2", True, "3 + 3 <= 12 / 2"),

    ("{n}({m}({n}(m*n))(n))(3)(4)", 12, "{n}({m}({n}(m * n))(n))(3)(4)"),

    ("round({m,d,x}(1/(d*sqrt(2pi))*exp(-((x-m)^2)/(2*d^2)))(100,5.7,110),3)", 0.015,
     "round({m, d, x}(1 / (d * sqrt(2 * pi)) * exp(-((x - m) ^ 2) / (2 * d ^ 2)))(100, 5.7, 110), 3)")
]


def run_tests():
    ev = Evaluator()

    for expr, exp_result, exp_beautified in tests:
        result = ev.evaluate(expr)
        expect(result, exp_result)
        expect(ev.beautified, exp_beautified)
