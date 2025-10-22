import os

script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
entrada_path = os.path.join(script_dir, 'filmes_avaliacao.txt')   
saida_path = os.path.join(script_dir, 'filmes_indicacao.txt')    

if not os.path.exists(entrada_path):
    print("Arquivo filmes_avaliacao.txt não encontrado em:", entrada_path)
    raise SystemExit

registros = []
with open(entrada_path, 'r', encoding='utf-8') as f:
    for i, linha in enumerate(f):
        linha = linha.strip()
        if not linha:
            continue
        if i == 0 and linha.lower().startswith('filme'):
            continue
        partes = linha.split(';')
        if len(partes) < 2:
            print("Linha em formato errado:", linha)
            continue
        filme = partes[0].strip()
        nota_str = partes[1].strip()
        try:
            nota = float(nota_str)
        except ValueError:
            print("Nota inválida na linha:", linha)
            continue
        if ',' in filme:
            _, titulo = filme.split(',', 1)
            titulo = titulo.strip()
        else:
            titulo = filme
        registros.append((filme, nota, titulo.lower()))

if not registros:
    print("Nenhum registro válido encontrado em", entrada_path)
    raise SystemExit

def chave_registro(item):
    filme, nota, titulo_lower = item
    return (-nota, titulo_lower)
registros_ordenados = sorted(registros, key=chave_registro)
top5 = registros_ordenados[:5]

with open(saida_path, 'w', encoding='utf-8') as f:
    f.write("filme;nota\n")
    for filme, nota, _ in top5:
        f.write(f"{filme};{nota}\n")

print("Arquivo de indicação criado em:", saida_path)
print("Conteúdo gravado:")
with open(saida_path, 'r', encoding='utf-8') as f:
    print(f.read())