file=open('coronathon_colaborador.txt','w')

file.write('\n')
esc=['pos','superior','tecnico','medio','fundamental','nenhum']
per1=['Qual seu nome','Quntos tipos de trabalho pretende se candidatar','Digite os códigos de trabalho separados por ;','responda com "S" ou"N" separada por";" se teve esperiencia em cada uma das areas','Escolaridade','Região de trabalho',"Idiomas setrangeiros?",'possui CNH?','Deficiencia','Quais','ja trabalhou de modo formal', 'descreva seu histórico']

pergunta=input('Nome')
file.write(pergunta+',')
pergunta=input('Numero de vagas almejadas')
file.write(pergunta+',')
pergunta=input('possui experiencia?')
file.write(pergunta+',')
pergunta=input('Escolaridade')
file.write(pergunta+',')

if pergunta==esc[0]:
    pergunta=input('digite todos os seus curcos de pós separados por ";"')
    file.write(pergunta+',')
    pergunta=input('digite todos os seus curcos de graduação separados por ";"')
    file.write(pergunta+',')
    pergunta=input('digite todos os seus curcos de técnicos separados por ";"')
    file.write(pergunta+',')
elif pergunta==esc[1]:
    file.write('Nenhum,')
    pergunta=input('digite todos os seus curcos de graduação separados por ";"')
    file.write(pergunta+',')
    pergunta=input('digite todos os seus curcos de técnicos separados por ";"')
    file.write(pergunta+',')
elif pergunta==esc[2]:
    file.write('Nenhum,')
    file.write('Nenhum,')
    pergunta=input('digite todos os seus curcos de técnicos separados por ";"')
    file.write(pergunta+',')
else:
    file.write('Nenhum,')
    file.write('Nenhum,')
    file.write('Nenhum,')
    
pergunta=input('Possui cursos profissionalizantes? responda com S ou N')
file.write(pergunta+',')

if pergunta=='S':
    pergunta=input('digite todos os seus curcos separados por ";"')
    file.write(pergunta+',')
else:
    file.write(pergunta+',')

pergunta=input('Possui disponibilida para trabalhar em qualquer lugar do Brasil? responda com S ou N')
file.write(pergunta+',')

    

if pergunta=='N':
    pergunta=input('digite quais regioes separadas por ";"')
    file.write(pergunta+',')
else:
    file.write(pergunta+',')

pergunta=input('Fala outros isiomas?')
if pergunta=='S':
    pergunta=input('espcifique')
    file.write(pergunta+',')
else:
    file.write(pergunta+',')



pergunta=input('Possui CNH?')
file.write(pergunta+',')

if pergunta=='S':
    pergunta=input('espcifique')
    file.write(pergunta+',')
else:
    file.write(pergunta+',')

pergunta=input('Possui deficiencia?')
file.write(pergunta+',')

if pergunta=='S':
    pergunta=input('espcifique')
    file.write(pergunta+',')
else:
    file.write(pergunta+',')




pergunta=input('Já trabalhaou formalmente?')
file.write(pergunta+',')


pergunta=input('Conte um pouco sobre vc')
file.write(pergunta)
file.close()







