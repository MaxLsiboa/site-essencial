from flask import Flask, render_template

app = Flask(__name__)

PIX_CODE = '4be263cc-cbf1-46c2-8bb0-aec274df9a4a'

# Dictionary to store the URLs corresponding to callback_data
url_dict = {
    'cpf': 'https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp',
    'gov_br': 'https://acesso.gov.br/',
    'obter' : 'https://www.gov.br/pt-br/servicos/obter-a-carteira-de-trabalho',
    'serasa' : 'https://empresas.serasaexperian.com.br/campanhas/gratuidades-serasa-experian?utm_channel=c04&utm_bu=pme&utm_source=microsoft&utm_medium=cpc&utm_campaign=pesquisa_produto_gratuidades_bing&msclkid=5f8ec50a5f851109f212a1962171a924',
    'fies': 'https://login.caixa.gov.br/auth/realms/internet/protocol/openid-connect/auth?response_type=code&client_id=cli-web-fes-devops&redirect_uri=https%3A%2F%2Ffies.caixa.gov.br%2Ffes-web%2F&state=ffc9b450-882d-4c77-a16d-e91ab0c0ceaf&login=true&scope=openid',
    'segunda_via_cpf': 'https://servicos.receita.fazenda.gov.br/servicos/cpf/impressaocomprovante/consultaimpressao.asp',
    'segunda_via_sus': 'https://conectesus-paciente.saude.gov.br/',
    'titulo_eleitor': 'https://www.tse.jus.br/eleitor/titulo-e-local-de-votacao/consulta-por-nome',
    'cnpj': 'https://www.receita.fazenda.gov.br/PessoaJuridica/CNPJ/cnpjreva/Cnpjreva_Solicitacao.asp',
    'das_mei': 'https://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app/Identificacao/',
    'certidao_criminal_federal': 'https://antecedentes.dpf.gov.br/antecedentes-criminais/certidao',
    'certidao_criminal_eleitoral': 'https://www.tse.jus.br/servicos-eleitorais/certidoes/certidao-de-crimes-eleitorais',
    'certidao_negativa_alistamento_eleitoral': 'https://www.tse.jus.br/servicos-eleitorais/certidoes/certidao-negativa-alistamento-eleitoral',
    'certidao_quitacao_eleitoral': 'https://www.tse.jus.br/servicos-eleitorais/certidoes/certidao-de-quitacao-eleitoral',
    'certidao_filiacao_partidaria': 'https://www.tse.jus.br/servicos-eleitorais/certidoes/certidao-de-filiacao-partidaria',
    'certificado_regularidade_fgts': 'https://www.fgts.gov.br/Pages/sou-empregador/certificado-de-regularidade-do-fgts-crf.aspx',
    'pis_pasep': 'https://www.caixa.gov.br/beneficios-trabalhador/pis/Paginas/default.aspx',
    'bcb' : 'https://www.bcb.gov.br/meubc/valores-a-receber',
    'eb' : 'https://alistamento.eb.mil.br/',
    'curso' : 'https://cadastro.escoladotrabalhador40.com.br/',
    'pro' : 'https://acessounico.mec.gov.br/programas',
    'enem' : 'https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem',
}

@app.route('/')
def start():
    return render_template('index.html', url_dict=url_dict, pix_code=PIX_CODE)

@app.route('/button/<selected_service>')
def button(selected_service):
    if selected_service in url_dict:
        return f"Obrigado por usar nosso serviço! Para fazer uma doação e apoiar nosso projeto, utilize o PIX: {PIX_CODE}"
    else:
        return "Serviço inválido selecionado."

if __name__ == '__main__':
    app.run(debug=True)
