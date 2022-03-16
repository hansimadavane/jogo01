
from random import randint
itens = ("pedra", "papel", "tesoura")
computador = randint(0, 2)
cpu= 0 
jgd= 0

print('''Suas Opcoes
	[0]Pedra
	[1]Papel
	[2]Tesoura''')
jogador = int(input("your choice: "))

print(f"o jogador jogou {itens[jogador]}")
print(f"O computador escolheu {itens[computador]}")

if computador == 0:#jogou pedra
	if jogador == 0:
		print("empatou");
	elif jogador== 1:
		jgd += 1
		print("you win");
	elif jogador== 2:
		cpu += 1
		print("you lose!");

elif computador == 1: #jogou papel
	if jogador == 0:
		cpu += 1
		print("you lose");
	elif jogador== 1:
		print("empatou");
	elif jogador== 2:
		jgd += 1
		print("you win!");

elif computador == 2: #jogou tesoura
	if jogador == 0:
		jgd += 1
		print("you win");
	elif jogador== 1:
		cpu += 1
		print("you lose");
	elif jogador== 2:
		print("empatou!");

print("game over")
print (f" O CPU venceu {cpu} vezes e o jogador venceu {jgd} vezes")
 

with open("cpu", "w+") as arquivo:
	arquivo.write(str(cpu))
	
		
	
	



"""with open("jgd", "w+") as arquivo:
	arquivo.write(str(jgd))"""

