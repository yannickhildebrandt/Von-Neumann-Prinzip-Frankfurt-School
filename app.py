import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# ------------------------------------------------------------------
# Seiteneinstellungen & globales Styling
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Von Neumann Discovery Lab",
    page_icon="🧠",
    layout="wide"
)

st.markdown(
    """
    <style>
        body {
            background: radial-gradient(circle at top left, #0f172a, #020617 65%);
            color: #e8ecf9;
            font-family: "Inter", sans-serif;
        }
        .block-container {
            padding-top: 2.5rem;
            padding-bottom: 3rem;
            max-width: 1300px;
        }
        .hero-title {
            font-size: 3.4rem;
            font-weight: 900;
            letter-spacing: 2px;
            text-transform: uppercase;
            text-align: center;
            margin-bottom: 0.4rem;
            background: -webkit-linear-gradient(120deg, #38f9d7, #43e7fe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-subtitle {
            text-align: center;
            font-size: 1.15rem;
            color: #9fb4ff;
            margin-bottom: 2rem;
        }
        .mission-card, .story-card {
            border-radius: 18px;
            padding: 1.6rem 2rem;
            backdrop-filter: blur(12px);
            border: 1px solid rgba(92, 156, 255, 0.25);
            box-shadow: 0 25px 60px rgba(2, 15, 45, 0.45);
            margin-bottom: 1.5rem;
        }
        .mission-card {
            background: linear-gradient(135deg, rgba(24, 55, 104, 0.55), rgba(33, 83, 115, 0.55));
        }
        .story-card {
            background: linear-gradient(140deg, rgba(10, 22, 52, 0.8), rgba(27, 86, 109, 0.55));
        }
        .intro-block {
            border-radius: 16px;
            padding: 1.2rem 1.6rem;
            margin-bottom: 1.1rem;
            background: linear-gradient(125deg, rgba(64, 93, 230, 0.35), rgba(103, 219, 255, 0.15));
            border: 1px solid rgba(155, 225, 255, 0.25);
        }
        .image-frame {
            width: 100%;
            padding-top: 54%;
            border-radius: 18px;
            background-size: cover;
            background-position: center;
            box-shadow: 0 22px 60px rgba(0, 0, 0, 0.55);
            margin-bottom: 0.8rem;
        }
        .image-caption {
            text-align: center;
            font-size: 0.95rem;
            color: #9fb4ff;
            margin-bottom: 1.6rem;
        }
        .metric-grid div[data-testid="stMetricValue"] {
            font-size: 1.6rem;
        }
        .footer {
            text-align: center;
            padding-top: 2rem;
            font-weight: 600;
            color: #43e7fe;
        }
        .stSelectbox label, .stSlider label, .stNumberInput label {
            font-weight: 600;
            color: #d7e1ff;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 1.2rem;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            border-radius: 12px;
            padding: 0 1.4rem;
            background: rgba(13, 32, 70, 0.6);
            color: #9fb4ff;
        }
        .stTabs [aria-selected="true"] {
            background: rgba(47, 207, 207, 0.35)!important;
            color: #ffffff!important;
        }
        .code-bubble {
            background: rgba(8, 24, 58, 0.9);
            border-left: 4px solid #43e7fe;
            padding: 0.9rem 1.2rem;
            border-radius: 12px;
            font-family: "Source Code Pro", monospace;
            margin-top: 0.7rem;
            margin-bottom: 0.7rem;
        }
        .highlight {
            color: #43e7fe;
            font-weight: 700;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------------------
# Utility-Funktionen
# ------------------------------------------------------------------
def render_cover(url: str, caption: str):
    st.markdown(
        f"""
        <div class="image-frame" style="background-image: url('{url}');"></div>
        <p class="image-caption">{caption}</p>
        """,
        unsafe_allow_html=True
    )

def human_number(value: float):
    thresholds = [
        (1e12, " Bio."),
        (1e9, " Mrd."),
        (1e6, " Mio."),
        (1e3, " Tsd.")
    ]
    for threshold, suffix in thresholds:
        if abs(value) >= threshold:
            return f"{value / threshold:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".") + suffix
    return f"{value:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")

def format_number(value, decimals=0):
    return f"{value:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ------------------------------------------------------------------
# Hero
# ------------------------------------------------------------------
st.markdown('<div class="hero-title">Von Neumann Discovery Lab</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Erlebe, wie ein Rechner sein Verhalten durch Software verändert – und warum genau das den Computer zum Universalwerkzeug macht.</div>',
    unsafe_allow_html=True
)

col_intro, col_scene = st.columns([5, 4])

with col_intro:
    st.markdown(
        """
        <div class="mission-card">
            <h3>Mission Brief</h3>
            <p>
                1945 beschrieb John von Neumann erstmals den Entwurf eines <span class="highlight">universell programmierbaren Rechners</span>.
                Programme und Daten teilen sich ein gemeinsames Speicherwerk, die CPU holt Instruktion für Instruktion, 
                und Ein-/Ausgabe binden den Rechner an die Außenwelt.
            </p>
            <p>
                Diese App führt dich durch vier Kontrollräume:
            </p>
            <ul>
                <li><strong>Blueprint Deck</strong> – die Architektur in einem holografischen Schaltplan.</li>
                <li><strong>Instruction Bay</strong> – der Fetch-Decode-Execute-Zyklus in Bewegung.</li>
                <li><strong>Reprogramming Workshop</strong> – du tauschst Programme im Speicher aus und beobachtest neue Ergebnisse.</li>
                <li><strong>EVA Composer</strong> – du entwirfst neue Aufgaben, indem du Ein-/Ausgabe und Programm kombinierst.</li>
            </ul>
            <p>
                Kernbotschaft: <span class="highlight">Weil Programme nur Speicherinhalt sind, lässt sich derselbe Rechner jederzeit neu erfinden.</span>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_scene:
    render_cover(
        "https://images.unsplash.com/photo-1580894897200-9c9e7c7825b0?auto=format&fit=crop&w=1600&q=80",
        "Ein Kontrollraum der frühen Computerära – Programmwechsel bedeutete plötzlich neue Aufgaben statt neuer Hardware."
    )

st.markdown("---")

# ------------------------------------------------------------------
# Navigation
# ------------------------------------------------------------------
st.sidebar.title("🎚️ Steuerkonsole")
mode = st.sidebar.radio(
    "Wähle ein Modul",
    [
        "Blueprint Deck",
        "Instruction Bay",
        "Reprogramming Workshop",
        "EVA Composer"
    ],
    index=0
)

# ------------------------------------------------------------------
# Modul 1 – Blueprint Deck
# ------------------------------------------------------------------
if mode == "Blueprint Deck":
    st.markdown(
        """
        <div class="intro-block">
            Du stehst vor einem transparenten Display, das den inneren Aufbau eines Von-Neumann-Rechners zeigt. 
            Jede Komponente leuchtet auf, sobald du sie ansteuerst, und die Datenwege verbinden die Stationen.
        </div>
        """,
        unsafe_allow_html=True
    )

    render_cover(
        "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80",
        "Von außen nur ein Kasten – innen eine orchestrierte Choreographie aus Speicher, Prozessor und Datenwegen."
    )

    st.markdown(
        """
        <div class="story-card">
            Ein Von-Neumann-Rechner besteht aus wenigen Bausteinen:
            <ul>
                <li><strong>Zentralprozessor (CPU)</strong> – interpretiert Instruktionen, steuert ALU und Register.</li>
                <li><strong>Hauptspeicher</strong> – hält Programm und Daten zugleich bereit.</li>
                <li><strong>I/O-Subsystem</strong> – verbindet Tastatur, Touch, Sensoren, Anzeigen.</li>
                <li><strong>Datenwege (Busse)</strong> – transportieren Adressen, Steuerimpulse und Daten.</li>
            </ul>
            Dass Programme im selben Speicher liegen wie Daten, macht einen beliebigen Funktionswechsel ohne Hardwareeingriff möglich.
        </div>
        """,
        unsafe_allow_html=True
    )

    component_descriptions = {
        "Zentralprozessor": ("Befehlszentrale", "Steuerwerk, Rechenwerk (ALU) und Register interpretieren Code – Befehl für Befehl."),
        "Hauptspeicher": ("Programm & Daten", "RAM oder Magnettrommel speichern Instruktionen und Werte in demselben Adressraum."),
        "Eingabe": ("Input-Kanal", "Geräte wie Tastatur, Scanner oder Netzwerk liefern Daten in den Speicher."),
        "Ausgabe": ("Output-Kanal", "Displays, Drucker oder Aktoren geben Ergebnisse an die Außenwelt."),
        "Bus-System": ("Datenwege", "Adress-, Daten- und Steuerbus koordinieren, was wohin fließt und wann etwas passiert.")
    }

    selection = st.segmentation.selectbox(
        "Welche Komponente willst du hervorheben?",
        list(component_descriptions.keys()),
        key="component_select"
    ) if hasattr(st, "segmentation") else st.selectbox(
        "Welche Komponente willst du hervorheben?",
        list(component_descriptions.keys()),
        index=0
    )

    # Plotly Blueprint
    nodes = {
        "Eingabe": (-1, 1),
        "Ausgabe": (1, 1),
        "Hauptspeicher": (0, 1.5),
        "Zentralprozessor": (0, 0),
        "ALU": (-0.5, -0.6),
        "Steuerwerk": (0.5, -0.6),
        "Register": (0, -1.2),
        "Bus-System": (0, 0.6)
    }

    edges = [
        ("Eingabe", "Bus-System"),
        ("Ausgabe", "Bus-System"),
        ("Bus-System", "Hauptspeicher"),
        ("Bus-System", "Zentralprozessor"),
        ("Zentralprozessor", "ALU"),
        ("Zentralprozessor", "Steuerwerk"),
        ("Zentralprozessor", "Register"),
        ("Register", "Bus-System"),
        ("Hauptspeicher", "Zentralprozessor")
    ]

    fig = go.Figure()

    for edge in edges:
        x0, y0 = nodes[edge[0]]
        x1, y1 = nodes[edge[1]]
        fig.add_trace(go.Scatter(
            x=[x0, x1], y=[y0, y1],
            mode="lines",
            line=dict(color="rgba(67, 231, 254, 0.5)", width=3),
            hoverinfo="none"
        ))

    for name, (x, y) in nodes.items():
        is_selected = name.startswith(selection) or (selection == "Bus-System" and name == "Bus-System")
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode="markers+text",
            marker=dict(
                size=22 if is_selected else 16,
                color="#43e7fe" if is_selected else "rgba(86,120,235,0.6)",
                line=dict(color="#ffffff", width=1.5)
            ),
            text=[name],
            textposition="top center",
            hoverinfo="text",
            opacity=1 if is_selected else 0.7
        ))

    fig.update_layout(
        height=520,
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=40, b=0),
        title="Architektur-Hologramm"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        f"""
        <div class="story-card">
            <h4>{component_descriptions[selection][0]}</h4>
            <p>{component_descriptions[selection][1]}</p>
            <p><span class="highlight">Warum das zählt:</span> Tausche den Code im Speicher aus – die CPU interpretiert automatisch eine neue Befehlsfolge. 
            Ohne Von-Neumann-Architektur gäbe es keine universell programmierbaren Maschinen.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------------------
# Modul 2 – Instruction Bay
# ------------------------------------------------------------------
elif mode == "Instruction Bay":
    st.markdown(
        """
        <div class="intro-block">
            Im Instruction Bay siehst du den Herzschlag eines Von-Neumann-Rechners. 
            Der Program Counter holt das nächste Wort aus dem Speicher, das Steuerwerk interpretiert es, 
            und die ALU führt es aus. Wechsle Schritte und beobachte, wie sich Daten quer durchs System bewegen.
        </div>
        """,
        unsafe_allow_html=True
    )

    render_cover(
        "https://images.unsplash.com/photo-1517430816045-df4b7de11d1d?auto=format&fit=crop&w=1600&q=80",
        "Instruktionszyklus als Taktgeber – Fetch, Decode, Execute und weiter zum nächsten Befehl."
    )

    mock_program = pd.DataFrame({
        "Adresse": ["0000", "0001", "0002", "0003", "0004", "0005"],
        "Maschinenwort": ["LOAD A0", "ADD A1", "STORE A2", "LOAD A3", "OUT", "HALT"],
        "Kommentar": [
            "Hole Startwert",
            "Addiere Eingabe",
            "Speichere Zwischenergebnis",
            "Lade Ausgabepegel",
            "Gib Resultat aus",
            "Stop"
        ]
    })

    st.table(mock_program)

    cycle = [
        {
            "phase": "Fetch",
            "beschreibung": "Program Counter adressiert 0000, Befehl wird aus dem Hauptspeicher gezogen.",
            "aktionen": ["PC ➜ Adressbus", "Speicherwort 0000 ➜ Instruktionsregister"],
            "pc": 0
        },
        {
            "phase": "Decode",
            "beschreibung": "Steuerwerk zerlegt „LOAD A0“: Opcode = LOAD, Operand = Adresse A0.",
            "aktionen": ["Opcode erkannt", "Adressfeld in Adressregister", "Steuerleitungen gesetzt"],
            "pc": 0
        },
        {
            "phase": "Execute",
            "beschreibung": "ALU/Datapath lädt den Wert an Adresse A0 in den Akku (ACC).",
            "aktionen": ["Adressbus ➜ A0", "Datenbus ➜ 42", "ACC = 42"],
            "pc": 0
        },
        {
            "phase": "Write Back & Increment",
            "beschreibung": "Ergebnis liegt in Registern, PC geht zur nächsten Instruktion.",
            "aktionen": ["ACC hält neuen Wert", "PC = PC + 1 = 0001"],
            "pc": 1
        },
        {
            "phase": "Nächster Zyklus",
            "beschreibung": "Die Pipeline startet erneut für Adresse 0001.",
            "aktionen": ["Fetch ADD A1", "Decode + ALU", "Write Back"],
            "pc": 1
        }
    ]

    step = st.slider("Instruktionsschritt", 0, len(cycle) - 1, 0)
    current = cycle[step]

    col_phase, col_viz = st.columns([1.6, 2.4])

    with col_phase:
        st.markdown(
            f"""
            <div class="story-card">
                <h3>{current['phase']}</h3>
                <p>{current['beschreibung']}</p>
                <div class="code-bubble">
                    PC = {current["pc"]:04d}<br>
                    Instruktionsregister = "{mock_program.iloc[current["pc"], 1]}"<br>
                    ACC = ? (wird im Execute-Schritt gesetzt)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_viz:
        fig = go.Figure()
        y_positions = np.linspace(1, 0, len(current["aktionen"]))
        fig.add_trace(go.Bar(
            x=[1] * len(current["aktionen"]),
            y=current["aktionen"],
            orientation="h",
            marker=dict(color=["#38f9d7"] + ["#43e7fe"] * (len(current["aktionen"]) - 1), opacity=0.85),
            width=0.4
        ))
        fig.update_layout(
            height=280,
            xaxis=dict(showticklabels=False),
            yaxis=dict(title="", automargin=True),
            margin=dict(l=0, r=20, t=30, b=30),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            title="Mikroaktionen in dieser Phase"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.info("Sobald im Speicher an Adresse 0000 ein anderer Befehl liegt, ändert sich der gesamte Ablauf. Genau das meint „programmierbar“.")

# ------------------------------------------------------------------
# Modul 3 – Reprogramming Workshop
# ------------------------------------------------------------------
elif mode == "Reprogramming Workshop":
    st.markdown(
        """
        <div class="intro-block">
            Willkommen im Speicherlabor. Hier tauscht du Instruktionen aus, lädst andere Werte in den Speicher 
            und siehst sofort, wie sich derselbe Rechner völlig anders verhält. 
            Programme sind hier nichts weiter als Daten – editierbar wie eine Tabelle.
        </div>
        """,
        unsafe_allow_html=True
    )

    render_cover(
        "https://images.unsplash.com/photo-1526379879527-8559ecfcaec0?auto=format&fit=crop&w=1600&q=80",
        "Programmwechsel ohne Schraubenzieher: Tape raus, neues Programm rein – und schon löst die Maschine eine neue Aufgabe."
    )

    st.markdown(
        """
        <div class="story-card">
            Befehle liegen als nummerierte Wörter im Speicher. Die CPU läuft Zeile für Zeile (fetch) und führt sie aus (execute). 
            Du kannst die Tabelle editieren, neue Instruktionen hinzufügen oder mit Vorlagen beginnen.
        </div>
        """,
        unsafe_allow_html=True
    )

    templates = {
        "Addition zweier Zahlen": [
            {"Adresse": "0000", "Instruktion": "LOAD A0"},
            {"Adresse": "0001", "Instruktion": "ADD A1"},
            {"Adresse": "0002", "Instruktion": "OUT"},
            {"Adresse": "0003", "Instruktion": "HALT"}
        ],
        "Celsius ➜ Fahrenheit": [
            {"Adresse": "0000", "Instruktion": "LOAD A0"},
            {"Adresse": "0001", "Instruktion": "MUL A1"},
            {"Adresse": "0002", "Instruktion": "DIV A2"},
            {"Adresse": "0003", "Instruktion": "ADD A3"},
            {"Adresse": "0004", "Instruktion": "OUT"},
            {"Adresse": "0005", "Instruktion": "HALT"}
        ],
        "Subtraktion mit Zweig": [
            {"Adresse": "0000", "Instruktion": "LOAD A0"},
            {"Adresse": "0001", "Instruktion": "SUB A1"},
            {"Adresse": "0002", "Instruktion": "JZ 5"},
            {"Adresse": "0003", "Instruktion": "OUT"},
            {"Adresse": "0004", "Instruktion": "HALT"},
            {"Adresse": "0005", "Instruktion": "LOAD A2"},
            {"Adresse": "0006", "Instruktion": "OUT"},
            {"Adresse": "0007", "Instruktion": "HALT"}
        ]
    }

    if "program_table" not in st.session_state:
        st.session_state.program_table = pd.DataFrame(templates["Addition zweier Zahlen"])

    template_choice = st.selectbox("Vorlage laden", list(templates.keys()), index=0)
    if st.button("Vorlage übernehmen", type="primary"):
        st.session_state.program_table = pd.DataFrame(templates[template_choice])
        st.success("Programm in den Speicher gelegt – du kannst sofort editieren.")

    st.write("### Speicherbereich (Instruktionsspeicher)")
    program_editor = st.data_editor(
        st.session_state.program_table,
        hide_index=True,
        num_rows="dynamic",
        key="program_editor"
    )

    st.write("---")
    st.write("### Datenspeicher")
    col_mem1, col_mem2, col_mem3, col_mem4 = st.columns(4)
    data_memory = {
        "A0": col_mem1.number_input("A0", value=5.0, step=1.0),
        "A1": col_mem2.number_input("A1", value=3.0, step=1.0),
        "A2": col_mem3.number_input("A2", value=5.0, step=1.0),
        "A3": col_mem4.number_input("A3", value=32.0, step=1.0),
        "A4": st.number_input("A4", value=10.0, step=1.0)
    }

    st.caption("Hinweis: Instruktionen unterstützen LOAD, STORE, ADD, SUB, MUL, DIV, SET, OUT, HALT, JUMP, JZ.")

    def run_program(df: pd.DataFrame, data_mem: dict):
        acc = 0.0
        pc = 0
        output_values = []
        history = []
        program = df.reset_index(drop=True)
        safety_counter = 0

        while pc < len(program):
            safety_counter += 1
            if safety_counter > 100:
                history.append("Abbruch: zu viele Schritte (mögliche Endlosschleife).")
                break

            instruction = str(program.loc[pc, "Instruktion"]).strip()
            if not instruction:
                history.append(f"PC {pc:02d}: (leer) -> weiter")
                pc += 1
                continue

            parts = instruction.split()
            opcode = parts[0].upper()
            operand = parts[1] if len(parts) > 1 else None
            history.append(f"PC {pc:02d}: {instruction}")

            try:
                if opcode == "LOAD":
                    acc = float(data_mem.get(operand, 0))
                elif opcode == "STORE":
                    data_mem[operand] = acc
                elif opcode == "ADD":
                    acc += float(data_mem.get(operand, 0))
                elif opcode == "SUB":
                    acc -= float(data_mem.get(operand, 0))
                elif opcode == "MUL":
                    acc *= float(data_mem.get(operand, 0))
                elif opcode == "DIV":
                    divisor = float(data_mem.get(operand, 1))
                    if divisor == 0:
                        history.append("⚠️ Division durch 0 – Abbruch.")
                        break
                    acc /= divisor
                elif opcode == "SET":
                    acc = float(operand)
                elif opcode == "OUT":
                    output_values.append(acc)
                elif opcode == "HALT":
                    history.append("Programm stoppt mit HALT.")
                    break
                elif opcode == "JUMP":
                    pc = int(operand)
                    continue
                elif opcode == "JZ":
                    if acc == 0:
                        pc = int(operand)
                        continue
                else:
                    history.append(f"Unbekannter Opcode: {opcode}")
                    break
            except Exception as exc:
                history.append(f"Fehler bei Instruktion '{instruction}': {exc}")
                break

            pc += 1

        return output_values, history, acc, data_mem

    if st.button("Programm ausführen", type="primary"):
        outputs, trace, final_acc, new_memory = run_program(program_editor, data_memory.copy())
        st.session_state.execution_trace = trace
        st.session_state.execution_output = outputs
        st.session_state.final_acc = final_acc
        st.session_state.after_memory = new_memory
    else:
        st.caption("Klicke auf „Programm ausführen“, um CPU und Speicherzyklus zu beobachten.")

    if "execution_trace" in st.session_state:
        st.write("### Laufzeit-Log")
        st.code("\n".join(st.session_state.execution_trace), language="text")

        st.write("### Ausgabe")
        if st.session_state.execution_output:
            st.success(f"OUT-Register: {', '.join(format_number(x, 2) for x in st.session_state.execution_output)}")
        else:
            st.info("Kein OUT-Befehl ausgeführt (oder Ergebnisliste leer).")

        st.write("### Finaler Akkumulator & Datenspeicher")
        st.metric("Akkumulator (ACC)", format_number(st.session_state.final_acc, 2))
        st.write(pd.DataFrame(st.session_state.after_memory.items(), columns=["Adresse", "Wert"]))

        st.markdown(
            """
            <div class="story-card">
                <strong>Interpretation:</strong> Ändere nur eine Instruktion oder tausche Datenwerte aus – sofort reagiert die Maschine anders.
                Genau so zeigt sich das Von-Neumann-Prinzip in der Praxis.
            </div>
            """,
            unsafe_allow_html=True
        )

# ------------------------------------------------------------------
# Modul 4 – EVA Composer
# ------------------------------------------------------------------
elif mode == "EVA Composer":
    st.markdown(
        """
        <div class="intro-block">
            EVA steht für <strong>Eingabe – Verarbeitung – Ausgabe</strong>. 
            Im Composer stellst du neue Aufgaben zusammen, indem du ein Input-Gerät, ein Software-Skript und eine Ausgabe kombinierst. 
            Schon kleine Änderungen im Programmslot erzeugen komplett neue Szenarien – der Rechner bleibt derselbe.
        </div>
        """,
        unsafe_allow_html=True
    )

    render_cover(
        "https://images.unsplash.com/photo-1527430253228-e93688616381?auto=format&fit=crop&w=1600&q=80",
        "Der selbe Rechner, unendlich viele Einsätze – solange du den richtigen EVA-Workflow programmierst."
    )

    st.markdown(
        """
        <div class="story-card">
            Input, Processing, Output. Alle drei stehen auf einer gemeinsamen Datenbasis. 
            Von Neumann machte Programme zu Speicherinhalt – du musst nur austauschen, was im Verarbeitungsschritt passiert.
        </div>
        """,
        unsafe_allow_html=True
    )

    col_input, col_program, col_output = st.columns(3)

    input_device = col_input.selectbox(
        "Eingabequelle",
        [
            "Tastatur (Text)",
            "Sensorpaket (Temperatur & Luftfeuchte)",
            "Kamera (Bilddaten)",
            "Netzwerkpaket (JSON)"
        ]
    )

    program_logic = col_program.selectbox(
        "Programm im Speicher",
        [
            "Text-Parser (Schlüsselwörter zählen)",
            "Klima-Analyse (Taupunkt berechnen)",
            "Bildfilter (Kanten hervorheben)",
            "API-Mapper (Daten strukturieren)"
        ]
    )

    output_device = col_output.selectbox(
        "Ausgabe",
        [
            "Konsole / Terminal",
            "Dashboard-Widget",
            "Motorsteuerung",
            "Push-Nachricht aufs Smartphone"
        ]
    )

    st.write("---")
    st.write("### EVA-Skript Synthese")

    eva_steps = [
        ("Eingabe", input_device),
        ("Verarbeitung", program_logic),
        ("Ausgabe", output_device)
    ]

    eva_df = pd.DataFrame(eva_steps, columns=["Phase", "Auswahl"])
    fig = px.funnel(
        eva_df,
        y="Phase",
        x=[1, 1, 1],
        text="Auswahl",
        color="Phase",
        color_discrete_sequence=["#38f9d7", "#43e7fe", "#6476ff"]
    )
    fig.update_traces(textposition="inside", textfont_size=14)
    fig.update_layout(
        height=360,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=40, r=40, t=40, b=40),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

    # Narrative Ergebnisbeschreibung
    scenario_map = {
        ("Tastatur (Text)", "Text-Parser (Schlüsselwörter zählen)", "Konsole / Terminal"):
            "Der Computer verwandelt sich in ein Analysewerkzeug für Live-Interviews. Jede Eingabe wird sofort auf Buzzwords geprüft.",
        ("Sensorpaket (Temperatur & Luftfeuchte)", "Klima-Analyse (Taupunkt berechnen)", "Dashboard-Widget"):
            "Aus dem Rechner wird eine Wetterstation: Sensorwerte gehen hinein, ein kleines Programm berechnet Taupunkt & Trend und zeigt sie im Dashboard.",
        ("Kamera (Bilddaten)", "Bildfilter (Kanten hervorheben)", "Motorsteuerung"):
            "In der Fertigungskette erkennt der Rechner Kanten und leitet den Roboterarm – reine Software entscheidet, welche Werkstücke sortiert werden.",
        ("Netzwerkpaket (JSON)", "API-Mapper (Daten strukturieren)", "Push-Nachricht aufs Smartphone"):
            "Der Rechner wird zur Benachrichtigungszentrale: API-Daten kommen rein, das Programm filtert die relevanten Felder und schickt Alerts."
    }

    scenario = scenario_map.get((input_device, program_logic, output_device),
                                "Neue Kombination – der Rechner erfüllt eine völlig andere Rolle, ohne dass du ihn neu verkabeln musst.")

    st.markdown(
        f"""
        <div class="story-card">
            <h4>Dein EVA-Setup</h4>
            <p>{scenario}</p>
            <p><span class="highlight">Takeaway:</span> Ändert sich nur der Programmslot, ändert sich das Verhalten des gesamten Systems. 
            Genau das ist der revolutionäre Gedanke hinter Von Neumann.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("### Datenwege & Taktung justieren")
    bus_width = st.slider("Busbreite (Bit)", 4, 128, 32, step=4)
    memory_latency = st.slider("Speicherzugriffszeit (ns)", 5, 500, 80, step=5)
    instruction_size = st.select_slider("Instruktionswortgröße (Bit)", [8, 16, 24, 32, 48, 64], value=16)

    bandwidth = (bus_width / instruction_size) * (1_000 / memory_latency)
    st.metric("Maximale Instruktionen pro µs", format_number(bandwidth, 2))
    st.caption("Busbreite + Speicherlatenz bestimmen, wie schnell neue Instruktionen in die CPU gelangen – ein Hinweis auf den Von-Neumann-Bottleneck.")

# ------------------------------------------------------------------
# Abschluss
# ------------------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div class="footer">
        Von-Neumann-Rechner leben davon, dass Programme nur Speicherinhalte sind. 
        Sobald du den Code austauschst, erfindet sich die Maschine neu – ohne einen einzigen Schraubenschlüssel.
    </div>
    """,
    unsafe_allow_html=True
)
