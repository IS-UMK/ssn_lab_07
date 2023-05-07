# SSN. Lab. 7. Samoorganizacja za pomocą reguły Hebba

Zapoznaj się z zawartością notatnika Jupyter umieszczonego w repozytorium  i wykonaj zawarte w nim ćwiczenia.


Notatnik: [07_hebb.ipynb](https://github.com/IS-UMK/ssn_23_lab_07/blob/master/07_hebb.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IS-UMK/ssn_23_lab_07/blob/master/07_hebb.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IS-UMK/ssn_23_lab_07/master?filepath=07_hebb.ipynb)

---

## Zad. 7. Ogólny algorytm Hebbowski (GHA)


Zaimplementuj sieć jednowarstwową realizującą rozkład na czynniki główne za pomocą ogólnego algorytmu hebbowsiego (GHA).  

**Algorytm GHA**  
Parametry początkowe:
* $N$ ilość epok
* $k$ ilość neuronów (komponentów)
* $\eta$ wartość kroku uczenia

1. Zainicjuj macierz wag $\mathbf{W}$ 
2. Powtarzaj $N$ razy:
3. <ul>Dla każdego $\mathbf{x}$ ze zbioru treningowego wykonaj</ul>
4. <ul><ul> wyznacz <br>

$$\mathbf{y} = \mathbf{W}\mathbf{x}$$
 </ul></ul>
5. <ul><ul>zaktualizuj wagi <br> 

$$\Delta W=\eta \left(\mathbf{y} \cdot \mathbf{x}^T-\mathrm{LT}\left[\mathbf{y} \cdot \mathbf{y}^T\right] \mathbf{W}\right)$$
</ul></ul>
gdzie iloczyn $\mathbf{a}\cdot \mathbf{b}^T$ oznacza iloczyn zewnętrzny, a funkcja $\mathrm{LT}[\mathbf{A}]$ ustawia wszystkie elementy macierzy $\mathbf{A}$ powyżej przekątnej na 0.

Przydatne funkcje:
* iloczyn zewnętrzny można wyznaczyć za pomocą funkcji [numpy.outer(a,b)](https://numpy.org/doc/stable/reference/generated/numpy.outer.html),
* funkcja [numpy.tril(x)](https://numpy.org/doc/stable/reference/generated/numpy.tril.html) zeruje wartości powyżej diagonali macierzy.

Wykorzystaj algorytm GHA do wyznaczenia $k > 1$ czynników głównych dla danych MNIST. W celu przyspieszenia działania wybierz do 1000 losowych przypadków ze zbioru cyfr. Dla wytrenowanego modelu wykonaj:
* przetransformuj dane treningowe do $k$ wymiarowj przestrzeni
* zrekonstruuj zbiór treningowy przez transformację odwrotną i zaprezentuj rekonstrukcję przykładowych cyfr w postaci obrazu 28x28
* przedstaw wizualizację wektorów własnych cyfr (obraz wag w postaci obrazów 28x28)
* przedstaw wykres rozrzutu prezentujący rozkład danych MNIST dla dwóch pierwszych składowych PC. Wyróżnij klasy różnymi kolorami. 

Dane MNIST zawierają 70K obrazków cyfr o wymiarach 28x28 (784 pikseli) i można je zaimportować w następujący sposób
```python
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', data_home='./dane/', parser='auto')
X = mnist.data.values
target = mnist.target.values
```



Rozwiązanie w postaci notatnika Jupyter (``.ipynb``) lub skrypt w języku Python (``.py``) umieść w Moodle lub prześlij do repozytorium GitHub.

---
## Materiały:
* [Generalized Hebbian algorithm](https://en.wikipedia.org/wiki/Generalized_Hebbian_algorithm), Wikipedia




