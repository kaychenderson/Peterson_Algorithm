<h1 align="center" style="font-weight: bold;"> 🔐 Algoritmo de Peterson 💻</h1>
<p align="center">
    <a href="#tech">Tecnologias</a> •
    <a href="#about">Sobre o Algoritmo</a> •
    <a href="#features">Funcionalidades</a> •
    <a href="#usage">Como Usar</a> •
    <a href="#code">Estrutura do Código</a> •
    <a href="#colab">Contribuidores</a>
</p>

<h2 id="tech" style="font-weight: bold; font-size: 2rem">Tecnologia Utilizada</h2> 
<img align="center" alt="python" src="https://img.shields.io/badge/Python-FFFFFF?style=for-the-badge&logo=python&logoColor=black"/>

<h2 id="about" style="font-weight: bold; font-size: 2rem">Sobre o Algoritmo</h2>

Este projeto implementa uma solução clássica para o problema de exclusão mútua entre dois processos, utilizando o Algoritmo de Peterson. Ele foi desenvolvido em Python utilizando threads para simular dois processos que alternam entre regiões críticas e não críticas de forma sincronizada.

O código utiliza variáveis compartilhadas como flag e turn para garantir que apenas um processo acesse a região crítica de cada vez. O exemplo mostrado envolve dois processos que simulam atividades críticas e não críticas, ilustrando um conceito fundamental da teoria de concorrência e sincronização.

<h2 id="about" style="font-weight: bold; font-size: 2rem">⚙ Funcionalidades</h2>

<h2> 🟢 Processo 0: </h2>
Região Crítica: O Processo 0 executa uma tarefa crítica (simulada com uma mensagem no console). <br>
Região Não Crítica: Após finalizar a região crítica, o Processo 0 realiza uma tarefa não crítica.

<h2> 🔵 Processo 1: </h2>
Região Crítica: O Processo 1 também executa uma tarefa crítica (simulada com uma mensagem no console). <br>
Região Não Crítica: O Processo 1 realiza uma tarefa não crítica após completar a região crítica.
<br><br>
Ambos os processos competem pela região crítica de forma sincronizada, utilizando o algoritmo de Peterson para garantir que não haja conflito entre eles.

<h2 id="about" style="font-weight: bold; font-size: 2rem">📦 Instalação</h2>
Para rodar o código em sua máquina, siga os passos abaixo:

1. Clone este repositório:
```bash
git clone https://github.com/kaychenderson/Peterson_Algorithm.git
```
3. Acesse o diretório do projeto:
```bash
cd Peterson_Algorithm
```
4. Execute o código:
Basta executar o arquivo principal no terminal:
```bash
python peterson.py
```
<h2 id="about" style="font-weight: bold; font-size: 2rem">💡 Como Usar</h2>
O código já está pronto para execução e irá iniciar automaticamente dois processos que competem pelas regiões críticas.

Ao rodar o script, você verá as mensagens no console indicarem qual processo está na região crítica e qual está na região não crítica.

<h2 id="about" style="font-weight: bold; font-size: 2rem">🛠 Estrutura do Código</h2>
O código está dividido da seguinte forma:

## peterson.py: 
Arquivo principal que implementa o Algoritmo de Peterson com duas threads representando os dois processos que competem pela região crítica. 
## Variáveis Compartilhadas:
### flag: Uma lista com duas posições para controlar se o processo deseja entrar na região crítica.
### turn: Variável que indica qual processo tem a vez de executar a região crítica.
## Funções:
### secao_critica(): Simula a execução de uma tarefa na região crítica.
### secao_nao_critica(): Simula a execução de uma tarefa na região não crítica.
## Threads:
### process_0(): Representa o primeiro processo que executa a região crítica e não crítica.
### process_1(): Representa o segundo processo que executa a região crítica e não crítica.

🔍 Exemplo de Execução
Ao executar o código, a saída no console será algo como:
```bash
Processo 0 está na região crítica.
Processo 1 está na região crítica.
Processo 0 está na região NÃO crítica.
Processo 1 está na região NÃO crítica.
```
