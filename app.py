from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware

#Criar instância FastAPI
app = FastAPI()
#Permitindo que sites usem os dados da API
origins = [
    "http://127.0.0.1:5000",
    "https://threeaiquestoes-c8d550369fc4.herokuapp.com",
	"https://threeaiquestoes2-b625d9efbacd.herokuapp.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
questions = {
	"Matemática": {
		"Grandezasproporcionais": [{"Fonte": "(Enem 2011)",
								    "Enunciado": "Muitas medidas podem ser tomadas em nossas casas visando à utilização racional de energia elétrica. Isso deve ser uma atitude diária de cidadania. Uma delas pode ser a redução do tempo no banho. Um chuveiro com potência de 4800 kWh consome 4,8 kW por hora. Uma pessoa que toma dois banhos diariamente, de 10 minutos cada, consumirá, em sete dias, quantos kW?",
									"Alternativas": "a) 0,8<br>b) 1,6<br>c) 5,6<br>d) 11,2<br>e) 33,6",
									"Resposta": "Resposta: Alternativa 'd'",
									"ID": 1},
								   {"Fonte": "(Enem 2011)",
									"Enunciado": "Sabe-se que a distância real, em linha reta, de uma cidade A, localizada no estado de São Paulo, a uma cidade	B, localizada no estado	de	Alagoas, é igual a 2 000 km. Um estudante, ao analisar um mapa,	verificou com sua régua	que	a distância	entre essas	duas cidades, A	e B, era 8 cm.<br>Os dados nos indicam que o mapa observado pelo estudante está na escala de",
									"Alternativas": "a) 1:250.<br>b) 1:2500.<br>c) 1:25000.<br>d) 1:250000.<br>e) 1:25000000.",
									"Resposta": "Resposta: Alternativa 'e'",
									"ID": 2},
								   {"Fonte": "(Enem 2012)",
									"Enunciado": "Uma mãe recorreu à bula para verificar a dosagem de um remédio que precisava dar a seu filho. Na recomendava-se a seguinte dosagem: 5 gotas para da 2 kg de massa corporal a cada 8 horas. Se a mãe ministrou corretamente 30 gotas do remédio a seu filho a cada 8 horas, então a massa corporal dele é de",
						  			"Alternativas": "a) 12 kg.<br>b) 16 kg.<br>c) 24 kg.<br>d) 36 kg.<br>e) 75 kg.",
	                      			"Resposta": "Resposta: Alternativa 'a'",
									"ID": 3},
								   {"Fonte": "(Enem 2013)",
									"Enunciado": "O contribuinte que vende mais de R$ 20 mil de ações em Bolsa de Valores em um mês deverá pagar Imposto de Renda. O pagamento para a Receita Federal consistirá em 15% do lucro obtido com a venda das ações.<br>Disponível em: www1.folha.uol.com.br. Acesso em: 26 abr. 2010 (adaptado).<br>Um contribuinte que vende por R$ 34 mil um lote de ações que custou R$ 26 mil terá de pagar de Imposto de Renda à Receita Federal o valor de",
									"Alternativas": "a) R$ 900,00.<br>b) R$ 1200,00.<br>c) R$ 2100,00.<br>d) R$ 3900,00.<br>e) R$ 5100,00.",
									"Resposta": "Resposta: Alternativa 'b'",
									"ID": 4},
								   {"Fonte": "(Enem 2013)",
									"Enunciado": "Para aumentar as vendas no início do ano, uma loja de departamentos remarcou os preços de seus produtos 20% abaixo do preço original. Quando chegam ao caixa, os clientes que possuem o cartão fidelidade da loja têm direito a um desconto adicional de 10% sobre o valor total de suas compras.<br>Um cliente deseja comprar um produto que custava R$50,00 antes da remarcação de preços. Ele não possui o cartão fidelidade da loja.<br>Caso esse cliente possuísse o cartão fidelidade da loja, a economia adicional que obteria ao efetuar a compra, em reais, seria de",
									"Alternativas": "a) 15,00.<br>b) 14,00.<br>c) 10,00.<br>d) 5,00.<br>e) 4,00.",
									"Resposta": "Resposta: Alternativa 'e'",
									"ID": 5}],
		"Probabilidade": [{"Fonte": "(Enem cancelado 2009)",
						   "Enunciado": "Dados do Instituto de Pesquisas Econômicas Aplicadas (IPEA) revelaram que no biênio 2004/2005, nas rodovias federais, os atropelamentos com morte ocuparam o segundo lugar no ranking de mortalidade por acidente. A cada 34 atropelamentos, ocorreram 10 mortes. Cerca de 4 mil atropelamentos/ano, um a cada duas horas, aproximadamente.<br>Disponível em: http://www.ipea.gov.br. Acesso em: 6 jan. 2009.<br>De acordo com os dados, se for escolhido aleatoriamente para investigação mais detalhada um dos atropelamentos ocorridos no biênio 2004/2005, a probabilidade de ter sido um atropelamento sem morte é",
						   "Alternativas": "a) 2/17<br>b) 5/17<br>c) 2/5<br>d) 3/5<br>e) 12/17",
						   "Resposta": "Resposta: Alternativa 'e'",
						   "ID": 1},
                          {"Fonte": "(Enem cancelado 2009)",
						   "Enunciado": "Um casal decidiu que vai ter 3 filhos. Contudo, quer exatamente 2 filhos homens e decide que, se a probabilidade fosse inferior a 50%, iria procurar uma clínica para fazer um tratamento específico para garantir que teria os dois filhos homens.<br>Após os cálculos, o casal concluiu que a probabilidade de ter exatamente 2 filhos homens é",
						   "Alternativas": "a) 66,7%, assim ele não precisará fazer um tratamento.<br>b) 50%, assim ele não precisará fazer um tratamento.<br>c) 7,5%, assim ele não precisará fazer um tratamento.<br>d) 25%, assim ele precisará procurar uma clínica para fazer um tratamento.<br>e) 37,5%, assim ele precisará procurar uma clínica para fazer um tratamento.",
						   "Resposta": "Resposta: Alternativa 'e'",
						   "ID": 2},
						  {"Fonte": "(Enem 2ª aplicação 2010)",
						   "Enunciado": "Em uma reserva florestal existem 263 espécies de peixes, 122 espécies de mamíferos, 93 espécies de répteis, 1 132 espécies de borboletas e 656 espécies de aves.<br>Disponível em: http:www.wwf.org.br. Acesso em: 23 abr. 2010 (adaptado).<br>Se uma espécie animal for capturada ao acaso, qual a probabilidade de ser uma borboleta?",
						   "Alternativas": "a) 63,31%<br>b) 60,18%<br>c) 56,52%<br>d) 49,96%<br>e) 43,27%",
						   "Resposta": "Resposta: Alternativa 'd'",
						   "ID": 3},
			              {"Fonte": "(Enem 2012)",
						   "Enunciado": "José, Paulo e Antônio estão jogando dados não viciados, nos quais, em cada uma das seis faces, há um número de 1 a 6. Cada um deles jogará dois dados simultaneamente. José acredita que, após jogar seus dados, os números das faces voltadas para cima lhe darão uma soma igual a 7. Já Paulo acredita que sua soma será igual a 4 e Antônio acredita que sua soma será igual a 8.<br>Com essa escolha, quem tem a maior probabilidade de acertar sua respectiva soma é",
						   "Alternativas": "a) Antônio, já que sua soma é a maior de todas as escolhidas.<br>b) José e Antônio, já que há 6 possibilidades tanto para a escolha de José quanto para a escolha de Antônio, e há apenas 4 possibilidades para a escolha de Paulo.<br>c) José e Antônio, já que há 3 possibilidades tanto para a escolha de José quanto para a escolha de Antônio, e há apenas 2 possibilidades para a escolha de Paulo.<br>d) José, já que ha 6 possibilidades para formar sua soma, 5 possibilidades para formar a soma de Antônio e apenas 3 possibilidades para formar a soma de Paulo.<br>e) Paulo, já que sua soma é a menor de todas.",
						   "Resposta": "Resposta: Alternativa 'd'",
						   "ID": 4},
						  {"Fonte": "(Enem 2013)",
						   "Enunciado": "Numa escola com 1 200 alunos foi realizada uma pesquisa sobre o conhecimento desses em duas línguas estrangeiras, inglês e espanhol. Nessa pesquisa constatou-se que 600 alunos falam inglês, 500 falam espanhol e 300 não falam qualquer um desses idiomas.<br>Escolhendo-se um aluno dessa escola ao acaso e sabendo-se que ele não fala inglês, qual a probabilidade de que esse aluno fale espanhol?",
						   "Alternativas": "a) 1/2<br>b) 5/8<br>c) 1/4<br>d) 5/6<br>e) 5/14",
						   "Resposta": "Resposta: Alternativa 'a'",
						   "ID": 5}]
	    },
	"Física": {
		"Energia": [{"Fonte": "(Enem 2010)",
					  "Enunciado": "Com o objetivo de se testar a eficiência de fornos de micro-ondas, planejou-se o aquecimento em 10°C de amostras de diferentes substâncias, cada uma com determinada massa, em cinco fornos de marcas distintas.<br>Nesse teste, cada forno operou à potência máxima.<br>O forno mais eficiente foi aquele que",
					  "Alternativas": "a) forneceu a maior quantidade de energia às amostras.<br>b) cedeu energia à amostra de maior massa em mais tempo.<br>c) forneceu a maior quantidade de energia em menos tempo.<br>d) cedeu energia à amostra de menor calor específico mais lentamente.<br>e) forneceu a menor quantidade de energia às amostras em menos tempo.",
					  "Resposta": "Resposta: Alternativa 'c'",
					  "ID": 1},
                     {"Fonte": "(Enem 2010)",
					  "Enunciado": "Deseja-se instalar uma estação de geração de energia elétrica em um município localizado no interior de um pequeno vale cercado de altas montanhas de difícil acesso. A cidade é cruzada por um rio, que é fonte de água para consumo, irrigação das lavouras de subsistência e pesca. Na região, que possui pequena extensão territorial, a incidência solar é alta o ano todo. A estação em questão irá abastecer apenas o município apresentado.<br>Qual forma de obtenção de energia, entre as apresentadas, é a mais indicada para ser implantada nesse município de modo a causar o menor impacto ambiental?",
					  "Alternativas": "a) Termelétrica, pois é possível utilizar a água do rio no sistema de refrigeração.<br>b) Eólica, pois a geografia do local é própria para a captação desse tipo de energia.<br>c) Nuclear, pois o modo de resfriamento de seus sistemas não afetaria a população.<br>d) Fotovoltaica, pois é possível aproveitar a energia solar que chega à superfície do local.<br>e) Hidrelétrica, pois o rio que corta o município é suficiente para abastecer a usina construída.",
					  "Resposta": "Resposta: Alternativa 'd'",
					  "ID": 2},
			         {"Fonte": "(Enem 2012) ",
					  "Enunciado": "Os carrinhos de brinquedo podem ser de vários tipos. Dentre eles, há os movidos a corda, em que uma mola em seu interior é comprimida quando a criança puxa o carrinho para trás. Ao ser solto, o carrinho entra em movimento enquanto a mola volta à sua forma inicial.<br>O processo de conversão de energia que ocorre no carrinho descrito também é verificado em",
					  "Alternativas": "a) um dínamo.<br>b) um freio de automóvel.<br>c) um motor a combustão.<br>d) uma usina hidroelétrica.<br>e) uma atiradeira (estilingue).",
					  "Resposta": "Resposta: Alternativa 'e'",
					  "ID": 3},
                     {"Fonte": "(Enem PPL 2012)",
					  "Enunciado": "A usina termelétrica a carvão é um dos tipos de unidades geradoras de energia elétrica no Brasil, Essas usinas transformam a energia contida no combustível (carvão mineral) em energia elétrica.<br>Em que sequência ocorrem os processos para realizar essa transformação?",
					  "Alternativas": "a) A usina transforma diretamente toda a energia química contida no carvão em energia elétrica, usando reações de fissão em uma célula combustível.<br>b) A usina queima o carvão, produzindo energia térmica, que é transformada em energia elétrica por dispositivos denominados transformadores.<br>c) A queima do carvão produz energia térmica, que é usada para transformar água em vapor. A energia contida no vapor é transformada em energia mecânica na turbina e, então, transformada em energia elétrica no gerador.<br>d) A queima do carvão produz energia térmica, que é transformada em energia potencial na torre da usina, Essa energia é então transformada em energia elétrica nas células eletrolíticas.<br>e) A queima do carvão produz energia térmica, que é usada para aquecer água, transformando-se novamente em energia química, quando a água é decomposta em hidrogênio e oxigênio, gerando energia elétrica.",
					  "Resposta": "Resposta: Alternativa 'c'",
					  "ID": 4},
                     {"Fonte": "(Enem PPL 2012)",
					  "Enunciado": "Um automóvel, em movimento uniforme, anda por uma estrada plana, quando começa a descer uma ladeira, na qual o motorista faz com que o carro se mantenha sempre com velocidade escalar constante.<br>Durante a descida, o que ocorre com as energias potencial, cinética e mecânica do carro?",
					  "Alternativas": "a) A energia mecânica mantém-se constante, já que a velocidade escalar não varia e, portanto, a energia cinética é constante.<br>b) A energia cinética aumenta, pois a energia potencial gravitacional diminui e quando uma se reduz, a outra cresce.<br>c) A energia potencial gravitacional mantém-se constante, já que há apenas forças conservativas agindo sobre o carro.<br>d) A energia mecânica diminui, pois a energia cinética se mantém constante, mas a energia potencial gravitacional diminui.<br>e) A energia cinética mantém-se constante, já que não há trabalho realizado sobre o carro.",
					  "Resposta": "Resposta: Alternativa 'd'",
					  "ID": 5}],
		"Ondulatória": [{"Fonte": "(Enem 2012)",
						 "Enunciado": "Nossa pele possui células que reagem à incidência de luz ultravioleta e produzem uma substância chamada melanina, responsável pela pigmentação da pele. Pensando em se bronzear, uma garota vestiu um biquíni, acendeu a luz de seu quarto e deitou-se exatamente abaixo da lâmpada incandescente. Após várias horas ela percebeu que não conseguiu resultado algum.<br>O bronzeamento não ocorreu porque a luz emitida pela lâmpada incandescente é de",
						 "Alternativas": "a) baixa intensidade.<br>b) baixa frequência.<br>c) um espectro contínuo.<br>d) amplitude inadequada.<br>e) curto comprimento de onda.",
						 "Resposta": "Resposta: Alternativa 'b'",
					     "ID": 1},
                        {"Fonte": "(Enem PPL 2012)",
						 "Enunciado": "Para afinar um violão, um músico necessita de uma nota para referência, por exemplo, a nota Lá em um piano. Dessa forma, ele ajusta as cordas do violão até que ambos os instrumentos toquem a mesma nota. Mesmo ouvindo a mesma nota, é possível diferenciar o som emitido pelo piano e pelo violão.<br>Essa diferenciação é possível, porque",
						 "Alternativas": "a) a ressonância do som emitido pelo piano é maior.<br>b) a potência do som emitido pelo piano é maior.<br>c) a intensidade do som emitido por cada instrumento é diferente.<br>d) o timbre do som produzido por cada instrumento é diferente.<br>e) a amplitude do som emitido por cada instrumento é diferente.",
						 "Resposta": "Resposta: Alternativa 'd'",
					     "ID": 2},
                   	    {"Fonte": "(Enem PPL 2013)",
						 "Enunciado": "Em um violão afinado, quando se toca a corda Lá com seu comprimento efetivo (harmônico fundamental), o som produzido tem frequência de 440 Hz.<br>Se a mesma corda do violão é comprimida na metade do seu comprimento, a frequência do novo harmônico",
						 "Alternativas": "a) se reduz à metade, porque o comprimento de onda dobrou.<br>b) dobra, porque o comprimento de onda foi reduzido à metade.<br>c) quadruplica, porque o comprimento de onda foi reduzido à metade.<br>d) quadruplica, porque o comprimento de onda foi reduzido à quarta parte.<br>e) não se modifica, porque é uma característica independente do comprimento da corda que vibra.",
						 "Resposta": "Resposta: Alternativa 'b'",
					     "ID": 3},
                   	    {"Fonte": "(Enem 2013)",
						 "Enunciado": "Em viagens de avião, é solicitado aos passageiros o desligamento de todos os aparelhos cujo funcionamento envolva a emissão ou a recepção de ondas eletromagnéticas. O procedimento é utilizado para eliminar fontes de radiação que possam interferir nas comunicações via rádio dos pilotos com a torre de controle.<br>A propriedade das ondas emitidas que justifica o procedimento adotado é o fato de",
						 "Alternativas": "a) terem fases opostas.<br>b) serem ambas audíveis.<br>c) terem intensidades inversas.<br>d) serem de mesma amplitude.<br>e) terem frequências próximas.",
						 "Resposta": "Resposta: Alternativa 'e'",
					     "ID": 4},
						{"Fonte": "(Enem PPL 2013)",
						 "Enunciado": "Visando reduzir a poluição sonora de uma cidade, a Câmara de Vereadores aprovou uma lei que impõe o limite máximo de 40 dB (decibéis) para o nível sonoro permitido após as 22 horas.<br>Ao aprovar a referida lei, os vereadores estão limitando qual característica da onda?",
						 "Alternativas": "a) A altura da onda sonora.<br>b) A amplitude da onda sonora.<br>c) A frequência da onda sonora.<br>d) A velocidade da onda sonora.<br>e) O timbre da onda sonora.",
						 "Resposta": "Resposta: Alternativa 'b'",
					     "ID": 5}]
	}
}

@app.get("/")
def home():
	return "API de questões do ENEM"

@app.get("/{disciplina}/{assunto}") # <- usamos get para obter informações
def questão(disciplina: str, assunto: str):
	return questions[disciplina][assunto]

@app.get("/{disciplina}/{assunto}/{enunciado}") # <- usamos get para obter informações
def questão(disciplina: str, assunto: str, enunciado: int):
	for x in questions[disciplina][assunto]:
		if enunciado in x.values():
			return x
	