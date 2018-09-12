import csv
from urllib.parse import urljoin
from datetime import datetime

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


# Read the data from the Brazilian repository of data catalogs

with open('../dados/catalogos.csv') as br_csv:
    br_catalogs = csv.DictReader(br_csv)
    with open ('portals.csv', 'w') as portals_csv:
        br_dataportals = csv.DictWriter(portals_csv, fieldnames=fieldnames)
        br_dataportals.writeheader()
        for br_catalog in br_catalogs:
            # Prepare a blank line
            new_portal = dict(map(lambda key: (key, ''),fieldnames))
            # Map values
            new_portal['name'] = br_catalog.get('Título','')
            new_portal['url'] = br_catalog['URL']
            tags = []
            if br_catalog.get('Município',''):
                tags.append('city')
                tags.append(br_catalog['Município'])
            if br_catalog.get('UF',''):
                tags.append('local-government')
                tags.append('br-' + br_catalog['UF'])
            if br_catalog.get('Solução','') == 'CKAN':
                tags.append(br_catalog['Solução'])
                new_portal['api_endpoint'] = urljoin(br_catalog['URL'], '/api/3')
                new_portal['api_type'] = 'CKAN'
            new_portal['tags'] = ','.join(tags)
            new_portal['generator'] = 'https://github.com/dadosgovbr/catalogos-dados-brasil'
            new_portal['metadatacreated'] = str(datetime.now())
            br_dataportals.writerow(new_portal)

