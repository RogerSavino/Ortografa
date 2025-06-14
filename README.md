# Ortografa

Projeto pesssoal feito em Python que ajuda os jogadores a praticarem a ortografia correta de palavras com foco especial no uso das letras **S** e **Z**. Ele utiliza síntese de voz para pronunciar palavras, e o usuário deve digitá-las corretamente com base no que ouve.

## 🎮 Funcionalidades

- ✅ Jogo com palavras de diferentes níveis de dificuldade
- 🗣️ Palavras são faladas usando voz automática (text-to-speech)
- ✍️ O jogador digita o que ouviu e recebe feedback imediato
- 📜 Regras gramaticais explicadas para uso correto de **S** e **Z**
- 🧠 Modo de treino específico para palavras com **S** ou com **Z**
- 🏁 Fim do jogo ao errar uma palavra, com exibição da pontuação
- 📚 Modo "sem fim" para treinar continuamente

## 📋 Estrutura do Menu
1 - Começar Jogo sem fim
2 - Jogo com 10 palavras
3 - Jogo com 20 palavras
4 - Jogo com 30 palavras
5 - Regras de quando usar S
6 - Treinar palavras com S
7 - Regras de quando usar Z
8 - Treinar palavras com Z
10 - Sair

## 🛠️ Tecnologias utilizadas

- Python 3
- `pyttsx3` para síntese de voz (funciona offline)
- `os` e `time` para funcionalidades do sistema
- `random` para seleção aleatória de palavras

## ▶️ Como executar

1. Instale as dependências (se ainda não instaladas):
```
pip install pyttsx3

Rode em: python main.py
