# 🛠 Fedora Development Environment Ansible Playbook

Este playbook Ansible automatiza a configuração de um ambiente de desenvolvimento completo no Fedora Linux. Ele instala e configura diversas ferramentas essenciais para desenvolvimento web, backend e containerização.

---

## 📋 Requisitos

- Fedora Linux com `dnf`
- Ansible instalado (`sudo dnf install ansible`)
- Permissão de superusuário (`sudo`)
- Conexão com a Internet

---

## 🚀 Como executar

1. Clone este repositório ou copie o arquivo `setup-dev.yaml`.
2. No terminal, navegue até o diretório do playbook.
3. Execute o comando:

   ```bash
   ansible-playbook setup-dev.yaml --ask-become-pass
   ```

O parâmetro `--ask-become-pass` solicitará sua senha de `sudo` durante a execução.

---

## ✨ O que este playbook faz (Explicação detalhada)

Abaixo, uma explicação clara e linha por linha de todas as tarefas:

---

### 🎯 Tarefas principais

1. **Atualizar pacotes**
   - Atualiza todos os pacotes do sistema para a versão mais recente usando `dnf`.
   - Equivalente a `dnf upgrade`.

2. **Instalar Git**
   - Instala o Git, sistema de controle de versão.

3. **Instalar chave GPG do repositório Visual Studio Code**
   - Importa a chave GPG da Microsoft, necessária para validar os pacotes.

4. **Adicionar repositório do Visual Studio Code**
   - Cria o arquivo `/etc/yum.repos.d/vscode.repo` com as configurações do repositório oficial.

5. **Instalar Visual Studio Code**
   - Instala o editor de código Visual Studio Code a partir do repositório configurado.

6. **Instalar Node.js e npm**
   - Instala o Node.js (versão definida pela variável `nodejs_version`, por padrão a 20) e o gerenciador de pacotes npm.

7. **Verificar instalação do npm**
   - Executa `npm --version` e falha se não estiver corretamente instalado.

8. **Instalar pnpm globalmente**
   - Instala `pnpm`, uma alternativa rápida ao npm.

9. **Instalar Yarn globalmente**
   - Instala `yarn`, outro gerenciador de pacotes JavaScript.

10. **Instalar PHP**
    - Instala o interpretador PHP.

11. **Instalar Composer**
    - Baixa o instalador do Composer e o salva em `/tmp`.

12. **Instalar Composer globalmente**
    - Executa o instalador e coloca o binário em `/usr/local/bin/composer`.

13. **Instalar NestJS CLI globalmente**
    - Instala o CLI oficial do NestJS via npm.

14. **Instalar Laravel Installer via Composer**
    - Usa o Composer para instalar globalmente o instalador do Laravel.
    - Define `COMPOSER_HOME` como `/root/.composer`.

15. **Adicionar Composer bin ao PATH**
    - Adiciona a pasta de executáveis globais do Composer ao `PATH` no `.bashrc`.

16. **Instalar Docker e Docker Compose**
    - Instala o Docker e o Docker Compose usando `dnf`.

17. **Iniciar e habilitar o serviço Docker**
    - Ativa e inicia o daemon do Docker.

18. **Adicionar o usuário atual ao grupo docker**
    - Permite rodar Docker sem `sudo`.

19. **Instalar GitHub CLI**
    - Instala o `gh`, a CLI oficial do GitHub.

20. **Instalar Flatpak**
    - Instala o Flatpak, sistema de empacotamento universal.

21. **Adicionar repositório Flathub**
    - Adiciona o repositório Flathub ao Flatpak se ele ainda não existir.

22. **Instalar LibreWolf via Flatpak**
    - Instala o navegador LibreWolf (foco em privacidade) via Flatpak.

---

## ⚙ Variáveis configuráveis

- `nodejs_version`: define a versão do Node.js a ser instalada (por padrão `"20"`).

---

## ✅ Resultado esperado

Ao final da execução:

- Seu Fedora estará atualizado.
- Ferramentas de desenvolvimento (Git, Node.js, npm, pnpm, yarn, PHP, Composer, NestJS CLI, Laravel Installer) estarão instaladas.
- Docker estará pronto para uso e seu usuário terá permissão.
- Visual Studio Code instalado a partir do repositório oficial.
- GitHub CLI disponível.
- Flatpak e LibreWolf configurados.

---

## 🧩 Observações importantes

- Algumas tarefas podem demorar dependendo da sua conexão.
- Após adicionar seu usuário ao grupo `docker`, pode ser necessário reiniciar a sessão.
- O Composer instala globalmente o Laravel Installer no diretório `/root/.composer/vendor/bin`.

---

## 📄 Licença

Este projeto é distribuído sem garantia. Sinta-se à vontade para adaptar conforme suas necessidades.

---

