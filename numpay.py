import numpy as np
import matplotlib.pyplot as plt
import numpy_financial as npf

# Parametry
cena_poczatkowa = 120000
stopa_wzrostu = 0.05
cena_celowa = 153150.63
stopa_procentowa = 0.12
kapitalizacja = 12
okres = 5

# Czas w miesiącach
misiace = np.arange(1, okres * kapitalizacja + 1)

# Wzrost wartości nieruchomości
wartosc_nieruchomosci = cena_poczatkowa * (1 + stopa_wzrostu) ** (misiace / kapitalizacja)

# Wartość lokaty w czasie
miesieczna_wplata = npf.pmt(stopa_procentowa / kapitalizacja, okres * kapitalizacja, 0, -cena_celowa)
wartosc_lokaty = npf.fv(stopa_procentowa / kapitalizacja, misiace, miesieczna_wplata, 0)

# Wykres
plt.plot(misiace, np.full_like(misiace, cena_poczatkowa), label="Cena początkowa")
plt.plot(misiace, wartosc_nieruchomosci, label="Wartość nieruchomości")
plt.plot(misiace, wartosc_lokaty, label="Wartość lokaty")
plt.legend()
plt.show()

# Wypisanie wyników
print(f"Kwota miesięcznej wpłaty: {miesieczna_wplata:.2f}")
print(f"Kwota końcowa lokaty: {wartosc_lokaty[-1]:.2f}")
print(f"Kwota końcowa nieruchomości: {wartosc_nieruchomosci[-1]:.2f}")