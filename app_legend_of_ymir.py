import streamlit as st

st.set_page_config(page_title="Legend of Ymir PRO Calculator", layout="wide")

st.markdown("<h1 style='text-align: center; color: #4B7BE5;'>Legend of Ymir – Market Calculator PRO</h1>", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.header("💼 Configurações")

# Valores das moedas
wemix_usd = st.sidebar.number_input("WEMIX (USD)", value=0.32, step=0.01, format="%.2f")
diam_usd = st.sidebar.number_input("1000 DIAMANTES (USD)", value=15.37, step=0.01, format="%.2f")

# Taxa e câmbio
tax = st.sidebar.slider("Taxa do Mercado (%)", 0, 50, 18)
usd_brl = st.sidebar.number_input("USD → BRL", value=5.00, step=0.01, format="%.2f")
usd_eur = st.sidebar.number_input("USD → EUR", value=0.92, step=0.01, format="%.2f")

# Entrada do item
st.sidebar.header("📦 Entrada do Item")
w_price = st.sidebar.number_input("Preço em WEMIX", min_value=0.0, value=0.0, step=1.0)
d_price = st.sidebar.number_input("Preço em DIAMANTES", min_value=0.0, value=0.0, step=1.0)

# ================= CÁLCULOS =================
wemix_liquido = w_price * (1 - tax / 100)
diamante_liquido = d_price * (1 - tax / 100)

net_w_usd = wemix_liquido * wemix_usd
net_d_usd = (diamante_liquido / 1000) * diam_usd

# ================= RESULTADOS =================
st.subheader("💰 Valor líquido após taxa (USD)")
c1, c2 = st.columns(2)
with c1:
    st.info(f"WEMIX → ${net_w_usd:,.2f}")
with c2:
    st.info(f"DIAMANTE → ${net_d_usd:,.2f}")

# Decisão baseada no valor líquido das moedas
if net_w_usd > net_d_usd:
    best = "VENDER EM WEMIX"
    wrong = "VENDER EM DIAMANTE"
    best_usd = net_w_usd
    wrong_usd = net_d_usd
elif net_d_usd > net_w_usd:
    best = "VENDER EM DIAMANTE"
    wrong = "VENDER EM WEMIX"
    best_usd = net_d_usd
    wrong_usd = net_w_usd
else:
    best = "VALORES IGUAIS"
    wrong = "—"
    best_usd = net_w_usd
    wrong_usd = net_d_usd

advantage_pct = ((best_usd - wrong_usd) / wrong_usd * 100) if wrong_usd > 0 else 0

# ================= RESULTADOS VISUAIS =================
col3, col4 = st.columns(2)

# Melhor opção
with col3:
    st.markdown(f"<h3 style='color: green;'>✔ Melhor opção: {best}</h3>", unsafe_allow_html=True)
    if best == "VENDER EM WEMIX":
        st.metric("Recebimento líquido", f"{wemix_liquido:,.2f} WEMIX")
    elif best == "VENDER EM DIAMANTE":
        st.metric("Recebimento líquido", f"{diamante_liquido:,.0f} DIAMANTES")
    st.metric("USD", f"${best_usd:,.2f}")
    st.metric("BRL", f"R$ {best_usd * usd_brl:,.2f}")
    st.metric("EUR", f"€ {best_usd * usd_eur:,.2f}")

# Pior opção
with col4:
    st.markdown(f"<h3 style='color: red;'>✖ Opção pior: {wrong}</h3>", unsafe_allow_html=True)
    if wrong == "VENDER EM WEMIX":
        st.metric("Recebimento líquido", f"{wemix_liquido:,.2f} WEMIX")
    elif wrong == "VENDER EM DIAMANTE":
        st.metric("Recebimento líquido", f"{diamante_liquido:,.0f} DIAMANTES")
    st.metric("USD", f"${wrong_usd:,.2f}")
    st.metric("BRL", f"R$ {wrong_usd * usd_brl:,.2f}")
    st.metric("EUR", f"€ {wrong_usd * usd_eur:,.2f}")

# Percentual de vantagem
st.divider()
st.markdown(f"<h3 style='text-align: center; color: #4B7BE5;'>📊 Vantagem da melhor escolha: {advantage_pct:.2f}%</h3>", unsafe_allow_html=True)
