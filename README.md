#  Testes Automatizados para Modelos de IA - Trabalho 1 (TDD)

## Sumário
- [Test Driven Development e GitHub Actions](#test-driven-development-e-github-actions)
- [Funções Implementadas](#funções-implementadas)
  - [1. `class_to_idx`](#1-class_to_idxitems-liststr---dictstr-int)
  - [2. `fit_label_encoder`](#2-fit_label_encodermapping-dictstr-int-items-liststr---listint)
- [Testes](#testes)
- [Demo de Função "bugada"](#demo-de-função-bugada)
- [Como Executar Localmente](#como-executar-localmente)
  - [1. Sincronizar o ambiente](#1-sincronizar-o-ambiente)
  - [2. Executar os testes com estatísticas](#2-executar-os-testes-com-estatísticas-do-hypothesis)
- [Matriz de Rastreabilidade TDD & GitHub Actions](#matriz-de-rastreabilidade-tdd--github-actions)
___

## Test Driven Development e GitHub Actions
Com intuito de evidenciar o ciclo de etapas do TDD, foi utilizado um pipeline simples do GitHub Actions para execução automática de testes, disponível em `/.github/workflows/test.yaml`. A seção ["Matriz de Rastreabilidade TDD & GitHub Actions"](#matriz-de-rastreabilidade-tdd--github-actions) proporciona uma visão geral de cada fase/commit.
Os testes utilizaram Hypothesis e Pytest, juntamente com `uv` para manejar o ambiente python nas execuções.

Dessa maneira, é possível acompanhar as etapas de RED/GREEN/REFACTOR na aba "Actions" do repositório, o qual mostra se os testes falharam ou foram bem sucedidos. Ao clicar em uma run, seguido do hash do commit, é possível ver o diff, tornando facilmente identificável a parte do código que foi modificada, demonstrando o que levou ao respectivo status do teste.

As mensagens de commit seguem um convenção mapeando às etapas do TDD: 

- **RED**: quando o teste falha pela ausência de uma funcionalidade específica ou **edge case**.
- **GREEN**: implementação mínima de código para o teste passar; geralmente envolvendo uma solução hardcoded.
- **REFACTOR(RED)**: quando o teste é incrementado e a função falha por ser hardcoded.
- **REFACTOR(GREEN)**: quando a implementação é de fato refatorada com a business logic correta, passando os testes presente naquele momento.

___
## Funções Implementadas
Imaginou-se o cenário de um **classifier** o qual não é capaz de lidar com targets do tipo string, sendo necessário converter as **classes/labels** para **integers**. Essas funções estão presentes em `/src/tdd_assignment/__init__.py`, fazendo parte do package nomeado de `tdd_assignment`.

### 1. `class_to_idx(items: list[str]) -> dict[str, int]`
Esta função cria um dicionário mapeando cada classe única para um índice inteiro contíguo, ordenado alfabeticamente.
```python
# Versão final
def class_to_idx(items: list[str]) -> dict[str, int]:
    return {item: idx for idx, item in enumerate(sorted(set(items)))}
```

### 2. `fit_label_encoder(mapping: dict[str, int], items: list[str]) -> list[int]`
Performa o **encoding** de uma lista de strings em índices com base no mapeamento fornecido. Categorias não mapeadas recebem, por padrão, o valor `-1`.

```python
# Versão final
def fit_label_encoder(mapping: dict[str, int], items: list[str]) -> list[int]:
    return [mapping.get(i, -1) for i in items]
```

## Testes
Os testes se encontram em `/tests`. E possuem três arquivos:

- `test_setup.py` utilizado para verificar a funcionalidade correta do GHA workflow.
- `test_mapper.py` contém os testes e verificação de propriedades para a função `class_to_idx`.
- `test_label_encoder.py` contém os testes para a função `fit_label_encoder` (mas que também utiliza `class_to_idx` em partes).

Foi combinado Pytest para execução de testes, e o Hypothesis para verificação de propriedade das funções. A explicação das propriedades se faz presente no código por meio de comentários. 

>Nota 
> Após o último commit do tipo `REFACTOR(GREEN)`, foram adicionados dois outros commits para verificar as propriedades das funções: `Add property check for class_to_idx. All passed.` (Run #17) e `Add property tests for label encoder` (Run #18), todos passantes. Esses dois commits tem como objetivo demonstrar que as duas funções finais, possuem um série de propriedades que emergiram a partir do TDD.
___

## Demo de Função "bugada"
Para demonstrar que as propriedades especificadas capturam um bug real, basta verificar a última run de commit `FAIL - introduce bug in function to showcase tests capture it`, o qual, sob inspeção do diff, nota-se que foi removido o `sorted` da função `class_to_idx` , promovendo uma falha proposital da propriedade `test_mapping_always_has_alphabetical_order`. 

```python
def class_to_idx(items: list[str]) -> dict[str, int]:
    return {item: idx for idx, item in enumerate(sorted(set(items)))}


# Buggy version: does not sort - Will fail properties
def class_to_idx(items: list[str]) -> dict[str, int]:
    return {item: idx for idx, item in enumerate(set(items))}
```
___
## Como Executar Localmente

### 1. Sincronizar o ambiente
[Requer uv instalado](https://docs.astral.sh/uv/getting-started/installation/).

```bash
uv sync --group test
```

### 2. Executar os testes com estatísticas do Hypothesis
```bash
uv run pytest tests/ -s -vv --hypothesis-show-statistics
```

## Matriz de Rastreabilidade TDD & GitHub Actions
> Nota 1: esta seção tem como objetivo facilitar o processo de avaliação. Foi gerada pelo Gemini 3.7 Flash combinando histórico de commits + histórico de runs do GHA. 

> Nota 2: é possível notar que o número das runs não é contíguo, por exemplo: pula de #14 para #17. Isto porque alguns commits estavam incompletos, essas runs foram apagadas para não poluir a página.

A tabela a seguir correlaciona cada commit, sua fase no ciclo TDD, a modificação realizada e o status registrado na pipeline de CI do GitHub Actions.


| Run CI | Commit SHA | Fase TDD | Mensagem do Commit | Descrição da Modificação / Diff | Status CI |
| :---: | :---: | :---: | :--- | :--- | :---: |
| **#1** | `84aea72` | **SETUP** | *Repo structuring + GHA workflow creation for tests* | Configuração do `pyproject.toml`, pipeline GHA e teste de sanidade `test_setup.py`. | ✅ Pass |
| **#2** | `c40b346` | **RED** | *RED - Add test* | Criação do teste unitário `test_fit_label_encoder`. Falha: função inexistente. | ❌ Fail |
| **#3** | `a340456` | **GREEN** | *GREEN - function implements hardcoded return* | Implementação ingênua com retorno fixo `[0, 0, 1, 1, 3]`. | ✅ Pass |
| **#4** | `fbb2749` | **REFACTOR(RED)** | *Refactor (RED): fails case with alternate mapping* | Adição de asserção com mapeamento invertido. Retorno fixo falha. | ❌ Fail |
| **#5** | `db57e66` | **REFACTOR(GREEN)** | *REFACTOR(GREEN) - add correct indexing* | Generalização via list comprehension: `[mapping[i] for i in items]`. | ✅ Pass |
| **#7** | `8620915` | **RED** | *RED - function does not handle non-mapped class* | Teste para classes não mapeadas (`airplane`). Falha: `KeyError`. | ❌ Fail |
| **#8** | `4d84476` | **GREEN** | *GREEN - hardcode non-mapped class* | Implementação mínima condicional: `... if i != 'airplane' else -1`. | ✅ Pass |
| **#9** | `dd84f81` | **REFACTOR(RED)** | *REFACTOR(RED) - Function fails for new class* | Adição da nova classe não mapeada `scooter`. Condicional hardcoded falha. | ❌ Fail |
| **#10** | `48e28da` | **REFACTOR(GREEN)** | *REFACTOR(GREEN) - Correct implementation for handling...* | Implementação definitiva com tratamento seguro: `[mapping.get(i, -1) for i in items]`. | ✅ Pass |
| **#11** | `6f61a7a` | **RED** | *RED - NameError: name 'class_to_idx' is not defined* | Teste `test_mapper()` criado. Falha: `NameError: class_to_idx`. | ❌ Fail |
| **#12** | `70a412d` | **GREEN** | *GREEN - hardcoded mapping list to pass test* | Retorno hardcoded: `{'dog': 0, 'cat': 1, 'bird': 2}`. | ✅ Pass |
| **#13** | `3085e5c` | **RED** | *RED - Fails class that was not absent in hardcoded dict* | Adição de `lizard` na entrada. Falha pelo dicionário fixo. | ❌ Fail |
| **#14** | `07c1b62` | **REFACTOR(GREEN)** | *REFACTOR(GREEN) - Note: had to refactor test to ensure...* | Implementação com `sorted(set(items))` e refatoração do teste para ordem alfabética. | ✅ Pass |
| **#17** | `076f628` | **PROPERTY** | *Add property check for `class_to_idx`. All passed.* | Adição de 4 testes de propriedades com Hypothesis em `test_mapper.py`. | ✅ Pass |
| **#18** | `29f4bfa` | **PROPERTY** | *Add property tests for label encoder* | Adição de 4 testes de propriedades com Hypothesis em `test_label_encoder.py`. | ✅ Pass |
| **#19** | `bf9ec76` | **BUG DEMO** | *FAIL - introduce bug in function to showcase tests capture it* | Remoção proposital de `sorted()` em `class_to_idx`. Violação de invariante capturada. | ❌ Fail |
