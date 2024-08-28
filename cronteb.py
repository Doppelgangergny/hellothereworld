import os
import subprocess

# Defina o usuário e o caminho do script Python
usuario = os.getenv("USER")  # Obtém o nome do usuário atual
bash_script_path = os.path.join(os.getenv("HOME"), ".legion.py")  # Obtém o caminho para .legion.py no diretório home

# Comando que será adicionado à crontab para rodar a cada 3 minutos
cron_command = f"*/3 * * * * python3 {bash_script_path}"

# Adiciona o comando à crontab do usuário
subprocess.run(f"(crontab -l -u {usuario}; echo '{cron_command}') | crontab -u {usuario} -", shell=True)
