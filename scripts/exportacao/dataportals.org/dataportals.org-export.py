import csv
from urllib.parse import urljoin
from datetime import datetime
import unicodedata, re

fieldnames = ['name',
 'title',
 'url',
 'author',
 'publisher',
 'issued',
 'publisher_classification',
 'description',
 'tags',
 'license_id',
 'license_url',
 'place',
 'location',
 'country',
 'language',
 'status',
 'metadatacreated',
 'generator',
 'api_endpoint',
 'api_type',
 'full_metadata_download']

def slug(name):
    'Creates a slug identifier from a name'
    slug = unicodedata.normalize('NFKD', name)
    slug = slug.lower()
    slug = re.sub(' ','-',slug)
    slug = re.sub('[^a-z0-9-]+', '', slug).strip('-')
    slug = re.sub('[-]+', '-', slug)
    return slug

def is_other(name):
    'Takes a guess whether or not the name refers to a another kind of entity, e.g. court of accounts.'
    other = False
    if 'tribunal' in name.lower():
        other = True
    elif 'tce' in name.lower():
        other = True
    elif 'tcm' in name.lower():
        other = True
    elif 'mp' in name.lower():
        other = True
    return other

def description(name, municipality, state, power):
    'Try to guess a description in some cases, if possible.'
    if is_other(name):
        return ''
    if municipality and state and power == 'Executivo':
        return 'Open Data portal of the city of {}, {}, in Brazil'.format(municipality, state)
    if state and power == 'Executivo':
        return 'Open Data portal of the state of {}, in Brazil'.format(state)
    if municipality and state and power == 'Legislativo':
        return 'Open Data portal of the local parliament of the city of {}, {}, in Brazil'.format(municipality, state)
    if state and power == 'Legislativo':
        return 'Open Data portal of the local parliament of the state of {}, in Brazil'.format(state)
    return ''

# Read the data from the Brazilian repository of data catalogs

with open('../../../dados/catalogos.csv') as br_csv:
    br_catalogs = csv.DictReader(br_csv)
    with open ('portals.csv', 'w') as portals_csv:
        br_dataportals = csv.DictWriter(portals_csv, fieldnames=fieldnames)
        br_dataportals.writeheader()
        for br_catalog in br_catalogs:
            # Prepare a blank line
            new_portal = dict(map(lambda key: (key, ''),fieldnames))
            # Map values
            new_portal['name'] = slug(br_catalog.get('Título',''))
            new_portal['title'] = br_catalog.get('Título','')
            new_portal['url'] = br_catalog['URL']
            new_portal['country'] = 'BR'
            new_portal['language'] = 'pt'
            new_portal['status'] = 'active'
            new_portal['publisher_classification'] = 'Government'
            tags = []
            # Is it a city catalog?
            if br_catalog.get('Município','') and br_catalog.get('UF',''):
                new_portal['place'] = ', '.join((br_catalog['Município'], br_catalog['UF'], 'Brazil'))
                new_portal['description'] = description(
                    br_catalog.get('Título',''),
                    br_catalog.get('Município',''),
                    br_catalog.get('UF',''),
                    br_catalog.get('Poder','')
                    )
                tags.append('city')
                tags.append('local-government')
                tags.append('br-' + br_catalog['UF'])
                tags.append(br_catalog['Município'])
            # or is it a state catalog?
            elif br_catalog.get('UF',''):
                new_portal['place'] = ', '.join((br_catalog['UF'], 'Brazil'))
                new_portal['description'] = description(
                    br_catalog.get('Título',''),
                    br_catalog.get('Município',''),
                    br_catalog.get('UF',''),
                    br_catalog.get('Poder','')
                    )
                tags.append('local-government')
                tags.append('br-' + br_catalog['UF'])
            # Does it use CKAN?
            if br_catalog.get('Solução','') == 'CKAN':
                tags.append(br_catalog['Solução'])
                new_portal['generator'] = br_catalog['Solução']
                new_portal['api_endpoint'] = urljoin(br_catalog['URL'], '/api/3')
                new_portal['api_type'] = 'CKAN API'
            new_portal['tags'] = ','.join(tags)
            new_portal['metadatacreated'] = datetime.now().isoformat(timespec='seconds')+'Z'
            br_dataportals.writerow(new_portal)

