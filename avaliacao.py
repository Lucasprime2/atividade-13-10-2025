import os
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
filmes_path = os.path.join(script_dir, 'filmes.txt')                    
saida_path = os.path.join(script_dir, 'filmes_avaliacao.txt')           

def ler_nota(prompt):
    while True:
        s = input(prompt).strip()
        s = s.replace(',', '.')        
        try:
            nota = float(s)
        except ValueError:
            print("Erro: digite um número 0-10.")
            continue
        if 0 <= nota <= 10:
            return nota
        else:
            print("Erro: Digite um número 0-10.")

if not os.path.exists(filmes_path):
    print("Arquivo de filmes não encontrado em:", filmes_path)
    raise SystemExit

filmes = []
with open(filmes_path, 'r', encoding='utf-8') as f:
    for linha in f:
        linha = linha.strip()
        if not linha:
            continue
        filmes.append(linha)

if not filmes:
    print("Nenhum registro encontrado em", filmes_path)
    raise SystemExit

avaliacoes = []
print("Digite as notas para os filmes:")
for registro in filmes:
 
    if ',' in registro:
        _, titulo = registro.split(',', 1)
        titulo = titulo.strip()
    else:
        titulo = registro
    prompt = f"Nota para '{titulo}': "
    nota = ler_nota(prompt)
    avaliacoes.append((registro, nota))

with open(saida_path, 'w', encoding='utf-8') as f:
    f.write("filme;nota\n")   
    for reg, nota in avaliacoes:
        f.write(f"{reg};{nota}\n")

print("\nArquivo de avaliações criado em:", saida_path)
print("Conteúdo gravado:")
with open(saida_path, 'r', encoding='utf-8') as f:
    print(f.read())