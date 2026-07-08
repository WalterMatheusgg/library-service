## Resumo

Este Pull Request implementa um projeto de portfólio Django personalizado chamado Biblioteca Digital.

O projeto foi desenvolvido com base na estrutura do projeto Taxi Service e inclui visualizações, modelos, autenticação e operações CRUD.

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

python manage.py seed_data


## Capturas de tela:

<img width="1314" height="726" alt="Screenshot 2026-07-07 01 12 38" src="https://github.com/user-attachments/assets/0b9d3210-eee0-405a-9c41-f7a0b9bd93df" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 12 27" src="https://github.com/user-attachments/assets/442ca21a-e49c-4907-9f2b-e188e0d6dd84" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 12 19" src="https://github.com/user-attachments/assets/8e739a35-5311-4d33-890b-bec6317f071a" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 12 09" src="https://github.com/user-attachments/assets/d782890a-2ac8-44c4-b2a5-c664b656d9ac" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 11 59" src="https://github.com/user-attachments/assets/9f07fb20-988c-421b-b1c3-5ed686eb6595" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 11 44" src="https://github.com/user-attachments/assets/e433fa32-83d9-4df3-8757-29a0ec6544a5" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 11 27" src="https://github.com/user-attachments/assets/31cf243a-abc4-4bb0-b93e-b399ac2bac20" />
<img width="1314" height="726" alt="Screenshot 2026-07-07 01 11 21" src="https://github.com/user-attachments/assets/c6a610cb-8f47-4682-aea0-1d1889f57b36" />
<img width="1318" height="727" alt="Screenshot 2026-07-07 00 51 55" src="https://github.com/user-attachments/assets/fc553bd5-0847-4752-a60b-36be7e054951" />
<img width="1318" height="727" alt="Screenshot 2026-07-07 00 50 57" src="https://github.com/user-attachments/assets/5c916f30-d475-46ed-a7f3-4fb3c3da00f5" />
<img width="1318" height="727" alt="Screenshot 2026-07-07 00 50 09" src="https://github.com/user-attachments/assets/80b05085-e079-4c25-bc08-3e56e0cc1b56" />
<img width="1318" height="727" alt="Screenshot 2026-07-07 00 49 26" src="https://github.com/user-attachments/assets/56ffe7e2-a49f-4520-9b58-eb72bb4abf8d" />



## Diagrama do banco de dados:

<img width="1800" height="1200" alt="diagrama_banco_biblioteca_digital" src="https://github.com/user-attachments/assets/5450f4e1-0274-411a-8971-266c7217fa4f" />

