"""
Sistema Especialista de Triagem de Atendimento — Oficina Mecânica Bom Motor
Disciplina: Programação de Sistemas Especialistas

Versão com if/elif direto + JSON: cada regra de diagnóstico é um bloco de
código explícito (if), e os DADOS (texto das perguntas e informações de cada
diagnóstico: setor, urgência, descrição) ficam no arquivo base_conhecimento.json.
Assim, dá para mudar um texto ou um setor sem mexer no código.
"""

import json
import os

# ============================================================
# BASE DE CONHECIMENTO (dados lidos do arquivo JSON)
# ============================================================

def carregar_base():
    """Lê o arquivo base_conhecimento.json (que fica na mesma pasta deste .py)."""
    pasta = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta, "base_conhecimento.json")
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Erro: arquivo base_conhecimento.json não encontrado.")
        print("Ele precisa estar na mesma pasta que este programa.")
        raise SystemExit(1)
    except json.JSONDecodeError:
        print("Erro: o arquivo base_conhecimento.json está com formato inválido.")
        raise SystemExit(1)


BASE = carregar_base()
PERGUNTAS = BASE["perguntas"]          # dicionário: nome do fato -> texto da pergunta
DIAGNOSTICOS = BASE["diagnosticos"]    # dicionário: número da regra -> dados do diagnóstico


def registrar(lista, id_regra, explicacao):
    """
    Chamada quando uma regra (if) dispara. Busca no JSON os dados daquela
    regra (setor, urgência, diagnóstico) e adiciona na lista de diagnósticos,
    junto com a explicação de quais fatos fizeram a regra disparar.
    """
    dados = DIAGNOSTICOS[str(id_regra)]   # chaves do JSON são sempre texto
    lista.append({
        "id": id_regra,
        "setor": dados["setor"],
        "urgente": dados["urgente"],
        "diagnostico": dados["diagnostico"],
        "explicacao": explicacao,
    })


# ============================================================
# COLETA DE FATOS (perguntas ao cliente)
# ============================================================

def perguntar_sim_nao(pergunta):
    while True:
        resposta = input(f"{pergunta} (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        elif resposta in ("n", "nao", "não"):
            return False
        else:
            print("  Entrada inválida. Responda com 's' para sim ou 'n' para não.")


def perguntar_categorica(pergunta, opcoes):
    while True:
        resposta = input(f"{pergunta} ").strip().lower()
        if resposta in opcoes:
            return resposta
        else:
            print(f"  Entrada inválida. Opções válidas: {opcoes}")


def perguntar_numerica(pergunta):
    while True:
        resposta = input(f"{pergunta} ").strip().replace(",", ".")
        try:
            return float(resposta)
        except ValueError:
            print("  Entrada inválida. Digite um número (ex: 3 ou 45000).")


def coletar_fatos():
    print("\n--- Triagem de atendimento ---")
    print("Responda às perguntas sobre o veículo. Se não sabe, responda 'n' ou 0.\n")

    ruido_motor = perguntar_sim_nao(PERGUNTAS["ruido_motor"])
    perda_potencia = perguntar_sim_nao(PERGUNTAS["perda_potencia"])
    superaquecimento = perguntar_sim_nao(PERGUNTAS["superaquecimento"])
    luz_oleo_acesa = perguntar_sim_nao(PERGUNTAS["luz_oleo_acesa"])
    dificuldade_ligar = perguntar_sim_nao(PERGUNTAS["dificuldade_ligar"])
    motor_engasga = perguntar_sim_nao(PERGUNTAS["motor_engasga"])

    bateria_fraca = perguntar_sim_nao(PERGUNTAS["bateria_fraca"])
    farol_fraco = perguntar_sim_nao(PERGUNTAS["farol_fraco"])
    painel_apaga = perguntar_sim_nao(PERGUNTAS["painel_apaga"])
    luz_bateria_acesa = perguntar_sim_nao(PERGUNTAS["luz_bateria_acesa"])

    pedal_freio_fundo = perguntar_sim_nao(PERGUNTAS["pedal_freio_fundo"])
    carro_puxa_lado = perguntar_sim_nao(PERGUNTAS["carro_puxa_lado"])
    vibracao_ao_frear = perguntar_sim_nao(PERGUNTAS["vibracao_ao_frear"])
    luz_freio_acesa = perguntar_sim_nao(PERGUNTAS["luz_freio_acesa"])

    barulho_em_buracos = perguntar_sim_nao(PERGUNTAS["barulho_em_buracos"])
    carro_balanca_curva = perguntar_sim_nao(PERGUNTAS["carro_balanca_curva"])
    desgaste_irregular_pneu = perguntar_sim_nao(PERGUNTAS["desgaste_irregular_pneu"])
    direcao_pesada = perguntar_sim_nao(PERGUNTAS["direcao_pesada"])

    ar_nao_gela = perguntar_sim_nao(PERGUNTAS["ar_nao_gela"])
    ar_nao_liga = perguntar_sim_nao(PERGUNTAS["ar_nao_liga"])

    vibracao_no_volante = perguntar_sim_nao(PERGUNTAS["vibracao_no_volante"])

    fumaca_escapamento = perguntar_categorica(
        PERGUNTAS["fumaca_escapamento"],
        ["nenhuma", "preta", "branca", "azul"],
    )
    ruido_ao_frear = perguntar_categorica(
        PERGUNTAS["ruido_ao_frear"],
        ["nenhum", "agudo"],
    )

    idade_veiculo = perguntar_numerica(PERGUNTAS["idade_veiculo"])
    quilometragem = perguntar_numerica(PERGUNTAS["quilometragem"])
    ultima_revisao_km = perguntar_numerica(PERGUNTAS["ultima_revisao_km"])

    # Guardamos tudo num dicionário só para facilitar passar para as
    # próximas funções (senão seriam 25 parâmetros soltos)
    return {
        "ruido_motor": ruido_motor,
        "perda_potencia": perda_potencia,
        "superaquecimento": superaquecimento,
        "luz_oleo_acesa": luz_oleo_acesa,
        "dificuldade_ligar": dificuldade_ligar,
        "motor_engasga": motor_engasga,
        "bateria_fraca": bateria_fraca,
        "farol_fraco": farol_fraco,
        "painel_apaga": painel_apaga,
        "luz_bateria_acesa": luz_bateria_acesa,
        "pedal_freio_fundo": pedal_freio_fundo,
        "carro_puxa_lado": carro_puxa_lado,
        "vibracao_ao_frear": vibracao_ao_frear,
        "luz_freio_acesa": luz_freio_acesa,
        "barulho_em_buracos": barulho_em_buracos,
        "carro_balanca_curva": carro_balanca_curva,
        "desgaste_irregular_pneu": desgaste_irregular_pneu,
        "direcao_pesada": direcao_pesada,
        "ar_nao_gela": ar_nao_gela,
        "ar_nao_liga": ar_nao_liga,
        "vibracao_no_volante": vibracao_no_volante,
        "fumaca_escapamento": fumaca_escapamento,
        "ruido_ao_frear": ruido_ao_frear,
        "idade_veiculo": idade_veiculo,
        "quilometragem": quilometragem,
        "ultima_revisao_km": ultima_revisao_km,
    }


# ============================================================
# MOTOR DE INFERÊNCIA — cada regra é um if/elif explícito
# ============================================================

def executar_inferencia(fatos):
    """
    Testa cada regra, uma por uma, com if comum. Cada regra que "bate"
    gera um diagnóstico, que é guardado numa lista junto com a explicação
    de por que ela disparou (quais fatos foram usados).
    """
    diagnosticos = []

    # --- Regras de Motor ---

    if fatos["fumaca_escapamento"] == "preta" and fatos["perda_potencia"] == True:
        registrar(diagnosticos, 1, "fumaça do escapamento é preta E há perda de potência")

    if fatos["fumaca_escapamento"] == "branca" and fatos["superaquecimento"] == True:
        registrar(diagnosticos, 2, "fumaça do escapamento é branca E o motor está superaquecendo")

    if fatos["fumaca_escapamento"] == "azul":
        registrar(diagnosticos, 3, "fumaça do escapamento é azul")

    if fatos["luz_oleo_acesa"] == True and fatos["ruido_motor"] == True:
        registrar(diagnosticos, 4, "luz de óleo acesa E ruído no motor")

    if fatos["dificuldade_ligar"] == True and fatos["bateria_fraca"] == False:
        registrar(diagnosticos, 5, "dificuldade para ligar E bateria não está fraca")

    if (fatos["motor_engasga"] == True
            and fatos["quilometragem"] > 60000
            and fatos["ultima_revisao_km"] > 10000):
        registrar(diagnosticos, 6, "motor engasga E quilometragem > 60.000 E última revisão há mais de 10.000 km")

    if fatos["superaquecimento"] == True and fatos["fumaca_escapamento"] == "nenhuma":
        registrar(diagnosticos, 7, "motor superaquecendo E sem fumaça no escapamento")

    # --- Regras de Elétrica ---

    if fatos["dificuldade_ligar"] == True and fatos["farol_fraco"] == True:
        registrar(diagnosticos, 8, "dificuldade para ligar E faróis fracos")

    if fatos["painel_apaga"] == True and fatos["farol_fraco"] == True:
        registrar(diagnosticos, 9, "painel apaga E faróis fracos")

    if fatos["luz_bateria_acesa"] == True:
        registrar(diagnosticos, 10, "luz de bateria acesa")

    if fatos["bateria_fraca"] == True and fatos["idade_veiculo"] > 3:
        registrar(diagnosticos, 11, "bateria fraca E veículo com mais de 3 anos")

    if (fatos["dificuldade_ligar"] == True
            and fatos["bateria_fraca"] == True
            and fatos["farol_fraco"] == False):
        registrar(diagnosticos, 12, "dificuldade para ligar E bateria fraca E faróis normais")

    # --- Regras de Freios ---

    if fatos["ruido_ao_frear"] == "agudo":
        registrar(diagnosticos, 13, "ruído agudo ao frear")

    if fatos["pedal_freio_fundo"] == True:
        registrar(diagnosticos, 14, "pedal do freio fundo")

    if fatos["carro_puxa_lado"] == True and fatos["vibracao_ao_frear"] == True:
        registrar(diagnosticos, 15, "carro puxa para o lado E vibra ao frear")

    if fatos["luz_freio_acesa"] == True:
        registrar(diagnosticos, 16, "luz de freio acesa")

    if fatos["ruido_ao_frear"] == "agudo" and fatos["vibracao_ao_frear"] == False:
        registrar(diagnosticos, 17, "ruído agudo ao frear E sem vibração ao frear")

    # --- Regras de Suspensão ---

    if fatos["barulho_em_buracos"] == True:
        registrar(diagnosticos, 18, "barulho ao passar em buracos")

    if fatos["carro_balanca_curva"] == True:
        registrar(diagnosticos, 19, "carro balança nas curvas")

    if fatos["desgaste_irregular_pneu"] == True and fatos["carro_puxa_lado"] == False:
        registrar(diagnosticos, 20, "desgaste irregular do pneu E carro não puxa para o lado")

    if fatos["direcao_pesada"] == True:
        registrar(diagnosticos, 21, "direção pesada")

    # --- Regras de Alinhamento ---

    if fatos["carro_puxa_lado"] == True and fatos["vibracao_no_volante"] == True:
        registrar(diagnosticos, 22, "carro puxa para o lado E volante vibra na estrada")

    if fatos["desgaste_irregular_pneu"] == True and fatos["carro_puxa_lado"] == True:
        registrar(diagnosticos, 23, "desgaste irregular do pneu E carro puxa para o lado")

    # --- Regra de Ar-condicionado ---

    if fatos["ar_nao_gela"] == True and fatos["ar_nao_liga"] == False:
        registrar(diagnosticos, 24, "ar não gela E o ar liga normalmente")

    return diagnosticos


# ============================================================
# EXPLICAÇÃO DO RACIOCÍNIO (por que / como)
# ============================================================

def explicar(diagnosticos):
    if len(diagnosticos) == 0:
        return ["Não foi possível concluir nenhum diagnóstico com as informações fornecidas."]

    explicacoes = []
    for d in diagnosticos:
        tag = ""
        if d["urgente"] == True:
            tag = " [URGENTE]"

        texto = (
            f"Regra #{d['id']} disparou porque: {d['explicacao']}.\n"
            f"  → Diagnóstico: {d['diagnostico']}\n"
            f"  → Setor recomendado: {d['setor']}{tag}"
        )
        explicacoes.append(texto)

    return explicacoes


# ============================================================
# APRESENTAÇÃO DO RESULTADO
# ============================================================

def exibir_resultado(diagnosticos):
    print("\n=== Resultado da triagem ===")

    if len(diagnosticos) == 0:
        print("Não foi possível concluir um diagnóstico com as informações fornecidas.")
        print("Recomendamos agendar uma avaliação presencial com um mecânico.")
        return

    tem_urgente = False
    for d in diagnosticos:
        if d["urgente"] == True:
            tem_urgente = True

    if tem_urgente == True:
        print("⚠ ATENÇÃO: foram identificados itens urgentes!\n")

    for d in diagnosticos:
        tag = ""
        if d["urgente"] == True:
            tag = " [URGENTE]"
        print(f"- Setor: {d['setor']}{tag}")
        print(f"  Diagnóstico: {d['diagnostico']}\n")

    resposta = input("Deseja ver a explicação do raciocínio (por que/como)? (s/n): ").strip().lower()
    if resposta == "s" or resposta == "sim":
        print("\n--- Explicação do raciocínio ---")
        lista_explicacoes = explicar(diagnosticos)
        for explicacao in lista_explicacoes:
            print(explicacao, "\n")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    print("=" * 60)
    print("SISTEMA ESPECIALISTA — OFICINA MECÂNICA BOM MOTOR")
    print("Triagem inicial de atendimento ao cliente")
    print("=" * 60)

    try:
        fatos = coletar_fatos()
    except (KeyboardInterrupt, EOFError):
        print("\nAtendimento interrompido pelo usuário.")
        return

    diagnosticos = executar_inferencia(fatos)
    exibir_resultado(diagnosticos)

    print("\nObrigado por usar o sistema de triagem da Oficina Bom Motor!")


if __name__ == "__main__":
    main()
