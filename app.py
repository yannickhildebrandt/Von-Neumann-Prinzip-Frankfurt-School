import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# ------------------------------------------------------
# Seiteneinstellungen & Formatierung
# ------------------------------------------------------
st.set_page_config(
    layout="wide",
    page_title="Von-Neumann-Mindset",
    page_icon="🧠"
)

st.markdown(
    """
    <style>
        body {
            background: radial-gradient(circle at top, #0b1230 0%, #03060f 60%);
            color: #e8ecff;
            font-family: 'Inter', sans-serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
        }
        .headline-gradient {
            font-size: 3.4rem;
            font-weight: 900;
            background: -webkit-linear-gradient(120deg, #4ce3f7, #8bff8e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: .4rem;
        }
        .subheadline {
            text-align: center;
            font-size: 1.25rem;
            color: #aab6ff;
            margin-bottom: 2.6rem;
            letter-spacing: 0.7px;
        }
        .intro-card, .story-card {
            border-radius: 18px;
            padding: 1.6rem 2rem;
            backdrop-filter: blur(14px);
            border: 1px solid rgba(140,190,255,0.18);
            box-shadow: 0 18px 55px rgba(12,30,70,0.45);
        }
        .intro-card {
            background: linear-gradient(140deg, rgba(60,90,220,0.35), rgba(24,140,180,0.28));
            margin-bottom: 1.4rem;
        }
        .story-card {
            background: linear-gradient(160deg, rgba(12,25,55,0.90), rgba(25,38,85,0.75));
            margin-bottom: 2rem;
        }
        .image-frame {
            width: 100%;
            padding-top: 56%;
            border-radius: 20px;
            background-size: cover;
            background-position: center;
            box-shadow: 0 24px 60px rgba(8,12,30,0.55);
            margin-bottom: 0.8rem;
        }
        .image-caption {
            text-align: center;
            color: #aab6ff;
            font-size: 0.95rem;
            margin-bottom: 1.6rem;
        }
        .metric-container .stMetric {
            background: rgba(7,12,30,0.75);
            border-radius: 16px;
            padding: 1.1rem;
            box-shadow: inset 0 0 0 1px rgba(140,210,255,0.25);
        }
        .highlight-bubble {
            background: rgba(82,255,196,0.14);
            border-left: 4px solid #52ffc4;
            padding: 1rem 1.3rem;
            border-radius: 12px;
            margin-top: 1.5rem;
            color: #d7fff3;
        }
        .footer-message {
            text-align: center;
            font-size: 1.1rem;
            color: #8bff8e;
            font-weight: 600;
        }
        .stExpander {
            background: rgba(10,16,36,0.6) !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------
# Hilfsfunktionen
# ------------------------------------------------------
def format_number(value, decimals=0):
    return f"{value:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")

def render_intro(text):
    st.markdown(f"<div class='intro-card'>{text}</div>", unsafe_allow_html=True)

def render_cover(url, caption):
    st.markdown(
        f"""
        <div class="image-frame" style="background-image:url('{url}');"></div>
        <p class="image-caption">{caption}</p>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------
# Hero-Bereich
# ------------------------------------------------------
st.markdown('<div class="headline-gradient">Von-Neumann-Mindset</div>', unsafe_allow_html=True)
st.markdown(
    "<div class='subheadline'>Vom starren Rechenautomaten zum universell programmierbaren Rechner – "
    "und warum dieser Paradigmenwechsel jedes Software-Update möglich macht.</div>",
    unsafe_allow_html=True
)

hero_col1, hero_col2 = st.columns([4, 5])
with hero_col1:
    st.markdown(
        """
        <div class="story-card">
            <p>
                Stellen wir uns die 1940er-Jahre vor: Computer waren raumfüllende Maschinen, verdrahtet für genau eine einzige Aufgabe.
                John von Neumann skizzierte einen radikalen Bruch – ein universeller Rechner, der sein Verhalten
                <strong>durch ein Programm im Speicher</strong> ändern kann. Heute ist das selbstverständlich, damals war es Revolution.
            </p>
            <p>
                Diese Experience führt Schritt für Schritt zu genau dieser Kernidee:
                <ul style="margin-top:0.5rem;">
                    <li>Wie die Architektur aufgebaut ist</li>
                    <li>Wie der Fetch-Decode-Execute-Zyklus funktioniert</li>
                    <li>Wie simples Umprogrammieren den Output verändert</li>
                    <li>Wo die Grenzen (Von-Neumann-Bottleneck) liegen</li>
                </ul>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
with hero_col2:
    render_cover(
        "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80",
        "Früher starre Verdrahtung, heute universelle Programmierbarkeit – Von-Neumann machte den Unterschied."
    )

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🧩 Architektur begreifen",
    "🔁 Befehlskreislauf erleben",
    "🛠️ Umprogrammieren & Effekt sehen",
    "🚦 Bottleneck simulieren"
])

# ------------------------------------------------------
# Tab 1: Architektur begreifen
# ------------------------------------------------------
with tab1:
    render_intro(
        "Du betrittst das Rechenzentrum der 1950er: Vor dir steht der frische Prototyp des IAS-Rechners. "
        "Hier erklärt dir eine Ingenieurin, wie CPU, Hauptspeicher, Ein-/Ausgabe und Datenwege zusammenspielen "
        "und warum das Programm plötzlich in magnetischen Trommeln gespeichert wird."
    )

    render_cover(
        "https://images.unsplash.com/photo-1581092334607-1e7e6fef3a22?auto=format&fit=crop&w=1600&q=80",
        "Vier Hauptkomponenten, unendlich viele Programme: das Herz der Von-Neumann-Architektur."
    )

    st.markdown(
        """
        <div class="story-card">
            <p><strong>Key Insight:</strong> Programm und Daten liegen gemeinsam im gleichen Speicher. 
            Der Prozessor holt sich beides, interpretiert Befehl für Befehl und kann dadurch völlig neue Aufgaben übernehmen – ohne Hardware umzubauen.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    component = st.radio(
        "Wähle eine Komponente für eine immersive Erklärung:",
        ["Zentralprozessor (CPU)", "Hauptspeicher", "Ein-/Ausgabe", "Datenwege (Busse)"],
        horizontal=True
    )

    explanations = {
        "Zentralprozessor (CPU)": {
            "text": (
                "Der CPU-Kern interpretiert Befehle aus dem Speicher, führt Rechnungen aus und steuert, welcher Schritt als nächstes kommt. "
                "Er besteht typischerweise aus Rechenwerk (ALU), Registersatz und Steuerwerk."
            ),
            "diagram": ["Fetch Steuerbefehle aus Speicher", "Dekodiere Opcode", "Steuere ALU/IO", "Schreibe Ergebnisse zurück"]
        },
        "Hauptspeicher": {
            "text": (
                "Im RAM (früher Trommelspeicher) liegen sowohl die Daten als auch das Programm nebeneinander. "
                "Der Clou: Tausche den Programmbereich aus, und der gleiche Rechner kann plötzlich ein anderes Problem lösen."
            ),
            "diagram": ["Adresse 0001: Befehl LOAD", "Adresse 0002: Befehl ADD", "Adresse 0003: Daten 42", "Adresse 0004: Daten 17"]
        },
        "Ein-/Ausgabe": {
            "text": (
                "Tastatur, Lochstreifenleser, Drucker – all diese Geräte liefern Daten an den Speicher oder empfangen Ergebnisse. "
                "Über spezielle I/O-Befehle interagiert das Programm mit der Außenwelt."
            ),
            "diagram": ["Eingabe -> Speicher", "CPU verarbeitet", "Ausgabe -> Anzeige"]
        },
        "Datenwege (Busse)": {
            "text": (
                "Adressbus, Datenbus, Steuerbus verbinden die Einheiten. "
                "Sie transportieren, welcher Speicherplatz angesprochen wird, welche Bits transportiert werden und wann eine Aktion startet."
            ),
            "diagram": ["Adressbus (sagt WO)", "Datenbus (liefert WAS)", "Steuerbus (steuert WANN)"]
        }
    }

    st.markdown(f"<div class='highlight-bubble'>{explanations[component]['text']}</div>", unsafe_allow_html=True)

    colA, colB = st.columns([3, 2])
    with colA:
        st.subheader("Informationsfluss visualisiert")
        df_flow = pd.DataFrame({
            "Schritt": explanations[component]["diagram"],
            "Position": list(range(1, len(explanations[component]["diagram"]) + 1))
        })
        fig_flow = px.area(
            df_flow,
            x="Position",
            y=[1]*len(df_flow),
            hover_data=["Schritt"],
            color_discrete_sequence=["#4ce3f7"]
        )
        fig_flow.update_layout(
            showlegend=False,
            xaxis=dict(showgrid=False, visible=False),
            yaxis=dict(showgrid=False, visible=False),
            height=220,
            margin=dict(l=30, r=30, t=30, b=20),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_flow, use_container_width=True)
    with colB:
        st.metric("Programm im Speicher?", "Ja – und jederzeit austauschbar")
        st.caption("Genau das unterscheidet den Von-Neumann-Rechner von verdrahteten Spezialmaschinen.")

# ------------------------------------------------------
# Tab 2: Fetch-Decode-Execute Zyklus
# ------------------------------------------------------
with tab2:
    render_intro(
        "Der Operator startet das Programm. Die Kontrolllampe blinkt: Fetch – Decode – Execute. "
        "Du blickst dem Steuerwerk beim Arbeiten über die Schulter und siehst, wie jedes Bit seinen Platz hat."
    )

    render_cover(
        "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80",
        "Instruktionszyklus als Herzschlag des Rechners."
    )

    st.markdown(
        """
        <div class="story-card">
            Jede Instruktion durchläuft drei Hauptphasen. Sobald der Speicher ein neues Wort liefert, 
            kann der Rechner – dank Von-Neumann – völlig andere Aktionen ausführen.
        </div>
        """,
        unsafe_allow_html=True
    )

    cycle_steps = [
        {
            "name": "1. Fetch",
            "description": "Der Program Counter (PC) zeigt auf die nächste Speicheradresse. Der Befehl wird in das Instruktionsregister geladen.",
            "visual": ["PC -> Adresse 0004", "Speicher[0004] -> Instruktionsregister"]
        },
        {
            "name": "2. Decode",
            "description": "Das Steuerwerk interpretiert den Opcode und bereitet die beteiligten Funktionseinheiten vor.",
            "visual": ["Opcode 01 = LOAD", "Operand = Adresse 0010", "Steuerleitungen setzen sich"]
        },
        {
            "name": "3. Execute",
            "description": "Die ALU oder I/O-Einheit führt die Aktion aus. Ergebnis kann in Register, Speicher oder Gerät fließen.",
            "visual": ["ALU addiert Register A + Speicher[0010]", "Ergebnis -> Register A"]
        },
        {
            "name": "4. Write-Back",
            "description": "Der Prozessor speichert das Ergebnis und erhöht den Program Counter – bereit für den nächsten Befehl.",
            "visual": ["Register A -> Speicher[0012]", "PC = PC + 1"]
        }
    ]

    step_idx = st.slider("Schritt im Instruktionszyklus", 0, len(cycle_steps) - 1, 0)
    current_step = cycle_steps[step_idx]

    col1, col2 = st.columns([2, 3])
    with col1:
        st.subheader(current_step["name"])
        st.markdown(f"<div class='highlight-bubble'>{current_step['description']}</div>", unsafe_allow_html=True)
    with col2:
        fig_cycle = px.timeline(
            pd.DataFrame({
                "Phase": current_step["visual"],
                "Start": np.arange(len(current_step["visual"])),
                "Ende": np.arange(1, len(current_step["visual"]) + 1)
            }),
            x_start="Start",
            x_end="Ende",
            y="Phase",
            color_discrete_sequence=["#8bff8e"]
        )
        fig_cycle.update_layout(
            height=260,
            xaxis=dict(visible=False),
            yaxis=dict(autorange="reversed"),
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_cycle, use_container_width=True)

    st.caption("Sobald im Speicher ein neuer Befehl liegt, ändert sich der Ablauf – ohne Hardware-Tausch.")

# ------------------------------------------------------
# Tab 3: Umprogrammieren & Effekt sehen
# ------------------------------------------------------
with tab3:
    render_intro(
        "Du sitzt an der Konsole des Röhrenrechners. Mit wenigen Bytes im Speicher bestimmst du, "
        "ob das System summiert oder multipliziert. Die Techniker:innen schauen gespannt zu: "
        "Kann wirklich derselbe Rechner zwei völlig verschiedene Probleme lösen?"
    )

    render_cover(
        "https://images.unsplash.com/photo-1526498460520-4c246339dccb?auto=format&fit=crop&w=1600&q=80",
        "Ein neues Programm, ein neuer Zweck – exakt das ist die Von-Neumann-Idee."
    )

    st.markdown(
        """
        <div class="story-card">
            Lade ein kleines Programm in den Speicher, führe es aus – ändere nur einen Befehl, erhalte ein komplett anderes Ergebnis.
            So demonstrierst du Studierenden die Macht des programmierbaren Rechners.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Mini-Assembler Playground")
    st.caption("Instruktionssatz: LOAD (L), STORE (S), ADD (A), MUL (M), OUT (O)")

    default_program = [
        {"Adresse": "000", "Instruktion": "L A0"},     # Lade Wert aus Speicheradresse A0
        {"Adresse": "001", "Instruktion": "A A1"},     # Addiere Wert an Adresse A1
        {"Adresse": "002", "Instruktion": "O"},        # Ausgabe
        {"Adresse": "003", "Instruktion": "HALT"}
    ]
    program_df = pd.DataFrame(default_program)

    edited_program = st.experimental_data_editor(program_df, num_rows="dynamic", key="program_editor")

    data_memory = {
        "A0": st.number_input("Wert an Adresse A0", -100, 100, 7),
        "A1": st.number_input("Wert an Adresse A1", -100, 100, 5),
        "A2": st.number_input("Wert an Adresse A2", -100, 100, 3)
    }

    def run_program(program, data):
        acc = 0
        output = None
        history = []
        for _, row in program.iterrows():
            instr = str(row["Instruktion"]).strip().upper()
            history.append(instr)
            if instr.startswith("L"):
                addr = instr.split()[1]
                acc = data.get(addr, 0)
            elif instr.startswith("A"):
                addr = instr.split()[1]
                acc += data.get(addr, 0)
            elif instr.startswith("M"):
                addr = instr.split()[1]
                acc *= data.get(addr, 0)
            elif instr.startswith("S"):
                addr = instr.split()[1]
                data[addr] = acc
            elif instr.startswith("O"):
                output = acc
            elif instr == "HALT":
                break
        return output, history

    output_value, history = run_program(edited_program, data_memory.copy())

    col_prog, col_history = st.columns([2, 3])
    with col_prog:
        st.metric("Programm-Output", output_value if output_value is not None else "kein OUT")
        st.caption("Ändere oben Instruktionen oder Werte. Ein einziger Opcode-Wechsel zeigt den Effekt.")
        st.markdown(
            """
            <div class="highlight-bubble">
                Tipp: Ersetze Zeile 001 durch <code>M A1</code> – derselbe Computer rechnet jetzt ein Produkt.
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_history:
        st.subheader("Instruction Trace")
        st.code("\n".join(history) if history else "Programm leer", language="text")

    st.caption("Genau deshalb spricht man vom Universaltalent: Programme sind nur Daten – und damit jederzeit austauschbar.")

# ------------------------------------------------------
# Tab 4: Von-Neumann-Bottleneck simulieren
# ------------------------------------------------------
with tab4:
    render_intro(
        "In der Maschinenhalle fällt dir auf: Die CPU langweilt sich, weil der Speicher so langsam liefert. "
        "Das wird später als Von-Neumann-Bottleneck bekannt – der Datenbus wird zum Engpass."
    )

    render_cover(
        "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80",
        "CPU vs. Speicherbandbreite – wer bestimmt das Tempo?"
    )

    st.markdown(
        """
        <div class="story-card">
            Die Leistungsfähigkeit eines Von-Neumann-Rechners hängt stark davon ab, wie schnell Befehle und Daten aus dem Speicher zur CPU gelangen.
            Durchforste mit den Reglern, wie sich Durchsatz und Auslastung verändern.
        </div>
        """,
        unsafe_allow_html=True
    )

    cpu_speed = st.slider("CPU-Geschwindigkeit (Millionen Instruktionen pro Sekunde)", 1, 400, 120, step=10)
    memory_bandwidth = st.slider("Speicher-Bandbreite (MB/s)", 10, 800, 80, step=10)
    bytes_per_instruction = st.select_slider(
        "Bytes pro Instruktion + Datenbedarf",
        options=[4, 8, 12, 16, 24, 32],
        value=16
    )

    required_bandwidth = cpu_speed * bytes_per_instruction
    utilization = min(memory_bandwidth / required_bandwidth, 1.0) * 100
    stall_percentage = 100 - utilization

    colA, colB, colC = st.columns(3)
    colA.metric("Instruktionsbedarf an Bandbreite", f"{required_bandwidth:.0f} MB/s")
    colB.metric("Verfügbare Bandbreite", f"{memory_bandwidth} MB/s")
    colC.metric("CPU-Auslastung", f"{utilization:.0f} %")

    st.caption(f"Stall-Zeit durch Wartezyklen: {stall_percentage:.0f} %")

    samples = np.linspace(4, 32, 50)
    throughput = np.minimum(memory_bandwidth / samples, cpu_speed)
    df_bottleneck = pd.DataFrame({
        "Bytes pro Instruktion": samples,
        "Mögliche Instruktionen/s": throughput
    })
    fig_bottle = px.line(
        df_bottleneck,
        x="Bytes pro Instruktion",
        y="Mögliche Instruktionen/s",
        labels={"Mögliche Instruktionen/s": "Instruktionen pro Sekunde (Mio.)"},
        color_discrete_sequence=["#4ce3f7"]
    )
    fig_bottle.add_scatter(
        x=[bytes_per_instruction],
        y=[min(memory_bandwidth / bytes_per_instruction, cpu_speed)],
        mode="markers",
        marker=dict(size=12, color="#8bff8e"),
        name="aktuelles Setup"
    )
    fig_bottle.update_layout(
        height=320,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color="#e8ecff"
    )
    st.plotly_chart(fig_bottle, use_container_width=True)

    st.markdown(
        """
        <div class="highlight-bubble">
            Lösungsideen: Caches, Prefetching, Harvard-Architektur, Parallelisierung. 
            Aber das Grundprinzip bleibt: Programme bleiben im Speicher und sind jederzeit austauschbar.
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------
# Abschluss
# ------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div class="footer-message">
        Von Neumann hat uns nicht nur eine Architektur geschenkt – sondern die Freiheit, jede Maschine
        allein durch Code in etwas Neues zu verwandeln.
    </div>
    """,
    unsafe_allow_html=True
)
