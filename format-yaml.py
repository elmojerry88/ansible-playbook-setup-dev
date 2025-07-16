import os
import sys
from pathlib import Path
from ruamel.yaml import YAML
import argparse

# Função que formata o YAML
def formatar_yaml(caminho_arquivo):
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)

    if not caminho_arquivo.exists():
        print(f"❌ Arquivo não encontrado: {caminho_arquivo}")
        return

    with caminho_arquivo.open("r", encoding="utf-8") as f:
        dados = yaml.load(f)

    with caminho_arquivo.open("w", encoding="utf-8") as f:
        yaml.dump(dados, f)

    print(f"✅ Arquivo formatado: {caminho_arquivo}")

# Função que formata arquivos de um diretório
def formatar_diretorio(diretorio):
    diretorio_path = Path(diretorio)
    if not diretorio_path.is_dir():
        print(f"❌ O diretório não existe: {diretorio}")
        return

    arquivos_yaml = diretorio_path.glob("**/*.yml")
    for arquivo in arquivos_yaml:
        formatar_yaml(arquivo)

# Função principal de CLI
def main():
    parser = argparse.ArgumentParser(
        description="Ferramenta CLI para formatar arquivos YAML (playbooks do Ansible)."
    )

    # Argumentos da CLI
    parser.add_argument(
        "-f", "--file",
        help="Caminho para o arquivo YAML a ser formatado",
        type=str
    )
    parser.add_argument(
        "-d", "--directory",
        help="Caminho para o diretório onde estão os arquivos YAML",
        type=str
    )
    parser.add_argument(
        "-v", "--verbose",
        help="Ativa a exibição de mais informações",
        action="store_true"
    )

    args = parser.parse_args()

    # Se foi passado o caminho de um arquivo
    if args.file:
        file_path = Path(args.file)
        formatar_yaml(file_path)

    # Se foi passado o caminho de um diretório
    elif args.directory:
        formatar_diretorio(args.directory)

    else:
        print("❌ Informe um arquivo ou diretório para formatação.")
        sys.exit(1)

# Executa o CLI
if __name__ == "__main__":
    main()
