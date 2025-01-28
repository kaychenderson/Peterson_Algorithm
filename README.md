<h1 align="center" style="font-weight: bold;"> 🔐 Algoritmo de Peterson 💻</h1>
<p align="center">
    <a href="#tech">Tecnologias</a> •
    <a href="#about">Sobre o Algoritmo</a> •
    <a href="#colab">Contribuidores</a>
</p>

<div>
  <h2 id="tech" style="font-weight: bold; font-size: 2rem">Tecnologia Utilizada</h2> 
  <img align="center" alt="python" src="https://img.shields.io/badge/Python-FFFFFF?style=for-the-badge&logo=python&logoColor=black"/>

  <h2 id="about" style="font-weight: bold; font-size: 2rem">Sobre o Algoritmo</h2>

O Algoritmo de Peterson é uma solução clássica para o problema da exclusão mútua em sistemas com múltiplos processos concorrentes. Ele permite que dois processos compartilhem uma região crítica sem conflitos, garantindo que apenas um processo acesse a região crítica de cada vez.

## Como Funciona

- **Flags de Interesse:** Cada processo indica seu interesse em entrar na região crítica através de um vetor de flags. 
- **Turno de Acesso:** O algoritmo usa uma variável `turn` para determinar qual processo tem prioridade, prevenindo que ambos tentem acessar a região crítica simultaneamente.
- **Alternância Segura:** Cada processo alterna entre a região crítica e a região não crítica, respeitando as regras de exclusão mútua.
