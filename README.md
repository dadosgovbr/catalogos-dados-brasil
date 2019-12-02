# Catálogos de dados abertos no Brasil

Um mapeamento de iniciativas (e catálogos) de dados abertos governamentais no Brasil.

[![goodtables.io](https://goodtables.io/badge/github/dadosgovbr/catalogos-dados-brasil.svg)](https://goodtables.io/github/dadosgovbr/catalogos-dados-brasil)

## Definição

Um catálogo de dados é uma coleção curada de metadados a respeito de conjuntos de dados. Essa é a definição especificada pelo [*Data Catalog Vocabulary* (DCAT)](https://www.w3.org/TR/vocab-dcat/#class-catalog).

Exemplos de catálogos de dados são: o portal de dados abertos da prefeitura do município X, o portal de dados abertos da assembleia legislativa do estado Y, etc.

## Como usar

Há várias maneiras possíveis de utilizar os dados.

* Pela web: a visualização do
  [Portal Brasileiro de Dados Abertos](http://dados.gov.br/pagina/outras-iniciativas)
  é sincronizada com este repositório.
* Pelo Github: veja a pré-visualização da
  [tabela](dados/catalogos.csv) que o próprio Github oferece.
* Pelo seu computador: faça clone do repositório e use a sua ferramenta
  favorita para abrir o arquivo CSV: Libreoffice Calc, Excel, etc.
* Pelo Jupyer Notebook / Jupyter Lab: veja o nosso
  [exemplo / tutorial](scripts/uso/como-usar-com-o-pandas.ipynb) de como usar.

## Como contribuir

Que contribuir com informações? Excelente! Leia o nosso
[guia de contribuição](CONTRIBUTING.md).

## Padronização

Os dados deste repositório estão descritos conforme o padrão
*[Tabular Data Packages](https://frictionlessdata.io/specs/tabular-data-package/)*
do *[Frictionless Data](https://frictionlessdata.io/)* (dados sem fricção).

Isto significa que, a cada atualização no repositório, os dados são validados
automaticamente conforme o esquema definido no arquivo
[datapackage.json](datapackage.json). O serviço de validação é oferecido pelo
site [goodtables.io](http://goodtables.io),
[fornecido pela Open Knowledge](https://discuss.okfn.org/t/launching-goodtables-io-tell-us-what-you-think/5165).

