# Sistema Especialista — Oficina Mecânica Bom Motor

Sistema especialista de triagem de atendimento para oficina mecânica.
Disciplina: Programação de Sistemas Especialistas.

Repositório: https://github.com/Caio9004/oficina-bom-motor

O sistema faz perguntas sobre o veículo (motor, elétrica, freios, suspensão, alinhamento e ar-condicionado),
aplica 24 regras de diagnóstico (`if` explícitos) e indica o **setor da oficina**, a **urgência** e o
**diagnóstico provável**, além de explicar o raciocínio (por que/como cada regra disparou).

## Integrantes
- Integrante 1 — _preencher nome_
- Integrante 2 — _preencher nome_

## Vídeo de demonstração
_colar link do vídeo aqui_

## Estrutura
| Arquivo | Descrição |
|---|---|
| `oficina_json.py` | Programa principal (coleta de fatos, motor de inferência, explicação) |
| `base_conhecimento.json` | Base de conhecimento: textos das perguntas e dados de cada diagnóstico (setor, urgência, descrição) |

Os dois arquivos precisam ficar **na mesma pasta**.

## Requisitos
- Python 3.8 ou superior
- Nenhuma biblioteca externa (usa apenas `json` e `os`)

## Como executar
```bash
git clone https://github.com/Caio9004/oficina-bom-motor.git
cd oficina-bom-motor
python oficina_json.py      # no Windows pode ser: py oficina_json.py
```

Responda `s`/`n` às perguntas sim/não, escolha uma opção nas perguntas categóricas
(fumaça: `nenhuma/preta/branca/azul`; ruído ao frear: `nenhum/agudo`) e digite números
nas perguntas numéricas (idade, quilometragem, km da última revisão).
No final, responda `s` para ver a explicação do raciocínio.

## Executar online (sem instalar nada)
Cole os dois arquivos em um compilador online que aceite múltiplos arquivos
(ex.: Replit, ou Google Colab enviando os arquivos) e rode `oficina_json.py`.
