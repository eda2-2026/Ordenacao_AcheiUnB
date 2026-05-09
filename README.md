# AcheiUnB

**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Ordenação<br>

## Alunos
| Matrícula | Aluno |
| -- | -- |
| 23/1011220  |  Davi Camilo Menezes |
| 23/1026714  |  Euller Júlio da Silva |

## Apresentação do trabalho
[Link para o vídeo de apresentação]([TODO: Inserir link do vídeo aqui])

## Sobre
O [AcheiUnB](https://github.com/unb-mds/2024-2-AcheiUnB) é um projeto criado para facilitar a busca e a recuperação de itens perdidos na Universidade de Brasília.

Este trabalho tem como objetivo aprimorar a recomendação de itens encontrados (matches) implementando um sistema de ranqueamento. A ideia principal é calcular um **score de similaridade** entre o item perdido e os possíveis candidatos encontrados, e então ordenar esses candidatos de forma decrescente utilizando o algoritmo de **Merge Sort** implementado manualmente. Isso permite que o usuário veja primeiro os itens que têm maior probabilidade de ser o seu objeto perdido.

<!-- Davi, você pode completar com mais detalhes sobre a justificativa da escolha do Merge Sort, estabilidade do algoritmo ou sobre os pesos do cálculo de similaridade. -->

## Screenshots
A seguir estão imagens do projeto em funcionamento.

### [TODO: Título da imagem (Ex: Resultado dos testes ou benchmark)]

![placeholder](docs/assets/[TODO:nome_da_imagem].png)

<!-- Davi, você pode [TODO: Adicionar uma breve descrição sobre o que a imagem acima está mostrando.] -->

### Execução local dos testes

Para garantir que o cálculo de score e a ordenação estão funcionando como esperado, foram criados arquivos de testes automatizados (`test_match_ranking.py` e `test_merge_sort.py`). 

<!-- Davi, você pode adicionar uma screenshot do terminal mostrando o `pytest` passando com 100% de sucesso. -->

## Instalação
**Linguagem**: Python 3.10+<br>
**Framework**: Não foi utilizado<br>
**Pré-requisitos:** Python instalado e `pytest` para rodar os testes.<br>

### Como rodar

1. Criar e ativar ambiente virtual (recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pytest
```

2. Executar a suíte de testes

```bash
# Na pasta tests/ rode o comando abaixo para executar todos os testes
pytest
```

## Uso
Para este projeto de EDA2, o uso principal do núcleo está na validação da ordenação e do ranqueamento:

1. Entender como a função de *score* foi montada para atributos categóricos e de texto.
2. Validar a corretude do **Merge Sort** ao ordenar listas de candidatos (matches) através dos testes automatizados.

<!-- Davi, você pode complementar se houver um script de uso interativo para simular as buscas além dos testes. -->

## Outros
Este repositório não representa o projeto AcheiUnB em si, mas sim o núcleo desacoplado desenvolvido para a disciplina de Estruturas de Dados 2 (EDA2). Sua função é concentrar a implementação do algoritmo de **Ordenação** (Merge Sort) de forma separada, facilitando testes, análise e a validação isolada do ranqueamento. A integração desse módulo ao fluxo real do AcheiUnB deverá ser realizada no repositório principal através de um Pull Request.
