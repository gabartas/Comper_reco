#!/usr/bin/python3
# -*- coding: utf-8 -*-

from defusedxml import minidom

from recommandations.referential.referential import (
    Node, Referential, referentiel_relations_inv_duplicate)


# parsing du référentiel
def parseNode(node):
    classe = node.getElementsByTagName(
        "Class")[0].getAttribute("IRI").split("#")[1]
    name = node.getElementsByTagName("NamedIndividual")[
        0].getAttribute("IRI").split("#")[1]
    isRacine = (classe == "framework")

    classe = classe.replace("Skills", "Skill")
    classe = classe.replace("framework", "Framework")
    return (classe, name, isRacine)


def parseRel(rel, name_to_id):
    name = rel.getElementsByTagName("ObjectProperty")[
        0].getAttribute("IRI").split("#")[1]
    nodefromId = name_to_id[rel.getElementsByTagName(
        "NamedIndividual")[0].getAttribute("IRI").split("#")[1]]
    nodetoId = name_to_id[rel.getElementsByTagName(
        "NamedIndividual")[1].getAttribute("IRI").split("#")[1]]

    return (name, nodefromId, nodetoId)


def parseInvRels(inv_rel):
    rel = inv_rel.getElementsByTagName("ObjectProperty")[
        0].getAttribute("IRI").split("#")[1]
    inv = inv_rel.getElementsByTagName("ObjectProperty")[
        1].getAttribute("IRI").split("#")[1]

    return (rel, inv)


def readReferentialXML(referentiel_file):
    # recuperation du référentiel xml

    document = minidom.parse(referentiel_file)

    nodes = document.getElementsByTagName("ClassAssertion")
    rels = document.getElementsByTagName("ObjectPropertyAssertion")
    inv_rels = document.getElementsByTagName("InverseObjectProperties")

    # on recupere la classe et le nom des noeuds sauf le framework en les triant par "Competency" puis "Knowledge" puis "Skill"
    nodes_data = sorted([parseNode(n) for n in nodes])

    # on en fait un dico pour attribuer un id
    # pour object referentiel
    nodes_ref = {i + 1: nodes_data[i] for i in range(len(nodes_data))}

    name_to_id = {n[1]: k for k, n in nodes_ref.items()}  # pour les rels
    # on recupere les données et relations en convertissant le nom en id
    rels_ref = [parseRel(rel, name_to_id) for rel in rels]

    # on recupère les relations inverses
    inv_rels_ref = {parseInvRels(inv_rel)[0]: parseInvRels(inv_rel)[
        1] for inv_rel in inv_rels}

    return nodes_ref, rels_ref, inv_rels_ref


def importReferential(referentiel_file, name):
    # lecture du referentiel
    nodes_ref, rels_ref, inv_rels_ref = readReferentialXML(referentiel_file)
    inv_rels_ref = referentiel_relations_inv_duplicate(inv_rels_ref)

    # creation du référentiel
    referentiel = Referential(name, inv_rels_ref)

    # nodes_ref traitement
    for id_n, (classe, name, isRacine) in nodes_ref.items():
        referentiel.add_node(Node(id_n, name, classe))
        if isRacine:
            referentiel.setRacine(id_n)

    # rels_ref traitement
    for (name, nodefromId, nodetoId) in rels_ref:
        referentiel.add_link(nodefromId, nodetoId, name)

    return referentiel
