# Socket TCP Client/Server em Python

Projeto para **testes de comunicação via sockets TCP** usando Python 3.

---

## Tech's

* Python 3
* Biblioteca padrão: `socket`
* Protocolo: **TCP** (`AF_INET` + `SOCK_STREAM`)

---

## Conceitos Utilizados

* Socket de rede IPv4 (`AF_INET`)
* Socket TCP orientado à conexão (`SOCK_STREAM`)
* Bind, Listen e Accept (servidor)
* Connect e Send (cliente)
* Envio e recebimento de dados em **bytes** (`encode` / `decode`)
* Buffer de leitura (`recv(1024)`)(Armazena dados para processar)

---

## Estrutura do Projeto

```
.
├── server.py    # Socket TCP servidor
└── cliente.py   # Socket TCP cliente
└── README.MD
```

---

## Pré-requisitos para testar na sua maquina

* Sistema operacional com Python 3 instalado
* Verifique a versão:

```bash
python3 --version
```

---

## Preparação do Ambiente

Clone o repositório e dê permissão de execução aos arquivos:

```bash
chmod +x server.py cliente.py
```

---

## Como Executar

### Iniciar o Servidor

Em um terminal:

```bash
./server.py
```

Informe:

* **Host**: pressione Enter para usar `127.0.0.1`
* **Porta**: ex: `9473` ou `5007`

O servidor ficará aguardando conexões:

```text
Server is listening on 127.0.0.1:9473
```

---

### Iniciar o Cliente

Em outro terminal:

```bash
./cliente.py
```

Informe o mesmo **host** e **porta** do servidor.

---

### Enviar Mensagens

Digite mensagens no cliente:

```text
Type your mensage:
Hello socket my brother
```

No servidor:

```text
New mensage from host ('127.0.0.1', 34900): Hello socket my brother
```

A conexão permanece ativa até encerrar a execução.

---

## Observações

* O servidor utiliza `recv(1024)` como tamanho de buffer
* Mensagens são enviadas em bytes (`encode`) e convertidas no servidor (`decode`)
* Utilize **portas acima de 1024**
* Projeto voltado para **testes locais**

---

## Referência

Documentação oficial do Python:

[https://docs.python.org/3/library/socket.html](https://docs.python.org/3/library/socket.html)

