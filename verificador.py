import pandas as pd
import datetime as dt
import smtplib
from email.message import EmailMessage

faturas_atrasadas = pd.read_csv('faturas.csv')

data_atual = dt.datetime.today()
faturas_atrasadas['data_vencimento'] = pd.to_datetime(faturas_atrasadas['data_vencimento'])
faturas_vencidas = faturas_atrasadas[faturas_atrasadas['data_vencimento'] < data_atual]

MEU_EMAIL = "seu_email@gmail.com"
MINHA_SENHA_APP = "sua_senha_app"

print("\n--- Iniciando envio de e-mails de cobrança ---")
for index, linha in faturas_vencidas.iterrows():
    cliente = linha['cliente']
    email = linha['email']
    valor = linha['valor']
    vencimento = linha['data_vencimento']
    print(f"Cliente: {cliente}, E-mail: {email} - Cobrança no valor de R${valor:.2f} vencida em {vencimento.strftime('%d/%m/%Y')}")

    msg = EmailMessage()
    msg['Subject'] = f"Aviso de fatura Vencida - {cliente}"
    msg['From'] = MEU_EMAIL
    msg['To'] = email

    corpo_email = f"""
    <p>Prezado(a) Cliente: {cliente},<p>
    <p>Este é um aviso automático referente à sua fatura no valor de <strong>R${valor:,.2f}</strong>, que venceu em <strong>{vencimento.strftime('%d/%m/%Y')}</strong>.</p>
    <p>Por favor, realize a regularização o mais breve possível para evitar maiores transtornos.</p>
    <p>Em caso de dúvidas ou se o pagamento já foi efetuado, por favor, desconsidere este e-mail.</p>
    <p>Atenciosamente,</p>
    <p>Sistema de Cobranças Automático</p>
    """
    msg.set_content(corpo_email, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(MEU_EMAIL, MINHA_SENHA_APP)
            smtp.send_message(msg)
            print(f"-> E-mail de cobrança para {cliente} enviado com sucesso!")
    except Exception as e:
        print(f"!! ERRO ao enviar e-mail para {cliente}: {e}")