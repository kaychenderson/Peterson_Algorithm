<h1 align="center" style="font-weight: bold;"> 🔐 Algoritmo de Peterson 💻</h1>
<p align="center">
    <a href="#about">Sobre o Algoritmo</a> •
    <a href="#features">Funcionalidades</a> •
    <a href="#install">Instação</a> •
    <a href="#usage">Como Usar</a> •
    <a href="#code">Estrutura do Código</a> •
</p>

### PEX0093 - Sistemas Operacionais
###### Professor: [Reudismam Rolim](https://github.com/reudismam)

###### Discrentes: Amanda Aparecida, Amanda Santiago, Joana Larissa e Kayc Henderson

#### Bacharelado Interdisciplinar em Tecnologia da Informação - UFERSA

<h2 id="tech" style="font-weight: bold; font-size: 2rem">Tecnologia Utilizada</h2> 
<img align="center" alt="python" src="https://img.shields.io/badge/Python-FFFFFF?style=for-the-badge&logo=python&logoColor=black"/>

<h2 id="about" style="font-weight: bold; font-size: 2rem">Sobre o Algoritmo</h2>

Este projeto implementa uma solução clássica para o problema de exclusão mútua entre dois processos, utilizando o Algoritmo de Peterson. Ele foi desenvolvido em Python utilizando threads para simular dois processos que alternam entre regiões críticas e não críticas de forma sincronizada.

O código utiliza variáveis compartilhadas como flag e turn para garantir que apenas um processo acesse a região crítica de cada vez. O exemplo mostrado envolve dois processos que simulam atividades críticas e não críticas, ilustrando um conceito fundamental da teoria de concorrência e sincronização.

<h2 id="features" style="font-weight: bold; font-size: 2rem">⚙ Funcionalidades</h2> 

<h2> 🟢 Processo 0: </h2>
Região Crítica: O Processo 0 executa uma tarefa crítica (simulada com uma mensagem no console). <br>
Região Não Crítica: Após finalizar a região crítica, o Processo 0 realiza uma tarefa não crítica.

<h2> 🔵 Processo 1: </h2>
Região Crítica: O Processo 1 também executa uma tarefa crítica (simulada com uma mensagem no console). <br>
Região Não Crítica: O Processo 1 realiza uma tarefa não crítica após completar a região crítica.
<br><br>
Ambos os processos competem pela região crítica de forma sincronizada, utilizando o algoritmo de Peterson para garantir que não haja conflito entre eles.

<h2 id="install" style="font-weight: bold; font-size: 2rem">📦 Instalação</h2>
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
<h2 id="usage" style="font-weight: bold; font-size: 2rem">💡 Como Usar</h2>
O código já está pronto para execução e irá iniciar automaticamente dois processos que competem pelas regiões críticas.

Ao rodar o script, você verá as mensagens no console indicarem qual processo está na região crítica e qual está na região não crítica.

<h2 id="code" style="font-weight: bold; font-size: 2rem">🛠 Estrutura do Código</h2>
O código está dividido da seguinte forma:

## peterson.py: 
Arquivo principal que implementa o Algoritmo de Peterson com duas threads representando os dois processos que competem pela região crítica. 
## Variáveis Compartilhadas:
- O algoritmo de Peterson utiliza duas variáveis compartilhadas para garantir a exclusão mútua e a comunicação entre os dois processos:

```flag```: Uma lista de dois elementos (flag[0] e flag[1]), onde cada posição indica se o processo correspondente deseja ou não entrar na região crítica.

```flag[0]```: indica se o primeiro processo (processo 0) deseja entrar na região crítica. <br>
```flag[1]```: indica se o segundo processo (processo 1) deseja entrar na região crítica.

```turn```: Uma variável de controle que determina qual processo tem a vez de executar a região crítica. O valor de turn é alternado entre 0 e 1 para indicar o próximo processo que deve entrar na região crítica, garantindo que o outro processo espere sua vez.

## Funções:
- O código define as seguintes funções que simulam a execução dos processos e as suas interações com a região crítica e não crítica:

### secao_critica(): 
Esta função simula a execução de uma tarefa na região crítica. Quando um processo entra na região crítica, ele executa esse bloco de código, indicando que está fazendo algo exclusivo que não pode ser interrompido.

### secao_nao_critica(): 
Esta função simula a execução de uma tarefa na região não crítica. Aqui, o processo pode executar outras ações que não requerem acesso exclusivo e podem ser realizadas sem conflitos.

## Threads:
- O algoritmo implementa duas threads para representar os dois processos concorrentes que competem pela região crítica. Cada thread executa um processo que alterna entre a região crítica e a região não crítica:

### process_0(): 
Representa o primeiro processo (processo 0) no sistema. Este processo tenta entrar na região crítica, mas só o fará se for a sua vez de acordo com a variável turn e a sua intenção, indicada pela lista flag.

### process_1(): 
Representa o segundo processo (processo 1), com o mesmo comportamento do processo 0. Ele também verifica a variável turn e a lista flag para garantir que não haja acesso simultâneo à região crítica.

## 🔍 Exemplo de Execução
Ao executar o código, a saída no console será algo como:
```bash
Processo 0 está na região crítica.
Processo 1 está na região crítica.
Processo 0 está na região NÃO crítica.
Processo 1 está na região NÃO crítica.
```

<h2 id="colab" style="font-weight: bold; font-size: 2rem">Contribuidores</h2>
 
  <table align="center">
    <tr>
      <td align="center">
        <a href="#">
          <img src="https://avatars.githubusercontent.com/u/146909378?v=4" width="100px;" alt="Foto de Perfil 1"/><br>
          <sub>
            <a href="https://github.com/kaychenderson"><b>Kayc Henderson</b></a>
          </sub>
        </a>
      </td>
          </sub>
        </a>
      </td>
      <td align="center">
        <a href="#">
        </a>
      </td>
      <td align="center">
        <a href="#">
          <img src="https://avatars.githubusercontent.com/u/97909025?v=4" width="100px;" alt="Foto de Perfil 2"/><br>
            <sub>
              <a href="https://github.com/JoanaLOliveira"><b>Joana Larissa</b></a>
            </sub>
        </a>
      </td>
    </tr>
  </table>
</div>
