# 📨 Notificador Automático de Faturas Vencidas

Este projeto é uma automação em Python que lê uma base de dados de faturas, identifica quais estão vencidas com base na data atual e envia automaticamente um e-mail de cobrança personalizado para cada cliente inadimplente.

---

## 📄 Sobre o Projeto

O objetivo deste script é automatizar o processo de cobrança inicial, uma tarefa essencial mas repetitiva. Utilizando `pandas` para a manipulação de dados e a biblioteca `datetime`, o sistema faz uma verificação diária e age de forma proativa, garantindo que nenhuma fatura vencida seja esquecida.

---

## ✨ Funcionalidades

-   **Leitura de Dados**: Carrega uma lista de faturas a partir de um arquivo `.csv`.
-   **Lógica de Datas**: Utiliza a biblioteca `datetime` para obter a data atual e compará-la com as datas de vencimento.
-   **Filtragem de Dados**: Isola de forma eficiente apenas as faturas que estão com o pagamento atrasado.
-   **Envio de E-mails Personalizados**: Itera sobre a lista de faturas vencidas e envia um e-mail em HTML para cada cliente, mencionando seu nome, o valor da fatura e a data de vencimento para uma comunicação clara e direta.

---

## 🗃️ Estrutura dos Dados

O script espera encontrar um arquivo chamado `faturas.csv` no mesmo diretório, com a seguinte estrutura de colunas:

-   `cliente`: Nome do cliente ou da empresa.
-   `email`: Endereço de e-mail do cliente para o qual a notificação será enviada.
-   `valor`: O valor monetário da fatura.
-   `data_vencimento`: A data de vencimento da fatura no formato `AAAA-MM-DD`.

---

## 💻 Tecnologias Utilizadas

-   **Python 3**
-   **Pandas**: Para leitura e manipulação eficiente dos dados da planilha.
-   **datetime**: Para lidar com a lógica de comparação de datas.
-   **smtplib & email.message**: Para a construção e envio dos e-mails.

---

## 🚀 Como Executar

Siga os passos abaixo para executar o projeto em sua máquina local.

1.  **Pré-requisitos**
    -   Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado.

2.  **Clone o Repositório**
    ```bash
    git clone [https://URL-DO-SEU-REPOSITORIO.git](https://URL-DO-SEU-REPOSITORIO.git)
    cd nome-do-diretorio-do-projeto
    ```

3.  **Crie e Ative um Ambiente Virtual** (Recomendado)
    ```bash
    # Para Linux/macOS
    python3 -m venv .venv
    source .venv/bin/activate

    # Para Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

4.  **Instale as Dependências**
    ```bash
    pip install pandas
    ```

5.  **Configure suas Credenciais de E-mail**
    -   Abra o script Python.
    -   Preencha as variáveis `MEU_EMAIL` e `MINHA_SENHA_APP` com seu e-mail do Gmail e uma [Senha de App](https://support.google.com/accounts/answer/185833) gerada.

6.  **Prepare os Dados**
    -   Certifique-se de que o arquivo `faturas.csv` está no mesmo diretório do script e preenchido com os dados a serem processados.

7.  **Execute o Script**
    ```bash
    python nome_do_seu_script.py
    ```

---

## 📈 Exemplo de Saída

Ao ser executado, o script irá imprimir no terminal uma mensagem de sucesso para cada e-mail de cobrança enviado:
```
-> E-mail de cobrança para Empresa Alpha enviado com sucesso!
-> E-mail de cobrança para Consultoria Gama enviado com sucesso!
```
