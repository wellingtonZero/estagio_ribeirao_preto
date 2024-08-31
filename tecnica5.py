# problema
'''
Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. 
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, 
usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? 
'''
# resolução

"""
então o problema tentei usar minha mente e cheguei a conclusão que se o teste acendendo o interruptor 1 e o interruptor 2 e visitando a primeira sala 
e ela não estiver acessa concluir que o interruptor 3 acende a lampada da sala 1. 
Então agora só precisa acender um dos interruptores supondo o interruptor 1 foi acionado e visitado a sala 2 verificou que não acendeu então conclui-se que o 
interruptor 1 acende a sala 3 e por eliminação o interruptor 2 acende a sala 2.
Então esse teste pode ser realizado acendo dois interruptores e verificando a sala e consequentemente por eliminação consegue se achar qual acente determinada sala
como referencia foi desenhado o esquema no arquivo esquema.png
"""