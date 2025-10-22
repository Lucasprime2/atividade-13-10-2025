import os
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
filmes_path = os.path.join(script_dir, 'filmes.txt')

conteudo = [
    "1982, TRON",
    "1983, WarGames",
    "1995, Hackers",
    "1999, Pirates of Silicon Valley",
    "2010, The Social Network",
    "2013, Jobs",
    "2014, The Imitation Game",
    "2014, Ex Machina",
    "2016, Snowden",
    "2018, Ready Player One",
]

with open(filmes_path, 'w', encoding='utf-8') as f:
    for linha in conteudo:
        f.write(linha + '\n')
print("Arquivo criado em:", filmes_path)
print("Conteúdo gravado no arquivo:")
with open(filmes_path, 'r', encoding='utf-8') as f:
    print(f.read())