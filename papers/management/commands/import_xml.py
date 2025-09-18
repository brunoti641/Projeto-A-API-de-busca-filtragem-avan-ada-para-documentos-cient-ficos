from django.core.management.base import BaseCommand
from lxml import etree
from papers.models import Paper, Author
class Command(BaseCommand):
    help = 'Import papers from an XML file (expecting <paper> items)'
    def add_arguments(self, parser):
        parser.add_argument('xml_file', type=str)
    def handle(self, *args, **options):
        xml_file = options['xml_file']
        context = etree.iterparse(xml_file, events=('end',), tag='paper')
        count = 0
        for event, elem in context:
            title = elem.findtext('title') or ''
            abstract = elem.findtext('abstract') or ''
            year = elem.findtext('year')
            doi = elem.findtext('doi') or None
            paper, created = Paper.objects.get_or_create(doi=doi, defaults={
                'title': title,
                'abstract': abstract,
                'published_year': int(year) if year and year.isdigit() else None,
                'xml_raw': etree.tostring(elem, encoding='unicode')
            })
            # authors
            for a in elem.findall('authors/author'):
                name = (a.text or '').strip()
                if name:
                    author, _ = Author.objects.get_or_create(name=name)
                    paper.authors.add(author)
            paper.save()
            count += 1
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]
        self.stdout.write(self.style.SUCCESS(f'Imported {count} papers'))
