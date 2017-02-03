#lunar.py
from math import sqrt

altitude = 500.
v = -50.
g = -5.
t = 1.
comb = 120.

print 'Simulacao de alunissagem'
print
print '(digite a quantidade de combustivel a queimar)'

fmt = 'ALt: %6.2f Vel: %6.2f Comb: %3d'
while x > 0:
	msg = fmt % (x, v, comb)
	if comb > 0:
		resp = raw_input(msg + ' Queima = ')
		try:
			queima = float(resp)
		except:
			queima = 0
		if queima > comb:
			queima = comb
		comb = comb - queima
		a = g + queima
	else:
		print msg
		a = g
	x0 = x
	v0 = v
	x = x0 + v0*t + a*t*t/2	#calc nova posicao
	v = v0 + a*t	#calc nova velocidade
vf = sqrt(v0*v0 + 2*-a*x0) # calcular vel. final
print '>>>CONTATO! Velocidade final: %6.2f' % (-vf)
if vf == 0:
	msg = 'Alunissagem perfeita!'
elif vf <= 2:
	msg = 'Alunissagem dentro do padrao.'
elif vf <= 10:
	msg = 'Alunissagem com avarias leves.'
elif vf <= 20:
	msg = 'Alunissagem com avarias severas.'
else:
	msg = 'Modulo lunar destruido no impacto.'
print '>>>' + msg
