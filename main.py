import os

print('Atualizando o sistema:')
atts = os.system("sudo dnf check-update")
attsResultado = os.system("sudo dnf update -y")


print('Instalando o HTTPD:')
instHttpd = os.system("sudo dnf install -y httpd")
enableHttpd = os.system("sudo systemctl enable httpd")
startHttpd = os.system("sudo systemctl start httpd")

print('Configurando o Firewall:')
addFirewall = os.system("sudo firewall-cmd --permanent --add-service=http")
reloadFirewall = os.system("sudo firewall-cmd --reload")

print('Instalando o GIT:')
instGit = os.system("sudo dnf install -y git")

print('Clonando o repositório do projeto:')
cloneGitProject = os.system("mkdir /tmp/project && cd /tmp/project && sudo git clone https://github.com/denilsonbonatti/mundo-invertido.git")

mvProjectDir = os.system("sudo mv /tmp/project/mundo-invertido/* /var/www/html/")
rmProjectDir = os.system("sudo rm -rf /tmp/project")

print('Deploy concluído com sucesso!')
