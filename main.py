from manim import *

class Aufgabe9Berechnung(Scene):
    def construct(self):
        # Schritt 1: Aufgabe darstellen
        aufgabe_text = Text("Aufgabe 9: Beryllium und Schwefel reagieren zu Berylliumsulfid").scale(0.7)
        self.play(Write(aufgabe_text))
        self.wait(2)
        
        # Schritt 2: Reaktionsgleichung darstellen
        reaktionsgleichung = Tex("Be + S \\rightarrow BeS").scale(0.9).next_to(aufgabe_text, DOWN)
        self.play(Write(reaktionsgleichung))
        self.wait(2)

        # Schritt 3: Atommasse von Beryllium erklären
        mol_berechnung = Tex("1 Mol Beryllium (Be) = 9{,}01 \\text{ g}").scale(0.8).next_to(reaktionsgleichung, DOWN)
        self.play(Write(mol_berechnung))
        self.wait(2)
        
        # Schritt 4: Beryllium-Menge berechnen
        beryllium_menge = Tex("90 \\text{ g} \\text{ Beryllium} \\Rightarrow \\frac{90}{9{,}01} = 9{,}99 \\text{ mol}").scale(0.8).next_to(mol_berechnung, DOWN)
        self.play(Write(beryllium_menge))
        self.wait(2)

        # Schritt 5: Schwefel-Bedarf berechnen
        schwefel_bedarf = Tex("1 Mol Schwefel (S) = 32{,}07 \\text{ g}").scale(0.8).next_to(beryllium_menge, DOWN)
        schwefel_bedarf_menge = Tex("9{,}99 \\text{ mol S} \\times 32{,}07 = 320{,}37 \\text{ g Schwefel}").scale(0.8).next_to(schwefel_bedarf, DOWN)
        self.play(Write(schwefel_bedarf))
        self.play(Write(schwefel_bedarf_menge))
        self.wait(2)

        # Schritt 6: Ergebnis anzeigen
        ergebnis = Text("Ergebnis: Für 90 g Beryllium benötigen wir 320,37 g Schwefel.").scale(0.7).next_to(schwefel_bedarf_menge, DOWN)
        self.play(Write(ergebnis))
        self.wait(3)

        # Szene abschließen
        self.play(FadeOut(aufgabe_text), FadeOut(reaktionsgleichung), FadeOut(mol_berechnung), FadeOut(beryllium_menge), FadeOut(schwefel_bedarf), FadeOut(schwefel_bedarf_menge), FadeOut(ergebnis))
