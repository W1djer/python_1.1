# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

n = int(input('Введите количество журавликов: '))
boy = n//6
girl = boy*4
print('Сергей и Петя сделали по:',boy)
print('Катя сделала:', girl)