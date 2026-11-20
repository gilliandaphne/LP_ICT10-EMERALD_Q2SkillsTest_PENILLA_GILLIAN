from pyscript import document

non_metals = {
    "H": ("Hydrogen",1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.904),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222),
}


def checknm(event):
    symbol = document.getElementById("Input").value.strip()
    symbol = symbol[:1].upper() + symbol[1:].lower()

    element = non_metals.get(symbol)

    if element is None:
        document.getElementById("result").innerHTML = (
            f"<b>Symbol:</b> {symbol or '(empty)'}<br>"
            "<b>Element:</b> Element not found"
        )
        return

    element_name, atomic_number, atomic_mass = element

    document.getElementById("result").innerHTML = f"""
        <b>Symbol:</b> {symbol}<br>
        <b>Element:</b> {element_name}<br>
        <b>Atomic Number:</b> {atomic_number}<br>
        <b>Atomic Mass:</b> {atomic_mass}
    """
