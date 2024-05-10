#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from ..priority import *

sys.path.append("../..")
from referential import Objectif
import datetime #to remove after logs ok

from ..priority import *
from ..logs import *

def traitementSelectionProcedure(traitement_param, selection_rules, current_obj, CIBLES, referentiel, objectifs, SELECTED_NODES, errors, alpha, prioTags, intention_obj_init, modules, f):
	node_obj = current_obj.getNode()
	intention_obj = current_obj.getIntention()

	for data in CIBLES:
		node = data["node"]
		Weight_node = data["Weight"]
		profondeur_node = data["profondeur"]
		relationFather = data["relationFromFather"]
		father = data["father"]
		path = data["path"]

		a_ete_traiter = False
		for r in selection_rules:
			if r.getCondition().evaluate(node):
				f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+modules+"[treatment]["+r.getId()+"]"+str({"node": (node.getId(), node.getName())})+"\n")
				a_ete_traiter = True

				#APPLICATION de la règle
				selection_part = r.getSelectionParameters()
				recursion_part = r.getRecursionParameters()

				#sélection du noeud
				if selection_part["isSelected"]:
					for tag in selection_part["tagSelection"]:
						f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+modules+"[treatment]["+r.getId()+"][selection]"+str({"node": (node.getId(), node.getName()), "weight": node.getWeight(), "tag": tag, "path": path})+"\n")
						SELECTED_NODES.append((node, \
											  tag, \
											  node.getWeight(), \
											  path \
											))
					tag_for_prio = selection_part["tagSelection"][0]
					#on ajoute f_node
					p_expert = weightNodeNodePart(alpha, prioTags, intention_obj_init, tag_for_prio)
					p = (1.0-alpha) * node.getWeight() + alpha * p_expert
					f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+modules+"[treatment]["+r.getId()+"][weight]"+str({"node": (node.getId(), node.getName()), "hierachical_part": node.getWeight(), "alpha": alpha, "node_part": p_expert, "weight_node": p})+"\n")
					node.setWeight(p)

				#récursion du noeud
				if recursion_part["hasRecursion"]:
					f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+modules+"[treatment]["+r.getId()+"][recursion]"+str({"node": (node.getId(), node.getName()), "intention": recursion_part["intention"]})+"\n")
					
					for intention in recursion_part["intention"]:
						new_obj = Objectif(referentiel, node, intention)
						new_obj.setPath(path)
						objectifs.append(new_obj)

		if not a_ete_traiter:
			f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+modules+"[treatment] No selection rules applicable for this node"+"\n")

	return objectifs, SELECTED_NODES, errors