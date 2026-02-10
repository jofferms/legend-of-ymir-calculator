import streamlit as st
import requests

# ---------------- Configuração da Página ----------------
st.set_page_config(
    page_title="Calculadora Legend of Ymir – Premium",
    layout="wide"
)

# ---------------- Função para obter cotações automáticas ----------------
@st.cache_data(ttl=3600)
def obter_cotacoes_auto():
    """Busca cotações de câmbio automaticamente com fallback seguro"""
    cotacoes = {"usd_to_brl": 5.00, "usd_to_eur": 0.92, "status": "Padrão"}
    
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=5)
        if response.status_code == 200:
            dados = response.json()
            cotacoes["usd_to_brl"] = round(dados.get("rates", {}).get("BRL", 5.00), 2)
            cotacoes["usd_to_eur"] = round(dados.get("rates", {}).get("EUR", 0.92), 4)
            cotacoes["status"] = "Atualizado ✅"
    except Exception:
        pass  # Silently use defaults on error
    
    return cotacoes

# ---------------- CSS Premium Dark Medieval ----------------
st.markdown("""
<style>
body {
    background-color: #0a0b10;
    color: #e6e6e6;
    font-family: 'Cinzel', 'Roboto', sans-serif;
}

h1 {
    color: #f0c75e;
    font-weight: 900;
    text-align: center;
    font-size: 50px;
    letter-spacing: 2px;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px #000;
}

.card {
    background: linear-gradient(145deg, #1a1c23, #101116);
    border: 3px solid #f0c75e;
    border-radius: 25px;
    padding: 40px;
    margin: 20px auto;
    max-width: 750px;
    text-align: center;
    box-shadow: 0 0 25px #f0c75e50;
}

.donation-box {
    background: linear-gradient(145deg, #4a1a1a, #2a0a0a);
    border: 3px solid #ff6b6b;
    border-radius: 15px;
    padding: 20px;
    margin: 15px auto;
    text-align: center;
    box-shadow: 0 0 20px #ff6b6b40;
}

.donation-title {
    color: #ff6b6b;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 8px;
}

.wallet-address {
    color: #00dd88;
    font-size: 13px;
    font-family: monospace;
    word-break: break-all;
}

.section-title {
    font-size: 32px;
    font-weight: 800;
    color: #f0c75e;
    margin-bottom: 25px;
    text-align: center;  
    text-shadow: 1px 1px 3px #000;
}

.stNumberInput input {
    background-color: #252734;
    color: #ffffff;
    border-radius: 15px;
    font-size: 36px;
    padding: 15px;
    text-align: center;
    width: 220px;
    margin: 0 15px;
}

/* ===== RESULTADO ===== */
[data-testid="column"] {
    display: flex;
    justify-content: center;
}

.result-card {
    width: 100%;
    max-width: 420px;
    background: linear-gradient(145deg, #1a1c23, #101116);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    transition: all 0.25s ease-in-out;
}

.result-card:hover {
    transform: scale(1.02);
}

.result-venda {
    border: 2px solid #00cc88;
    box-shadow: 0 0 18px #00cc8840;
}

.result-compra {
    border: 2px solid #ffaa00;
    box-shadow: 0 0 18px #ffaa0040;
}

.result-card h3 {
    margin-bottom: 12px;
    font-size: 1.6rem;
    font-weight: 800;
}

.result-liq {
    font-size: 0.9rem;
    color: #aaa;
    margin-top: 6px;
}

.comparison-title {
    font-size: 24px;
    font-weight: 700;
    color: #f0c75e;
    text-align: center;
    margin-top: 30px;
    margin-bottom: 20px;
}

.comparison-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    margin: 20px auto;
}

.comparison-card {
    background: linear-gradient(145deg, #1a1c23, #101116);
    border: 2px solid #444;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
}

.comparison-card h4 {
    color: #f0c75e;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Título e Doação ----------------
st.markdown("<h1>⚔️ Calculadora Legend of Ymir – Premium ⚔️</h1>", unsafe_allow_html=True)

# Seção de Doação
st.markdown("""
<div class="donation-box">
    <div class="donation-title">💝 AJUDE O DESENVOLVEDOR</div>
    <div class="wallet-address">0xec93c5ba7015f3c2720da1437f03cb7be4e5942a</div>
</div>
""", unsafe_allow_html=True)

# ---------------- Sidebar Configurações ----------------
with st.sidebar:
    st.header("⚙️ Configurações")
    taxa_mercado = st.slider("Taxa do mercado (%)", 0.0, 30.0, 18.0, 0.5)
    st.divider()
    
    # ===== Cotações Automáticas =====
    st.subheader("💱 Valores das moedas")
    cotacoes = obter_cotacoes_auto()
    
    if cotacoes["status"] == "Atualizado ✅":
        st.success("✅ Cotações atualizadas em tempo real")
    else:
        st.info("ℹ️ Usando valores padrão")
    
    usd_to_brl = st.number_input("1 USD em BRL", value=cotacoes["usd_to_brl"], step=0.05)
    usd_to_eur = st.number_input("1 USD em EUR", value=cotacoes["usd_to_eur"], step=0.01)
    
    st.divider()
    st.subheader("🎮 Valores do Jogo")
    valor_wemix_usd = st.number_input("1 WEMIX em USD", value=0.32, step=0.01)
    valor_1000_diamantes_brl = st.number_input("Valor de 1000 DIAMANTES em R$", value=80.0, step=1.0)

# ---------------- 💰 VALOR DO ITEM ----------------
st.markdown('<div class="card"><h2 class="section-title">💰 VALOR DO ITEM</h2></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    qty_wemix = st.number_input("WEMIX", min_value=0.0, step=0.1, key="qty_wemix")
with col2:
    qty_diamante = st.number_input("DIAMANTES", min_value=0.0, step=10.0, key="qty_diamante")

# ---------------- CÁLCULOS ----------------
fator_liquido = 1 - (taxa_mercado / 100)

wemix_venda_liq = qty_wemix * fator_liquido
wemix_venda_usd = wemix_venda_liq * valor_wemix_usd
wemix_venda_brl = wemix_venda_usd * usd_to_brl
wemix_venda_eur = wemix_venda_usd * usd_to_eur

diamante_venda_liq = qty_diamante * fator_liquido
diamante_venda_brl = (diamante_venda_liq / 1000) * valor_1000_diamantes_brl
diamante_venda_usd = diamante_venda_brl / usd_to_brl
diamante_venda_eur = diamante_venda_usd * usd_to_eur

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

wemix_compra_usd = qty_wemix * valor_wemix_usd
wemix_compra_brl = wemix_compra_usd * usd_to_brl
wemix_compra_eur = wemix_compra_usd * usd_to_eur

diamante_compra_usd = (qty_diamante / 1000) * valor_1000_diamantes_brl / usd_to_brl
diamante_compra_brl = diamante_compra_usd * usd_to_brl
diamante_compra_eur = diamante_compra_usd * usd_to_eur

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

# ---------------- 📊 RESULTADO ----------------
if qty_wemix == 0 and qty_diamante == 0:
    st.info("Preencha a quantidade de WEMIX ou DIAMANTES para ver o resultado.")
else:
    col_esq, col_dir = st.columns(2)

    with col_esq:
        st.markdown(f"""
        <div class="result-card result-venda">
            <h3 style="color:#00cc88;">✅ Melhor Venda<br>{melhor_venda_nome}</h3>
            USD <b>${melhor_venda_usd:,.2f}</b><br>
            BRL <b>R$ {melhor_venda_brl:,.2f}</b><br>
            EUR <b>€ {melhor_venda_eur:,.2f}</b><br>
            <div class="result-liq">Líquido ({taxa_mercado:.0f}%): {melhor_venda_liq:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col_dir:
        st.markdown(f"""
        <div class="result-card result-compra">
            <h3 style="color:#ffaa00;">ℹ️ Melhor Compra<br>{melhor_compra_nome}</h3>
            USD <b>${melhor_compra_usd:,.2f}</b><br>
            BRL <b>R$ {melhor_compra_brl:,.2f}</b><br>
            EUR <b>€ {melhor_compra_eur:,.2f}</b><br>
            <div class="result-liq">Custo ({taxa_mercado:.0f}%): {melhor_compra_liq:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    # ===== COMPARAÇÃO DETALHADA =====
    st.markdown('<p class="comparison-title">📊 COMPARAÇÃO DETALHADA</p>', unsafe_allow_html=True)
    
    comp1, comp2 = st.columns(2)
    
    with comp1:
        st.markdown(f"""
        <div class="comparison-card">
            <h4>💰 WEMIX - Venda</h4>
            ${wemix_venda_usd:,.2f} | R$ {wemix_venda_brl:,.2f}
        </div>
        <div class="comparison-card">
            <h4>💎 DIAMANTE - Venda</h4>
            ${diamante_venda_usd:,.2f} | R$ {diamante_venda_brl:,.2f}
        </div>
        """, unsafe_allow_html=True)
    
    with comp2:
        st.markdown(f"""
        <div class="comparison-card">
            <h4>💰 WEMIX - Compra</h4>
            ${wemix_compra_usd:,.2f} | R$ {wemix_compra_brl:,.2f}
        </div>
        <div class="comparison-card">
            <h4>💎 DIAMANTE - Compra</h4>
            ${diamante_compra_usd:,.2f} | R$ {diamante_compra_brl:,.2f}
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.caption("⚔️ Calculadora Legend of Ymir – Premium • 2026 • Community Edition")

