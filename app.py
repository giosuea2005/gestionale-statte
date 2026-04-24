import streamlit as st
import os

# Configurazione della pagina
st.set_page_config(page_title="PATRONATO ENASC CAF UNSIC STATTE", layout="wide", page_icon="🏛️")

# --- STILE CSS PERSONALIZZATO (BLU E GIALLO) ---
st.markdown("""
    <style>
    /* Sfondo generale e font */
    .main {
        background-color: #f0f2f6;
    }
    /* Titolo Principale */
    h1 {
        color: #003366; /* Blu Scuro */
        font-family: 'Helvetica Neue', sans-serif;
        text-align: center;
        border-bottom: 3px solid #ffcc00; /* Linea Gialla */
        padding-bottom: 10px;
    }
    /* Sottotitoli */
    h4 {
        color: #00509d;
        text-align: center;
    }
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #003366;
        color: white;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    /* Pulsanti */
    .stButton>button {
        background-color: #ffcc00; /* Giallo */
        color: #003366 !important; /* Testo Blu */
        border-radius: 10px;
        border: 2px solid #003366;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #003366;
        color: #ffcc00 !important;
    }
    /* Tab e Expander */
    .st-expander {
        border: 1px solid #003366 !important;
        background-color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER CON LOGO E TITOLO ---
col_logo, col_titolo = st.columns([1, 4])

with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)

with col_titolo:
    st.title("🏛️ PATRONATO ENASC - CAF UNSIC STATTE")
    st.markdown("#### 📍 Piazza Vittorio Veneto, 5 - Statte (TA)")

# --- CONTATTI RAPIDI ---
st.info(f"✨ **BENVENUTO** | 📞 Tel: **3249230401** | 📧 Sede di Statte")

# --- DATABASE DELLE PRATICHE ---
servizi = {
    "📌 AREA FISCALE (CAF)": {
        "ISEE": {
            "documenti": [
                "Saldo e Giacenza media al 31/12/2024 (tutti i conti correnti bancari e postali)",
                "Codici Fiscali di tutto il nucleo familiare",
                "Targhe dei veicoli (auto, moto > 500cc, camper)",
                "Contratto di affitto con estremi registrazione (se in affitto)",
                "Visure catastali per immobili di proprietà",
                "Certificazioni di invalidità (se presenti)"
            ],
            "info": "L'ISEE 2026 si basa sui redditi e patrimoni del 2024."
        },
        "730": {
            "documenti": [
                "CU (Certificazione Unica) dipendenti o pensionati",
                "Codici fiscali di tutti i familiari a carico",
                "Visure catastali di immobili (se si hanno proprietà)",
                "Scontrini farmacia, fatture mediche e dentistiche",
                "Interessi passivi Mutuo",
                "Bonifici per ristrutturazione o bonus mobili",
                "Dichiarazione anno precedente"
            ],
            "info": "Dichiarazione redditi per rimborsi IRPEF."
        },
        "RED": {
            "documenti": ["Lettera matricola INPS", "Documento d'identità in corso di validità"],
            "info": "Comunicazione redditi pensionati."
        },
        "INVCIV": {
            "documenti": ["Modello ACC.AS/PS o ICLAV/ICRIC inviato dall'INPS", "Documento d'identità"],
            "info": "Dichiarazione annuale invalidi civili."
        },
        "CONTRATTI DI LOCAZIONE": {
            "documenti": ["Visura catastale", "Documenti identità parti", "APE (Prestazione Energetica)", "Canone pattuito"],
            "info": "Gestione contratti d'affitto."
        }
    },
    "🏥 AREA PATRONATO": {
        "SFL (Supporto Formazione e Lavoro)": {
            "documenti": ["Documenti di identità", "Codice IBAN", "ISEE in corso di validità"],
            "info": "Indennità mensile di **500€** per formazione. **Soglia ISEE 10.140€.**"
        },
        "NASpI (Disoccupazione)": {
            "documenti": ["Ultime buste paga", "Contratto di lavoro", "Documenti di identità", "Codice IBAN"],
            "info": "Indennità per perdita involontaria del lavoro."
        },
        "Invalidità Civile": {
            "documenti": ["Modello C (medico di base)", "Documento d'identità", "Tessera Sanitaria", "Codice IBAN"],
            "info": "Riconoscimento invalidità o Legge 104."
        },
        "Assegno Unico": {
            "documenti": ["Codice Fiscale figli e genitori", "IBAN richiedente", "ISEE 2026 aggiornato"],
            "info": "Sostegno figli a carico fino a 21 anni."
        },
        "Pensione di Vecchiaia": {
            "documenti": ["Estratto conto contributivo", "Documento identità", "Cessazione servizio"],
            "info": "Domanda di pensione ordinaria."
        },
        "Assegno Inclusione (ADI)": {
            "documenti": ["ISEE 2026", "Documenti identità"],
            "info": "Sostegno economico per nuclei fragili."
        }
    }
}

# --- TABS CON STILE ---
tabs = st.tabs([f"📂 {cat}" for cat in servizi.keys()])

for i, categoria in enumerate(servizi.keys()):
    with tabs[i]:
        st.write("") # Spazio
        cols = st.columns(1) # Layout a colonna singola larga per pulizia
        
        for nome_pratica, dati in servizi[categoria].items():
            with st.expander(f"🔹 {nome_pratica.upper()}", expanded=False):
                c1, c2 = st.columns([2, 1])
                with c1:
                    st.markdown("##### 📋 Elenco Documenti:")
                    for doc in dati["documenti"]:
                        st.markdown(f"✅ {doc}")
                with c2:
                    st.warning(f"**INFO:**\n{dati['info']}")
                
                st.divider()
                
                # Sezione Messaggio
                msg = st.text_input("Hai una domanda veloce?", key=f"in_{nome_pratica}", placeholder="Scrivi qui...")
                if st.button(f"📲 Chiedi per {nome_pratica}", key=f"btn_{nome_pratica}"):
                    if msg:
                        testo = f"Sede Statte - {nome_pratica}: {msg}"
                        link = f"https://wa.me/393249230401?text={testo.replace(' ', '%20')}"
                        st.link_button("Apri WhatsApp", link)
                    else:
                        st.error("Scrivi qualcosa prima di inviare!")

# --- SIDEBAR ESTETICA ---
st.sidebar.image("https://img.icons8.com/fluency/96/government.png") # Icona istituzionale generica
st.sidebar.header("📍 SEDE STATTE")
st.sidebar.write("Piazza Vittorio Veneto, 5")
st.sidebar.write("74010 Statte (TA)")
st.sidebar.markdown("---")
st.sidebar.write("📞 **Contatto Diretto:**")
st.sidebar.write("3249230401")
st.sidebar.markdown("---")
st.sidebar.caption("Sviluppato per Patronato ENASC - CAF UNSIC")