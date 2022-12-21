# Реализовать калькулятор с системой логирования:
# 1) решение вводимых примеров (2+3) -> 5
# 2) решение уравнений (x+3 = 0) -> -3
# 3) упрощение многочленов (x*2 + 3*x2 + 4) -> 4*x*2 + 4
# Записать в файл "задачу" от пользователя и ответ.


import controller

controller.run_calc()





# import sympy   догадаетесь сами, где может пригодиться) (в model)

# expr = input('Enter expr: ')
# x = sympy.Symbol('x')
# try:
#     ans = sympy.solve(expr, x)
#     print(ans)
# except ValueError:
#     print('Incorrect input')
