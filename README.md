# docsearch_api (skeleton)
Este é um esqueleto de projeto Django + DRF focado em **busca/filtragem avançada** para documentos científicos.

Como usar (local, rápido):
1. Crie um virtualenv (Python 3.11+ recomendado)
2. Instale dependências: `pip install -r requirements.txt`
3. Rode migrações: `python manage.py migrate`
4. Crie superuser: `python manage.py createsuperuser`
5. Rode o servidor: `python manage.py runserver`

Endpoints principais:
- `GET /api/papers/?q=termo&author=nome&min_year=2000&ordering=-published_year`

Este é um esqueleto para estudo e ampliação (incluir Celery, Redis, Postgres, Elastic, testes, etc.).
