with open('./tabelas_sir/tabela_medias.csv', 'r') as f:
    arq = f.read()
modificado = arq.replace('.', ',')
with open('./tabelas_sir/tabela_medias.csv', 'w') as f:
    f.write(modificado)
    
with open('./tabelas_sir/tabela_porcentagem_classes.csv', 'r') as f:
    arq = f.read()
modificado = arq.replace('.', ',')
with open('./tabelas_sir/tabela_porcentagem_classes.csv', 'w') as f:
    f.write(modificado)
    
with open('./tabelas_sir/tabela_tempo_classes.csv', 'r') as f:
    arq = f.read()
modificado = arq.replace('.', ',')
with open('./tabelas_sir/tabela_tempo_classes.csv', 'w') as f:
    f.write(modificado)