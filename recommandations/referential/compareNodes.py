#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .referential import Node


def sortCompetenciesByMastery_KnownANDTrust_Id(node1: Node, node2: Node):
    # >0 --> node 1 > node 2
    # 0  --> node 1 == node 2
    # <0 --> node 1 < node 2
    # infos node1

    id_1 = node1.getId()
    print(id_1)
    mastery_1, trust_1, cover_1 = node1.getData()

    # infos node2
    id_2 = node2.getId()
    print(id_2)
    mastery_2, trust_2, cover_2 = node2.getData()

    # compare
    # mastery : non, peu, part, full, unknown
    if (trust_1 == 0 and trust_2 == 0) or (mastery_1 == mastery_2):
        return 0
    elif (trust_1 > 0 and trust_2 == 0) or (trust_1 > 0 and trust_2 > 0 and mastery_1 > mastery_2):
        return (1.0 - mastery_1)  # less mastery more important
    else:
        # less mastery more important but negative value
        return -(1.0 - mastery_2)


def sortCompetenciesById(node1: Node, node2: Node):
    # infos node1
    id_1 = node1.getId()

    # infos node2
    id_2 = node2.getId()

    # compare
    if id_1 < id_2:
        return -1
    elif id_1 > id_2:
        return 1
    else:
        return 0
