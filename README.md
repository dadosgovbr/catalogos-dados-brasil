# Catálogos de dados abertos no Brasil

Um mapeamento de iniciativas (e catálogos) de dados abertos governamentais no Brasil.

[![goodtables.io](https://goodtables.io/badge/github/dadosgovbr/catalogos-dados-brasil.svg)](https://goodtables.io/github/dadosgovbr/catalogos-dados-brasil)

## Definição

Um catálogo de dados é uma coleção curada de metadados a respeito de conjuntos de dados. Essa é a definição especificada pelo [*Data Catalog Vocabulary* (DCAT)](https://www.w3.org/TR/vocab-dcat/#class-catalog).

Exemplos de catálogos de dados são: o portal de dados abertos da prefeitura do município X, o portal de dados abertos da assembleia legislativa do estado Y, etc.

## Critérios de qualificação

Para fazer parte dessa lista, a iniciativa deve satisfazer as seguintes condições:

* ser de responsabilidade de algum órgão público brasileiro;
* o órgão público não ser vinculado ou subordinado a uma instituição superior que também possui iniciativa de dados abertos (nesses casos, os dados devem ser agregados no portal desta instituição e este, por sua vez, será incluído na base);
* conter um catálogo ou portal com múltiplos [conjuntos de dados](http://dados.gov.br/paginas/faq/#q10), dos quais uma expressiva parte possam ser considerados [dados abertos](http://dados.gov.br/pagina/dados-abertos) e que abranjam uma expressiva parte do portfólio da instituição pública;
* conter metadados relevantes que contextualizem os dados, tais como título, descrição, informação de quem são os responsáveis pelos dados, etc.

Em especial, são exemplos de sites que não se qualificam:

* um único conjunto de dados;
* repositórios de arquivos sem os respectivos metadados que os contextualizem;
* APIs de dados abertos, quando representarem um único conjunto de dados de
  uma única área específica dentro da instituição;
* portais da transparência ou outros que contenham informações, mas não dados
  brutos e estruturados (estes estão catalogados no
  [levantamento de portais de transparência e dados abertos](https://github.com/augusto-herrmann/transparencia-dados-abertos-brasil/blob/master/LEIAME.md);
* portais de dados que contenham predominantemente dados não abertos ou com
  licença restritiva;
* portais de dados abertos de órgãos públicos vinculados ou subordinados a
  outros que também possam portais de dados abertos (nesses casos, os dados
  devem ser agregados no portal desta instituição e este, por sua vez, será
  incluído na base);
* portais que contenham apenas catálogo de bases de dados, sem disponibilizar
  downloads de dados abertos relacionados a essas bases;
* visualizações, painéis de *business intelligence/analytics* ou similares.

## Como contribuir

Contribuições são bem vindas! Se você encontrou um catálogo de dados, verifique
primeiro se ele atende aos critérios de qualificação acima. Confira também se
ele já está na planilha em [dados/catalogos.csv](/dados/catalogos.csv).
Para propor a inclusão de um novo catálogo de dados, edite a planilha e faça um
*[pull request](https://help.github.com/articles/about-pull-requests/)*.

Certifique-se de manter a estrutura da planilha (delimitador de campos, uso de
aspas, etc.), de modo que o commit apenas acrescente a(s) linha(s) que pretende
contribuir e não altere todo o arquivo.

Se encontrou algum problema no reposítório, você também pode abrir uma
*[issue](../../issues)* no Github.

## Padronização

Os dados deste repositório estão descritos conforme o padrão
*[Tabular Data Packages](https://frictionlessdata.io/specs/tabular-data-package/)*
do *[Frictionless Data](https://frictionlessdata.io/)* (dados sem fricção).

Isto significa que, a cada atualização no repositório, os dados são validados
automaticamente conforme o esquema definido no arquivo
[datapackage.json](datapackage.json). O serviço de validação é oferecido pelo
site [goodtables.io](http://goodtables.io),
[fornecido pela Open Knowledge](https://discuss.okfn.org/t/launching-goodtables-io-tell-us-what-you-think/5165).

