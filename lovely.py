from flask import Flask

app = Flask(__name__)

class WarqadJacayl:
    def __init__(self):
        self.diray = "Aniga"
        self.qaata = "Adiga"
        self.dareen = "aan dhammaad lahayn"
        self.xaalad = "si waalan kuu jecel ❤️"

    def muujin(self):
        return f"""
        <pre>
Boqorkayga {self.qaata},

Markii aan ku arkay, qalbigaygu wuxuu qaaday calan —
Boolean noqday True oo aan weligiis False noqonin.

Adigu waad tahay error-kii aanan rabin in aan qabto,
Bug aan diyaar u ahay in aan nolosheyda oo dhan xalliyo,
Loop aan jeclahay in aan marnaba joojin.

Dhoolla-caddayntaadu waa syntax-ka aan ugu jecelahay,
Joogitaankaaguna si qurux badan buu u compile-gareeyaa noloshayda.

Haddii aan list ka sameeyo dhammaan waxyaabaha aan jeclahay...
Adigu waxaad noqon lahayd midka kaliya ee ku jira.

Adigoo ila jooga, daqiiqad walba waa si fiican loo indent gareeyey,
Nolosheyduna waxay ku jirtaa block-keeda saxda ah.

Si joogto ah waxa kuu leh,
{self.diray} 🐍
        </pre>
        """

@app.route('/')
def show_love():
    warqad = WarqadJacayl()
    return warqad.muujin()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
