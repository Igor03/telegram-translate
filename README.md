<h1 align = "center">
<strong>Telegram Translate</strong>
</h1>

## Descrição
Um serviço de tradução de textos utilizando a API do Google Translate e o Telegram.

## Tecnologias e ferramentas ultilizadas
* [Python 3.7](https://www.python.org/) - Linguagem utilizada para desenvolver as funcionalidades do projeto
* [Docker](https://www.docker.com/) - Utilizado para criação dos containers onde a aplicação deverá rodar
* [Visual Studio Code](https://code.visualstudio.com/) - IDE utilizada para desenvolvimento do projeto
* [Insomnia](https://insomnia.rest/) - Ferramenta utilizada para testar chamadas às API's utilizadas

## Instalação
Assumindo que você já possui o [GIT](https://git-scm.com/)  instalado em seu ambiente, clone o repositório usando o seguinte comando:
```
git clone https://github.com/Igor03/telegram-translate.git
```
Em seguida, navega até o diretório onde o repositório foi clonado
```
cd telegram-translate/
```
o rode o seguinte comando
```
docker build -t ${imagename} .
```

Então rode localmente, a imagem criada 
```
docker run ${imagename}
```

## Observação
Para que a aplicação rode, é necessário que você tenha, em seu ambiente, duas variáveis com os seguintes nomes
```
TELEGRAM-BOT-TOKEN
```
e
```
X-RAPIDAPI-KEY
```
que correspondem ao token de acesso à API do telegram, e ao Token de acesso à API do Google Translate.

Tais tokens de acesso podem ser facilmente obtidos seguindo as instruções dos links abaixo.
* [Para token Telegram](https://core.telegram.org/)
* [Para token Google Translate](https://rapidapi.com/googlecloud/api/google-translate1)

Sinta-se à vontade para alterar quaisquer nomes de variáveis que julgue inapropriado
