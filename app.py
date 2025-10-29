import streamlit as st

# ------------------------------------------------------
# Grundkonfiguration
# ------------------------------------------------------
st.set_page_config(
    page_title="Von-Neumann-Küche",
    page_icon="🍲",
    layout="wide"
)

st.markdown(
    """
    <style>
        body {background: #0f172a; color: #e2e8f0;}
        .block-container {padding-top: 2rem; padding-bottom: 2rem; max-width: 1100px;}
        h1, h2, h3 {color: #f8fafc;}
        .info-box {
            background: rgba(15, 118, 110, 0.18);
            border-radius: 14px;
            padding: 1.1rem 1.4rem;
            margin-bottom: 1rem;
        }
        .note-box {
            background: rgba(79, 70, 229, 0.16);
            border-radius: 14px;
            padding: 1.1rem 1.4rem;
            margin-top: 1rem;
        }
        .metric-box {
            background: rgba(15, 23, 42, 0.8);
            border-radius: 14px;
            padding: 0.9rem 1.2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------
# Einstieg
# ------------------------------------------------------
st.title("🍲 Die Von-Neumann-Küche")
st.subheader("Computer verstehen – so einfach wie Kochen nach Rezept")

st.write(
    """
    Stell dir deinen Computer als Großküche vor.  
    • **Der Prozessor** ist der Chefkoch.  
    • **Der Hauptspeicher** ist die Vorratskammer.  
    • **Das Programm** ist das Rezept.  
    • **Eingabe/Ausgabe** sind die Lieferanten und Gäste.  
    Das Von-Neumann-Prinzip sagt: Solange der Chefkoch ein neues Rezept in der
    Vorratskammer findet, kann er ein völlig neues Gericht zaubern – ohne dass wir die Küche umbauen müssen.
    """
)

tabs = st.tabs([
    "1️⃣ Mannschaft & Räume",
    "2️⃣ Der Kochablauf",
    "3️⃣ Rezept wechseln",
    "4️⃣ Wo es hakt"
])

# ------------------------------------------------------
# Tab 1 – Mannschaft & Räume
# ------------------------------------------------------
with tabs[0]:
    st.header("Die Mannschaft & die Räume der Von-Neumann-Küche")

    st.write(
        """
        Wähle eine Rolle aus und lies, wie sie in unserer Küchen-Metapher funktioniert.
        """
    )

    komponenten = {
        "Chefkoch (CPU)": {
            "bild": "👨‍🍳",
            "beschreibung": (
                "Der Chefkoch liest das Rezept Zeile für Zeile, entscheidet welcher Kochtopf dran ist "
                "und rührt, schneidet oder kostet. Er interpretiert also die Befehle und führt sie aus."
            ),
            "schritte": [
                "nimmt den nächsten Schritt aus dem Rezept",
                "holt die benötigten Zutaten aus der Vorratskammer",
                "führt die Aktion aus (mischen, erhitzen, servieren)"
            ]
        },
        "Vorratskammer (Hauptspeicher)": {
            "bild": "🧺",
            "beschreibung": (
                "Hier liegen Zutaten *und* Rezepte nebeneinander. Das ist der Trick: Tauschen wir das Rezept aus, "
                "kocht der Chef automatisch etwas anderes – die Küche bleibt die gleiche."
            ),
            "schritte": [
                "lagert frische Zutaten",
                "bewahrt Rezepte auf",
                "liefert auf Zuruf genau die richtige Menge"
            ]
        },
        "Lieferanten & Gäste (Ein-/Ausgabe)": {
            "bild": "🚚",
            "beschreibung": (
                "Lieferanten bringen neue Zutaten (z. B. Tastatureingaben). Gäste bekommen das fertige Essen "
                "(z. B. Bildschirm-Ausgabe). Ohne sie wäre die Küche sinnlos."
            ),
            "schritte": [
                "Lieferwagen bringt Zutaten (Eingabe)",
                "Küche verarbeitet alles",
                "Gäste bekommen das Gericht (Ausgabe)"
            ]
        },
        "Laufwege & Küchenhilfen (Datenbusse)": {
            "bild": "🛒",
            "beschreibung": (
                "Zwischen Vorratskammer und Herd helfen Laufwege und Küchenhilfen, alles schnell zu transportieren. "
                "In Computern übernehmen das Daten- und Adressbusse."
            ),
            "schritte": [
                "Küchenhilfe holt die Zutatentüte",
                "trägt sie zum Herd",
                "bringt fertige Zutaten zurück ins Regal"
            ]
        }
    }

    auswahl = st.radio(
        "Welche Rolle möchtest du genauer betrachten?",
        list(komponenten.keys()),
        horizontal=True
    )

    info = komponenten[auswahl]
    st.markdown(f"### {info['bild']} {auswahl}")
    st.write(info["beschreibung"])
    st.write("Typischer Ablauf:")
    for nummer, punkt in enumerate(info["schritte"], start=1):
        st.write(f"• Schritt {nummer}: {punkt}")

    st.markdown(
        """
        <div class='note-box'>
            **Merke:** Rezepte (Programme) und Zutaten (Daten) liegen am gleichen Ort. Deswegen kann ein Computer jederzeit
            umprogrammiert werden. Wir müssen nur ein anderes Rezept in die Vorratskammer legen.
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------
# Tab 2 – Kochablauf (Fetch–Decode–Execute)
# ------------------------------------------------------
with tabs[1]:
    st.header("Der Kochablauf: Vom Rezept zur fertigen Mahlzeit")

    st.write(
        """
        Jeder Befehl durchläuft dieselbe kurze Tour. Du kannst hier Schritt für Schritt erleben, was der Chefkoch macht.
        """
    )

    schritte = [
        {
            "titel": "1. Rezeptzeile holen (Fetch)",
            "text": "Der Chefkoch liest die nächste Zeile aus dem Rezept in der Vorratskammer."
        },
        {
            "titel": "2. Verstehen (Decode)",
            "text": "Er interpretiert, was zu tun ist: schneiden, erhitzen, würzen?"
        },
        {
            "titel": "3. Ausführen (Execute)",
            "text": "Er tut genau das – holt Zutaten, stellt den Herd an, rührt."
        },
        {
            "titel": "4. Aufräumen & weiterblättern",
            "text": "Das Ergebnis landet in der Schüssel, der Koch schaut in die nächste Zeile."
        }
    ]

    aktueller_schritt = st.slider(
        "Welchen Abschnitt möchtest du ansehen?",
        min_value=1,
        max_value=len(schritte),
        value=1
    )

    daten = schritte[aktueller_schritt - 1]
    st.subheader(daten["titel"])
    st.write(daten["text"])

    st.markdown(
        """
        <div class='info-box'>
            Sobald im Regal ein neues Rezept liegt, läuft der gleiche Ablauf – nur mit anderen Handgriffen. <br>
            Genau deshalb ist ein Computer flexibel programmierbar.
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------
# Tab 3 – Rezept wechseln (Programm = Daten)
# ------------------------------------------------------
with tabs[2]:
    st.header("Selbst ausprobieren: Rezept tauschen, Gericht tauschen")

    st.write(
        """
        Unten gibst du Werte ein. Dann wählst du ein „Rezept“, also ein kleines Programm.
        Beobachte, wie sich das Ergebnis verändert – ganz ohne neue Hardware.
        """
    )

    zahl_a = st.number_input("Zutat A (erste Zahl)", value=4.0)
    zahl_b = st.number_input("Zutat B (zweite Zahl)", value=2.0)
    rezept = st.selectbox(
        "Welches Rezept (Programm) soll der Chefkoch nutzen?",
        [
            "Addieren (Suppe mischen)",
            "Multiplizieren (Teig aufgehen lassen)",
            "Durchschnitt bilden (Smoothie mixen)",
            "Größere Zahl finden (welches Glas ist voller?)"
        ]
    )

    if rezept == "Addieren (Suppe mischen)":
        ergebnis = zahl_a + zahl_b
        beschreibung = "Der Koch schüttet beide Zutaten zusammen. Mehr wird es durch Addition."
    elif rezept == "Multiplizieren (Teig aufgehen lassen)":
        ergebnis = zahl_a * zahl_b
        beschreibung = "Hier verstärkt sich alles gegenseitig – wie Hefeteig, der aufgeht."
    elif rezept == "Durchschnitt bilden (Smoothie mixen)":
        ergebnis = (zahl_a + zahl_b) / 2
        beschreibung = "Beide Zutaten werden komplett durchmischt, am Ende schmeckt es nach der Mitte."
    else:
        ergebnis = max(zahl_a, zahl_b)
        beschreibung = "Der Koch hält zwei Gläser gegen das Licht und serviert das vollere."

    st.markdown(
        f"""
        <div class='metric-box'>
            <strong>Ergebnis:</strong> {ergebnis:.2f} <br>
            <strong>Was passiert ist:</strong> {beschreibung}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='note-box'>
            Stell dir vor, du würdest oben statt „Addieren“ plötzlich „Multiplizieren“ wählen.
            Der gleiche Computer, die gleiche Küche – aber ein völlig anderes Ergebnis.  
            Das ist die Kernidee des Von-Neumann-Prinzips.
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------
# Tab 4 – Wo es hakt (Von-Neumann-Bottleneck)
# ------------------------------------------------------
with tabs[3]:
    st.header("Wenn der Chef warten muss: Der Von-Neumann-Flaschenhals")

    st.write(
        """
        Manchmal dauert es länger, bis die Vorratskammer Zutaten liefert. Dann steht der Koch herum.
        Das passiert auch im Computer: Der Prozessor wartet auf Daten aus dem Speicher.
        """
    )

    chef_tempo = st.slider("Geschwindigkeit des Chefkochs (Arbeitsschritte pro Minute)", 10, 200, 120)
    lager_tempo = st.slider("Liefergeschwindigkeit der Vorratskammer (Zutaten pro Minute)", 10, 200, 80)

    if lager_tempo >= chef_tempo:
        auslastung = 100
    else:
        auslastung = int(lager_tempo / chef_tempo * 100)

    st.metric("Der Koch ist beschäftigt zu", f"{auslastung} %")
    st.write(
        "Wenn die Vorratskammer langsamer ist, steht der Koch herum. "
        "In Computern heißt das: Der Speicher limitiert die CPU. "
        "Lösungen heißen z. B. Caches (kleine Zwischenlager) oder zwei getrennte Vorratskammern "
        "(Harvard-Architektur)."
    )

# ------------------------------------------------------
# Abschluss
# ------------------------------------------------------
st.markdown("---")
st.success(
    "Zusammenfassung: Ein Computer ist wie eine flexible Küche. Solange wir neue Rezepte in den Speicher legen, kann "
    "der gleiche Chefkoch neue Gerichte zubereiten. Das ist das Von-Neumann-Prinzip."
)
