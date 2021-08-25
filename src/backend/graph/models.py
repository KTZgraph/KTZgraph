from django.db import models


class Graph(models.Model):
    # czy graf całkowity

    # czy spójny https://mathworld.wolfram.com/ConnectedGraph.html
    is_connected = models.BooleanField(default=False)
    # czy graf pełny https://mathworld.wolfram.com/CompleteGraph.html
    is_complete = models.BooleanField(default=False)

    # czy cykliczny C4, C6, https://en.wikipedia.org/wiki/Cycle_graph
    is_cycle = models.BooleanField(default=False)
    is_tree = models.BooleanField(default=False)

    # czy graf PST
    is_PST = models.BooleanField(default=False)

    # r regularność https://inf.ug.edu.pl/~hanna/grafy/ATG_W01b.pdf str 6

    # graf dswudzielny
    is_bipartite = models.BooleanField(default=False)

    # graf k dzielny
    is_multipartite = models.BooleanField(default=False)

    # czy gwiazda np. K1,4 https://en.wikipedia.org/wiki/Star_(graph_theory)
    is_star = models.BooleanField(default=False)

    # czy ścieżka np P2, P3 https://en.wikipedia.org/wiki/Path_graph
    is_path = models.BooleanField(default=False)

    # https://pl.wikipedia.org/wiki/Graf_hamiltonowski https://pl.wikipedia.org/wiki/Twierdzenie_Diraca https://pl.wikipedia.org/wiki/Twierdzenie_Bondy%E2%80%99ego-Chv%C3%A1tala
    is_hamiltonian = models.BooleanField(default=False)

    # liczba wierzchołków
    # liczba krawędzi
    # liczba składowych
    # największy stopień wierzchołka
    # rząd cykliczności
    # rząd rozciecia
    # najkrótsza droga
    # kolorowanie wierzchołków
    # las spinający
    # łańcuch Eulera
    # cykl Eulera
    # cykl Hamiltona
    # Twierdzenie Orego


class AdjacencyMatrix(models.Model):
    """Macierz sąsiedztwa https://en.wikipedia.org/wiki/Adjacency_matrix"""
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE, related_name='adjacency_matrix')
    matrix = models.TextField() #macierz kwadratowa


class IncidenceMatrix(models.Model):
    """Macierz incydencji https://en.wikipedia.org/wiki/Incidence_matrix"""
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE, related_name='incidence_matrix')
    matrix = models.TextField() #macierz prostokątna