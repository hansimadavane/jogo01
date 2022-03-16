ida=mas=fem=0
while True:
	sexo= str(input("Qual o seu sexo? [M/F] ")).strip().upper()[0]
	while sexo not in "FfMm":
		print("genero inexistente, tente novamente!")
		sexo= str(input("Qual o seu sexo? [M/F] ")).strip().upper()[0]

	idade = int(input("Qual a sua idade? "))
	continuar = str(input("quer continuar? [S/N]")).strip().upper()[0]

	if idade >= 18:
		ida+=1
	if sexo == "M":
		mas+=1
	if sexo == "F" and idade >= 18:
		fem+=1


	while continuar not in "SN":
		continuar = str(input("quer continuar? [S/N]")).strip().upper()[0]
	if continuar == "N":
		break

print(f"numero de pessoas maiores de 18: {ida}")
print(f"temos {mas} pessoas do sexo Masculino")
print(f"temos {fem} do sexo femenino com mais de 18 anos")





