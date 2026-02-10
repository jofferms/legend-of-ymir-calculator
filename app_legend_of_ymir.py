import streamlit as st

# ---------------- Configuração da Página ----------------
st.set_page_config(
    page_title="Calculadora Legend of Ymir – Premium",
    layout="wide"
)

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
    margin-bottom: 40px;
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

.medieval-arc {
    font-size: 48px;
    color: #f0c75e;
    font-weight: 900;
    text-shadow: 2px 2px 4px #000;
}

.result-values {
    font-size: 28px;
    line-height: 1.8;
    margin-top: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Título ----------------
st.markdown("<h1>🛡️ Calculadora Legend of Ymir – Premium 🛡️</h1>", unsafe_allow_html=True)

# ---------------- Sidebar Configurações ----------------
with st.sidebar:
    st.header("⚙️ Configurações")
    taxa_mercado = st.slider("Taxa do mercado (%)", 0.0, 30.0, 18.0, 0.5)
    st.divider()
    st.subheader("💱 Valores das moedas")
    valor_wemix_usd = st.number_input("1 WEMIX em USD", value=0.32, step=0.01)
    usd_to_brl = st.number_input("USD → BRL", value=5.00, step=0.05)
    usd_to_eur = st.number_input("USD → EUR", value=0.92, step=0.01)
    valor_1000_diamantes_brl = st.number_input("Valor de 1000 DIAMANTES em R$", value=80.0, step=1.0)

# ---------------- 💰 VALOR DO ITEM ----------------
st.markdown('<div class="card"><h2 class="section-title">💰 VALOR DO ITEM</h2></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    qty_wemix = st.number_input("WEMIX", min_value=0.0, step=0.1, key="wemix_qty")
with col2:
    qty_diamante = st.number_input("DIAMANTES", min_value=0.0, step=10.0, key="diamante_qty")

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

# ---------------- 📊 RESULTADO ----------------
st.markdown(
    '''
    <div class="card" style="max-width: 900px; margin: 25px auto; padding: 20px 30px;">
        <h2 class="section-title" style="font-size: 32px; margin-bottom: 20px;">📊 RESULTADO</h2>
    </div>
    ''',
    unsafe_allow_html=True
)

if qty_wemix == 0 and qty_diamante == 0:
    st.info("Preencha a quantidade de WEMIX ou DIAMANTES para ver o resultado.")
else:
    col_esq, col_dir = st.columns([1, 1], gap="medium")

    with col_esq:
        st.markdown(
            f"""
            <div style="text-align: center; background: linear-gradient(145deg, #1a1c23, #101116); 
                        border: 2px solid #00cc88; border-radius: 14px; padding: 18px 16px; 
                        box-shadow: 0 0 15px #00cc8830;">
                <h3 style="color: #00cc88; margin: 0 0 12px 0; font-size: 1.45rem;">
                    💵 Melhor Venda<br>
                    <span style="font-size: 1.1rem;">{melhor_venda_nome}</span>
                </h3>
                <div style="font-size: 1.1rem; line-height: 1.7; color: #e6e6e6;">
                    USD <b>${melhor_venda_usd:,.2f}</b><br>
                    BRL <b>R$ {melhor_venda_brl:,.2f}</b><br>
                    EUR <b>€ {melhor_venda_eur:,.2f}</b><br>
                    <span style="color: #aaa; font-size: 0.9rem;">
                        Líquido ({taxa_mercado:.0f}%): {melhor_venda_liq:,.2f}
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_dir:
        st.markdown(
            f"""
            <div style="text-align: center; background: linear-gradient(145deg, #1a1c23, #101116); 
                        border: 2px solid #ffaa00; border-radius: 14px; padding: 18px 16px; 
                        box-shadow: 0 0 15px #ffaa0030;">
                <h3 style="color: #ffaa00; margin: 0 0 12px 0; font-size: 1.45rem;">
                    🛒 Melhor Compra<br>
                    <span style="font-size: 1.1rem;">{melhor_compra_nome}</span>
                </h3>
                <div style="font-size: 1.1rem; line-height: 1.7; color: #e6e6e6;">
                    USD <b>${melhor_compra_usd:,.2f}</b><br>
                    BRL <b>R$ {melhor_compra_brl:,.2f}</b><br>
                    EUR <b>€ {melhor_compra_eur:,.2f}</b><br>
                    <span style="color: #aaa; font-size: 0.9rem;">
                        Líquido ({taxa_mercado:.0f}%): {melhor_compra_liq:,.2f}
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()
st.caption("Calculadora Legend of Ymir – Premium • 2026")
