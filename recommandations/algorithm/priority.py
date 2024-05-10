#!/usr/bin/python3
# -*- coding: utf-8 -*-

def weightNodeHierarchicalPart(alpha, depth_node, weight_relation, weight_father):
    return weight_relation * weight_father


def weightNodeNodePart(alpha, prioTags, intention, tag):
    max_v = max(prioTags[intention].values())

    return (max_v - prioTags[intention][tag]) / max_v
