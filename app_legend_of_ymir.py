import streamlit as st
import requests
from datetime import datetime, timedelta

# ===== FUNÇÃO PARA BUSCAR COTAÇÕES AUTOMÁTICAS =====
@st.cache_data(ttl=3600)  # Cache de 1 hora
def obter_cotacoes_auto():
    """Busca cotações de câmbio automaticamente com fallback seguro"""
    cotacoes = {
        "usd_to_brl": 5.00,
        "usd_to_eur": 0.92,
        "status": "Padrão"
    }
    
    try:
        # Tenta buscar de uma API gratuita
        response = requests.get(
            "https://api.exchangerate-api.com/v4/latest/USD",
            timeout=5
        )
        if response.status_code == 200:
            dados = response.json()
            cotacoes["usd_to_brl"] = round(dados.get("rates", {}).get("BRL", 5.00), 2)
            cotacoes["usd_to_eur"] = round(dados.get("rates", {}).get("EUR", 0.92), 4)
            cotacoes["status"] = "Atualizado"
            return cotacoes
    except Exception as e:
        # Silenciosamente usa valores padrão
        pass
    
    return cotacoes

# ---------------- Configuração da Página ----------------
st.set_page_config(
    page_title="Calculadora Legend of Ymir – Premium",
    layout="wide"
)

# ---------------- CSS Premium Dark Medieval ----------------
st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: linear-gradient(135deg, #0a0b10 0%, #1a1a2e 100%);
    color: #e6e6e6;
    font-family: 'Segoe UI', 'Roboto', sans-serif;
}

h1 {
    color: #f0c75e;
    font-weight: 900;
    text-align: center;
    font-size: 55px;
    letter-spacing: 3px;
    margin-bottom: 10px;
    text-shadow: 0 0 20px #f0c75e80, 2px 2px 8px #000;
    animation: glow 2s ease-in-out infinite;
}

@keyframes glow {
    0%, 100% { text-shadow: 0 0 20px #f0c75e80, 2px 2px 8px #000; }
    50% { text-shadow: 0 0 30px #f0c75e, 2px 2px 8px #000; }
}

.card {
    background: linear-gradient(145deg, #1a1c25, #0f1118);
    border: 2px solid #f0c75e;
    border-radius: 20px;
    padding: 35px;
    margin: 20px auto;
    max-width: 800px;
    text-align: center;
    box-shadow: 0 0 30px #f0c75e40, inset 0 0 20px #f0c75e10;
    backdrop-filter: blur(10px);
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #f0c75e;
    margin-bottom: 20px;
    text-align: center;
    text-shadow: 0 0 15px #f0c75e60;
    letter-spacing: 1px;
}

.input-row {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin: 25px 0;
    flex-wrap: wrap;
}

.input-group {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

.input-label {
    font-size: 16px;
    font-weight: 600;
    color: #f0c75e;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stNumberInput input {
    background: linear-gradient(145deg, #2a2d35, #1f2228) !important;
    color: #ffffff !important;
    border: 2px solid #f0c75e40 !important;
    border-radius: 12px !important;
    font-size: 24px !important;
    padding: 12px 15px !important;
    text-align: center !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.stNumberInput input:focus {
    border-color: #f0c75e !important;
    box-shadow: 0 0 15px #f0c75e40 !important;
}

.result-card {
    background: linear-gradient(145deg, #1a1c25, #0f1118);
    border: 2px solid #444;
    border-radius: 16px;
    padding: 25px;
    text-align: center;
    transition: all 0.3s ease;
}

.result-card:hover {
    transform: translateY(-5px);
    border-color: #f0c75e;
    box-shadow: 0 10px 30px #f0c75e30;
}

.result-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 15px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.result-value {
    font-size: 24px;
    font-weight: 700;
    line-height: 1.8;
    margin: 8px 0;
}

.currency-row {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin: 12px 0;
    flex-wrap: wrap;
}

.currency-item {
    background: rgba(240, 199, 94, 0.05);
    border: 1px solid rgba(240, 199, 94, 0.3);
    border-radius: 10px;
    padding: 12px 20px;
    min-width: 150px;
}

.currency-label {
    font-size: 12px;
    color: #999;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 5px;
}

.currency-value {
    font-size: 18px;
    font-weight: 700;
    color: #f0c75e;
}

.sell-card {
    border-color: #00dd88 !important;
    box-shadow: 0 0 20px #00dd8830 !important;
}

.sell-card .result-title {
    color: #00dd88;
}

.buy-card {
    border-color: #ff9900 !important;
    box-shadow: 0 0 20px #ff990030 !important;
}

.buy-card .result-title {
    color: #ff9900;
}

.indicator {
    display: inline-block;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    margin-right: 8px;
    vertical-align: middle;
}

.sell-indicator {
    background-color: #00dd88;
}

.buy-indicator {
    background-color: #ff9900;
}

.comparison-text {
    font-size: 14px;
    color: #999;
    margin-top: 10px;
    font-style: italic;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #f0c75e40, transparent);
    margin: 20px 0;
}

.footer {
    text-align: center;
    color: #666;
    font-size: 12px;
    margin-top: 30px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Título ----------------
st.markdown("<h1>⚔️ CALCULADORA LEGEND OF YMIR ⚔️</h1>", unsafe_allow_html=True)

# Seção de Doação
with st.container():
    col1, col_center, col2 = st.columns([0.5, 2, 0.5])
    with col_center:
        st.markdown('<p style="text-align: center; color: #ff6b6b; font-size: 18px; font-weight: 900; text-transform: uppercase;">💝 AJUDE O DESENVOLVEDOR</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; color: #fff; font-size: 12px;">Muitas horas de trabalho nesta ferramenta!</p>', unsafe_allow_html=True)
        
        # Carteira
        with st.container():
            st.markdown('<div style="background: rgba(255, 107, 107, 0.15); border: 2px solid #ff6b6b; border-radius: 12px; padding: 18px; margin: 15px 0; text-align: center;"><p style="color: #999; font-size: 10px; text-transform: uppercase; margin: 0 0 10px 0;">Carteira Digital - Ethereum/Polygon</p><p style="color: #00dd88; font-size: 13px; font-weight: 900; margin: 0; word-break: break-all; font-family: monospace;">0xec93c5ba7015f3c2720da1437f03cb7be4e5942a</p></div>', unsafe_allow_html=True)
        
        st.markdown('<p style="text-align: center; color: #ccc; font-size: 11px;">✨ Obrigado! ✨</p>', unsafe_allow_html=True)

# ---------------- Sidebar Configurações ----------------
with st.sidebar:
    st.markdown("<div style='text-align: center; margin-bottom: 20px;'><span style='color: #f0c75e; font-size: 24px; font-weight: 700;'>⚙️</span></div>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #f0c75e; text-align: center; font-size: 18px; letter-spacing: 1px;'>CONFIGURAÇÕES</h2>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<div style='color: #f0c75e; font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;'>📊 Taxa do Mercado</div>", unsafe_allow_html=True)
    taxa_mercado = st.slider("Taxa (%)", 0.0, 30.0, 18.0, 0.5, label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("<div style='color: #f0c75e; font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;'>💱 Cotação de Moedas</div>", unsafe_allow_html=True)
    
    # Buscar cotações automaticamente
    cotacoes = obter_cotacoes_auto()
    
    # Mostrar status
    if cotacoes["status"] == "Atualizado":
        st.success("✅ Cotações atualizadas automaticamente")
    else:
        st.info("ℹ️ Usando valores padrão")
    
    # Inputs com valores automáticos
    valor_wemix_usd = st.number_input("1 WEMIX em USD", value=0.32, step=0.01, format="%.4f")
    usd_to_brl = st.number_input("1 USD em BRL", value=cotacoes["usd_to_brl"], step=0.05, format="%.2f")
    usd_to_eur = st.number_input("1 USD em EUR", value=cotacoes["usd_to_eur"], step=0.01, format="%.4f")
    
    st.markdown("---")
    st.markdown("<div style='color: #f0c75e; font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;'>💎 Preço Diamantes</div>", unsafe_allow_html=True)
    valor_1000_diamantes_brl = st.number_input("1000 DIAMANTES em R$", value=80.0, step=1.0, format="%.2f")

# ---------------- 💰 VALOR DO ITEM ----------------
st.markdown('<h2 style="text-align: center; color: #f0c75e; margin: 40px 0 30px 0;">💰 INFORME OS VALORES</h2>', unsafe_allow_html=True)

# Centralizar inputs em 2 colunas no meio
_, col_center, _ = st.columns([1, 2, 1])

with col_center:
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("<div style='text-align: center; color: #f0c75e; font-size: 14px; font-weight: 700; margin-bottom: 10px;'>⚔️ WEMIX</div>", unsafe_allow_html=True)
        qty_wemix = st.number_input("", min_value=0.0, step=0.1, key="wemix_qty", label_visibility="collapsed")
    
    with col2:
        st.markdown("<div style='text-align: center; color: #f0c75e; font-size: 14px; font-weight: 700; margin-bottom: 10px;'>💎 DIAMANTES</div>", unsafe_allow_html=True)
        qty_diamante = st.number_input("", min_value=0.0, step=10.0, key="diamante_qty", label_visibility="collapsed")

# ---------------- CÁLCULOS ----------------
fator_liquido = 1 - (taxa_mercado / 100)

# === VENDA ===
# WEMIX
wemix_venda_liq = qty_wemix * fator_liquido
wemix_venda_usd = wemix_venda_liq * valor_wemix_usd
wemix_venda_brl = wemix_venda_usd * usd_to_brl
wemix_venda_eur = wemix_venda_usd * usd_to_eur

# DIAMANTES
diamante_venda_liq = qty_diamante * fator_liquido
diamante_venda_brl = (diamante_venda_liq / 1000) * valor_1000_diamantes_brl
diamante_venda_usd = diamante_venda_brl / usd_to_brl
diamante_venda_eur = diamante_venda_usd * usd_to_eur

# Melhor venda
if wemix_venda_usd >= diamante_venda_usd:
    melhor_venda_nome = "WEMIX"
    melhor_venda_usd = wemix_venda_usd
    melhor_venda_brl = wemix_venda_brl
    melhor_venda_eur = wemix_venda_eur
    melhor_venda_liq = wemix_venda_liq
else:
    melhor_venda_nome = "DIAMANTE"
    melhor_venda_usd = diamante_venda_usd
    melhor_venda_brl = diamante_venda_brl
    melhor_venda_eur = diamante_venda_eur
    melhor_venda_liq = diamante_venda_liq

# === COMPRA ===
# WEMIX
wemix_compra_usd = qty_wemix * valor_wemix_usd
wemix_compra_brl = wemix_compra_usd * usd_to_brl
wemix_compra_eur = wemix_compra_usd * usd_to_eur

# DIAMANTES
diamante_compra_usd = (qty_diamante / 1000) * valor_1000_diamantes_brl / usd_to_brl
diamante_compra_brl = diamante_compra_usd * usd_to_brl
diamante_compra_eur = diamante_compra_usd * usd_to_eur

# Melhor compra (menor custo = melhor)
if wemix_compra_usd <= diamante_compra_usd:
    melhor_compra_nome = "WEMIX"
    melhor_compra_usd = wemix_compra_usd
    melhor_compra_brl = wemix_compra_brl
    melhor_compra_eur = wemix_compra_eur
    melhor_compra_liq = wemix_compra_usd * fator_liquido
else:
    melhor_compra_nome = "DIAMANTE"
    melhor_compra_usd = diamante_compra_usd
    melhor_compra_brl = diamante_compra_brl
    melhor_compra_eur = diamante_compra_eur
    melhor_compra_liq = diamante_compra_usd * fator_liquido

# -------- 📊 RESULTADO --------
st.markdown('<h2 style="text-align: center; color: #f0c75e; margin: 50px 0 30px 0;">📊 RESULTADO FINAL</h2>', unsafe_allow_html=True)

if qty_wemix == 0 and qty_diamante == 0:
    st.warning("⚠️ Informe os valores de WEMIX ou DIAMANTES para ver os resultados!")
else:
    # Determinhar qual é o melhor
    venda_melhor = "🟢 VENDA" if melhor_venda_nome == "WEMIX" else "🔵 VENDA"
    compra_melhor = "🟢 COMPRA" if melhor_compra_nome == "WEMIX" else "🔵 COMPRA"
    
    # ===== MELHOR VENDA =====
    st.markdown(f'<h3 style="text-align: center; color: #00dd88; font-size: 28px; margin: 30px 0 10px 0;">💰 MELHOR PARA VENDER: {melhor_venda_nome}</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #999; font-size: 13px;">Escolha este para ganhar mais</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💵 USD", f"${melhor_venda_usd:,.2f}")
    with col2:
        st.metric("🇧🇷 BRL", f"R$ {melhor_venda_brl:,.2f}")
    with col3:
        st.metric("🇪🇺 EUR", f"€ {melhor_venda_eur:,.2f}")
    
    # Valor líquido destaque
    st.markdown(f'<div style="background: linear-gradient(90deg, rgba(0, 221, 136, 0.3), rgba(0, 221, 136, 0.1)); padding: 25px; border-radius: 12px; border-left: 5px solid #00dd88; margin: 20px auto; max-width: 600px;"><p style="color: #999; font-size: 12px; text-transform: uppercase; margin: 0 0 10px 0;">📌 Valor Que Você Recebe (após {taxa_mercado:.0f}% taxa)</p><p style="color: #00dd88; font-size: 32px; font-weight: 900; margin: 0; text-align: center;">+ {melhor_venda_liq:,.2f} {melhor_venda_nome}</p></div>', unsafe_allow_html=True)
    
    # ===== MELHOR COMPRA =====
    st.markdown(f'<h3 style="text-align: center; color: #ff9900; font-size: 28px; margin: 40px 0 10px 0;">🛍️ MELHOR PARA COMPRAR: {melhor_compra_nome}</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #999; font-size: 13px;">Escolha este para gastar menos</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💵 USD", f"${melhor_compra_usd:,.2f}")
    with col2:
        st.metric("🇧🇷 BRL", f"R$ {melhor_compra_brl:,.2f}")
    with col3:
        st.metric("🇪🇺 EUR", f"€ {melhor_compra_eur:,.2f}")
    
    # Valor líquido destaque
    st.markdown(f'<div style="background: linear-gradient(90deg, rgba(255, 153, 0, 0.3), rgba(255, 153, 0, 0.1)); padding: 25px; border-radius: 12px; border-left: 5px solid #ff9900; margin: 20px auto; max-width: 600px;"><p style="color: #999; font-size: 12px; text-transform: uppercase; margin: 0 0 10px 0;">📌 Valor Que Você Paga (após {taxa_mercado:.0f}% taxa)</p><p style="color: #ff9900; font-size: 32px; font-weight: 900; margin: 0; text-align: center;">- {melhor_compra_liq:,.2f} {melhor_compra_nome}</p></div>', unsafe_allow_html=True)
    
    # ===== COMPARAÇÃO CLARA =====
    st.markdown('<div style="margin: 50px 0;"></div>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; color: #f0c75e; font-size: 22px; margin: 30px 0;">📊 COMPARAÇÃO ENTRE OPÇÕES</h3>', unsafe_allow_html=True)
    
    # VENDA
    st.markdown('<p style="text-align: center; color: #f0c75e; font-weight: bold; margin: 20px 0 15px 0;">💵 VENDENDO</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        indicador = "✅ MELHOR" if melhor_venda_nome == "WEMIX" else "ℹ️ ALTERNATIVA"
        cor = "#00dd88" if melhor_venda_nome == "WEMIX" else "#666"
        st.markdown(f'<div style="background: rgba(0, 221, 136, 0.1); border: 2px solid {cor}; padding: 20px; border-radius: 10px; text-align: center;"><p style="color: {cor}; font-weight: bold; margin: 0 0 10px 0;">{indicador}</p><p style="color: #f0c75e; font-size: 24px; font-weight: 900; margin: 0 0 5px 0;">⚔️ WEMIX</p><p style="color: #fff; font-size: 18px; font-weight: 700; margin: 0;">${wemix_venda_usd:,.2f}</p><p style="color: #999; font-size: 12px; margin: 5px 0 0 0;">R$ {wemix_venda_brl:,.2f}</p></div>', unsafe_allow_html=True)
    
    with col2:
        indicador = "✅ MELHOR" if melhor_venda_nome == "DIAMANTE" else "ℹ️ ALTERNATIVA"
        cor = "#00dd88" if melhor_venda_nome == "DIAMANTE" else "#666"
        st.markdown(f'<div style="background: rgba(0, 221, 136, 0.1); border: 2px solid {cor}; padding: 20px; border-radius: 10px; text-align: center;"><p style="color: {cor}; font-weight: bold; margin: 0 0 10px 0;">{indicador}</p><p style="color: #f0c75e; font-size: 24px; font-weight: 900; margin: 0 0 5px 0;">💎 DIAMANTE</p><p style="color: #fff; font-size: 18px; font-weight: 700; margin: 0;">${diamante_venda_usd:,.2f}</p><p style="color: #999; font-size: 12px; margin: 5px 0 0 0;">R$ {diamante_venda_brl:,.2f}</p></div>', unsafe_allow_html=True)
    
    # COMPRA
    st.markdown('<p style="text-align: center; color: #f0c75e; font-weight: bold; margin: 20px 0 15px 0;">🛒 COMPRANDO</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        indicador = "✅ MELHOR" if melhor_compra_nome == "WEMIX" else "ℹ️ ALTERNATIVA"
        cor = "#ff9900" if melhor_compra_nome == "WEMIX" else "#666"
        st.markdown(f'<div style="background: rgba(255, 153, 0, 0.1); border: 2px solid {cor}; padding: 20px; border-radius: 10px; text-align: center;"><p style="color: {cor}; font-weight: bold; margin: 0 0 10px 0;">{indicador}</p><p style="color: #f0c75e; font-size: 24px; font-weight: 900; margin: 0 0 5px 0;">⚔️ WEMIX</p><p style="color: #fff; font-size: 18px; font-weight: 700; margin: 0;">${wemix_compra_usd:,.2f}</p><p style="color: #999; font-size: 12px; margin: 5px 0 0 0;">R$ {wemix_compra_brl:,.2f}</p></div>', unsafe_allow_html=True)
    
    with col2:
        indicador = "✅ MELHOR" if melhor_compra_nome == "DIAMANTE" else "ℹ️ ALTERNATIVA"
        cor = "#ff9900" if melhor_compra_nome == "DIAMANTE" else "#666"
        st.markdown(f'<div style="background: rgba(255, 153, 0, 0.1); border: 2px solid {cor}; padding: 20px; border-radius: 10px; text-align: center;"><p style="color: {cor}; font-weight: bold; margin: 0 0 10px 0;">{indicador}</p><p style="color: #f0c75e; font-size: 24px; font-weight: 900; margin: 0 0 5px 0;">💎 DIAMANTE</p><p style="color: #fff; font-size: 18px; font-weight: 700; margin: 0;">${diamante_compra_usd:,.2f}</p><p style="color: #999; font-size: 12px; margin: 5px 0 0 0;">R$ {diamante_compra_brl:,.2f}</p></div>', unsafe_allow_html=True)

st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>⚔️ Calculadora Legend of Ymir – Premium Edition • 2026 ⚔️</div>", unsafe_allow_html=True)
