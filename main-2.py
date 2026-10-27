import os
from datetime import datetime
import time

diretorio_origem = '/var/www/html'
diretorio_destino = '/backup/web'

print('Verificando/Criando diretório de backup...')
if not os.path.exists(diretorio_destino):
    os.system(f"mkdir -p {diretorio_destino}")

print('Geração da cópia compactada:')
agora = datetime.now()
data_hora_str = agora.strftime("%Y-%m-%d_%H-%M")
nome_arquivo = f"backup_web_{data_hora_str}.tar.gz"
caminho_tar = os.path.join(diretorio_destino, nome_arquivo)

print(f"Iniciando backup de '{diretorio_origem}'...")
print(f"Arquivo de saída: {caminho_tar}")

# Compactando com o comando tar do Linux
codigo_retorno_tar = os.system(f"tar -czf {caminho_tar} -C /var/www html")

if codigo_retorno_tar == 0:
    print("Backup compactado com sucesso!")
else:
    print("Ocorreu um erro durante a compactação pelo sistema.")
    exit(1)

# Gerando o hash SHA-256 com o comando sha256sum do Linux
print("Gerando hash SHA-256:")
caminho_hash = os.path.join(diretorio_destino, f"{nome_arquivo}.sha256")

codigo_retorno_hash = os.system(f"sha256sum {caminho_tar} > {caminho_hash}")

if codigo_retorno_hash == 0:
    print(f"Hash salvo em: {caminho_hash}")
else:
    print("Ocorreu um erro ao gerar o hash pelo sistema.")
    exit(1)


print('Limpando backups com mais de 7 dias...')
tempo_atual = time.time()
limite_segundos = 7 * 24 * 60 * 60  # 7 dias em segundos
arquivos_removidos = 0

for arquivo in os.listdir(diretorio_destino):
    caminho_arquivo = os.path.join(diretorio_destino, arquivo)
    
    if os.path.isfile(caminho_arquivo):
        tempo_modificacao = os.path.getmtime(caminho_arquivo)
        
        if (tempo_atual - tempo_modificacao) > limite_segundos:
            os.remove(caminho_arquivo)
            print(f"Removido: {arquivo}")
            arquivos_removidos += 1

if arquivos_removidos == 0:
    print("Nenhum arquivo ultrapassou o período de retenção de 7 dias.")

print('Processo concluído com sucesso!')
