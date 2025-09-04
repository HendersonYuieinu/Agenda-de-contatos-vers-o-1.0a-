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
pagina única, nele podemos ver todos os contatos. temos as funções de adicionar contato, apagar e editar, até o momento a função de pesquisa e adicionar foto de perfil não foi criado.

<img width="462" height="791" alt="Captura de tela 2025-09-04 191433" src="https://github.com/user-attachments/assets/7211ad13-de6d-4e6d-9650-e7caa8e99ced" />


## Adicionar
botao de adicionar fica no canto superior direito, com esse icone indicado.

<img width="460" height="787" alt="Captura de tela 2025-09-04 191639" src="https://github.com/user-attachments/assets/7ff5ad35-6a1c-4714-9b56-607425e9bbfb" />
<img width="459" height="787" alt="Captura de tela 2025-09-04 191554" src="https://github.com/user-attachments/assets/3a76d747-8a5c-4d0b-a951-4da0a051d577" />

o numero de telefone já é automaticamente formatado para o formato de (99) 99999-9999
<img width="461" height="496" alt="Captura de tela 2025-09-04 191608" src="https://github.com/user-attachments/assets/951fe60c-9318-4e72-9662-6dfd9b2bf1a2" />

## Editar
em cada contato tem uma botao icone de editar, ao lado do botão de remover. Ele mostra os campos daquele contato e você pode atualizar as informações, que serão salvas ao clicar em confirmar.

<img width="459" height="793" alt="Captura de tela 2025-09-04 191654" src="https://github.com/user-attachments/assets/1ca6749d-e2cd-4d4a-ae44-d708abc53937" />
<img width="458" height="786" alt="Captura de tela 2025-09-04 191702" src="https://github.com/user-attachments/assets/fd109f9b-922d-458c-ab46-5bc41754f572" />

<img width="464" height="504" alt="Captura de tela 2025-09-04 193640" src="https://github.com/user-attachments/assets/8530b10e-702b-4cf7-baef-4e3255bd4965" />

exemplo editado.

## Deletar
em cada contato tem o botão icone de lixeira, onde vai pedir uma confirmação e ao confirmar, vai ser removido do banco de dados.

<img width="459" height="783" alt="Captura de tela 2025-09-04 191714" src="https://github.com/user-attachments/assets/e62103b8-16dd-4cae-adde-ecf89856bf48" />
<img width="460" height="787" alt="Captura de tela 2025-09-04 191723" src="https://github.com/user-attachments/assets/b8754097-2c13-41b4-8e89-a692bd014bcf" />


<img width="459" height="789" alt="Captura de tela 2025-09-04 191739" src="https://github.com/user-attachments/assets/5f7ab444-65b8-4767-a8c6-5dc945f50988" />

exemplo apagado com sucesso.


## Adendo 
O aplicativo até o momento não tem conexão com nenhum sistema de contatos externos para fazer conexão e importação dos contatos.
