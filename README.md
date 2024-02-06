# GitHub Trending Repositories

This Python project uses the GitHub API to get the trending repositories for a specific programming language and generates a Markdown report with the retrieved information.

## English 🌎

### How to Run

1. Make sure you have Python installed on your machine.
2. Download the `main.py` file.
3. Open a terminal and navigate to the directory where you downloaded the file.
4. Run the script with the command `python main.py`.

### How it Works

The script creates an instance of the `GitHubTrendingRepos` class and calls the `generate_report` method with 'Python' as the argument. The `generate_report` method calls the `get_trending_repos` method, which makes a request to the GitHub API and returns the data of the trending repositories. The `generate_report` method then generates a Markdown report with the repository data and prints it.

## Português 🌎

### Como executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Baixe o arquivo `main.py`.
3. Abra um terminal e navegue até o diretório onde você baixou o arquivo.
4. Execute o script com o comando `python main.py`.

### Como funciona

O script cria uma instância da classe `GitHubTrendingRepos` e chama o método `generate_report` com 'Python' como argumento. O método `generate_report` chama o método `get_trending_repos`, que faz uma solicitação à API do GitHub e retorna os dados dos repositórios em tendência. O método `generate_report` então gera um relatório em Markdown com os dados do repositório e o imprime.
