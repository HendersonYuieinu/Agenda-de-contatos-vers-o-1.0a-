# Agenda-de-contatos-vers-o-1.0a-
aplicativo ainda em desenvolvimento para armazenar e organizar contatos, incluindo nome, e-mail, telefone e notas sobre.

## Técnologias usadas
para a interface gráfica, flet.
para a criação e manipulação do banco de dados, foi usado o SQLalchemy

## Banco de dados
usando um banco de dados relacional, temos 3 tabelas: <br>
Contato: com os campos ID, nome, sobrenome e nota.<br>
Email: com os campos ID, a chave estrangeira relacionada ao contato e o email.<br>
Telefone: com os campos ID, a chave estrangeira tambem relacionada ao contato e o numero de telefone.

## Interface
pagina única, nele podemos ver todos os contatos. temos as funções de adicionar contato, apagar e editar, até o momento a função de pesquisa e adicionar foto de perfil não foi criado. <br>
as informações dos contatos já adicionados estão censurados para proteger privacidade.

<img width="462" height="791" alt="Captura de tela 2025-09-04 191433" src="https://github.com/user-attachments/assets/7211ad13-de6d-4e6d-9650-e7caa8e99ced" />

## Adendo 
O aplicativo até o momento não tem conexão com nenhum sistema de contatos externos para fazer conexão e importação dos contatos.
