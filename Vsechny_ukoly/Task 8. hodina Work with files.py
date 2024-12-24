def analyzuj_text(vstupni_soubor, vystupni_soubor):

    try:

        with open(vstupni_soubor, "r", encoding="utf-8") as soubor:
            obsah = soubor.read()

        pocet_znaku = len(obsah)


        pocet_radku = obsah.count("\n") + 1  # Každý nový řádek plus poslední


        samohlásky = "aeiouyáéíóúůě"
        pocet_samohlasek = sum(1 for znak in obsah.lower() if znak in samohlásky)

        souhlásky = "bcdfghjklmnpqrstvwxyzčďňřšťž"
        pocet_souhlasek = sum(1 for znak in obsah.lower() if znak in souhlásky)

        pocet_cisel = sum(1 for znak in obsah if znak.isdigit())


        with open(vystupni_soubor, "w", encoding="utf-8") as vystup:
            vystup.write(f"Počet znaků: {pocet_znaku}\n")
            vystup.write(f"Počet řádků: {pocet_radku}\n")
            vystup.write(f"Počet samohlásek: {pocet_samohlasek}\n")
            vystup.write(f"Počet souhlásek: {pocet_souhlasek}\n")
            vystup.write(f"Počet číslic: {pocet_cisel}\n")

        print("Analýza dokončena. Statistiky byly zapsány do souboru:", vystupni_soubor)

    except FileNotFoundError:
        print("Vstupní soubor nebyl nalezen.")
    except Exception as chyba:
        print("Došlo k chybě:", chyba)

analyzuj_text("zdrojovy_soubor.txt", "statistiky_souboru.txt")
