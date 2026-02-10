# ⚔️ Calculadora Legend of Ymir – Premium Edition

Uma calculadora avançada para o jogo **Legend of Ymir**, desenvolvida em Python com Streamlit.

## 🎮 Funcionalidades

✨ **Cálculos de Câmbio Automáticamente**
- USD → BRL (Real)
- USD → EUR (Euro)
- Cotações em tempo real com fallback seguro

💰 **Análise Completa de Transações**
- Comparação entre WEMIX e DIAMANTES
- Melhor opção para comprar e vender
- Cálculo de taxas de mercado

🎨 **Interface Moderna**
- Design Dark Medieval
- Layout responsivo e centralizado
- Indicadores visuais claros

💝 **Seção de Doação**
- Apoie o desenvolvedor
- Carteira Ethereum/Polygon

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/jofferms/legend-of-ymir-calculator.git
cd legend-of-ymir-calculator
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

### Executando a Aplicação

```bash
streamlit run app_legend_of_ymir.py
```

A aplicação abrirá automaticamente em seu navegador no endereço `http://localhost:8501`

## ⚙️ Configurações

### Na Sidebar

**📊 Taxa do Mercado**
- Ajuste a percentagem de taxa (padrão: 18%)
- Afeta o cálculo do valor líquido

**💱 Cotação de Moedas**
- **USD → BRL**: Atualiza automaticamente
- **USD → EUR**: Atualiza automaticamente
- **WEMIX → USD**: Edite conforme necessário

**💎 Preço de Diamantes**
- Valor de 1000 DIAMANTES em R$ (padrão: R$ 80.00)

## 📊 Como Usar

1. **Informe os Valores**
   - Digite a quantidade de WEMIX ou DIAMANTES que deseja negociar

2. **Veja os Resultados**
   - **Melhor para Vender**: Qual ativo você deve vender para ganhar mais
   - **Melhor para Comprar**: Qual ativo você deve comprar para gastar menos

3. **Compare os Preços**
   - Seção de Comparação mostra todas as 4 opções (WEMIX e DIAMANTE, VENDA e COMPRA)

## 🌐 APIs Utilizadas

- **exchangerate-api.com**: Cotações de câmbio em tempo real
- Cache de 1 hora para otimizar o desempenho

## 📝 Dependências

- `streamlit`: Framework web interativo
- `requests`: Cliente HTTP para requisições

Veja `requirements.txt` para versões completas

## 💝 Apoie o Desenvolvedor

Se esta ferramenta foi útil para você, considere fazer uma doação:

**Carteira Digital (Ethereum/Polygon):**
```
0xec93c5ba7015f3c2720da1437f03cb7be4e5942a
```

## 📄 Licença

Projeto aberto e livre para uso

## 🐛 Reportar Problemas

Encontrou um bug? Abra uma issue no GitHub!

## 📧 Contato

Para dúvidas ou sugestões, utilize a seção de Issues do repositório.

---

**Desenvolvido com ❤️ para a comunidade Legend of Ymir**

⚔️ **2026** - Calculadora Legend of Ymir Premium Edition
