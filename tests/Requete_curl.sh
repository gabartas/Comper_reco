curl --location --request POST 'http://localhost:3000/api/generateFromProfile/' \
        --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiXHUwMGU5bFx1MDBlOHZlX2lkIDogMTIyMSIsInJvbGUiOiJsZWFybmVyIiwidXNlcm5hbWUiOiJcdTAwZTlsXHUwMGU4dmVfMiIsImZ3aWQiOjE1MSwib2JqZWN0aXZlcyI6W1siQ29tcHJlbmRyZV9sZXNfbW90c19ldF9ncm91cGVzX2RlX21vdHMiLCJTb3V0aWVuIl1dLCJleHAiOjE2OTY1MTYzMTIuMjMxNTc3NH0.CgvYm-1CJ2Dz0-8peangAGDH9oH47yIyCbQDkGBgHvBZ81Gwo9Bt_Lx8KjVq_Z-laTVP_fpB2_m6j9Z7VUlOgz_uW1mEge5auZ5bpyZl63zDmrThDipZkt1qnzKk2OLOxY9ico_DoMIqb1Q_q7hXdFppHrRqAVttWtJsUXOfmyItgKgzZo0DRpmCAymvmVJAmneEM4OVgCKpQvHaj3BrMOhZPP8l_gmHTTx4NHKjFa_ubjNbtIvqgKPI2AuiNBDuTh_LVxyMvA9LnGlEtWs04Mlo2rjIrt2x5afqI9mdOuMZPGglZTfvNRcEP8uV6SQ7SQtsqMzZpBXERz2XkeI33Ktru7zujof2_XmJsmgkHZzZj7CufbC0c2tRlgf8uBiOJGCJwmxA45CWS9nwIBWYIcdtFgdb5ACe1arq4VMM75F5tSXjfqaznTLim_-7Z8eT3khZC9COBdHu096axfUvtjqtlR09RKSgqdmS0YNPb0XNRtG1nBid4kAvCN7fRQmxficAS70GMu1StFeuoTAtoGscAKeq8L59TC-u8HNiDOKqgU9qW3BhbTnh8WK1Dj-pYHv6lhCFsiX2d710Q_bNdgzZPlPuEb7WBrxmijfAQ01j5izN_BXktx1A2RG9sH7mNaL5h7-pBfsdqxsom03nmijsLrEGt3a81udz-ZnkV1U' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "name": "PEAPL_PER",
            "objects": [
                {
                    "name": "Lire_des_mots_connus",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [
                            "Lire_et_comprendre_des_mots_écrits"
                        ],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Comprendre_les_mots_et_groupes_de_mots",
                    "type": "Skills",
                    "mastery": 1,
                    "trust": 0.2,
                    "cover": 0.14285714285714285,
                    "relations": {
                        "isSkillOf": [
                            "Lire_et_comprendre_des_mots_écrits"
                        ],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [
                            "Identifier_le_sens_propre",
                            "Identifier_la_valeur_d_une_préposition",
                            "Identifier_une_information_explicite",
                            "Identifier_le_sens_figuré",
                            "Comprendre_le_contexte_de_la_phrase",
                            "Identifier_un_verbe_d_état",
                            "Identifier_un_verbe_de_déplacement"
                        ],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_un_substitut_placé_avant",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_les_substituts_d_un_référent"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_une_relation_de_conséquence",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_l_ironie",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_une_information_implicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites",
                    "type": "Skills",
                    "mastery": 1,
                    "trust": 0.3000173682494222,
                    "cover": 0.14285714285714285,
                    "relations": {
                        "isSkillOf": [
                            "Lire_et_comprendre_des_phrases_écrites_(processus_d_intégration)"
                        ],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [
                            "Identifier_une_relation_logique_ou_un_raisonnement",
                            "Produire_une_disposition_spatiale",
                            "Mettre_en_relation_un_paragraphe_et_des_images_séquentielles",
                            "Produire_une_chronologie",
                            "Identifier_une_relation_de_manière",
                            "Identifier_une_relation_de_conséquence",
                            "Produire_un_déplacement_sur_un_plan_en_fonction_d_une_consigne",
                            "Identifier_une_relation_de_but",
                            "Produire_une_relation_logique_ou_un_raisonnement",
                            "Mettre_en_relation_un_paragraphe_et_une_illustration",
                            "Identifier_une_disposition_spatiale",
                            "Mettre_en_relation_un_paragraphe_et_un_schéma",
                            "Identifier_une_chronologie",
                            "Identifier_une_relation_de_cause"
                        ],
                        "requires": [
                            "Comprendre_les_mots_et_groupes_de_mots"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Comprendre_une_information_implicite",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [
                            "Lire_et_comprendre_des_phrases_écrites_(processus_d_intégration)"
                        ],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [
                            "Identifier_un_sentiment",
                            "Identifier_des_indices_dans_le_texte",
                            "Justifier_une_inférence",
                            "Identifier_une_sensation",
                            "Produire_une_inférence_pragmatique",
                            "Produire_une_inférence_logique",
                            "Identifier_l_ironie",
                            "Mettre_en_relation_informations_explicites_et_informations_externes"
                        ],
                        "requires": [
                            "Comprendre_les_mots_et_groupes_de_mots",
                            "Identifier_le_contexte_du_texte"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_une_relation_de_but",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_un_référent_placé_après",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_le_référent_d_un_substitut"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Mettre_en_relation_un_paragraphe_et_une_illustration",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_une_disposition_spatiale"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_les_substituts_d_un_référent",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_reprises_anaphoriques"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [
                            "Identifier_un_substitut_placé_après",
                            "Identifier_un_substitut_placé_avant",
                            "Identifiant_un_nom_ou_GN_substitut",
                            "Identifier_un_pronom_substitut"
                        ],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_un_élément_de_raisonnement",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_une_information_explicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": [
                            "Identifier_un_élément_de_raisonnement"
                        ]
                    }
                },
                {
                    "name": "Mettre_en_relation_un_paragraphe_et_un_schéma",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_une_relation_logique_ou_un_raisonnement",
                            "Identifier_une_chronologie"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Déchiffrer_des_mots_inconnus",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [
                            "Lire_et_comprendre_des_mots_écrits"
                        ],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_la_valeur_de_la_ponctuation",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_marques_morphosyntaxiques"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_une_chronologie",
                    "type": "Skills",
                    "mastery": 1,
                    "trust": 0.3000173682494222,
                    "cover": 1,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_les_indices_de_temps",
                            "Identifier_une_information_de_temps",
                            "identifier_un_connecteur_de_temps"
                        ],
                        "hasLearning": [],
                        "hasTraining": [
                            "GamesHub:528",
                            "GamesHub:623",
                            "GamesHub:560"
                        ],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": [
                            "Identifier_une_chronologie"
                        ]
                    }
                },
                {
                    "name": "Identifier_une_information_de_lieu",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_une_information_explicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_la_valeur_d_une_préposition",
                            "Identifier_un_verbe_de_déplacement",
                            "identifier_un_connecteur_de_lieu"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": [
                            "Identifier_une_information_de_lieu"
                        ]
                    }
                },
                {
                    "name": "Identifiant_un_nom_ou_GN_substitut",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_les_substituts_d_un_référent"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_un_référent_placé_avant",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_le_référent_d_un_substitut"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_le_sens_propre",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_mots_et_groupes_de_mots"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Définir_le_sens_propre"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": [
                            "Identifier_le_sens_propre",
                            "Identifier_le_sens_propre"
                        ]
                    }
                },
                {
                    "name": "Identifier_les_indices_de_temps",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_marques_morphosyntaxiques"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_un_verbe_d_état",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_mots_et_groupes_de_mots"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Produire_une_inférence_pragmatique",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_une_information_implicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_des_indices_dans_le_texte",
                            "Mettre_en_relation_informations_explicites_et_informations_externes"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_le_contexte_du_texte",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [
                            "Lire_et_comprendre_des_textes_écrits_(macroprocessus_et_processus_d_élaboration)"
                        ],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "identifier_un_connecteur_logique",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_une_information_explicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Justifier_une_inférence",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_une_information_implicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_la_valeur_d_une_préposition",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_mots_et_groupes_de_mots"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Produire_un_déplacement_sur_un_plan_en_fonction_d_une_consigne",
                    "type": "Skills",
                    "mastery": 1,
                    "trust": 0.3000173682494222,
                    "cover": 1,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_une_disposition_spatiale",
                            "Identifier_une_information_de_lieu"
                        ],
                        "hasLearning": [],
                        "hasTraining": [
                            "GamesHub:559",
                            "GamesHub:527",
                            "GamesHub:528",
                            "GamesHub:587",
                            "GamesHub:555",
                            "GamesHub:622",
                            "GamesHub:623",
                            "GamesHub:535",
                            "GamesHub:529",
                            "GamesHub:617",
                            "GamesHub:609",
                            "GamesHub:586",
                            "GamesHub:11",
                            "GamesHub:581",
                            "GamesHub:560"
                        ],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Produire_une_relation_logique_ou_un_raisonnement",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Connaitre_les_connecteurs_logiques"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Comprendre_le_contexte_de_la_phrase",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_mots_et_groupes_de_mots"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_une_information_explicite"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_une_disposition_spatiale",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "identifier_un_connecteur_de_lieu",
                            "Identifier_une_information_de_lieu"
                        ],
                        "hasLearning": [],
                        "hasTraining": [
                            "GamesHub:559",
                            "GamesHub:587",
                            "GamesHub:535",
                            "GamesHub:586",
                            "GamesHub:617",
                            "GamesHub:11",
                            "GamesHub:529",
                            "GamesHub:581"
                        ],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": [
                            "Identifier_une_disposition_spatiale"
                        ]
                    }
                },
                {
                    "name": "Identifier_les_indices_de_nombre",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_marques_morphosyntaxiques"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_un_pronom_substitut",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_les_substituts_d_un_référent"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "identifier_un_connecteur_de_temps",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_une_information_explicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": [
                            "identifier_un_connecteur_de_temps"
                        ]
                    }
                },
                {
                    "name": "Identifier_des_indices_dans_le_texte",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_une_information_implicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_une_sensation",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_une_information_implicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Produire_une_disposition_spatiale",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Connaitre_les_connecteurs_de_lieu"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_une_relation_de_manière",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_une_information_de_temps",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_une_information_explicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_les_indices_de_temps",
                            "identifier_un_connecteur_de_temps"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": [
                            "Identifier_une_information_de_temps"
                        ]
                    }
                },
                {
                    "name": "Identifier_un_verbe_de_déplacement",
                    "type": "Skills",
                    "mastery": 1,
                    "trust": 0.2,
                    "cover": 1,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_mots_et_groupes_de_mots"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [
                            "GamesHub:527",
                            "GamesHub:528",
                            "GamesHub:609"
                        ],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "identifier_un_connecteur_de_lieu",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_une_information_explicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Comprendre_un_énoncé_de_problème_mathématique",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [
                            "Lire_et_comprendre_des_phrases_écrites_(processus_d_intégration)"
                        ],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_les_genres_textuels",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [
                            "Lire_et_comprendre_des_textes_écrits_(macroprocessus_et_processus_d_élaboration)"
                        ],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_un_substitut_placé_après",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_les_substituts_d_un_référent"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_une_relation_de_cause",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_les_indices_de_genre",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_marques_morphosyntaxiques"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_les_personnages_principaux",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Identifier_une_information_explicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_une_relation_logique_ou_un_raisonnement",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_un_élément_de_raisonnement",
                            "identifier_un_connecteur_logique"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": [
                            "Identifier_une_relation_logique_ou_un_raisonnement"
                        ]
                    }
                },
                {
                    "name": "Identifier_un_sentiment",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_une_information_implicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_une_information_explicite",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_mots_et_groupes_de_mots"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [
                            "Identifier_les_personnages_principaux",
                            "Identifier_une_information_de_temps",
                            "identifier_un_connecteur_de_lieu",
                            "Identifier_un_élément_de_raisonnement",
                            "Identifier_une_information_de_lieu",
                            "identifier_un_connecteur_logique",
                            "identifier_un_connecteur_de_temps"
                        ],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Mettre_en_relation_un_paragraphe_et_des_images_séquentielles",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_une_chronologie"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Comprendre_les_reprises_anaphoriques",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [
                            "Lire_et_comprendre_des_phrases_écrites_(processus_d_intégration)"
                        ],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [
                            "Identifier_les_substituts_d_un_référent",
                            "Identifier_le_référent_d_un_substitut"
                        ],
                        "requires": [
                            "Comprendre_les_mots_et_groupes_de_mots"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Produire_une_chronologie",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Connaitre_les_connecteurs_de_temps"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Comprendre_les_marques_morphosyntaxiques",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [
                            "Lire_et_comprendre_des_phrases_écrites_(processus_d_intégration)"
                        ],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [
                            "Identifier_les_indices_de_temps",
                            "Identifier_les_indices_de_mode",
                            "Identifier_les_indices_de_nombre",
                            "Identifier_la_valeur_de_la_ponctuation",
                            "Identifier_les_indices_de_genre"
                        ],
                        "requires": [
                            "Comprendre_les_mots_et_groupes_de_mots"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_les_indices_de_mode",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_marques_morphosyntaxiques"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_le_sens_figuré",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_mots_et_groupes_de_mots"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_le_contexte_du_texte",
                            "Définir_le_sens_figuré"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": [
                            "Identifier_le_sens_figuré",
                            "Identifier_le_sens_figuré"
                        ]
                    }
                },
                {
                    "name": "Produire_une_inférence_logique",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_une_information_implicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Identifier_des_indices_dans_le_texte",
                            "Mettre_en_relation_informations_explicites_et_informations_externes"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Identifier_le_référent_d_un_substitut",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_les_reprises_anaphoriques"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [
                            "Identifier_un_référent_placé_après",
                            "Identifier_un_référent_placé_avant"
                        ],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Mettre_en_relation_informations_explicites_et_informations_externes",
                    "type": "Skills",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "Comprendre_une_information_implicite"
                        ],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Définir_les_genres_textuels",
                    "type": "Knowledge",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [
                            "Lire_et_comprendre_des_textes_écrits_(macroprocessus_et_processus_d_élaboration)"
                        ],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Connaitre_les_connecteurs_de_temps",
                    "type": "Knowledge",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [
                            "Lire_et_comprendre_des_phrases_écrites_(processus_d_intégration)"
                        ],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [
                            "GamesHub:555"
                        ],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Connaitre_les_connecteurs_logiques",
                    "type": "Knowledge",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [
                            "Lire_et_comprendre_des_phrases_écrites_(processus_d_intégration)"
                        ],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Connaitre_les_connecteurs_de_lieu",
                    "type": "Knowledge",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [
                            "Lire_et_comprendre_des_phrases_écrites_(processus_d_intégration)"
                        ],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Définir_le_sens_propre",
                    "type": "Knowledge",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [
                            "Lire_et_comprendre_des_mots_écrits"
                        ],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Définir_le_sens_figuré",
                    "type": "Knowledge",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [
                            "Lire_et_comprendre_des_mots_écrits"
                        ],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Lire_et_comprendre_des_mots_écrits",
                    "type": "Competency",
                    "mastery": 1,
                    "trust": 0.2,
                    "cover": 0.02857142857142857,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "L1_21_Lire_de_manière_autonome_des_textes_variés_et_développer_son_efficacité_en_lecture"
                        ],
                        "hasSkill": [
                            "Lire_des_mots_connus",
                            "Comprendre_les_mots_et_groupes_de_mots",
                            "Déchiffrer_des_mots_inconnus"
                        ],
                        "hasKnowledge": [
                            "Définir_le_sens_propre",
                            "Définir_le_sens_figuré"
                        ],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "L1_28_Utiliser_l_écriture_et_les_instruments_de_la_communication_pour_planifier_et_réaliser_des_documents",
                    "type": "Competency",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "L1_23_Comprendre_des_textes_oraux_variés_propres_à_des_situations_de_la_vie_courante",
                    "type": "Competency",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "L1_24__Produire_des_textes_oraux_variés_propres_à_des_situations_de_la_vie_courante",
                    "type": "Competency",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Lire_et_comprendre_des_textes_écrits_(macroprocessus_et_processus_d_élaboration)",
                    "type": "Competency",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "L1_21_Lire_de_manière_autonome_des_textes_variés_et_développer_son_efficacité_en_lecture"
                        ],
                        "hasSkill": [
                            "Identifier_les_genres_textuels",
                            "Identifier_le_contexte_du_texte"
                        ],
                        "hasKnowledge": [
                            "Définir_les_genres_textuels"
                        ],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "L1_26_Construire_une_représentation_de_la_langue_pour_comprendre_et_produire_des_textes",
                    "type": "Competency",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [
                            "Lire_et_comprendre_des_mots_écrits"
                        ],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "Lire_et_comprendre_des_phrases_écrites_(processus_d_intégration)",
                    "type": "Competency",
                    "mastery": 1,
                    "trust": 0.3000173682494222,
                    "cover": 0.017857142857142856,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [
                            "L1_21_Lire_de_manière_autonome_des_textes_variés_et_développer_son_efficacité_en_lecture"
                        ],
                        "hasSkill": [
                            "Comprendre_un_énoncé_de_problème_mathématique",
                            "Comprendre_les_reprises_anaphoriques",
                            "Comprendre_les_marques_morphosyntaxiques",
                            "Comprendre_les_liens_entre_2_ou_plusieurs_informations_explicites",
                            "Comprendre_une_information_implicite"
                        ],
                        "hasKnowledge": [
                            "Connaitre_les_connecteurs_de_temps",
                            "Connaitre_les_connecteurs_logiques",
                            "Connaitre_les_connecteurs_de_lieu"
                        ],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "L1_21_Lire_de_manière_autonome_des_textes_variés_et_développer_son_efficacité_en_lecture",
                    "type": "Competency",
                    "mastery": 1,
                    "trust": 0.2500086841247111,
                    "cover": 0.015476190476190477,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [
                            "Lire_et_comprendre_des_mots_écrits",
                            "Lire_et_comprendre_des_textes_écrits_(macroprocessus_et_processus_d_élaboration)",
                            "Lire_et_comprendre_des_phrases_écrites_(processus_d_intégration)"
                        ],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                },
                {
                    "name": "L1_22_Ecrire_des_textes_variés_à_l_aide_de_diverses_références",
                    "type": "Competency",
                    "mastery": 0,
                    "trust": 0,
                    "cover": 0,
                    "relations": {
                        "isSkillOf": [],
                        "isKnowledgeOf": [],
                        "composes": [],
                        "hasSkill": [],
                        "hasKnowledge": [],
                        "isComposedOf": [],
                        "requires": [],
                        "hasLearning": [],
                        "hasTraining": [],
                        "isComplexificationOf": [],
                        "isLevelOfUnderstandingOf": []
                    }
                }
            ],
            "resources": [
                {
                    "id": "GamesHub:528",
                    "name": "Par ici ou par-là : Forêt-2",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 2,
                    "difficulty": 1,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/528",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:623",
                    "name": "Par ici ou par-là : Cour-3",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 1,
                    "difficulty": 1,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/623",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:560",
                    "name": "Par ici ou par-là : Village-2",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 1,
                    "difficulty": 2,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/560",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:559",
                    "name": "Par ici ou par-là : Village-1",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 2,
                    "difficulty": 0,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/559",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:527",
                    "name": "Par ici ou par-là : Forêt-1",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 2,
                    "difficulty": 0,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/527",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:587",
                    "name": "Par ici ou par-là : Rome-3",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 2,
                    "difficulty": 1,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/587",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:555",
                    "name": "Par ici ou par-là : Espace-2",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 2,
                    "difficulty": 0,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/555",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:622",
                    "name": "Par ici ou par-là : Rome-1",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 1,
                    "difficulty": 2,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/622",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:535",
                    "name": "Par ici ou par-là : Ville-1",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 2,
                    "difficulty": 0,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/535",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:529",
                    "name": "Par ici ou par-là : Forêt-3",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 1,
                    "difficulty": 2,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/529",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:617",
                    "name": "Par ici ou par-là : Ville-2",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 0,
                    "difficulty": 0,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/617",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:609",
                    "name": "Par ici ou par-là : Cour1",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 2,
                    "difficulty": 0,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/609",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:586",
                    "name": "Par ici ou par-là : Rome-2",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 2,
                    "difficulty": 1,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/586",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:11",
                    "name": "Par ici ou par-là : Rome-1",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 2,
                    "difficulty": 0,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/622",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                },
                {
                    "id": "GamesHub:581",
                    "name": "Par ici ou par-là : Espace-3",
                    "interactivityType": "active",
                    "learningResourceType": "performance",
                    "significanceLevel": 2,
                    "difficulty": 2,
                    "typicalLearningTime": 3,
                    "learningPlatform": "GamesHub",
                    "location": "https://hep3.emf-infopro.ch/581",
                    "author": "HEP",
                    "language": "fr",
                    "generative": false
                }
            ],
            "colors": [
                "0.25",
                "0.5",
                "0.75"
            ],
            "computedAt": {
                "date": "2023-09-25 15:03:54.000000",
                "timezone_type": 3,
                "timezone": "UTC"
            }
        }'