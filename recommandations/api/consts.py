#!/usr/bin/python3
# -*- coding: utf-8 -*-

DEFAULT_CONFIG = "resources/default.ini"
SCHEMA_PS_FILE = "resources/grammar/grammar_v3.schema.json"
DATA_PATH = "data/"
REP_SP = DATA_PATH + "PS/"


inverse_relations = {'isComposedOf': 'composes',
                     'comprises': 'isComprisedIn',
                     'hasKnowledge': 'isKnowledgeOf',
                     'hasLearning': 'isLearningOf',
                     'isSkillOf': 'hasSkill',
                     'hasTraining': 'isTrainingOf',
                     'isComplexifiedBy': 'isComplexificationOf',
                     'isLeverOfUnderstandingOf': 'isUnderstoodBy',
                     'isRequiredBy': 'requires',
                     'composes': 'isComposedOf',
                     'isComprisedIn': 'comprises',
                     'isKnowledgeOf': 'hasKnowledge',
                     'isLearningOf': 'hasLearning',
                     'hasSkill': 'isSkillOf',
                     'isTrainingOf': 'hasTraining',
                     'isComplexificationOf': 'isComplexifiedBy',
                     'isUnderstoodBy': 'isLeverOfUnderstandingOf',
                     'requires': 'isRequiredBy'}
