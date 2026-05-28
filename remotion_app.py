import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="ReMotion",
    page_icon="💙",
    layout="wide"
)

def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

exo_b64   = img_to_base64("exoesqueleto.png")
team_b64  = img_to_base64("team_photo.png")

exo_tag  = f'<img src="data:image/png;base64,{exo_b64}"  style="width:100%;border-radius:14px;background:#e8edf2;"/>' if exo_b64  else ""
team_tag = f'<img src="data:image/png;base64,{team_b64}" style="width:100%;border-radius:14px;"/>'                      if team_b64 else ""

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family:'Inter',sans-serif; background:#05111c; color:#e8f0f8; }
.stApp { background:#05111c; }

/* HERO */
.hero {
    padding:5rem 3rem 4rem; border-radius:28px;
    background:linear-gradient(135deg,#0b2d4e 0%,#0d3d6e 50%,#0a4f8f 100%);
    text-align:center; margin-bottom:2.5rem;
    border:1px solid rgba(100,180,255,0.15);
}
.hero-tag {
    display:inline-block; background:rgba(30,120,255,0.2);
    border:1px solid rgba(100,180,255,0.3); color:#7ecfff;
    font-family:'Sora',sans-serif; font-size:0.75rem; font-weight:600;
    letter-spacing:0.15em; text-transform:uppercase;
    padding:0.35rem 1rem; border-radius:100px; margin-bottom:1.5rem;
}
.hero h1 { font-family:'Sora',sans-serif; font-size:4.5rem; font-weight:800; color:#fff; letter-spacing:-0.02em; margin:0 0 0.5rem; }
.hero h1 span { color:#4db8ff; }
.hero-sub  { font-family:'Sora',sans-serif; font-size:1.2rem; color:#a8d4ff; font-weight:300; }
.hero-desc { max-width:620px; margin:1.5rem auto 0; font-size:1rem; color:#c0d8f0; line-height:1.7; }

/* STATS */
.stats-bar { display:flex; gap:1.5rem; margin-bottom:2.5rem; }
.stat-card {
    flex:1; background:linear-gradient(135deg,rgba(13,61,110,0.6),rgba(10,40,80,0.8));
    border:1px solid rgba(100,180,255,0.12); border-radius:18px; padding:1.8rem 1.5rem; text-align:center;
}
.stat-number { font-family:'Sora',sans-serif; font-size:2.6rem; font-weight:800; color:#4db8ff; line-height:1; margin-bottom:0.5rem; }
.stat-label  { font-size:0.9rem; color:#a0c4e8; line-height:1.4; }
.stat-source { font-size:0.72rem; color:#5a8ab0; margin-top:0.4rem; }

/* SECTION WRAPPER */
.section {
    padding:2.5rem; border-radius:22px;
    background:rgba(13,40,70,0.4); border:1px solid rgba(100,180,255,0.08);
    margin-bottom:2rem;
}
.section-title { font-family:'Sora',sans-serif; font-size:1.6rem; font-weight:700; color:#7ecfff; margin-bottom:1.2rem; }
.section p { font-size:1rem; color:#c0d8f0; line-height:1.8; margin-bottom:1rem; }

/* FEATURE GRID */
.feature-grid { display:flex; gap:1.2rem; margin-top:1rem; }
.feature-card {
    flex:1; background:rgba(10,50,90,0.5); border:1px solid rgba(100,180,255,0.12);
    border-radius:16px; padding:1.6rem;
}
.feature-icon { font-size:1.8rem; margin-bottom:0.8rem; }
.feature-card h4 { font-family:'Sora',sans-serif; font-size:1rem; font-weight:700; color:#fff; margin-bottom:0.5rem; }
.feature-card p  { font-size:0.88rem; color:#a0c0e0; line-height:1.6; margin:0; }

/* COMPARISON TABLE */
.comp-table { width:100%; border-collapse:collapse; margin-top:1rem; font-size:0.9rem; }
.comp-table th { background:rgba(30,100,200,0.3); color:#7ecfff; font-family:'Sora',sans-serif; font-weight:600; padding:1rem 1.2rem; text-align:left; border-bottom:2px solid rgba(100,180,255,0.2); }
.comp-table td { padding:0.9rem 1.2rem; border-bottom:1px solid rgba(100,180,255,0.07); color:#c0d8f0; vertical-align:top; }
.comp-table tr:last-child td { border-bottom:none; }
.comp-table tr.hl td { background:rgba(30,100,200,0.12); color:#fff; }
.comp-table tr.hl td:first-child { color:#4db8ff; font-weight:700; }
.lim { display:inline-block; background:rgba(255,80,80,0.1); border:1px solid rgba(255,100,100,0.2); color:#ff9a9a; border-radius:6px; padding:0.2rem 0.5rem; font-size:0.82rem; }

/* TARGET CARDS */
.target-card { background:rgba(10,40,80,0.5); border:1px solid rgba(100,180,255,0.1); border-radius:18px; padding:2rem; text-align:center; height:100%; }
.target-emoji { font-size:2.5rem; margin-bottom:1rem; }
.target-card h3 { font-family:'Sora',sans-serif; font-size:1.05rem; font-weight:700; color:#fff; margin-bottom:0.6rem; }
.target-card p  { font-size:0.9rem; color:#9abcdc; margin:0; }

/* FOOTER */
.footer { text-align:center; padding:3rem 2rem; border-top:1px solid rgba(100,180,255,0.08); margin-top:2rem; color:#4a7aaa; font-size:0.88rem; line-height:2; }
.footer strong { color:#6aaadd; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-tag">🔬 Engenharia Biomédica · Universidade do Minho</div>
    <h1>Re<span>Motion</span></h1>
    <div class="hero-sub">A independência que move o futuro.</div>
    <div class="hero-desc">
        Um exoesqueleto de reabilitação de membros superiores controlado por sinais eletromiográficos (EMG),
        desenvolvido para devolver mobilidade e autonomia a pessoas com distúrbios neuromotores, nomeadamente pós-AVC.
    </div>
</div>
""", unsafe_allow_html=True)

# ── STATS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-bar">
    <div class="stat-card">
        <div class="stat-number">15M</div>
        <div class="stat-label">pessoas sofrem AVC por ano em todo o mundo</div>
        <div class="stat-source">Fonte: A Voz de Trás-os-Montes</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">5M</div>
        <div class="stat-label">ficam com sequelas permanentes após AVC</div>
        <div class="stat-source">Fonte: A Voz de Trás-os-Montes</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">26/dia</div>
        <div class="stat-label">novos casos de AVC sinalizados pelo INEM em Portugal</div>
        <div class="stat-source">Fonte: DNoticias, Abr. 2026</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">9 490</div>
        <div class="stat-label">utentes sinalizados pelo INEM em 2025</div>
        <div class="stat-source">Fonte: DNoticias, 2026</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── O QUE É + IMAGEM ──────────────────────────────────────────────────────────
col_t, col_i = st.columns([1.3, 1], gap="large")
with col_t:
    st.markdown("""
    <div class="section">
        <div class="section-title">🦾 O que é o ReMotion?</div>
        <p>O ReMotion é um <strong>exoesqueleto de reabilitação de membros superiores</strong> que utiliza
        sinais eletromiográficos (EMG) para detetar a intenção de movimento do utilizador e fornecer
        assistência apenas quando necessária, tornando a reabilitação mais personalizada, segura e eficaz.</p>
        <p>A sua principal inovação é o <strong>controlo subMVC</strong>: ao contrário das soluções existentes,
        não obriga o paciente a executar contrações musculares máximas, usando um limite confortável e individual,
        reduzindo o risco de lesão e fadiga muscular.</p>
        <p>Através da tecnologia <strong>Assist-As-Needed</strong>, o exoesqueleto só apoia o movimento quando
        o paciente realmente precisa, estimulando o esforço ativo e acelerando a recuperação neuromotora.</p>
        <p>Adicionalmente, o <strong>sistema de deteção de fadiga</strong> proporciona uma assistência mais segura
        ao detetar quando o músculo começa a falhar, evitando esforços excessivos.</p>
    </div>
    """, unsafe_allow_html=True)
with col_i:
    st.markdown(f"""
    <div style="padding:1.5rem;background:rgba(13,61,110,0.3);border:1px solid rgba(100,180,255,0.12);
         border-radius:22px;margin-top:0.5rem;text-align:center;">
        {exo_tag}
        <p style="font-size:0.78rem;color:#5a8ab0;margin-top:0.8rem;margin-bottom:0;">
            Figura 1 — Modelação do ReMotion em FreeCAD
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── TECNOLOGIA ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-title">⚙️ Tecnologia Inovadora</div>
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">📡</div>
            <h4>Controlo através de sinal EMG com subMVC</h4>
            <p>Deteta intenção de movimento a partir de sinais EMG residuais. Ao contrário da tecnologia convencional, utilizamos um valor confortável de contração para a calibração, de modo a que o paciente não seja obrigado a esforçar-se demasiado, evitando lesões.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤝</div>
            <h4>Assist-As-Needed</h4>
            <p>O exoesqueleto apoia apenas quando o paciente não consegue completar o movimento sozinho. Utiliza o conceito de controlo por impedância de forma a criar uma "mola virtual" dinâmica através do software desenvolvido. Se o paciente conseguir cumprir o movimento sozinho, o robô permanece invisível e maleável. No entanto, se o braço não for capaz, o motor injeta automaticamente o torque exato para mover o membro</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔋</div>
            <h4>Deteção de Fadiga</h4>
            <p>Sempre que o utilizador exerce forças exigentes acima de um limite de conforto (30 Nm), o algoritmo calcula a acumulação de fadiga. Ao atingir um nível crítico de exaustão (75% de fadiga acumulada), o exoesqueleto assume progressivamente o controlo mecânico. Isto garante que o paciente treina na sua zona de máximo estímulo sem atingir a exaustão total, evitando lesões, dores ou posturas incorretas, e tornando o uso domiciliário seguro e autónomo.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SOLUÇÕES EXISTENTES ───────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-title">🔍 Análise das Soluções Existentes</div>
    <p>Comparando o ReMotion com as abordagens atuais de reabilitação neuromotora:</p>
    <table class="comp-table">
        <thead><tr><th>Solução</th><th>Descrição</th><th>Limitação</th></tr></thead>
        <tbody>
            <tr><td><strong>Fisioterapia tradicional</strong></td><td>Exercícios assistidos por fisioterapeuta para recuperar força e coordenação motora</td><td><span class="lim">Sessões longas e exercícios repetitivos</span></td></tr>
            <tr><td><strong>Estimulação Elétrica Funcional (FES)</strong></td><td>Aplica corrente elétrica ao músculo para forçar a sua contração</td><td><span class="lim">Cansa rapidamente o músculo; ignora sinal EMG residual</span></td></tr>
            <tr><td><strong>Interfaces Cérebro-Máquina</strong></td><td>Captam sinais cerebrais para controlar dispositivos externos</td><td><span class="lim">Invasivo e de custo muito elevado</span></td></tr>
            <tr><td><strong>Exoesqueletos EMG convencionais</strong></td><td>Leem sinais EMG do paciente para controlar o exoesqueleto</td><td><span class="lim">Exigem contração máxima (MVC) — inacessível a muitos pacientes</span></td></tr>
            <tr><td><strong>Controlo de impedância</strong></td><td>Medem força do braço e torques para gerar movimento assistido</td><td><span class="lim">Requerem força mecânica detetável</span></td></tr>
            <tr class="hl"><td>✦ ReMotion (subMVC)</td><td>Controlo EMG com limite subMVC + Assist-As-Needed + Deteção de fadiga</td><td style="color:#4dffa0;">✓ Acessível, seguro, uso domiciliário</td></tr>
        </tbody>
    </table>
</div>
""", unsafe_allow_html=True)

# ── PÚBLICO-ALVO ──────────────────────────────────────────────────────────────
st.markdown('<div class="section"><div class="section-title">🚀 Contextos de Aplicação do Exoesqueleto</div></div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.markdown("""<div class="target-card"><div class="target-emoji">🏥</div>
    <h3>Ambiente Clínico / Hospitais</h3>
    <p>Integração em unidades de saúde para complementar as sessões tradicionais de fisioterapia, otimizando o tempo de intervenção dos terapeutas.</p>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown("""<div class="target-card"><div class="target-emoji">🏠</div>
    <h3>Uso Domiciliário Autónomo</h3>
    <p>Aplicação em ambiente doméstico após a alta hospitalar, permitindo a continuidade do treino diário sem necessidade de supervisão clínica constante.</p>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown("""<div class="target-card"><div class="target-emoji">🌐</div>
    <h3>Tele-reabilitação</h3>
    <p>Uso emfisioterapia à distância, onde os dados de torque e fadiga guardados pelo sistema podem ser enviados para análise do fisioterapeuta.</p>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── MODELO DE NEGÓCIO ─────────────────────────────────────────────────────────
st.markdown('<div class="section"><div class="section-title">💼 Modelo de Negócio</div></div>', unsafe_allow_html=True)

col_b1, col_b2, col_b3 = st.columns(3, gap="medium")

with col_b1:
    st.markdown("#### 📈 Fase Inicial — B2B")
    st.markdown("""
Direcionado a instituições de saúde com capacidade de integração imediata:
- Hospitais públicos e privados
- Clínicas de fisioterapia e neurologia
- Centros especializados de reabilitação
""")

with col_b2:
    st.markdown("#### 🏠 Expansão — B2B2C")
    st.markdown("""
Após validação clínica, expansão para o contexto domiciliário:
- Uso domiciliário supervisionado
- Check-ups periódicos remotos
- Feedback de dados clínicos ao médico assistente
""")

with col_b3:
    st.markdown("#### 💰 Fontes de Receita")
    st.markdown("""
Modelo misto para maximizar acessibilidade e sustentabilidade:
- Venda direta do dispositivo
- Aluguer temporário para reabilitação
- Subscrição de software de monitorização
""")

st.markdown("<br>", unsafe_allow_html=True)

# ── PREVISÃO FINANCEIRA ───────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-title">📊 Previsão Financeira (2026–2031)</div>
    <table class="comp-table">
        <thead><tr><th>Métrica</th><th>2026</th><th>2027</th><th>2028</th><th>2029</th><th>2030</th><th>2031</th></tr></thead>
        <tbody>
            <tr><td><strong>Nº Vendas</strong></td><td>0</td><td>35</td><td>53</td><td>105</td><td>142</td><td>163</td></tr>
            <tr><td><strong>Trabalhadores</strong></td><td>11</td><td>13</td><td>15</td><td>19</td><td>23</td><td>24</td></tr>
            <tr><td><strong>Vendas (€)</strong></td><td>0</td><td>1 296 295</td><td>1 944 443</td><td>3 888 885</td><td>5 249 995</td><td>6 037 494</td></tr>
            <tr><td><strong>Gastos (€)</strong></td><td>464 575</td><td>1 225 979</td><td>1 681 215</td><td>2 909 203</td><td>3 799 129</td><td>4 296 059</td></tr>
            <tr class="hl"><td><strong>Lucros (€)</strong></td><td style="color:#ff9a9a;">-479 127</td><td>44 151</td><td>232 083</td><td>786 028</td><td>1111 666</td><td>1 349 024</td></tr>
        </tbody>
    </table>
    <p style="font-size:0.82rem;color:#4a7aaa;margin-top:1rem;margin-bottom:0;">
        Projeção assume fase de I&D e investimento estrutural em 2026, com início de faturação e vendas a partir de 2027.
    </p>
</div>
""", unsafe_allow_html=True)

# ── MILESTONES ────────────────────────────────────────────────────────────────
st.markdown('<div class="section"><div class="section-title">🗓️ Estado e Milestones</div></div>', unsafe_allow_html=True)

m1, m2, m3 = st.columns(3, gap="medium")

with m1:
    st.markdown("#### 2 · Agora → 2026")
    st.info("""
**Investigação & Desenvolvimento**
- Investigação e desenvolvimento tecnológico
- Desenho e refinamento do protótipo funcional
    """)

with m2:
    st.markdown("#### 2 · Finais 2026 – Início 2027")
    st.warning("""
**Primeiro Envio**
- Conclusão do protótipo final
- Início de testes piloto e ensaios clínicos
- Submissão do processo de certificação médica para uso domiciliário
    """)

with m3:
    st.markdown("#### 3 · 2027")
    st.success("""
**Primeira Faturação**
- Lançamento oficial do ReMotion no mercado hospitalar
- Entrada das primeiras receitas
    """)

st.markdown("<br>", unsafe_allow_html=True)

# ── VISÃO FUTURA ──────────────────────────────────────────────────────────────
st.markdown('<div class="section"><div class="section-title">🚀 Visão Futura</div></div>', unsafe_allow_html=True)

v1, v2 = st.columns(2, gap="medium")

with v1:
    st.markdown("**1 · Integração de Inteligência Artificial**")
    st.markdown("Algoritmos de IA para adaptação automática dos parâmetros de assistência com base na evolução clínica de cada paciente.")
    st.markdown("---")
    st.markdown("**2 · Personalização Automática**")
    st.markdown("Calibração dinâmica do limite subMVC em tempo real, sem necessidade de intervenção clínica constante.")

with v2:
    st.markdown("**3 · Expansão do Público-Alvo**")
    st.markdown("Alargamento a outras condições neuromotoras: esclerose múltipla, lesões medulares e doença de Parkinson.")
    st.markdown("---")
    st.markdown("**4 · Expansão Internacional**")
    st.markdown("Certificação CE e entrada nos mercados europeu e norte-americano, aproveitando a crescente procura por dispositivos de reabilitação robótica.")

st.markdown("<br>", unsafe_allow_html=True)

# ── EQUIPA ────────────────────────────────────────────────────────────────────
st.markdown('<div class="section"><div class="section-title">👩‍🔬 A Equipa</div><p>Somos quatro estudantes da Licenciatura em Engenharia Biomédica da Universidade do Minho, unidas pelo objetivo de tornar a reabilitação motora mais acessível, inteligente e centrada no paciente.</p></div>', unsafe_allow_html=True)

col_photo, col_names = st.columns([1.2, 1], gap="large")

with col_photo:
    st.markdown(f"""
    <div style="padding:1rem;background:rgba(13,61,110,0.3);border:1px solid rgba(100,180,255,0.12);
         border-radius:18px;text-align:center;">
        {team_tag}
        <p style="font-size:0.78rem;color:#5a8ab0;margin-top:0.8rem;margin-bottom:0;">
            A equipa ReMotion
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_names:
    st.markdown("""
    <div style="padding:1.5rem;">
    """, unsafe_allow_html=True)
    members = [
        ("Vera Campos", "a107235"),
        ("Ana Carolina Guimarães", "a107196"),
        ("Matilde Campos", "a107190"),
        ("Andriana Smoliy", "a107188"),
    ]
    for name, num in members:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:1rem;padding:0.9rem 0;
             border-bottom:1px solid rgba(100,180,255,0.08);">
            <div style="min-width:40px;height:40px;background:linear-gradient(135deg,#0d47a1,#1976d2);
                 border-radius:50%;display:flex;align-items:center;justify-content:center;
                 font-size:1rem;">👩</div>
            <div>
                <div style="font-family:'Sora',sans-serif;font-weight:700;color:#fff;font-size:0.98rem;">{name}</div>
                <div style="font-size:0.82rem;color:#5a8ab0;">{num} · Eng. Biomédica, UMinho</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <strong>ReMotion</strong> — A independência que move o futuro.<br>
    Licenciatura em Engenharia Biomédica · Universidade do Minho<br>
    UC: Formação Empresarial em Engenharia Biomédica<br><br>
    <span style="color:#2a5a80;font-size:0.8rem;">
        Docentes: Manuel José Lopes Nunes · Fernando Oliveira Barbosa · Paulo Manuel Ferreira Sousa · Paulo Sérgio Lima Pereira Afonso
    </span>
</div>
""", unsafe_allow_html=True)
