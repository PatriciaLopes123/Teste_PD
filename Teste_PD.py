#Entrada

print("\nSoftware de geração de comentário para a nota fiscal da PD Soluções\n")

valorFiscal = input("Valor total da nota fiscal: ")
valorFiscal = float(valorFiscal.replace('.','').replace(',','.'))

arquivo = open('entrada.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()

print("\n")

#Saída

arquivo = open('saida.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()


uniaoPorcentagem = 8.05486
municipioPorcentagem = 3.87827

totalPorcentagem = uniaoPorcentagem + municipioPorcentagem
total = (totalPorcentagem / 100) * valorFiscal


uniaoTotal = (uniaoPorcentagem / 100) * valorFiscal
municipioTotal = (municipioPorcentagem / 100) * valorFiscal


print("\n Em atendimento à Lei 12.741/2012 (Lei do Imposto na Nota Fiscal) informamos que o valor aproximado dos tributos incidentes sobre  deas operaçõesste")
print("estabelecimento é de", "%.2f" % totalPorcentagem, "% ( R$", "%.2f" % total, "), assim distribuídos:")
print("- Uniao:", "%.2f" % uniaoPorcentagem, "% (R$", "%.2f" % uniaoTotal, ").")
print("- Municipio:", "%.2f" % municipioPorcentagem, "% (R$", "%.2f" % municipioTotal, ").")