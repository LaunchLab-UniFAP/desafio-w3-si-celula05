# LaunchLab UniFAP - Desenvolvimento ADS
# Código de projeção de focos epidemiológicos

def calcular_projecao_focos(focos_atuais, taxa_reproducao):
    print("--- MONITORAMENTO DE ENDEMIAS UniFAP ---
")
    
    # O conflito intencional:
    # Aluno A implementará uma lógica baseada em crescimento linear.
    # Aluno B implementará uma lógica baseada em crescimento exponencial.
    # A dupla deve resolver o Merge Conflict na mantendo a segurança ética dos dados.
    
    focos_projetados = focos_atuais * taxa_reproducao
    return focos_projetados

if __name__ == "__main__":
    print(f"Total Projetado: {calcular_projecao_focos(10, 1.5)}")
