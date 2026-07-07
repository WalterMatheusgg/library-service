## Biblioteca Digital 


## Resumo

Este Pull Request implementa um projeto de portfólio Django personalizado chamado Biblioteca Digital.

O projeto foi desenvolvido com base na estrutura do projeto Taxi Service e inclui visualizações, modelos, autenticação e operações CRUD. O principal objetivo é demonstrar habilidades em Django por meio de um aplicativo web completo que pode ser anexado a um currículo.

## Funcionalidades implementadas

- Página inicial com estatísticas do projeto
- Página de lista de livros com funcionalidade de pesquisa
- Página de detalhes do livro
- Criar, atualizar e excluir livros
- Página de lista de autores
- Página de detalhes do autor
- Criar, atualizar e excluir autores
- Página de lista de gêneros
- Criar, atualizar e excluir gêneros
- Autenticação de usuário com visualizações de autenticação integradas do Django
- Funcionalidade de empréstimo de livros
- Funcionalidade de devolução de livros
- Página Meus Empréstimos
- Layout responsivo baseado em Bootstrap
- Configuração de administração do Django para todos os modelos

## Estrutura do banco de dados

O projeto inclui os seguintes modelos:

- Autor
- Gênero
- Livro
- Empréstimo

Relacionamentos:

- Um Autor pode ter muitos Livros
- Um Livro pode ter muitos Gêneros
- Um Gênero pode ser conectado a muitos Livros
- Um Usuário pode ter muitos Empréstimos
- Um Livro pode ter muitos Empréstimos

## Funcionalidade opcional

O projeto inclui o empréstimo e a devolução de livros, permitindo que usuários autenticados gerenciem seus próprios livros emprestados por meio da página Meus Empréstimos.

## Diagrama do banco de dados

Um diagrama do banco de dados foi adicionado para mostrar a estrutura e os relacionamentos entre os modelos principais.

## Dados de exemplo

Foi criado um comando customizado para popular o sistema com livros, autores e gêneros reais:

```bash
python manage.py seed_data

O projeto também inclui um usuário comum para testes:

Usuário: demo
Senha: demo12345


## Capturas de tela:
<img width="1318" height="727" alt="Screenshot 2026-07-07 00 52 08" src="https://github.com/user-attachments/assets/956f9a0d-08f6-4338-9fad-dd8c3f4aa098" />
<img width="1318" height="727" alt="Screenshot 2026-07-07 00 51 55" src="https://github.com/user-attachments/assets/24bdf4e0-a8e2-425e-b08f-7bc4b5cdc0e1" />
<img width="1318" height="727" alt="Screenshot 2026-07-07 00 50 57" src="https://github.com/user-attachments/assets/81742362-2e34-4c30-ab04-19e10dd1f55b" />
<img width="1318" height="727" alt="Screenshot 2026-07-07 00 50 09" src="https://github.com/user-attachments/assets/deca437f-6572-45ec-9a0e-2b92a00b3f79" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 12 38" src="https://github.com/user-attachments/assets/a8ccd85e-2147-4b97-adee-fa0f781c6cf5" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 12 38" src="https://github.com/user-attachments/assets/2f23b654-8f50-4c3e-9121-e108f0107a66" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 12 27" src="https://github.com/user-attachments/assets/a77168e6-c4f2-43be-962a-93e354f22840" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 12 19" src="https://github.com/user-attachments/assets/53cab7c6-2a7e-4da7-bc94-f94ed2ec8801" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 12 09" src="https://github.com/user-attachments/assets/9e8b888c-116f-4949-9158-81b38f848b1e" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 11 59" src="https://github.com/user-attachments/assets/936762ec-377d-40a6-97af-e797ecb53506" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 11 44" src="https://github.com/user-attachments/assets/25a61252-a6d8-48ae-912f-ce723bc19ce0" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 11 27" src="https://github.com/user-attachments/assets/f5bd9b2c-8f76-44ea-a3f9-0f37dcb419db" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 11 21" src="https://github.com/user-attachments/assets/8125aca8-84c4-4f1b-ab6c-6d20ad9a759b" />



## diagrama do banco de dados:

<img width="1800" height="1200" alt="diagrama_banco_biblioteca_digital" src="https://github.com/user-attachments/assets/5450f4e1-0274-411a-8971-266c7217fa4f" />


