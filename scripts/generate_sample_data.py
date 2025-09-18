# script para populacao rapida (execute via: python manage.py shell < scripts/generate_sample_data.py)
from papers.models import Author, Paper
a1, _ = Author.objects.get_or_create(name='Maria Silva')
a2, _ = Author.objects.get_or_create(name='Joao Souza')
for i in range(1,21):
    p = Paper.objects.create(title=f'Pesquisa sobre tema {i}', abstract='Resumo do estudo '+str(i),
                             published_year=2000 + (i % 25), doi=f'10.1000/test{i}', keywords=['ml','ai'], xml_raw='')
    p.authors.add(a1 if i%2==0 else a2)
print('20 papers criados')
