#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from ..priority import *

import datetime #to remove after logs ok

def initialisationSelectionProcedure(init_param, current_obj, weight_r, alpha, modules, f):
	node_obj = current_obj.getNode()
	intention_obj = current_obj.getIntention()
	path_obj = current_obj.getPath()

	init_relations_to_follow = init_param["relations_to_follow"]
	profondeur_max = init_param["depth_max"]

	f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+modules+"[initialisation][parameters] init_relations_to_follow = "+str(init_relations_to_follow)+"\n")
	f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+modules+"[initialisation][parameters] profondeur_max = "+str(profondeur_max)+"\n")

	A_TRAITER = [{"node": node_obj, \
				  "Weight": node_obj.getWeight(), \
				  "profondeur": 0, \
				  "relationFromFather" : None, \
				  "father": None, \
				  "path": path_obj \
				  }]

	if init_relations_to_follow != []:
		listNodeParcours = [{"node": node_obj, "profondeur": 0, "relation": None, "path": path_obj}]

		id_list = [node_obj.getId()]

		while len(listNodeParcours) != 0:
			data = listNodeParcours.pop(0)
			
			node = data["node"]
			path = data["path"]
			profondeur_node = data["profondeur"]
			
			f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+modules+"[initialisation][node] Followed "+str({"node": (node.getId(), node.getName())})+"\n")
			for relation in init_relations_to_follow:
				for descendant in node.getDescendants(relation):
					#priorité des descendants
					p = weightNodeHierarchicalPart(alpha, profondeur_node+1, weight_r[relation], node.getWeight())
					descendant.setWeight(p)
					f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+modules+"[initialisation][node][weight] "+str({"node": (descendant.getId(), descendant.getName()), "alpha": alpha, "depth": profondeur_node+1, "weight_r": weight_r[relation], "weight_father": node.getWeight(), "Weight_node": p})+"\n")
					
					if descendant.getId() not in id_list:
						id_list.append(descendant.getId())
						new_path = list(path)
						new_path.append([(descendant.getId(), descendant.getName()), relation])
						new_A_TRAITER = {"node": descendant, \
										 "Weight": descendant.getWeight(), \
										 "profondeur": profondeur_node+1, \
										 "relationFromFather": relation, \
										 "father": node, \
										 "path": new_path \
										}
						f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+modules+"[initialisation][node] Added "+str({"node": (descendant.getId(), descendant.getName()), \
																																						  "weight": descendant.getWeight(), \
																																						  "depth": profondeur_node+1, \
																																						  "relation": relation, \
																																						  "father": (node.getId(), node.getName()), \
																																						  "path": new_path })+"\n")
						A_TRAITER.append(new_A_TRAITER)
					 
						if profondeur_max == 0 or profondeur+1 <= profondeur_max:
							new_path = list(path)
							new_path.append([(descendant.getId(), descendant.getName()), relation])
							listNodeParcours.append({"node": descendant, \
													 "profondeur": profondeur_node+1, \
													 "relation": relation, \
													 "path": new_path \
													})
	
	for data in A_TRAITER:
		f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f")+modules+"[initialisation][output] "+str({"node": (data["node"].getId(), data["node"].getName()), \
																																	  "weight": data["node"].getWeight(), \
																																	  "depth": data["profondeur"], \
																																	  "relation": data["relationFromFather"], \
																																	  "father": (data["father"].getId(), data["father"].getName()) \
																																	  			if data["father"] != None \
																																	  			else (None, None), \
																																	  "path": data["path"] \
																																	})+"\n")
	
	return A_TRAITER