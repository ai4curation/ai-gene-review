window.GUIDELINES_DATA = {
 "guidelines": [
  {
   "id": "MF-1",
   "title": "Assert an MF only for an activity the gene product itself performs",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC",
   "aspects": [
    "F"
   ],
   "go_terms": [
    {
     "term_id": "GO:0060090",
     "label": "molecular adaptor activity"
    },
    {
     "term_id": "GO:0004679",
     "label": "AMP-activated protein kinase activity"
    },
    {
     "term_id": "GO:0019887",
     "label": "protein kinase regulator activity"
    },
    {
     "term_id": "GO:0000030",
     "label": "mannosyltransferase activity"
    }
   ],
   "sources": [
    {
     "kind": "wiki",
     "title": "Enables",
     "url": "https://wiki.geneontology.org/index.php/Enables",
     "href": "https://wiki.geneontology.org/index.php/Enables"
    },
    {
     "kind": "repo",
     "title": "CLAUDE.md",
     "path": "CLAUDE.md",
     "href": "https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md"
    },
    {
     "kind": "wiki",
     "title": "Contributes to",
     "url": "https://wiki.geneontology.org/index.php/Contributes_to",
     "href": "https://wiki.geneontology.org/index.php/Contributes_to"
    },
    {
     "kind": "wiki",
     "title": "Guidelines for new Molecular Functions",
     "url": "https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions",
     "href": "https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-1. Assert an MF only for an activity the gene product itself performs\n\n## Decision\n\nUse `enables` for an activity the gene product carries out, alone or as the\nresponsible subunit of a complex. Do not use an MF term to record a process role, a\nphenotype, an interaction partner's activity, or an activity the protein merely\nsupports.\n\n## Context\n\n`enables` is the default MF relation and is reserved for \"gene products\nthat mediate a Molecular Function\"; accessory subunits \"should not be annotated to a\nMolecular Function in which they do not directly participate\" and usually take\n`GO:0060090` molecular adaptor activity or a regulator term instead\n([wiki: Enables](https://wiki.geneontology.org/index.php/Enables)). A gene product that\nis necessary for an activity is not thereby its performer; the same distinction\ngoverns BP `involved_in` ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), \"Do not add what curators\ndeliberately declined to add\").\n\n## Application\n\nWorked example. In the AMP-activated protein kinase, PRKAA1 is the catalytic subunit\nand enables `GO:0004679` AMP-activated protein kinase activity. PRKAG1 binds AMP/ADP and\nstabilises the activation loop; it is annotated to `GO:0019887` protein kinase\nregulator activity and does *not* contribute to the kinase activity\n([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). In the\nPIGM–PIGX mannosyltransferase, only PIGM enables `GO:0000030` mannosyltransferase\nactivity, although PIGX is required.\n\nWhere the responsible subunit of a complex is unknown, make no MF annotation; capture\nthe complex membership (CC) and the process (BP)\n([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). The\n`contributes_to` qualifier is reserved for irreducible molecular machines; see\n[protein-complexes.md](../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html).",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-1.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-1.html"
  },
  {
   "id": "MF-2",
   "title": "Annotate at the depth this row's evidence supports, and refine only on that evidence",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC_PLUS",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IDA",
    "IEA"
   ],
   "go_terms": [
    {
     "term_id": "GO:0004930",
     "label": "G protein-coupled receptor activity"
    },
    {
     "term_id": "GO:0004941",
     "label": "beta2-adrenergic receptor activity"
    },
    {
     "term_id": "GO:0003674",
     "label": "molecular_function"
    },
    {
     "term_id": "GO:0005488",
     "label": "binding"
    }
   ],
   "related": [
    "MF-11"
   ],
   "differences": [
    {
     "prior_source": "CLAUDE.md before the 2026-11-14 ruling",
     "prior_said": "`TOO_GENERAL` usable for any general term with a specific term elsewhere, including `GO:0004930`",
     "we_recommend": "`TOO_GENERAL` only for terms imprecise on their own; `MODIFY` needs the row's own evidence",
     "why": "Two reviews read the enum in opposite ways; earlier reviews are not retroactively defective"
    }
   ],
   "sources": [
    {
     "kind": "repo",
     "title": "CLAUDE.md",
     "path": "CLAUDE.md",
     "href": "https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md"
    },
    {
     "kind": "repo",
     "title": "action consistency",
     "path": "docs/action_consistency.md",
     "href": "https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md"
    },
    {
     "kind": "wiki",
     "title": "Guidelines for catalytic activity terms",
     "url": "https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms",
     "href": "https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-2. Annotate at the depth this row's evidence supports, and refine only on that evidence\n\n## Decision\n\nChoose the most specific term that the cited evidence supports. In review, a correct\nbut general term is `MODIFY` only when the row's own evidence supports a named deeper\nterm; otherwise keep it. `TOO_GENERAL` is for terms that are imprecise on their own\nonce a more specific term is asserted elsewhere.\n\n## Context\n\nElectronic and family-level rows legitimately stop at the level their\nsignature can justify. Refining such a row to the specific term invents evidence. The\n2026-11-14 maintainer ruling in [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) settled a split between\nreviews that read the action enum two ways: `MODIFY` needs both a deeper replacement\nand this row's evidence for it.\n\n## Application\n\nWorked example. An InterPro2GO row maps a generic GPCR signature to `GO:0004930` G\nprotein-coupled receptor activity on ADRB2. The signature cannot identify the ligand,\nso the row stays at `GO:0004930` (`ACCEPT` if core). A separate IDA row from a\nligand-binding and signaling paper supports `GO:0004941` beta2-adrenergic receptor\nactivity. The IEA row is not `TOO_GENERAL`: a receptor class term is respectably\nspecific. By contrast, a `GO:0003674` molecular_function-level grouping term or bare\n`GO:0005488` binding beside a specific term is imprecise on its own.\n\nWhen a pleiotropic gene has several supported specific activities, list each one\nrather than picking one ([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)). Lateral corrections (wrong\nsubstrate, wrong cofactor) are also `MODIFY`, and their replacement need not be a\ndescendant ([MF-11](#MF-11)).",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-2.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-2.html"
  },
  {
   "id": "MF-3",
   "title": "Prefer an activity term to a binding term",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC",
   "aspects": [
    "F"
   ],
   "go_terms": [
    {
     "term_id": "GO:0005515",
     "label": "protein binding"
    },
    {
     "term_id": "GO:0005068",
     "label": "transmembrane receptor protein tyrosine kinase adaptor activity"
    },
    {
     "term_id": "GO:0005091",
     "label": "guanyl-nucleotide exchange factor adaptor activity"
    },
    {
     "term_id": "GO:0001784",
     "label": "phosphotyrosine residue binding"
    },
    {
     "term_id": "GO:0051082",
     "obsolete": true
    },
    {
     "term_id": "GO:0044183",
     "label": "protein folding chaperone"
    },
    {
     "term_id": "GO:0140309",
     "label": "unfolded protein holdase activity"
    },
    {
     "term_id": "GO:0140318",
     "label": "protein transporter activity"
    },
    {
     "term_id": "GO:0019901",
     "label": "protein kinase binding"
    },
    {
     "term_id": "GO:0035612",
     "label": "AP-2 adaptor complex binding"
    }
   ],
   "related": [
    "MF-6"
   ],
   "open_questions": [
    "**Holdase term.** `GO:0051082` unfolded protein binding is obsolete, and `GO:0140309` still requires escorting the client to an acceptor. In-situ holdases (CRYAA, CRYAB, HSPB6, CLU, DNAJB6, DNAJB8) need a general holdase chaperone term."
   ],
   "sources": [
    {
     "kind": "wiki",
     "title": "Non-catalytic Molecular Functions",
     "url": "https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions",
     "href": "https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions"
    },
    {
     "kind": "wiki",
     "title": "Annotating binding",
     "url": "https://wiki.geneontology.org/index.php/Annotating_binding",
     "href": "https://wiki.geneontology.org/index.php/Annotating_binding"
    },
    {
     "kind": "repo",
     "title": "worked example",
     "path": "projects/MOLECULAR_ADAPTOR_ACTIVITY/worked-example-GRB2.md",
     "href": "../../pages/projects/MOLECULAR_ADAPTOR_ACTIVITY/worked-example-GRB2.html"
    },
    {
     "kind": "repo",
     "title": "UNFOLDED_PROTEIN_BINDING",
     "path": "projects/UNFOLDED_PROTEIN_BINDING.md",
     "href": "../../pages/projects/UNFOLDED_PROTEIN_BINDING.html"
    },
    {
     "kind": "repo",
     "title": "MOLECULAR_ADAPTOR_ACTIVITY",
     "path": "projects/MOLECULAR_ADAPTOR_ACTIVITY.md",
     "href": "../../pages/projects/MOLECULAR_ADAPTOR_ACTIVITY.html"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-3. Prefer an activity term to a binding term\n\n## Decision\n\nWhen the evidence shows what a binding interaction achieves (bridging, carrying,\nsequestering, catalysis, regulation, signal transduction, folding), annotate that\nactivity. Use a binding term only when binding itself is the biologically meaningful\nend point, or when binding is all that has been shown.\n\n## Context\n\nGO's stated aim is \"an annotation to a term other than binding or protein\nbinding\" for every gene product\n([wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)).\nBinding annotations are for interactions that inform the product's normal role;\n\"protein-protein interactions for which there is not yet sufficient biological context\nare out of scope for GO MF annotations\"\n([wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)).\n\n## Application\n\nWorked examples.\n\n- GRB2 carries hundreds of `GO:0005515` rows. Its function is to link activated\n  receptor tyrosine kinases to effectors: `GO:0005068` transmembrane receptor protein\n  tyrosine kinase adaptor activity and `GO:0005091` guanyl-nucleotide exchange factor\n  adaptor activity, with `GO:0001784` phosphotyrosine residue binding as the recognition\n  step (`genes/human/GRB2`;\n  [worked example](../../pages/projects/MOLECULAR_ADAPTOR_ACTIVITY/worked-example-GRB2.html)).\n- Chaperone rows on the obsolete `GO:0051082` unfolded protein binding were reassigned\n  to mechanism terms: foldases to `GO:0044183` protein folding chaperone, carrier\n  holdases such as the small TIMs to `GO:0140309` unfolded protein holdase activity, and\n  SCG5 to `GO:0140318` protein transporter activity. In-situ holdases (CRYAB and others)\n  have no fitting term yet and use a proposed \"holdase chaperone activity\" term\n  ([UNFOLDED_PROTEIN_BINDING](../../pages/projects/UNFOLDED_PROTEIN_BINDING.html)).\n- When a binding protein's activity is unknown, a class-level binding term is the right\n  stopping point, for example `GO:0019901` protein kinase binding or `GO:0035612` AP-2\n  adaptor complex binding with the partner in `has_input` ([MF-6](#MF-6)).",
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-3.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-3.html"
  },
  {
   "id": "MF-4",
   "title": "Do not co-annotate binding that an activity term already implies",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IDA",
    "IEA"
   ],
   "go_terms": [
    {
     "term_id": "GO:0004674",
     "label": "protein serine/threonine kinase activity"
    },
    {
     "term_id": "GO:0005524",
     "label": "ATP binding"
    },
    {
     "term_id": "GO:0046872",
     "label": "metal ion binding"
    }
   ],
   "related": [
    "MF-13"
   ],
   "differences": [
    {
     "prior_source": "[wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding) (2020 proposal)",
     "prior_said": "\"Annotation to these compounds is not discouraged\" (substrate and cofactor binding)",
     "we_recommend": "Do not co-annotate substrate, product, cofactor or solute binding implied by an activity",
     "why": "The sentence contradicts its own heading and the older [Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines); we read it as a typo for \"is discouraged\""
    }
   ],
   "sources": [
    {
     "kind": "wiki",
     "title": "Binding Guidelines",
     "url": "https://wiki.geneontology.org/index.php/Binding_Guidelines",
     "href": "https://wiki.geneontology.org/index.php/Binding_Guidelines"
    },
    {
     "kind": "wiki",
     "title": "Annotating binding",
     "url": "https://wiki.geneontology.org/index.php/Annotating_binding",
     "href": "https://wiki.geneontology.org/index.php/Annotating_binding"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-4. Do not co-annotate binding that an activity term already implies\n\n## Decision\n\nDo not add binding annotations for the substrates, products, cofactors or transported\nsolutes of an enzyme or transporter activity that is annotated. Annotate the binding term\nonly when binding is shown and the activity is not.\n\n## Context\n\n\"An enzyme MUST bind all of the substrates and products of the reaction it\ncatalyzes. Similarly, a transporter MUST bind the molecules it transports\"\n([wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines)).\nRedundant binding rows add noise and are a common carrier for pseudoenzyme errors,\nbecause cofactor-binding IEA rows travel with the catalytic term ([MF-13](#MF-13)).\n\n## Application\n\nWorked examples.\n\n- A kinase annotated to `GO:0004674` protein serine/threonine kinase activity does not\n  need `GO:0005524` ATP binding from the same evidence.\n- A paper that shows binding of a non-hydrolysable ATP analogue but no ATPase activity\n  supports `GO:0005524` ATP binding by IDA, with the analogue in With/From where the\n  evidence code allows it ([wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines)).\n- Do not put the bound entity in an extension when the term already names it\n  (`GO:0005524` ATP binding with `has_input` ATP is redundant).\n\nIn review, an existing implied-binding row is true; it is not `REMOVE`. Use\n`KEEP_AS_NON_CORE`, or `TOO_GENERAL` when it is a general term such as `GO:0046872`\nmetal ion binding beside an activity that specifies the metal-dependent chemistry.",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-4.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-4.html"
  },
  {
   "id": "MF-5",
   "title": "Treat bare `GO:0005515` protein binding as uninformative: never propose it, and in review replace or remove it",
   "status": "proposed",
   "topic": "MF",
   "provenance": "NEW",
   "provenance_note": "[NEW] for the review actions (this repository's policy, ahead of a pending GOC proposal); [GOC] for the QC rules.",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IDA",
    "ISS",
    "TAS",
    "NAS",
    "IEA"
   ],
   "go_terms": [
    {
     "term_id": "GO:0005515",
     "label": "protein binding"
    },
    {
     "term_id": "GO:0042802",
     "label": "identical protein binding"
    },
    {
     "term_id": "GO:0046983",
     "label": "protein dimerization activity"
    },
    {
     "term_id": "GO:0140767",
     "label": "enzyme-substrate adaptor activity"
    }
   ],
   "enforced_by": [
    "src/ai_gene_review/validation/protein_binding_policy.py"
   ],
   "differences": [
    {
     "prior_source": "[wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines); [wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29)",
     "prior_said": "Reciprocal GO:0005515 IPI annotations must be made",
     "we_recommend": "Do not create new bare GO:0005515 annotations at all; reciprocity is moot for new work",
     "why": "Protein binding records interaction, which MI databases curate; the 2026 IEA WG proposal would make it do-not-annotate"
    },
    {
     "prior_source": "[Drive: protein binding announcement (go-ontology#11094)](https://drive.google.com/open?id=1CDLNsl-FgwqdsLP3jTfuA7h3nTdGq_ASEyYyLiTLhWE)",
     "prior_said": "Convert identical protein binding and homodimerization rows to GO:0005515 with `has_input`",
     "we_recommend": "Do not convert into GO:0005515; refine to an informative MF or remove",
     "why": "Conversion moves the problem; the 2026 proposal treats both terms as equally uninformative"
    },
    {
     "prior_source": "[Drive: oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo)",
     "prior_said": "Assembled subunits may be given structural molecule activity, \"protein binding, bridging\" or protein binding",
     "we_recommend": "Structural or adaptor terms only with evidence for them; never GO:0005515 as a landing term",
     "why": "Same reason; \"protein binding, bridging\" is now `GO:0030674` and needs two partners"
    },
    {
     "prior_source": "protein_binding_policy docstring vs [MOLECULAR_ADAPTOR_ACTIVITY](../../pages/projects/MOLECULAR_ADAPTOR_ACTIVITY.html)",
     "prior_said": "The policy says REMOVE is the general case and MODIFY when the paper supports an informative MF; the project page says the policy \"prefers MODIFY\"",
     "we_recommend": "MODIFY when the row's paper supports the informative term; otherwise REMOVE",
     "why": "The two repo texts read the same policy differently; the validator accepts either action, so the evidence decides",
     "issue": 6443
    }
   ],
   "open_questions": [
    "**Protein binding and oligomerisation terms.** Should GO adopt the 2026 IEA working group proposal to make `GO:0005515`, `GO:0042802` and the dimerization terms do-not-annotate, and archive the IntAct-derived rows in a MITAB file? This document assumes yes for new work but cannot retire existing rows."
   ],
   "sources": [
    {
     "kind": "drive",
     "title": "protein binding do_not_annotate proposal",
     "url": "https://drive.google.com/open?id=1KKM7gxsPvQgszjppuyD_ZldM_T8cGV0ajSUIfLmyNQc",
     "href": "https://drive.google.com/open?id=1KKM7gxsPvQgszjppuyD_ZldM_T8cGV0ajSUIfLmyNQc"
    },
    {
     "kind": "repo",
     "title": "protein_binding_policy.py",
     "path": "src/ai_gene_review/validation/protein_binding_policy.py",
     "href": "https://github.com/ai4curation/ai-gene-review/blob/main/src/ai_gene_review/validation/protein_binding_policy.py"
    },
    {
     "kind": "repo",
     "title": "CLAUDE.md",
     "path": "CLAUDE.md",
     "href": "https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md"
    },
    {
     "kind": "wiki",
     "title": "Binding Guidelines",
     "url": "https://wiki.geneontology.org/index.php/Binding_Guidelines",
     "href": "https://wiki.geneontology.org/index.php/Binding_Guidelines"
    },
    {
     "kind": "issue",
     "title": "go-annotation#3314",
     "url": "https://github.com/geneontology/go-annotation/issues/3314",
     "href": "https://github.com/geneontology/go-annotation/issues/3314"
    },
    {
     "kind": "repo",
     "title": "worked example",
     "path": "projects/MOLECULAR_ADAPTOR_ACTIVITY/worked-example-RPTOR.md",
     "href": "../../pages/projects/MOLECULAR_ADAPTOR_ACTIVITY/worked-example-RPTOR.html"
    },
    {
     "kind": "issue",
     "title": "go-annotation#2683",
     "url": "https://github.com/geneontology/go-annotation/issues/2683",
     "href": "https://github.com/geneontology/go-annotation/issues/2683"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-5. Treat bare `GO:0005515` protein binding as uninformative: never propose it, and in review replace or remove it\n\n## Decision\n\nNever make a new bare `GO:0005515` annotation. In review, an existing bare\n`GO:0005515` row is `MODIFY` when the row's paper supports a more informative MF\n(adaptor, regulator, a class-level binding term), otherwise `REMOVE`, or `UNDECIDED` when\nthe paper cannot be read. Never `ACCEPT`, `KEEP_AS_NON_CORE` or `MARK_AS_OVER_ANNOTATED`\nit. A `REMOVE` says the annotation is uninformative, not that the interaction is false.\n\n## Context\n\nGO:0005515 says that a protein sticks to something, not what it does. An\nIEA working group proposal (2026) puts the scale plainly: protein binding is 33% of all\nexperimental annotations and 70% of experimental MF annotations, 82% of those come from\nIntAct exports, and many groups do not curate it at all\n([Drive: protein binding do_not_annotate proposal](https://drive.google.com/open?id=1KKM7gxsPvQgszjppuyD_ZldM_T8cGV0ajSUIfLmyNQc)).\nThe same proposal would add `GO:0042802` identical protein binding and\n`GO:0046983` protein dimerization activity (and its homo- and hetero- children) to the\ndo-not-annotate subset, because they carry the same information content and\nmultimerisation is out of scope for GO. This repository already enforces the policy on\nGO:0005515 as a validator warning\n([protein_binding_policy.py](https://github.com/ai4curation/ai-gene-review/blob/main/src/ai_gene_review/validation/protein_binding_policy.py)).\nIt is the one sanctioned case where `REMOVE` may be used on a true statement\n([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).\n\nRules that still apply to any surviving GO:0005515 row, and that a reviewer should\ncheck: the partner must be in With/From (gorule-0000003, gorule-0000018); `NOT` must\nnot be used with GO:0005515; ISS must not be used; and interspecies binding is allowed\nonly for physiological interactions, with the experimentally used partner in With/From\n([wiki: Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines);\n[go-annotation#3314](https://github.com/geneontology/go-annotation/issues/3314)).\n\n## Application\n\nWorked example. RPTOR has 61 GO:0005515 rows. Split by partner, they fall into two\ngroups: binding to MTOR, and binding to TOS-motif substrates such as the 4E-BPs and\nS6 kinases. The second group supports `GO:0140767` enzyme-substrate adaptor activity\n(`MODIFY`); single co-immunoprecipitation hits with no bridging context are `REMOVE`\n([worked example](../../pages/projects/MOLECULAR_ADAPTOR_ACTIVITY/worked-example-RPTOR.html)).\n\nFor `GO:0042802` and `GO:0046983` rows: until GO decides the proposal, keep a row only\nwhen the oligomer is itself functionally informative and the evidence shows it;\notherwise treat the row the way GO:0005515 is treated. Earlier GOC reviews moved\n`IDA` heterodimerization rows to GO:0005515 with an interactor in With/From and removed\n`NAS`/`TAS` rows\n([go-annotation#2683](https://github.com/geneontology/go-annotation/issues/2683)).",
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-5.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-5.html"
  },
  {
   "id": "MF-6",
   "title": "Use class-level binding children; name the specific partner in `has_input`",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IPI"
   ],
   "go_terms": [
    {
     "term_id": "GO:0019901",
     "label": "protein kinase binding"
    },
    {
     "term_id": "GO:0030971",
     "label": "receptor tyrosine kinase binding"
    },
    {
     "term_id": "GO:0005515",
     "label": "protein binding"
    },
    {
     "term_id": "GO:0051015",
     "label": "actin filament binding"
    }
   ],
   "sources": [
    {
     "kind": "wiki",
     "title": "Guidelines for new Binding terms",
     "url": "https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms",
     "href": "https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms"
    },
    {
     "kind": "wiki",
     "title": "Proposal to obsolete children of \"transcription factor binding\"",
     "url": "https://wiki.geneontology.org/index.php/Proposal_to_obsolete_children_of_%22transcription_factor_binding%22",
     "href": "https://wiki.geneontology.org/index.php/Proposal_to_obsolete_children_of_%22transcription_factor_binding%22"
    },
    {
     "kind": "wiki",
     "title": "Annotating binding",
     "url": "https://wiki.geneontology.org/index.php/Annotating_binding",
     "href": "https://wiki.geneontology.org/index.php/Annotating_binding"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-6. Use class-level binding children; name the specific partner in `has_input`\n\n## Decision\n\nWhen a binding term is warranted, choose the child that names the class of partner\n(`GO:0019901` protein kinase binding, `GO:0030971` receptor tyrosine kinase binding).\nPut the specific physiological partner in `has_input`; put the partner actually used in\nthe experiment in With/From. Do not request binding terms for individual proteins.\n\n## Context\n\nSubclasses of GO:0005515 \"should represent general classes of proteins, not\nspecific proteins\"\n([wiki: Guidelines for new Binding terms](https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms)).\nGO obsoleted the per-partner children of transcription factor binding for the same\nreason ([wiki: Proposal to obsolete children of \"transcription factor binding\"](https://wiki.geneontology.org/index.php/Proposal_to_obsolete_children_of_%22transcription_factor_binding%22)).\nWith/From supports the evidence; the extension modifies the term. A mouse receptor shown\nto bind a human ligand is annotated with the human ligand in With/From and the\northologous mouse ligand in `has_input`\n([wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)).\n\n## Application\n\nWorked example. C. elegans UNC-115 binds filaments made from rabbit skeletal muscle\nactin: `GO:0051015` actin filament binding, IPI, rabbit actin in With/From. Actin,\ntubulin and histone binding are exceptions to the `has_input` recommendation because\nmany identical copies exist and the copy used is rarely known\n([wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)).",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-6.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-6.html"
  },
  {
   "id": "MF-7",
   "title": "For small molecules, annotate the physiological ligand; never the drug or probe",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC",
   "aspects": [
    "F"
   ],
   "go_terms": [
    {
     "term_id": "GO:0005488",
     "label": "binding"
    },
    {
     "term_id": "GO:0051378",
     "label": "serotonin binding"
    },
    {
     "term_id": "GO:0016594",
     "label": "glycine binding"
    },
    {
     "term_id": "GO:0003755",
     "label": "peptidyl-prolyl cis-trans isomerase activity"
    },
    {
     "term_id": "GO:0005528",
     "label": "FK506 binding"
    }
   ],
   "open_questions": [
    "**Drug-named binding terms.** `GO:0005528` FK506 binding names an exogenous compound. Should such terms be reviewed under the 2020 drug-binding rules?"
   ],
   "sources": [
    {
     "kind": "wiki",
     "title": "Annotation Conf. Call 2020-02-04",
     "url": "https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04",
     "href": "https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04"
    },
    {
     "kind": "issue",
     "title": "go-annotation#3166",
     "url": "https://github.com/geneontology/go-annotation/issues/3166",
     "href": "https://github.com/geneontology/go-annotation/issues/3166"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-7. For small molecules, annotate the physiological ligand; never the drug or probe\n\n## Decision\n\nAnnotate small-molecule binding as `GO:0005488` binding (or an existing specific\nbinding term) with `has_input` a ChEBI entity, rather than requesting a new\npre-composed term. When a compound was used as a proxy for a natural ligand, annotate\nbinding of the natural ligand. Make no binding annotation for a drug interaction that\nis a gain of function outside the protein's normal role.\n\n## Context\n\nThe 2020 ontology editors' decision asks curators to use binding plus\n`has_input` ChEBI for chemical binding\n([wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)).\nThe obsoletion of \"drug binding\" set the three-way rule for compounds\n([go-annotation#3166](https://github.com/geneontology/go-annotation/issues/3166)):\nproxy for a natural ligand, annotate the natural ligand; pathway inhibitor, annotate the\npathway BP only for products that normally act in it; gain-of-function drug binding,\nannotate nothing.\n\n## Application\n\nWorked examples. LSD binding to a serotonin receptor supports `GO:0051378` serotonin\nbinding (LSD in With/From where allowed); strychnine binding supports `GO:0016594`\nglycine binding. FKBP1A (FKBP12) inhibits TORC1 only when bound to rapamycin, which is\nnot part of its normal role, so its drug binding rows were deleted and no TORC1\nsignaling annotation is made for it. Its own enzymatic activity,\n`GO:0003755` peptidyl-prolyl cis-trans isomerase activity, is the informative MF.\n(`GO:0005528` FK506 binding is itself a drug-named term worth questioning; see Open\nquestions.)",
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-7.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-7.html"
  },
  {
   "id": "MF-8",
   "title": "Distinguish adaptor, scaffold, sequestering, carrier and regulator by what the binding does",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC_PLUS",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IPI"
   ],
   "go_terms": [
    {
     "term_id": "GO:0140378",
     "label": "protein complex scaffold activity"
    },
    {
     "term_id": "GO:0160072",
     "label": "ubiquitin ligase complex scaffold activity"
    },
    {
     "term_id": "GO:0005198",
     "label": "structural molecule activity"
    },
    {
     "term_id": "GO:0060090",
     "label": "molecular adaptor activity"
    },
    {
     "term_id": "GO:0140693",
     "label": "molecular condensate scaffold activity"
    },
    {
     "term_id": "GO:0140566",
     "label": "histone reader activity"
    },
    {
     "term_id": "GO:0035615",
     "label": "clathrin-cargo adaptor activity"
    },
    {
     "term_id": "GO:1990756",
     "label": "ubiquitin-like ligase-substrate adaptor activity"
    },
    {
     "term_id": "GO:0140311",
     "label": "protein sequestering activity"
    },
    {
     "term_id": "GO:0140104",
     "label": "molecular carrier activity"
    }
   ],
   "differences": [
    {
     "prior_source": "[MOLECULAR_ADAPTOR_ACTIVITY](../../pages/projects/MOLECULAR_ADAPTOR_ACTIVITY.html)",
     "prior_said": "Names `GO:0032947` as \"protein-containing complex scaffold activity\", the out-of-branch scaffold term",
     "we_recommend": "Use `GO:0140378` protein complex scaffold activity",
     "why": "GO:0032947 does not resolve in the GO release used here; GO:0140378 is the live structural scaffold term",
     "issue": 6444
    }
   ],
   "open_questions": [
    "**Adaptor with one input.** The GO-CAM guideline permits a single `has_input` on an adaptor activity while warning that it may be the wrong term. Should that be a hard requirement of two inputs?"
   ],
   "sources": [
    {
     "kind": "drive",
     "title": "MF guidelines for GO-CAM",
     "url": "https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4",
     "href": "https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4"
    },
    {
     "kind": "repo",
     "title": "MOLECULAR_ADAPTOR_ACTIVITY",
     "path": "projects/MOLECULAR_ADAPTOR_ACTIVITY.md",
     "href": "../../pages/projects/MOLECULAR_ADAPTOR_ACTIVITY.html"
    },
    {
     "kind": "wiki",
     "title": "Non-catalytic Molecular Functions",
     "url": "https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions",
     "href": "https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions"
    },
    {
     "kind": "issue",
     "title": "go-annotation#3510",
     "url": "https://github.com/geneontology/go-annotation/issues/3510",
     "href": "https://github.com/geneontology/go-annotation/issues/3510"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-8. Distinguish adaptor, scaffold, sequestering, carrier and regulator by what the binding does\n\n## Decision\n\nChoose among the non-catalytic activities by the test in the [Decision aid](#chapter/MF):\nadaptor (brings two or more molecules together so they act in a coordinated way),\nscaffold (structural organiser of a complex), sequestering (binds a molecule to keep it\nfrom its partners or location), carrier (moves with its cargo to an acceptor or\nlocation), regulator (modulates the target's activity directly). An adaptor annotation\nneeds evidence of at least two bridged partners.\n\n## Context\n\nThe GO-CAM activity-unit guidelines define each activity by its inputs and\nits causal effect\n([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).\nThe adaptor activity \"has input the two (or more) molecules it brings together\", and the\nguideline warns that a single input suggests adaptor activity may not be the right term.\nA single binary interaction (one IPI hit) evidences binding, not bridging\n([MOLECULAR_ADAPTOR_ACTIVITY](../../pages/projects/MOLECULAR_ADAPTOR_ACTIVITY.html), decision rule 1).\nIn the ontology the adaptor and scaffold branches are separate: `GO:0140378` protein\ncomplex scaffold activity (and its child `GO:0160072` ubiquitin ligase complex scaffold\nactivity) sit under `GO:0005198` structural molecule activity, not under `GO:0060090`\nmolecular adaptor activity, whereas `GO:0140693` molecular condensate scaffold activity\nand `GO:0140566` histone reader activity are adaptor children (checked against the\nlocal GO release, 2026-11-15).\n\n## Application\n\nWorked examples.\n\n- LDLRAP1 bridges the LDL receptor's NPxY motif to clathrin and AP-2:\n  `GO:0035615` clathrin-cargo adaptor activity (`genes/human/LDLRAP1`).\n- In a cullin–RING ligase, CUL4A or DDB1 enables `GO:0160072` ubiquitin ligase complex\n  scaffold activity with `has_input` the substrate adaptor and the ligase, and the\n  substrate receptor enables `GO:1990756` ubiquitin-like ligase-substrate adaptor\n  activity with `has_input` the substrate\n  ([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).\n- CAV1 binds TLR4 and holds it inactive: `GO:0140311` protein sequestering activity,\n  `has_input` TLR4, part of negative regulation of the TLR4 pathway.\n- CD14 delivers LPS to TLR4–MD-2: `GO:0140104` molecular carrier activity; the\n  carrier \"moves with the substrate it carries\", which distinguishes it from a\n  transporter ([wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)).\n\nIn standard annotation, the MF-to-MF relations (`directly positively regulates`,\n`provides input for`) are not captured; record the MF, its `has_input` partners, the BP\nand the CC ([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).\nA general adaptor term may stand beside a specific child only for a distinct bridging\nevent the child does not cover; otherwise the parent is `TOO_GENERAL`\n([MOLECULAR_ADAPTOR_ACTIVITY](../../pages/projects/MOLECULAR_ADAPTOR_ACTIVITY.html), decision rule 5).",
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-8.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-8.html"
  },
  {
   "id": "MF-9",
   "title": "Support catalytic activity with evidence of catalysis, at the enzyme's natural specificity",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IPI"
   ],
   "go_terms": [
    {
     "term_id": "GO:0003824",
     "label": "catalytic activity"
    },
    {
     "term_id": "GO:0004620",
     "label": "glycerophospholipase activity"
    },
    {
     "term_id": "GO:0036424",
     "label": "L-phosphoserine phosphatase activity"
    },
    {
     "term_id": "GO:0042800",
     "label": "histone H3K4 methyltransferase activity"
    }
   ],
   "differences": [
    {
     "prior_source": "[wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)",
     "prior_said": "Binding annotations use IPI",
     "we_recommend": "IPI when the partner can be identified; IDA when it cannot; never IPI for catalytic terms",
     "why": "Matches the IPI page; the binding page oversimplifies"
    }
   ],
   "sources": [
    {
     "kind": "wiki",
     "title": "IPI",
     "url": "https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29",
     "href": "https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29"
    },
    {
     "kind": "issue",
     "title": "go-annotation#2131",
     "url": "https://github.com/geneontology/go-annotation/issues/2131",
     "href": "https://github.com/geneontology/go-annotation/issues/2131"
    },
    {
     "kind": "wiki",
     "title": "Annotation Conf. Call 2021-08-03",
     "url": "https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2021-08-03",
     "href": "https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2021-08-03"
    },
    {
     "kind": "wiki",
     "title": "Guidelines for catalytic activity terms",
     "url": "https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms",
     "href": "https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-9. Support catalytic activity with evidence of catalysis, at the enzyme's natural specificity\n\n## Decision\n\nAnnotate a catalytic activity only from evidence that the product catalyses the\nreaction (an activity assay, a catalytic-residue mutant, a complementation with\nactivity read-out). Never use IPI for catalytic activity terms. Choose the term whose\nsubstrate range matches the enzyme's in vivo specificity: annotate the L-amino acid or\nD-sugar form by default, and annotate both the NAD+ and NADP+ terms when the enzyme\nuses both.\n\n## Context\n\nGorule-0000007 forbids IPI for `is_a` descendants of `GO:0003824` catalytic\nactivity: \"It is unlikely that enough information can be obtained from a binding\ninteraction to support such an annotation\"\n([wiki: IPI](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29);\n[go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)). The\n2021 Rhea jamboree set the specificity rules: \"The specificity of GO MFs is at the same\nlevel of the specificity of enzymes; we do not create terms for each substrate if an\nenzyme can act on a group of substrates\"; amino acids default to the L form and sugars\nto the D form; NAD(P) in a GO label means the cofactor is *unknown*, unlike IUBMB usage,\nso an enzyme known to use both gets two annotations\n([wiki: Annotation Conf. Call 2021-08-03](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2021-08-03);\n[wiki: Guidelines for catalytic activity terms](https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms)).\n\n## Application\n\nWorked examples. Phospholipases that act on many acyl chains are annotated to the\ngeneral reaction (`GO:0004620` glycerophospholipase activity and its reaction-level\nchildren), not to one Rhea reaction per chain. Phosphoserine phosphatases are annotated\nto `GO:0036424` L-phosphoserine phosphatase activity; the parent and the D-form term\nwere merged or obsoleted after a spot check showed every annotation concerned the L\nform. Positional terms for protein substrates are out of scope except for the histone\ncode (`GO:0042800` histone H3K4 methyltransferase activity) and ncRNA modifications.",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-9.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-9.html"
  },
  {
   "id": "MF-10",
   "title": "Annotate the physiological reaction, not the assay substrate",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC_PLUS",
   "provenance_note": "[GOC] for the principle; [GOC+] for the synthetic-substrate distinction.",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IEA"
   ],
   "go_terms": [
    {
     "term_id": "GO:0003840",
     "obsolete": true
    },
    {
     "term_id": "GO:0102306",
     "obsolete": true
    },
    {
     "term_id": "GO:0016616",
     "label": "oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor"
    }
   ],
   "differences": [
    {
     "prior_source": "[go-annotation#5840](https://github.com/geneontology/go-annotation/issues/5840)",
     "prior_said": "\"It's in RHEA and EC - usually we've been keeping these\"",
     "we_recommend": "Physiological relevance decides; presence in EC or Rhea does not",
     "why": "The same thread ended by moving the annotations up a level, and GO later obsoleted the term"
    }
   ],
   "open_questions": [
    "**Rhea residues of obsoletions.** Nine Rhea reactions now sit as narrow matches on EC grouping classes (for example Rhea:25968 on `GO:0016616`) and generate uninformative IEA rows. Who owns the clean-up, GO or the rhea2go pipeline?"
   ],
   "sources": [
    {
     "kind": "drive",
     "title": "2017 GOC training talk",
     "url": "https://drive.google.com/open?id=1m9v6KbdXs32ihzMjqGJYQpuK1Qf49Gh-",
     "href": "https://drive.google.com/open?id=1m9v6KbdXs32ihzMjqGJYQpuK1Qf49Gh-"
    },
    {
     "kind": "issue",
     "title": "go-annotation#1953",
     "url": "https://github.com/geneontology/go-annotation/issues/1953",
     "href": "https://github.com/geneontology/go-annotation/issues/1953"
    },
    {
     "kind": "issue",
     "title": "go-annotation#1514",
     "url": "https://github.com/geneontology/go-annotation/issues/1514",
     "href": "https://github.com/geneontology/go-annotation/issues/1514"
    },
    {
     "kind": "issue",
     "title": "go-annotation#1519",
     "url": "https://github.com/geneontology/go-annotation/issues/1519",
     "href": "https://github.com/geneontology/go-annotation/issues/1519"
    },
    {
     "kind": "issue",
     "title": "go-annotation#5840",
     "url": "https://github.com/geneontology/go-annotation/issues/5840",
     "href": "https://github.com/geneontology/go-annotation/issues/5840"
    },
    {
     "kind": "repo",
     "title": "NONPHYSIOLOGICAL_REACTIONS",
     "path": "projects/NONPHYSIOLOGICAL_REACTIONS.md",
     "href": "../../pages/projects/NONPHYSIOLOGICAL_REACTIONS.html"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-10. Annotate the physiological reaction, not the assay substrate\n\n## Decision\n\nDo not annotate an activity whose only support is an assay substrate, a chromogenic or\nfluorogenic surrogate, a tracer ion, or a non-physiological reaction. Annotate the\nphysiological activity the assay was designed to measure, if the paper supports it;\notherwise annotate the more general activity the assay does establish.\n\n## Context\n\n\"Annotate the conclusion rather than the assay\": rubidium is used to assay\npotassium transport, and kinases are often tested on histones that are not their\nsubstrates ([Drive: 2017 GOC training talk](https://drive.google.com/open?id=1m9v6KbdXs32ihzMjqGJYQpuK1Qf49Gh-)).\nPomBase does not annotate in vitro substrates known to be irrelevant in vivo\n([go-annotation#1953](https://github.com/geneontology/go-annotation/issues/1953)). GO\nhas obsoleted molecular function terms for non-physiological reactions, keeping the EC\nnumber but removing the EC-to-GO mapping\n([go-annotation#1514](https://github.com/geneontology/go-annotation/issues/1514),\n[go-annotation#1519](https://github.com/geneontology/go-annotation/issues/1519)).\n\n## Application\n\nWorked examples.\n\n- Gamma-glutamyl transpeptidases hydrolyse glutathione; transfer to an acceptor needs\n  millimolar acceptor concentrations. `GO:0003840` gamma-glutamyltransferase activity is\n  now obsolete for that reason.\n- `GO:0102306` benzil reductase [(S)-benzoin-forming] activity was a chromogenic\n  read-out that EC and Rhea turned into a reaction; GO obsoleted it, and the S. pombe\n  annotations were moved up to the grouping class `GO:0016616` oxidoreductase\n  activity, acting on the CH-OH group of donors, NAD or NADP as acceptor\n  ([go-annotation#5840](https://github.com/geneontology/go-annotation/issues/5840)).\n  The obsoletion left Rhea:25968 as a narrow match on that grouping class, which now\n  generates uninformative IEA rows ([NONPHYSIOLOGICAL_REACTIONS](../../pages/projects/NONPHYSIOLOGICAL_REACTIONS.html)).\n- A synthetic substrate is not by itself the test. Atrazine chlorohydrolase and\n  haloalkane dehalogenase act on man-made chemicals but are selected,\n  pathway-committed enzymes; they keep their specific terms. Use pathway membership and\n  host genetics to tell an evolved xenobiotic-degrading enzyme from an assay artefact;\n  kinetics alone is the weakest signal ([NONPHYSIOLOGICAL_REACTIONS](../../pages/projects/NONPHYSIOLOGICAL_REACTIONS.html)).",
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-10.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-10.html"
  },
  {
   "id": "MF-11",
   "title": "Measured activity is not automatically function: apply the three tiers",
   "status": "proposed",
   "topic": "MF",
   "provenance": "NEW",
   "provenance_note": "[NEW]. GOC guidance says to annotate physiological activities but gives no rule for graded promiscuity.",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IDA"
   ],
   "go_terms": [
    {
     "term_id": "GO:0061710",
     "label": "L-threonylcarbamoyladenylate synthase activity"
    },
    {
     "term_id": "GO:0047400",
     "label": "phosphonoacetate hydrolase activity"
    }
   ],
   "differences": [
    {
     "prior_source": "GOC guidance (none)",
     "prior_said": "No rule for weak or promiscuous measured activities",
     "we_recommend": "Three tiers: non-core, over-annotated, removed",
     "why": "Needed to treat noise-level activity of a paralog differently from a genuine side activity"
    }
   ],
   "open_questions": [
    "**Promiscuity tiers in the ontology.** The tiers of [MF-11](#MF-11) are a review convention. Should GO record graded relevance (for example, a qualifier for non-physiological activity), or keep relying on removal?"
   ],
   "sources": [
    {
     "kind": "paper",
     "title": "PMID:40703034",
     "url": "https://europepmc.org/article/MED/40703034",
     "href": "https://europepmc.org/article/MED/40703034"
    },
    {
     "kind": "repo",
     "title": "ENZYME_SPECIFICITY",
     "path": "projects/ENZYME_SPECIFICITY.md",
     "href": "../../pages/projects/ENZYME_SPECIFICITY.html"
    },
    {
     "kind": "repo",
     "title": "CLAUDE.md",
     "path": "CLAUDE.md",
     "href": "https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-11. Measured activity is not automatically function: apply the three tiers\n\n## Decision\n\nFor an enzyme activity that was measured but is weak or promiscuous, decide whether\nthe protein evolved to catalyse the reaction, and act by tier: a genuine secondary\nactivity is `KEEP_AS_NON_CORE`; real in vitro activity of unknown relevance is\n`MARK_AS_OVER_ANNOTATED`; noise-level activity, when a dedicated enzyme for the same\nreaction exists in the organism, is `REMOVE`, even on an IDA row. State the judgement in\n`reason`; there is no numeric cutoff.\n\n## Context\n\nThe tiers follow de Crécy-Lagard et al. 2025\n([PMID:40703034](https://europepmc.org/article/MED/40703034), a framework for\nevaluating function predictions) and were adopted after a single \"secondary activities\nare non-core\" rule would have kept a noise-level activity\n([ENZYME_SPECIFICITY](../../pages/projects/ENZYME_SPECIFICITY.html); [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md)).\n`REMOVE` in the third tier accepts the measurement and argues that the activity is not\nthe gene's function, which is the \"genuinely contradicted function\" case that permits\nremoving an experimental row.\n\nIndicators for the `REMOVE` tier (most should hold): a dedicated enzyme for the reaction\nexists in the same organism, ideally essential or non-redundant; the activity is orders\nof magnitude below it (about 10³-fold or more as a guide); the protein sits in a\ndifferent subfamily or lacks the specificity determinants; there is no in vivo\nphenotype for the reaction.\n\n## Application\n\nWorked pair ([ENZYME_SPECIFICITY](../../pages/projects/ENZYME_SPECIFICITY.html)).\n\n- E. coli YciO, `GO:0061710` L-threonylcarbamoyladenylate synthase activity: `REMOVE`.\n  TsaC is the essential dedicated enzyme, YciO's rate is about 10⁴-fold lower, and\n  YciO lacks the KRSN tetrad and sits in another subfamily.\n- E. coli YjdM, `GO:0047400` phosphonoacetate hydrolase activity:\n  `MARK_AS_OVER_ANNOTATED`. The phosphonate link is a name collision, but E. coli has no\n  dedicated phosphonoacetate hydrolase, so the activity cannot be assigned elsewhere.",
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-11.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-11.html"
  },
  {
   "id": "MF-12",
   "title": "Check each axis of specificity before accepting a family-derived enzyme term",
   "status": "proposed",
   "topic": "MF",
   "provenance": "NEW",
   "provenance_note": "[NEW] for the four-axis check; [GOC] for the underlying \"annotate in vivo specificity\" principle.",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IBA",
    "ISS",
    "IEA"
   ],
   "go_terms": [
    {
     "term_id": "GO:0004622",
     "label": "phosphatidylcholine lysophospholipase A1 activity"
    },
    {
     "term_id": "GO:0102545",
     "label": "B-type glycerophospholipase activity"
    },
    {
     "term_id": "GO:0016509",
     "label": "long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity"
    },
    {
     "term_id": "GO:0003857",
     "label": "(3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity"
    },
    {
     "term_id": "GO:0008483",
     "label": "transaminase activity"
    },
    {
     "term_id": "GO:0016838",
     "label": "carbon-oxygen lyase activity, acting on phosphates"
    },
    {
     "term_id": "GO:0008194",
     "label": "UDP-glycosyltransferase activity"
    },
    {
     "term_id": "GO:0016758",
     "label": "hexosyltransferase activity"
    },
    {
     "term_id": "GO:0003985",
     "label": "acetyl-CoA C-acetyltransferase activity"
    },
    {
     "term_id": "GO:0034736",
     "label": "cholesterol O-acyltransferase activity"
    },
    {
     "term_id": "GO:0004616",
     "label": "phosphogluconate dehydrogenase (decarboxylating) activity"
    }
   ],
   "sources": [
    {
     "kind": "repo",
     "title": "ENZYME_SPECIFICITY",
     "path": "projects/ENZYME_SPECIFICITY.md",
     "href": "../../pages/projects/ENZYME_SPECIFICITY.html"
    },
    {
     "kind": "repo",
     "title": "RHEA",
     "path": "projects/RHEA.md",
     "href": "../../pages/projects/RHEA.html"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-12. Check each axis of specificity before accepting a family-derived enzyme term\n\n## Decision\n\nBefore accepting a catalytic term that rests on family membership (IEA, IBA, ISS, or\nan experimental row that names a broad class), check four axes: substrate range (and\nchain length), cofactor or donor, reaction mechanism, and subunit, paralog or name\nidentity. A failure on any axis is `MODIFY` (lateral or refining) or `REMOVE`.\n\n## Context\n\nSpecificity errors are where family-based annotation is most confidently\nwrong: the fold and often the EC class are right, so nothing looks amiss until someone\nchecks the substrate, cofactor or subunit ([ENZYME_SPECIFICITY](../../pages/projects/ENZYME_SPECIFICITY.html)).\n\n## Application\n\nWorked examples, all from completed reviews in this repository:\n\n| Axis | Gene | Row | Action |\n|---|---|---|---|\n| Substrate too narrow | C. albicans LPL1 | `GO:0004622` phosphatidylcholine lysophospholipase A1 activity | `MODIFY` → `GO:0102545` B-type glycerophospholipase activity |\n| Chain length | human HADH | `GO:0016509` long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity | `MARK_AS_OVER_ANNOTATED`; the short/medium-chain `GO:0003857` is correct |\n| Mechanism | human PHYKPL | `GO:0008483` transaminase activity | `REMOVE`; the enzyme is a phospho-lyase (`GO:0016838` carbon-oxygen lyase activity, acting on phosphates) |\n| Donor | S. erythraea EryCIII | `GO:0008194` UDP-glycosyltransferase activity | `REMOVE`; it transfers a dTDP-sugar, and `GO:0016758` hexosyltransferase activity is already present |\n| Subunit | human HADHA | `GO:0003985` acetyl-CoA C-acetyltransferase activity | `REMOVE`; thiolase is the HADHB subunit's activity |\n| Name collision | human ACAT1 | `GO:0034736` cholesterol O-acyltransferase activity | `REMOVE`; the row came from a SOAT1 paper via the shared \"ACAT1\" nickname |\n\nA specific term should be verified, not assumed, even when it is probably right: the\nC. albicans GND1 review confirmed NADP+ specificity (`GO:0004616`) from the coenzyme\nmotifs rather than accepting it from family membership.",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-12.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-12.html"
  },
  {
   "id": "MF-13",
   "title": "Do not annotate catalysis to a pseudoenzyme; annotate what it does instead",
   "status": "proposed",
   "topic": "MF",
   "provenance": "NEW",
   "provenance_note": "[NEW]. GOC guidance does not address pseudoenzymes as a class; PAINT handles them case by case through loss annotations.",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IBA"
   ],
   "go_terms": [
    {
     "term_id": "GO:0003924",
     "label": "GTPase activity"
    },
    {
     "term_id": "GO:0032452",
     "label": "histone demethylase activity"
    },
    {
     "term_id": "GO:0051213",
     "label": "dioxygenase activity"
    },
    {
     "term_id": "GO:0016491",
     "label": "oxidoreductase activity"
    },
    {
     "term_id": "GO:0032454",
     "label": "histone H3K9 demethylase activity"
    },
    {
     "term_id": "GO:0004497",
     "label": "monooxygenase activity"
    },
    {
     "term_id": "GO:0005506",
     "label": "iron ion binding"
    },
    {
     "term_id": "GO:0020037",
     "label": "heme binding"
    },
    {
     "term_id": "GO:0043539",
     "label": "protein serine/threonine kinase activator activity"
    }
   ],
   "differences": [
    {
     "prior_source": "GOC guidance (none)",
     "prior_said": "No class rule for pseudoenzymes",
     "we_recommend": "Residue-plus-context check and action ladder",
     "why": "Pseudoenzymes are a predictable error source for every family-based pipeline"
    }
   ],
   "sources": [
    {
     "kind": "repo",
     "title": "PSEUDOENZYMES",
     "path": "projects/PSEUDOENZYMES.md",
     "href": "../../pages/projects/PSEUDOENZYMES.html"
    },
    {
     "kind": "repo",
     "title": "FUNCTION_REQUIREMENT_RULES",
     "path": "projects/FUNCTION_REQUIREMENT_RULES.md",
     "href": "../../pages/projects/FUNCTION_REQUIREMENT_RULES.html"
    },
    {
     "kind": "paper",
     "title": "PMID:40703034",
     "url": "https://europepmc.org/article/MED/40703034",
     "href": "https://europepmc.org/article/MED/40703034"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-13. Do not annotate catalysis to a pseudoenzyme; annotate what it does instead\n\n## Decision\n\nA protein that keeps an enzyme fold but lacks the catalytic machinery does not get the\nfamily's catalytic activity, or the cofactor-binding and process terms that follow from\nit. Check catalytic residues, the motif context around them, and biochemical data. Where\na non-catalytic role is shown (activator, scaffold, reader, decoy, chaperone), annotate\nthat role.\n\n## Context\n\nInterPro2GO, EC2GO, UniRule, ARBA and IBA propagate catalytic terms from\nfamily membership without checking residue conservation, so pseudoenzymes are a\nsystematic source of false enzyme annotations\n([PSEUDOENZYMES](../../pages/projects/PSEUDOENZYMES.html)). The same check generalises as \"function\nrequirement\" rules: a catalytic or transport term should be flagged when the protein\nlacks a domain the activity needs. Flags from those rules include beta-adrenergic\nreceptors annotated to `GO:0003924` GTPase activity (a GPCR activates G proteins and does\nnot hydrolyse GTP) and G beta and gamma subunits annotated `enables` GTPase activity\n([FUNCTION_REQUIREMENT_RULES](../../pages/projects/FUNCTION_REQUIREMENT_RULES.html)).\n\nAction ladder ([PSEUDOENZYMES](../../pages/projects/PSEUDOENZYMES.html), decision tree):\n\n1. Confirm the protein is in the family you think (a \"broken\" Cu/Zn-SOD can be a normal\n   Mn-SOD from another family).\n2. Catalytic residues lost: `MARK_AS_OVER_ANNOTATED` the catalytic rows.\n3. Residues present but family motif context broken: `MARK_AS_OVER_ANNOTATED`, with the\n   caveat stated.\n4. Activity refuted biochemically: `REMOVE` the catalytic rows and their dependent\n   cofactor and process rows, and add `NEW` rows for the shown function.\n5. Residues intact, no assay: keep the catalytic row, noting it rests on sequence.\n\n## Application\n\nWorked examples. S. pombe Epe1, a JmjC protein with no detectable demethylase activity:\nelectronic `GO:0032452` histone demethylase activity, `GO:0051213` dioxygenase activity\nand `GO:0016491` oxidoreductase activity rows `REMOVE`; experimental `GO:0032454`\nhistone H3K9 demethylase activity rows `UNDECIDED`, since a latent activity is not\nexcluded. EryCII, a P450-fold activator of the glycosyltransferase EryCIII:\n`GO:0004497` monooxygenase activity, `GO:0005506` iron ion binding and `GO:0020037`\nheme binding `REMOVE`. Human pseudokinases illustrate the replacement terms: STRAD\nactivates LKB1 (`GO:0043539` protein serine/threonine kinase activator activity).",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-13.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-13.html"
  },
  {
   "id": "MF-14",
   "title": "Give each subunit of a complex the activity it performs",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC",
   "aspects": [
    "F"
   ],
   "go_terms": [
    {
     "term_id": "GO:0001671",
     "label": "ATPase activator activity"
    },
    {
     "term_id": "GO:0030674",
     "label": "protein-macromolecule adaptor activity"
    },
    {
     "term_id": "GO:0016247",
     "label": "channel regulator activity"
    }
   ],
   "sources": [
    {
     "kind": "wiki",
     "title": "Contributes to",
     "url": "https://wiki.geneontology.org/index.php/Contributes_to",
     "href": "https://wiki.geneontology.org/index.php/Contributes_to"
    },
    {
     "kind": "issue",
     "title": "go-annotation#3510",
     "url": "https://github.com/geneontology/go-annotation/issues/3510",
     "href": "https://github.com/geneontology/go-annotation/issues/3510"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-14. Give each subunit of a complex the activity it performs\n\n## Decision\n\nAnnotate the catalytic subunit with `enables`; annotate regulatory subunits with a\nregulator activity, bridging subunits with an adaptor activity, and structural subunits\nwith a structural or scaffold activity. Use `contributes_to` only for an irreducible\nmachine whose activity cannot be ascribed to a subset of subunits.\n\n## Context\n\nThe 2020 complex working group established that the MF goes to the subunit\nthat performs it and that non-participating subunits receive no MF\n([wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)). Its\nchecklist asks whether the activity occurs without the subunit, whether the subunit can\nbe given another MF, and whether the annotation would still hold if the qualifier were\ndropped. Details and the complex-membership rules are in\n[protein-complexes.md](../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html).\n\n## Application\n\nWorked examples. Non-catalytic subunits of the Na+/K+-ATPase move from `contributes_to`\nthe pump activity to `GO:0001671` ATPase activator activity, `GO:0030674`\nprotein-macromolecule adaptor activity or `GO:0016247` channel regulator activity, with\n`has_input` the catalytic subunit\n([go-annotation#3510](https://github.com/geneontology/go-annotation/issues/3510)).\neIF2 gamma enables GTPase activity; eIF2 alpha and beta do not.",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-14.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-14.html"
  },
  {
   "id": "MF-15",
   "title": "Annotate transport as a specific transmembrane transporter or channel activity, on the physiological solute",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC_PLUS",
   "provenance_note": "[GOC] for the do-not-annotate and orthology rules; [GOC+] for the membrane-requirement check.",
   "aspects": [
    "F"
   ],
   "go_terms": [
    {
     "term_id": "GO:0022857",
     "label": "transmembrane transporter activity"
    },
    {
     "term_id": "GO:0015267",
     "label": "channel activity"
    },
    {
     "term_id": "GO:0015293",
     "label": "symporter activity"
    },
    {
     "term_id": "GO:0015297",
     "label": "antiporter activity"
    },
    {
     "term_id": "GO:0042626",
     "label": "ATPase-coupled transmembrane transporter activity"
    },
    {
     "term_id": "GO:0005215",
     "label": "transporter activity"
    },
    {
     "term_id": "GO:0005249",
     "label": "voltage-gated potassium channel activity"
    },
    {
     "term_id": "GO:0140104",
     "label": "molecular carrier activity"
    }
   ],
   "related": [
    "MF-8"
   ],
   "sources": [
    {
     "kind": "issue",
     "title": "go-annotation#2311",
     "url": "https://github.com/geneontology/go-annotation/issues/2311",
     "href": "https://github.com/geneontology/go-annotation/issues/2311"
    },
    {
     "kind": "issue",
     "title": "go-annotation#2033",
     "url": "https://github.com/geneontology/go-annotation/issues/2033",
     "href": "https://github.com/geneontology/go-annotation/issues/2033"
    },
    {
     "kind": "repo",
     "title": "FUNCTION_REQUIREMENT_RULES",
     "path": "projects/FUNCTION_REQUIREMENT_RULES.md",
     "href": "../../pages/projects/FUNCTION_REQUIREMENT_RULES.html"
    },
    {
     "kind": "repo",
     "title": "TCDB",
     "path": "projects/TCDB.md",
     "href": "../../pages/projects/TCDB.html"
    },
    {
     "kind": "repo",
     "title": "NONPHYSIOLOGICAL_REACTIONS",
     "path": "projects/NONPHYSIOLOGICAL_REACTIONS.md",
     "href": "../../pages/projects/NONPHYSIOLOGICAL_REACTIONS.html"
    },
    {
     "kind": "drive",
     "title": "Transporter activity guidelines (archived)",
     "url": "https://drive.google.com/open?id=1h26nq-KExaYZKuBVKqJ2yWkK06dCWUQelZkTI262_PA",
     "href": "https://drive.google.com/open?id=1h26nq-KExaYZKuBVKqJ2yWkK06dCWUQelZkTI262_PA"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-15. Annotate transport as a specific transmembrane transporter or channel activity, on the physiological solute\n\n## Decision\n\nUse a descendant of `GO:0022857` transmembrane transporter activity that names the\nsolute and, where known, the mechanism (`GO:0015267` channel activity, `GO:0015293`\nsymporter activity, `GO:0015297` antiporter activity, `GO:0042626` ATPase-coupled\ntransmembrane transporter activity). Never annotate `GO:0005215` transporter activity\n(do-not-annotate). Name the physiological solute, not the tracer. Do not transfer\nsubstrate specificity across species without clear 1:1 orthology.\n\n## Context\n\nGO:0005215 was made do-not-annotate in 2019\n([go-annotation#2311](https://github.com/geneontology/go-annotation/issues/2311)).\nTransporter substrate specificity diverges among paralogs, so a mammalian substrate\nshould not be propagated to yeast without a clear 1:1 relationship\n([go-annotation#2033](https://github.com/geneontology/go-annotation/issues/2033)).\nA transmembrane transporter needs a transmembrane segment or a membrane barrel, carrier\nor channel family (FRR:0004 in [FUNCTION_REQUIREMENT_RULES](../../pages/projects/FUNCTION_REQUIREMENT_RULES.html)).\nTCDB classification would be a good source of transporter MF annotations, but GO has no\n`tc2go` pipeline, and family-level TC leads over-propagate\n([TCDB](../../pages/projects/TCDB.html)).\n\n## Application\n\nWorked examples. A ⁸⁶Rb⁺ flux assay on a potassium channel supports `GO:0005249`\nvoltage-gated potassium channel activity if voltage gating is shown, or a potassium\nchannel term otherwise; it does not support a rubidium term (GO obsoleted rubidium ion\ntransmembrane transporter activity because it \"represents an assay\";\n[NONPHYSIOLOGICAL_REACTIONS](../../pages/projects/NONPHYSIOLOGICAL_REACTIONS.html)). A secreted\nlipid-binding protein that shuttles its ligand is a carrier (`GO:0140104`), not a\ntransporter ([MF-8](#MF-8)).",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-15.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-15.html"
  },
  {
   "id": "MF-16",
   "title": "Annotate a receptor's signaling activity and a ligand's ligand activity, not reciprocal binding",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IBA"
   ],
   "go_terms": [
    {
     "term_id": "GO:0038023",
     "label": "signaling receptor activity"
    },
    {
     "term_id": "GO:0048018",
     "label": "receptor ligand activity"
    },
    {
     "term_id": "GO:0005102",
     "label": "signaling receptor binding"
    },
    {
     "term_id": "GO:0007165",
     "label": "signal transduction"
    },
    {
     "term_id": "GO:0004941",
     "label": "beta2-adrenergic receptor activity"
    },
    {
     "term_id": "GO:0015026",
     "label": "coreceptor activity"
    }
   ],
   "related": [
    "MF-2"
   ],
   "sources": [
    {
     "kind": "drive",
     "title": "MF guidelines for GO-CAM",
     "url": "https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4",
     "href": "https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4"
    },
    {
     "kind": "repo",
     "title": "LIGANDS_IN_SIGNALING",
     "path": "projects/LIGANDS_IN_SIGNALING.md",
     "href": "../../pages/projects/LIGANDS_IN_SIGNALING.html"
    },
    {
     "kind": "repo",
     "title": "TRANSCRIPTION_FACTORS",
     "path": "projects/TRANSCRIPTION_FACTORS.md",
     "href": "../../pages/projects/TRANSCRIPTION_FACTORS.html"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-16. Annotate a receptor's signaling activity and a ligand's ligand activity, not reciprocal binding\n\n## Decision\n\nA signaling receptor enables `GO:0038023` signaling receptor activity or a descendant\n(ligand-specific where the evidence identifies the ligand). A protein ligand enables\n`GO:0048018` receptor ligand activity or a descendant, with `has_input` its receptor. The\nreceptor's input is its effector, not its ligand. Small-molecule ligands are not\nannotated.\n\n## Context\n\nThe GO-CAM receptor guideline (reviewed 2023 and 2026) keeps the causal flow\nfrom ligand to receptor to effector\n([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).\nIn the ontology, `GO:0048018` receptor ligand activity has part `GO:0005102` signaling\nreceptor binding and is part of `GO:0007165` signal transduction, so a ligand annotated\ncorrectly does not also need the binding term. Ligands carrying only a\nreceptor-specific binding term (such as \"Roundabout binding\") instead of a ligand\nactivity are a recurring gap ([LIGANDS_IN_SIGNALING](../../pages/projects/LIGANDS_IN_SIGNALING.html)).\nPathway membership of ligands and receptors is covered in\n[regulation-and-signaling.md](../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html).\n\n## Application\n\nWorked example. Netrin-1 enables `GO:0048018` receptor ligand activity with\n`has_input` DCC (`genes/human/NTN1`); its IBA rows to DNA-binding transcription factor\nactivity were `REMOVE` ([TRANSCRIPTION_FACTORS](../../pages/projects/TRANSCRIPTION_FACTORS.html)). A\nligand-specific receptor term such as `GO:0004941` beta2-adrenergic receptor activity\nneeds evidence that identifies the ligand ([MF-2](#MF-2)). A coreceptor that is\nactivated by the ligand-bound receptor enables `GO:0015026` coreceptor activity.",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-16.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-16.html"
  },
  {
   "id": "MF-17",
   "title": "Reserve regulator MFs for direct, non-covalent action on an identified target activity",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC_PLUS",
   "provenance_note": "[GOC+]. GOC states the definition; the \"covalent means catalytic\" and \"unknown mechanism means BP\" rules are spread across several calls and are stated here together.",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IPI",
    "IC"
   ],
   "go_terms": [
    {
     "term_id": "GO:0098772",
     "label": "molecular function regulator activity"
    },
    {
     "term_id": "GO:0004857",
     "label": "enzyme inhibitor activity"
    },
    {
     "term_id": "GO:0008047",
     "label": "enzyme activator activity"
    },
    {
     "term_id": "GO:0019887",
     "label": "protein kinase regulator activity"
    },
    {
     "term_id": "GO:0008200",
     "label": "ion channel inhibitor activity"
    },
    {
     "term_id": "GO:0004867",
     "label": "serine-type endopeptidase inhibitor activity"
    },
    {
     "term_id": "GO:0004860",
     "label": "protein kinase inhibitor activity"
    },
    {
     "term_id": "GO:0140311",
     "label": "protein sequestering activity"
    }
   ],
   "differences": [
    {
     "prior_source": "[wiki: Guidelines for new Molecular Functions](https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions); term definition of `GO:0140416`",
     "prior_said": "Regulators act \"solely by non-covalent means\"; but GO:0140416 transcription regulator inhibitor activity is defined \"via direct binding and/or post-translational modification\"",
     "we_recommend": "Treat covalent modification as a catalytic activity with `has_input` the target",
     "why": "The ontology is internally inconsistent; we follow the general MF principle and flag the term (Open questions)"
    },
    {
     "prior_source": "[wiki: Annotation Conf. Call, January 14, 2014](https://wiki.geneontology.org/index.php/Annotation_Conf._Call,_January_14,_2014)",
     "prior_said": "Proposed making enzyme regulator activity a child of enzyme binding; left open whether ortholog binding evidence suffices",
     "we_recommend": "Direct binding to the target is required; binding may come from a second experiment combined by IC, but binding shown only in an ortholog supports ISS at most",
     "why": "Keeps the regulator claim about the product itself"
    }
   ],
   "open_questions": [
    "**Covalent regulators.** Should `GO:0140416` transcription regulator inhibitor activity (and similar terms) drop \"and/or post-translational modification\" from the definition, to match the regulator principle?"
   ],
   "sources": [
    {
     "kind": "wiki",
     "title": "Guidelines for new Molecular Functions",
     "url": "https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions",
     "href": "https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions"
    },
    {
     "kind": "issue",
     "title": "go-annotation#2131",
     "url": "https://github.com/geneontology/go-annotation/issues/2131",
     "href": "https://github.com/geneontology/go-annotation/issues/2131"
    },
    {
     "kind": "wiki",
     "title": "Annotation Conf. Call, January 14, 2014",
     "url": "https://wiki.geneontology.org/index.php/Annotation_Conf._Call,_January_14,_2014",
     "href": "https://wiki.geneontology.org/index.php/Annotation_Conf._Call,_January_14,_2014"
    },
    {
     "kind": "wiki",
     "title": "Annotation Conf. Call 2019-11-19",
     "url": "https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19",
     "href": "https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19"
    },
    {
     "kind": "wiki",
     "title": "Annotation Conf. Call 2020-02-04",
     "url": "https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04",
     "href": "https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-17. Reserve regulator MFs for direct, non-covalent action on an identified target activity\n\n## Decision\n\nAnnotate a molecular function regulator (a descendant of `GO:0098772`, such as\n`GO:0004857` enzyme inhibitor activity, `GO:0008047` enzyme activator activity,\n`GO:0019887` protein kinase regulator activity or `GO:0008200` ion channel inhibitor\nactivity) only when the product binds the target and changes its activity without\ncovalently modifying it. Name the target in `has_input`. If the target is modified\ncovalently, annotate the catalytic activity. If direct action is not shown, annotate the\nBP regulation term instead. Never annotate `GO:0098772` itself (do-not-annotate).\n\n## Context\n\nGO defines a regulator as acting \"via non-covalent binding that does not\nresult in covalent modification to the target\"; catalytic activities that modify a\ntarget are out of scope for regulator terms\n([wiki: Guidelines for new Molecular Functions](https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions)).\nPomBase's practice, recorded in the 2018 IPI discussion, is to capture direct\nregulation as an MF and to avoid BP \"regulation of enzyme activity\", which can be far\nupstream ([go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)).\nIn 2014 GO agreed that binding and regulation may come from two experiments in one\npaper, or from two papers, and be combined into one regulator annotation by IC\n([wiki: Annotation Conf. Call, January 14, 2014](https://wiki.geneontology.org/index.php/Annotation_Conf._Call,_January_14,_2014)).\nIPI is permitted for enzyme regulator terms: gorule-0000007 applies only to `is_a`\ndescendants of catalytic activity ([go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131)).\n\n## Application\n\nWorked examples.\n\n- A serpin that binds and inactivates a serine protease: `GO:0004867` serine-type\n  endopeptidase inhibitor activity, `has_input` the protease.\n- A kinase that phosphorylates and inactivates another kinase: protein kinase activity\n  with `has_input` the target, not `GO:0004860` protein kinase inhibitor activity.\n- A knockdown that raises a kinase's activity in cell lysates, with no binding data:\n  a BP regulation term ([regulation-and-signaling.md](../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html)),\n  not an MF.\n- A decoy receptor that binds a ligand so it cannot reach the signaling receptor: in\n  GO-CAM, binding that `directly negatively regulates` the receptor activity\n  ([wiki: Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19));\n  in standard annotation, `GO:0140311` protein sequestering activity with `has_input`\n  the ligand.\n- An endogenous small molecule that activates the product is not a reason for a\n  regulator MF on the product. The 2019–2020 reannotation turned `activated_by`\n  extensions into a binding annotation on the product, and restricted\n  `directly regulates` to activities of different gene products\n  ([wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)).",
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-17.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-17.html"
  },
  {
   "id": "MF-18",
   "title": "Treat an electronic MF as a claim about the family, and check it fits this member",
   "status": "proposed",
   "topic": "MF",
   "provenance": "GOC_PLUS",
   "aspects": [
    "F"
   ],
   "evidence_codes": [
    "IBA",
    "IEA"
   ],
   "go_terms": [
    {
     "term_id": "GO:0047372",
     "label": "monoacylglycerol lipase activity"
    }
   ],
   "related": [
    "MF-13",
    "MF-12",
    "MF-8"
   ],
   "sources": [
    {
     "kind": "repo",
     "title": "CLAUDE.md",
     "path": "CLAUDE.md",
     "href": "https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md"
    },
    {
     "kind": "repo",
     "title": "ENZYME_SPECIFICITY",
     "path": "projects/ENZYME_SPECIFICITY.md",
     "href": "../../pages/projects/ENZYME_SPECIFICITY.html"
    }
   ],
   "date": "2026-11-15",
   "body": "# MF-18. Treat an electronic MF as a claim about the family, and check it fits this member\n\n## Decision\n\nAn IEA or IBA MF row is a claim that this member shares the family's activity. Accept\nit when the member retains what the activity requires and nothing specific contradicts\nit. Challenge it with member-specific evidence (lost residues, different subfamily,\ndivergent substrate, contrary experiment), not with the type of evidence.\n\n## Context\n\nAn IBA carries a PAINT curator's judgement about where in the tree a function\narose; challenging it means arguing with the node placement, not with donor counts\n([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md); [phylogenetic-propagation.md](../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html)).\nInterPro2GO and UniRule mappings are usually right for most members and wrong for\nspecific subfamilies, which is where curated exception rules belong\n([electronic-annotation.md](../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html)). The common MF failure modes,\nall with worked cases above, are pseudoenzymes ([MF-13](#MF-13)), wrong-paralog\nspecificity ([MF-12](#MF-12)), and adaptor or dbTF terms over-propagated to members\nthat do not bridge or bind DNA ([MF-8](#MF-8);\n[transcription-regulation.md](../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html)).\n\n## Application\n\nWorked example. C. albicans LPL1's `GO:0047372` monoacylglycerol lipase activity IBA\ntraced to the S. cerevisiae ROG1 paralog at the PAINT node; LPL1 sits in the\nphospholipase B branch, so the row was `REMOVE`\n([ENZYME_SPECIFICITY](../../pages/projects/ENZYME_SPECIFICITY.html)).",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/MF-18.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/MF-18.html"
  }
 ],
 "chapters": [
  {
   "id": "MF",
   "title": "Molecular function",
   "status": "proposed",
   "aspects": [
    "F"
   ],
   "differences": [
    {
     "prior_source": "[wiki: Contributes to](https://wiki.geneontology.org/index.php/Contributes_to)",
     "prior_said": "RNA polymerase example uses `GO:0001055` RNA polymerase II activity",
     "we_recommend": "Use a live term (`GO:0003899` DNA-directed RNA polymerase activity)",
     "why": "GO:0001055 is obsolete; the example needs updating"
    },
    {
     "prior_source": "[wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)",
     "prior_said": "Lists `GO:0140299` as \"small molecule sensor activity\"",
     "we_recommend": "The term is now labelled \"molecular sensor activity\"",
     "why": "Label drift; the page was last reviewed in 2022"
    }
   ],
   "date": "2026-11-15",
   "body": "# Molecular function: GO annotation guidelines\n\nStatus: see each guideline · Part of [GO_GUIDELINES](../../pages/projects/GO_GUIDELINES.html)\n\n**In brief:**\n\n- A molecular function (MF) annotation says that this gene product, alone or as an\n  identified part of a complex, *performs* an activity. It is not a statement about a\n  process the product takes part in, a phenotype, or a partner it was seen with.\n- Prefer an activity to a binding term. Bare `GO:0005515` protein binding is never a\n  goal: in review, replace it with an informative term that the same paper supports, or\n  remove it.\n- Annotate the activity the protein evolved to perform, on its physiological substrate.\n  An assay substrate, a proxy compound or a measurable side reaction is not a function.\n- Family membership is a hypothesis about activity, not evidence of it. Check the\n  catalytic residues, the substrate, the cofactor and the subunit before accepting a\n  family-derived enzyme term.\n- A regulator MF needs direct, non-covalent action on an identified target activity.\n  Without that, the claim belongs in biological process (BP).\n- The term is as deep as *this row's* evidence. A correct general term is refined\n  (`MODIFY`) only when the row's own evidence supports the deeper term.\n\n## Scope\n\n\nThis document covers what an MF annotation asserts and how to choose the term:\nactivity versus binding; the protein binding policy; non-catalytic activities\n(adaptor, scaffold, sequestering, carrier, chaperone); enzyme activities, substrate\nspecificity and promiscuous or non-physiological reactions; pseudoenzymes;\ntransporters and channels; receptors and ligands (briefly); and regulator activities.\n\nCovered elsewhere: the `contributes_to` qualifier and complex subunits in detail\n([protein-complexes.md](../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html)); signaling pathways and BP regulation\n([regulation-and-signaling.md](../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html)); transcription regulators\n([transcription-regulation.md](../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html)); evidence codes\n([evidence-codes.md](../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html)); extension syntax\n([annotation-extensions.md](../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html)); NOT annotations\n([qualifiers-and-negation.md](../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html)); IBA and electronic\npipelines ([phylogenetic-propagation.md](../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html),\n[electronic-annotation.md](../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html)).\n\n## Principles\n\n\n**An MF is something a molecule does.** The GO editors' definition is \"a molecular\nprocess that can be carried out by the action of a single macromolecular machine\",\na protein, a non-coding RNA or a complex, usually through direct physical interaction\nwith other molecules ([wiki: Guidelines for new Molecular Functions](https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions)).\nMF and BP are meant to be orthogonal: a concept that is really a process (for example\nthe obsolete \"apoptosis inhibitor activity\") does not become a function by adding the\nword \"activity\".\n\n**The function is the biological one.** MF substrate specificity represents \"the\ninferred, in vivo biological specificity of the gene product, which may or may not\ncorrespond exactly to the substrate used in the experiment\"\n([wiki: Guidelines for catalytic activity terms](https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms)).\nCurators annotate the conclusion of a paper, not its read-out\n([Drive: 2017 GOC training talk](https://drive.google.com/open?id=1m9v6KbdXs32ihzMjqGJYQpuK1Qf49Gh-)).\n\n**Binding is the weakest kind of MF statement.** Every activity involves binding.\nA binding term is informative only when binding is the end point (a stable,\nbiologically meaningful interaction) or when it is all the evidence shows. GO's\nnon-catalytic MF refactoring created adaptor, carrier, sequestering, receptor and\nchaperone terms precisely so that curators could say what a binding protein does\n([wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)).\n\n**Depth follows evidence, row by row.** A review judges each claim about the gene,\nbut the action on a row depends on what that row's evidence supports\n([CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md), maintainer ruling of 2026-11-14).\n\n## Rules\n\nEach rule is its own record in this folder. Its frontmatter holds the metadata (status, provenance, differences from prior guidance, open questions, sources).\n\n\n\n## Decision aid\n\n\n### Choosing an MF for a binding protein\n\n| What the evidence shows | Term family | Required context |\n|---|---|---|\n| Catalysis of a reaction (assay, active-site mutant) | descendant of `GO:0003824` catalytic activity | substrate in the term or `has_input`; never IPI |\n| Brings two or more molecules together so they act together | `GO:0060090` molecular adaptor activity or a child (`GO:0030674` and below) | `has_input` both partners |\n| Holds a complex together structurally | `GO:0140378` protein complex scaffold activity or `GO:0005198` structural molecule activity | complex in CC |\n| Binds a molecule to keep it from partners or location | `GO:0140313` molecular sequestering activity (`GO:0140311` for proteins) | `has_input` the sequestered molecule; BP is negative regulation of its process |\n| Binds and moves with a molecule to an acceptor or location | `GO:0140104` molecular carrier activity | `has_input` the cargo |\n| Moves a solute across a membrane without moving itself | descendant of `GO:0022857` | solute in term or `has_input` |\n| Binds a target and changes its activity, non-covalently | descendant of `GO:0098772` (not the root) | `has_input` the target |\n| Receives a signal and transmits it | descendant of `GO:0038023` signaling receptor activity | `has_input` the effector |\n| Activates a receptor as its ligand | `GO:0048018` receptor ligand activity or a child | `has_input` the receptor |\n| Assists folding | `GO:0044183` protein folding chaperone; carrier holdases `GO:0140309` | see [UNFOLDED_PROTEIN_BINDING](../../pages/projects/UNFOLDED_PROTEIN_BINDING.html) |\n| Binding of a defined class, role unknown | class-level binding child (e.g. `GO:0019901`) | `has_input` the specific partner |\n| Binding of an unnamed protein class, role unknown | nothing new; in review `MODIFY` or `REMOVE` existing `GO:0005515` | partner in With/From |\n\n### Reviewing a measured enzyme activity\n\n1. Is the activity on the physiological substrate? If no, go to [MF-10](#MF-10).\n2. Is the protein catalytically competent (residues, motif, assay)? If no, go to\n   [MF-13](#MF-13).\n3. Is the substrate, cofactor, mechanism and subunit right? If no, go to\n   [MF-12](#MF-12).\n4. Is it the protein's evolved activity? Apply the tiers of [MF-11](#MF-11).\n5. Is the term as deep as this row's evidence, and no deeper? See [MF-2](#MF-2).\n\n### MF regulator or BP regulation?\n\n| Evidence | Annotation |\n|---|---|\n| Direct binding and a change in the target's activity, no covalent change | regulator MF, `has_input` target |\n| Covalent modification of the target that changes its activity | catalytic MF, `has_input` target |\n| Change in target activity, mechanism unknown | BP regulation term |\n| Binding only | class-level binding term at most |\n| Binding (one experiment) plus regulation (another) | regulator MF by IC citing both |\n\n## Common errors\n\n\n**Bare protein binding kept as core.** Reviews that `ACCEPT` or `KEEP_AS_NON_CORE`\nGO:0005515 preserve an annotation with no functional content. Fix: `MODIFY` to the\ninformative term the same paper supports, else `REMOVE` ([MF-5](#MF-5)).\n\n**Adaptor activity from one IPI hit.** A single binary interaction becomes\n`GO:0060090`. Fix: use a class-level binding term unless two bridged partners are\nshown ([MF-8](#MF-8)).\n\n**Scaffold filed as adaptor, or adaptor as scaffold.** Fix: check the branch. Complex\nscaffolds are structural molecule activity; condensate scaffolds and histone readers are\nadaptor children.\n\n**Implied binding stacked on an activity.** ATP binding, metal ion binding and heme\nbinding rows beside a kinase, metalloenzyme or P450. Fix: do not add them; in review,\nmark them non-core or `TOO_GENERAL` rather than removing a true statement ([MF-4](#MF-4)).\nWhen the activity itself is wrong (a pseudoenzyme), remove the dependent rows with it\n([MF-13](#MF-13)).\n\n**Assay substrate as function.** Histone kinase activity for a kinase tested on\nhistones; a chromogenic-substrate reductase; a rubidium flux. Fix: annotate the\nphysiological activity or the general activity the assay supports ([MF-10](#MF-10)).\n\n**Catalytic activity by IPI.** Fix: re-code to the assay that shows catalysis, or remove\n(gorule-0000007).\n\n**Family membership read as specificity.** Transaminase activity for a phospho-lyase\nin the aminotransferase family; UDP-sugar transferase for a dTDP-sugar enzyme. Fix:\ncheck the four axes of [MF-12](#MF-12).\n\n**Regulator MF from a knockdown.** A loss-of-function change in an enzyme's activity\nannotated as enzyme activator activity. Fix: BP regulation unless direct binding is shown\n([MF-17](#MF-17)).\n\n**GTPase activity on GPCRs and G beta/gamma.** Fix: `REMOVE`; the receptor's MF is\nreceptor activity, and G beta/gamma hold G alpha in the GDP-bound state rather than\nhydrolysing GTP ([FUNCTION_REQUIREMENT_RULES](../../pages/projects/FUNCTION_REQUIREMENT_RULES.html)).\n\n**Transporter activity root.** `GO:0005215` is do-not-annotate. Fix: use the specific\ntransmembrane transporter, channel or carrier term the evidence supports.\n\n**Oligomerisation as function.** `GO:0042802` identical protein binding or protein\ndimerization activity used to record that a protein forms a dimer. Fix: capture the\ncomplex in CC; keep an oligomerisation MF only when the oligomer is the functional\npoint, and expect these terms to become do-not-annotate ([MF-5](#MF-5)).\n\n## Reading list\n\n\n**GO wiki**\n\n- [Guidelines for new Molecular Functions](https://wiki.geneontology.org/index.php/Guidelines_for_new_Molecular_Functions) (reviewed 2024)\n- [Guidelines for catalytic activity terms](https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms)\n- [Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions) (reviewed 2022)\n- [Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding) (2020 proposal, marked to be reviewed)\n- [Binding Guidelines](https://wiki.geneontology.org/index.php/Binding_Guidelines) (2014, partly unresolved)\n- [Guidelines for new Binding terms](https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms)\n- [Enables](https://wiki.geneontology.org/index.php/Enables) (reviewed 2018)\n- [Contributes to](https://wiki.geneontology.org/index.php/Contributes_to) (reviewed 2023, edited 2026)\n- [Inferred from Physical Interaction (IPI)](https://wiki.geneontology.org/index.php/Inferred_from_Physical_Interaction_%28IPI%29) (reviewed 2018)\n- [Proposal to obsolete children of \"transcription factor binding\"](https://wiki.geneontology.org/index.php/Proposal_to_obsolete_children_of_%22transcription_factor_binding%22)\n- [Annotation Conf. Call, January 14, 2014](https://wiki.geneontology.org/index.php/Annotation_Conf._Call,_January_14,_2014)\n- [Annotation Conf. Call 2019-11-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2019-11-19)\n- [Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)\n- [Annotation Conf. Call 2021-08-03](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2021-08-03)\n\n**GO Consortium Drive**\n\n- [MF guidelines for GO-CAM (copy; reviewed 2026-03)](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)\n- [IEA WG: protein binding do_not_annotate proposal (2026-05)](https://drive.google.com/open?id=1KKM7gxsPvQgszjppuyD_ZldM_T8cGV0ajSUIfLmyNQc) (pending)\n- [Protein binding announcement, go-ontology#11094](https://drive.google.com/open?id=1CDLNsl-FgwqdsLP3jTfuA7h3nTdGq_ASEyYyLiTLhWE) (status unclear)\n- [Protein oligomerization obsoletion proposal](https://drive.google.com/open?id=1JxzNwl1fr5Fj-IJy_Fo1lLfAlAQB8IxPDwwYKxIXBZo)\n- [2017 GOC training talk: translating research data into GO annotations](https://drive.google.com/open?id=1m9v6KbdXs32ihzMjqGJYQpuK1Qf49Gh-)\n- [Transporter activity annotation guidelines (archived)](https://drive.google.com/open?id=1h26nq-KExaYZKuBVKqJ2yWkK06dCWUQelZkTI262_PA)\n\n**go-annotation issues**\n\n- [go-annotation#1514](https://github.com/geneontology/go-annotation/issues/1514), [#1519](https://github.com/geneontology/go-annotation/issues/1519) (non-physiological gamma-glutamyltransferase)\n- [go-annotation#1953](https://github.com/geneontology/go-annotation/issues/1953) (in vitro histone substrates)\n- [go-annotation#2033](https://github.com/geneontology/go-annotation/issues/2033) (transporter specificity transfer)\n- [go-annotation#2131](https://github.com/geneontology/go-annotation/issues/2131) (gorule-0000007, IPI and catalytic activity)\n- [go-annotation#2311](https://github.com/geneontology/go-annotation/issues/2311) (transporter activity do-not-annotate)\n- [go-annotation#2683](https://github.com/geneontology/go-annotation/issues/2683) (heterodimerization review)\n- [go-annotation#3166](https://github.com/geneontology/go-annotation/issues/3166) (drug binding obsoletion)\n- [go-annotation#3314](https://github.com/geneontology/go-annotation/issues/3314) (interspecies protein binding)\n- [go-annotation#3510](https://github.com/geneontology/go-annotation/issues/3510) (non-catalytic transporter subunits)\n- [go-annotation#5840](https://github.com/geneontology/go-annotation/issues/5840) (benzil reductase)\n\n**Papers**\n\n- [PMID:40703034](https://europepmc.org/article/MED/40703034) de Crécy-Lagard et al. 2025, assessment categories for function predictions\n\n**Repository pages**\n\n- [CLAUDE.md](https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md) (MODIFY/TOO_GENERAL ruling; protein binding; measured activity is not function; IBA reading)\n- [protein_binding_policy.py](https://github.com/ai4curation/ai-gene-review/blob/main/src/ai_gene_review/validation/protein_binding_policy.py)\n- [action consistency](https://github.com/ai4curation/ai-gene-review/blob/main/docs/action_consistency.md)\n- [MOLECULAR_ADAPTOR_ACTIVITY](../../pages/projects/MOLECULAR_ADAPTOR_ACTIVITY.html) and its GRB2, LDLRAP1 and RPTOR worked examples\n- [ENZYME_SPECIFICITY](../../pages/projects/ENZYME_SPECIFICITY.html)\n- [NONPHYSIOLOGICAL_REACTIONS](../../pages/projects/NONPHYSIOLOGICAL_REACTIONS.html)\n- [PSEUDOENZYMES](../../pages/projects/PSEUDOENZYMES.html)\n- [FUNCTION_REQUIREMENT_RULES](../../pages/projects/FUNCTION_REQUIREMENT_RULES.html)\n- [UNFOLDED_PROTEIN_BINDING](../../pages/projects/UNFOLDED_PROTEIN_BINDING.html)\n- [LIGANDS_IN_SIGNALING](../../pages/projects/LIGANDS_IN_SIGNALING.html)\n- [GPCR](../../pages/projects/GPCR.html)\n- [TCDB](../../pages/projects/TCDB.html)\n- [RHEA](../../pages/projects/RHEA.html)\n- [TRANSCRIPTION_FACTORS](../../pages/projects/TRANSCRIPTION_FACTORS.html)",
   "open_questions": [],
   "path": "projects/GO_GUIDELINES/guidelines/MF/README.md",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/MF/README.html"
  }
 ],
 "unsplit_rules": [
  {
   "id": "AE-1",
   "title": "An extension must narrow the term, so that the annotation stays true without it. Do not use extensions for conditions, negation or exclusivity.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-1"
  },
  {
   "id": "AE-2",
   "title": "Use comma for facts that hold together and pipe for independent statements. Make separate annotations for alternative substrates or targets.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-2"
  },
  {
   "id": "AE-3",
   "title": "Use `has_input` for the specific, physiologically relevant molecular target that the term does not already name: a substrate, a binding partner, a target gene, or the gene product a regulator acts on.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-3"
  },
  {
   "id": "AE-4",
   "title": "Use `has_output` only for a specific product the term does not already name, and only for a single reaction.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-4"
  },
  {
   "id": "AE-5",
   "title": "Use `occurs_in` for the place where an MF happens, or where *every* step of a BP happens. Choose a location that places the activity unambiguously, and do not restate the term.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-5"
  },
  {
   "id": "AE-6",
   "title": "On CC annotations, use `part_of` with a cell or anatomy term for the cell or tissue in which the component sits, and an existence relation for the stage.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-6"
  },
  {
   "id": "AE-7",
   "title": "Use `happens_during` only for a biological phase or life stage, never for a process that merely coincides.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-7"
  },
  {
   "id": "AE-8",
   "title": "Use `part_of`(BP) on an MF to say which process the activity serves. Make the matching BP annotation as a separate row, and do not add a `part_of` the ontology already entails.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-8"
  },
  {
   "id": "AE-9",
   "title": "Do not use `part_of(Y)` to rebuild a precomposed \"X involved in Y\" term that GO has obsoleted for GO-CAM.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-9"
  },
  {
   "id": "AE-10",
   "title": "Prefer an extension for target-, cell-type- and stage-specific context. Request a precomposed term only for a recognised biological concept that is not an arbitrary cross-product.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-10"
  },
  {
   "id": "AE-11",
   "title": "Keep extensions to what a single statement can hold. Causal, chained or multi-activity knowledge goes in a GO-CAM.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-11"
  },
  {
   "id": "AE-12",
   "title": "An extension needs the same evidence as the annotation. Do not expect or invent extensions on propagated rows.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-12"
  },
  {
   "id": "AE-13",
   "title": "Before judging a row, read its extension in QuickGO or GOA. The repository's cached GOA file does not include one.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-13"
  },
  {
   "id": "AE-14",
   "title": "When reviewing, judge an extension like the term: keep it if it holds, fix its relation if that is legacy, and remove it if it restates the term or encodes a condition.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/annotation-extensions.html#ae-14"
  },
  {
   "id": "BP-1",
   "title": "Use `involved in` only when the gene product's activity is a step of the process",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-1"
  },
  {
   "id": "BP-2",
   "title": "Name the entity that performs the step; substrates and products are not participants unless they do some of the work",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-2"
  },
  {
   "id": "BP-3",
   "title": "Run the comparator check before treating an absence as a gap",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-3"
  },
  {
   "id": "BP-4",
   "title": "When the mechanism is unknown, use `acts upstream of or within`, choose a sign, and choose the most proximal process",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-4"
  },
  {
   "id": "BP-5",
   "title": "Use `acts upstream of` (without \"or within\") only when the mechanism is known and the activity is outside the process and does not regulate it",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-5"
  },
  {
   "id": "BP-6",
   "title": "Annotate the process the gene product acts in, not the readout that was measured",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-6"
  },
  {
   "id": "BP-7",
   "title": "Organism-level and other \"high-level\" processes need a mechanism",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-7"
  },
  {
   "id": "BP-8",
   "title": "Give pleiotropic core machinery its core processes, not every process it affects",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-8"
  },
  {
   "id": "BP-9",
   "title": "Developmental processes: annotate the cell-level step, at the right grain, for genes that perform it",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-9"
  },
  {
   "id": "BP-10",
   "title": "Cell death: choose the phase, keep regulation for specific effects, and do not equate death with apoptosis",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-10"
  },
  {
   "id": "BP-11",
   "title": "Do not request, add or split precomposed \"X involved in Y\" terms; decompose them to X and record where Y went",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-11"
  },
  {
   "id": "BP-12",
   "title": "Annotate the step term when the evidence reaches it; do not demand BP specificity that only restates the MF",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-12"
  },
  {
   "id": "BP-13",
   "title": "Choose the deepest term the row's own evidence supports, and no deeper",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-13"
  },
  {
   "id": "BP-14",
   "title": "In review, separate core processes from real but peripheral ones, and reserve REMOVE for contradicted claims",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-14"
  },
  {
   "id": "BP-15",
   "title": "Do not propagate developmental, behavioural or stimulus-response terms without a conserved mechanism, and check that the pathway can exist in the target taxon",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/biological-process.html#bp-15"
  },
  {
   "id": "CAM-1",
   "title": "Model activities, not genes: each activity unit has one function, one enabler, one location chain and one process chain.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-1"
  },
  {
   "id": "CAM-2",
   "title": "Give a gene product a second activity node only when the function, input, location, process or time differs.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-2"
  },
  {
   "id": "CAM-3",
   "title": "The enabler is the gene product that performs the activity; use a complex as enabler only for an emergent activity, and never the root complex term.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-3"
  },
  {
   "id": "CAM-4",
   "title": "Type each activity by the role it plays in the flow; a bare binding term is not an activity.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-4"
  },
  {
   "id": "CAM-5",
   "title": "`has input` names what the activity acts on; the ligand of a receptor is upstream, not input.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-5"
  },
  {
   "id": "CAM-6",
   "title": "Link metabolic steps through the ChEBI product; use `provides input for` only when the intermediate is a macromolecule or has no ChEBI entry.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-6"
  },
  {
   "id": "CAM-7",
   "title": "Choose the causal relation by relationship type, then sign, then directness.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-7"
  },
  {
   "id": "CAM-8",
   "title": "Use a \"directly\" relation only between successive activities of different gene products, where the upstream activity acts on the downstream enabler; route small-molecule effects through the molecule.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-8"
  },
  {
   "id": "CAM-9",
   "title": "Control through gene expression is always indirect; the regulator's input is the target gene and its process names the mechanism.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-9"
  },
  {
   "id": "CAM-10",
   "title": "Use `constitutively upstream of` for required housekeeping steps, not regulation.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-10"
  },
  {
   "id": "CAM-11",
   "title": "Use `removes input for` only for a switch in which the upstream activity uses up the downstream activity's input site.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-11"
  },
  {
   "id": "CAM-12",
   "title": "Connect an activity to a process by a causal edge only when the mechanism is unknown; otherwise use `part of`.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-12"
  },
  {
   "id": "CAM-13",
   "title": "Give each activity one location that resolves to a distinct compartment.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-13"
  },
  {
   "id": "CAM-14",
   "title": "A material-flow edge must not cross a membrane without the activity that crosses it; a regulation edge may join compartments only if the regulated protein moves.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-14"
  },
  {
   "id": "CAM-15",
   "title": "Every asserted edge carries its own evidence: one ECO class and one reference per evidence instance, supporting that edge.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-15"
  },
  {
   "id": "CAM-16",
   "title": "A model is a module: include the activities specific to its process, reuse general machinery by reference, and link models through a shared activity.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-16"
  },
  {
   "id": "CAM-17",
   "title": "Know the standard annotations your model will export, and review exported rows against the model.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-17"
  },
  {
   "id": "CAM-18",
   "title": "In pathway imports, the enabler is the active unit, not the catalyst entity as drawn.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-18"
  },
  {
   "id": "CAM-19",
   "title": "When reviewing, check each activity against the gene review, and treat a model as one curator's assertion, not as evidence.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/gocam-modeling.html#cam-19"
  },
  {
   "id": "CC-1",
   "title": "Use `located_in` by default, `is_active_in` only when the activity is shown at that location, and `part_of` only for complex terms.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-1"
  },
  {
   "id": "CC-2",
   "title": "Do not make new `colocalizes_with` annotations; resolve existing ones to `located_in`, `is_active_in`, a binding term, or removal.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-2"
  },
  {
   "id": "CC-3",
   "title": "Treat an `is_active_in` row from IBA, a root-term ND, or a pipeline default as no stronger than `located_in` until the activity location is checked.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-3"
  },
  {
   "id": "CC-4",
   "title": "Annotate residence, not transit.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-4"
  },
  {
   "id": "CC-5",
   "title": "Record sequestration and regulated relocation with `located_in`; reserve `is_active_in` for the compartment where the protein works.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-5"
  },
  {
   "id": "CC-6",
   "title": "A root organelle term is informative: never `TOO_GENERAL`, and never `MODIFY` it to a sub-compartment.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-6"
  },
  {
   "id": "CC-7",
   "title": "Examine every root organelle row that comes from synthesis (IBA, ISS, ISO, IEA, IC, RCA); keep it only if the organelle claim survives the check.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-7"
  },
  {
   "id": "CC-8",
   "title": "Add the sub-compartment as a separate row when at least two independent lines agree; do not substitute it for the root.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-8"
  },
  {
   "id": "CC-9",
   "title": "A soluble protein stably tethered to an organelle by a named integral partner gets the cytoplasmic-side term; brief or regulated recruitment stays at the root.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-9"
  },
  {
   "id": "CC-10",
   "title": "Do not encode membrane topology with \"integral\" or \"anchored\" terms; use the membrane term, refine generic `membrane`, and use side terms only when the leaflet is known.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-10"
  },
  {
   "id": "CC-11",
   "title": "When a generic plasma-membrane row misleads about which side the protein is on, or whether it is in the plasma membrane at all, `MODIFY` it; otherwise accept it at its own resolution and add the specific term as a `NEW` row.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-11"
  },
  {
   "id": "CC-12",
   "title": "Annotate secreted proteins to `GO:0005576` extracellular region (or a specific extracellular structure), never to `GO:0005615`; use cell surface for proteins held on the outer face.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-12"
  },
  {
   "id": "CC-13",
   "title": "Localization from overexpression, tagging or mutants supports a CC row only when a marker resolves the compartment and the protein is wild type.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-13"
  },
  {
   "id": "CC-14",
   "title": "High-throughput localization supports `located_in` at the assay's resolution; weigh the source's grade, and treat \"additional\" locations as non-core by default.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-14"
  },
  {
   "id": "CC-15",
   "title": "Annotate presence in a condensate as a location; claim condensate formation only with condensate-grade evidence, and never infer a localization process from co-localization.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-15"
  },
  {
   "id": "CC-16",
   "title": "Prefer `GO:0005829` cytosol to `GO:0005737` cytoplasm, and refine `GO:0005634` nucleus to its interior structures when the evidence allows; keep the nucleus row when the refinement is chromatin.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-16"
  },
  {
   "id": "CC-17",
   "title": "Do not propagate a location across paralogs that live in different compartments.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-17"
  },
  {
   "id": "CC-18",
   "title": "A gene product acting in another organism is annotated to that organism's compartment; a host protein co-opted by a pathogen keeps its own.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-18"
  },
  {
   "id": "CC-19",
   "title": "In `core_functions`, name the location where the core activity is shown to happen, not every well-supported location.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/cellular-component.html#cc-19"
  },
  {
   "id": "EV-1",
   "title": "Use the most specific experimental code; do not use EXP when IDA, IPI, IMP, IGI or IEP applies.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-1"
  },
  {
   "id": "EV-2",
   "title": "Use IDA when the experiment measures the gene product's own activity, location or complex membership directly.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-2"
  },
  {
   "id": "EV-3",
   "title": "Use IPI only with the partner's identifier in WITH/FROM, and only for binding, complex or interaction-dependent terms; never for catalytic activity.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-3"
  },
  {
   "id": "EV-4",
   "title": "Use IMP when the inference rests on comparing alleles, or perturbed and unperturbed states, of one gene.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-4"
  },
  {
   "id": "EV-5",
   "title": "Use IGI when the inference depends on perturbing two or more genes; put the other gene in WITH/FROM; annotate only the gene whose role the experiment informs.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-5"
  },
  {
   "id": "EV-6",
   "title": "Use IEP only for biological process terms, only from normal expression, and only when the gene product's job is the response itself.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-6"
  },
  {
   "id": "EV-7",
   "title": "Classify a paper as high-throughput by how it was done, not by how many genes it names; then hold its annotations to the low-throughput standard.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-7"
  },
  {
   "id": "EV-8",
   "title": "Use ISS, ISO, ISA or ISM only after a curator has reviewed the inference; name the experimentally supported donor or the model in WITH/FROM.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-8"
  },
  {
   "id": "EV-9",
   "title": "Treat the phylogenetic codes as a PAINT curator's node judgement; challenge the node placement, not the donor count.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-9"
  },
  {
   "id": "EV-10",
   "title": "Use TAS only when the cited source is traceable and you cannot annotate from the primary paper; a textbook or \"common knowledge\" is not traceable.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-10"
  },
  {
   "id": "EV-11",
   "title": "Use NAS only for an author's assertion, not for their speculation.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-11"
  },
  {
   "id": "EV-12",
   "title": "Use IC only for a one-step inference from another annotation on the same gene product; put the GO id of that annotation in WITH/FROM.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-12"
  },
  {
   "id": "EV-13",
   "title": "ND says a curator searched the literature for one aspect and found nothing; accept it when that is still true, whatever inferred rows exist.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-13"
  },
  {
   "id": "EV-14",
   "title": "Use RCA and IEA only for what they define; do not recode reviewed work as IEA or unreviewed predictions as anything else.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-14"
  },
  {
   "id": "EV-15",
   "title": "Read the ECO class, not only the GAF code.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-15"
  },
  {
   "id": "EV-16",
   "title": "Several codes from one paper are several annotations; never let a code stand in for a judgement of the claim.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/evidence-codes.html#ev-16"
  },
  {
   "id": "IEA-1",
   "title": "Identify the pipeline before judging the row",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-1"
  },
  {
   "id": "IEA-2",
   "title": "A signature mapping must hold for every member of the entry",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-2"
  },
  {
   "id": "IEA-3",
   "title": "Map a domain to what the domain does, not to what proteins containing it do",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-3"
  },
  {
   "id": "IEA-4",
   "title": "Never map to root, do-not-annotate, binding-only or obsolete terms",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-4"
  },
  {
   "id": "IEA-5",
   "title": "Accept only one-hop provenance",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-5"
  },
  {
   "id": "IEA-6",
   "title": "Know the current status of each pipeline",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-6"
  },
  {
   "id": "IEA-7",
   "title": "Use only exact reaction mappings, and only for physiological reactions",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-7"
  },
  {
   "id": "IEA-8",
   "title": "A keyword or location mapping must respect GO's distinctions, which vocabularies often do not",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-8"
  },
  {
   "id": "IEA-9",
   "title": "Judge a rule by its condition sets, as conjunctions, against the experimental record",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-9"
  },
  {
   "id": "IEA-10",
   "title": "Automated orthology transfer must preserve relations and stop at context",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-10"
  },
  {
   "id": "IEA-11",
   "title": "An inferred annotation falls with its premise",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-11"
  },
  {
   "id": "IEA-12",
   "title": "Review actions: keep true general rows, remove wrong ones, never cite an IEA as evidence",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-12"
  },
  {
   "id": "IEA-13",
   "title": "When a mapping is wrong, route the fix to the mapping and record it in a form the source can use",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-13"
  },
  {
   "id": "IEA-14",
   "title": "Use a curated conditional rule when only a condition can separate right from wrong members",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-14"
  },
  {
   "id": "IEA-15",
   "title": "Do not launder a prediction into manual evidence",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-15"
  },
  {
   "id": "IEA-16",
   "title": "Hold new prediction pipelines to the rubric before they enter GO",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/electronic-annotation.html#iea-16"
  },
  {
   "id": "LIT-1",
   "title": "Annotate the conclusion the experiment supports, not the assay's name or the authors' framing.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-1"
  },
  {
   "id": "LIT-2",
   "title": "Let the readout's proximity to the gene product set the aspect and the depth of the term.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-2"
  },
  {
   "id": "LIT-3",
   "title": "An in vitro activity supports a molecular function only at the depth that was tested; decide whether the protein evolved to perform it.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-3"
  },
  {
   "id": "LIT-4",
   "title": "Weigh localisation data by what was localised: endogenous protein in its native cell outranks a tagged, overexpressed construct.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-4"
  },
  {
   "id": "LIT-5",
   "title": "In overexpression and heterologous systems, separate the assay from the phenotype, and annotate the gene that was expressed.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-5"
  },
  {
   "id": "LIT-6",
   "title": "Annotate the gene product and organism actually assayed; a paper about a paralog, ortholog or partner is not evidence for your gene.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-6"
  },
  {
   "id": "LIT-7",
   "title": "Cite the primary paper that contains the evidence, and verify that the identifier resolves to it.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-7"
  },
  {
   "id": "LIT-8",
   "title": "A phenotype shows necessity; annotate the most proximal process and use the weakest relation the evidence allows.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-8"
  },
  {
   "id": "LIT-9",
   "title": "Read what the paper reports as negative; never annotate a negative control or a failed assay as a positive.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-9"
  },
  {
   "id": "LIT-10",
   "title": "Know which findings are not annotatable, and leave them out.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-10"
  },
  {
   "id": "LIT-11",
   "title": "Make one annotation per claim per method, each traceable to a result; do not harvest every term a paper touches.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-11"
  },
  {
   "id": "LIT-12",
   "title": "Judge a paper against the rest of the literature: contested, superseded and retracted findings need explicit handling.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-12"
  },
  {
   "id": "LIT-13",
   "title": "When reviewing someone else's literature annotation, read what they read before overruling it; an abstract can confirm, but only the full text can refute.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-13"
  },
  {
   "id": "LIT-14",
   "title": "Record provenance so the next reader can check the inference without rereading the paper.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/from-paper-to-annotation.html#lit-14"
  },
  {
   "id": "MO-1",
   "title": "Annotate each organism's gene products with the terms written from that organism's side.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-1"
  },
  {
   "id": "MO-2",
   "title": "\"Host\" means the larger organism and \"symbiont\" the smaller; neither says anything about harm.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-2"
  },
  {
   "id": "MO-3",
   "title": "Do not annotate a host gene product to a viral or symbiont process because the symbiont uses it.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-3"
  },
  {
   "id": "MO-4",
   "title": "A symbiont term requires that the symbiont product evolved to cause the effect; being recognised is not a symbiont process.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-4"
  },
  {
   "id": "MO-5",
   "title": "Give an effector its molecular function, its host target and its host location, not only a process term.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-5"
  },
  {
   "id": "MO-6",
   "title": "Use a single-organism process term only for a process within the organism that encodes the gene product.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-6"
  },
  {
   "id": "MO-7",
   "title": "Locate symbiont products in host compartments with host CC terms, and virion proteins with virion terms.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-7"
  },
  {
   "id": "MO-8",
   "title": "Record the other organism for interspecies annotations, and only for physiological interactions.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-8"
  },
  {
   "id": "MO-9",
   "title": "On the host side, annotate participation in defence to the most specific defence or immune term the evidence supports, and keep response-to and susceptibility separate.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-9"
  },
  {
   "id": "MO-10",
   "title": "An induced effector is not a participant in the signalling pathway that induces it, and an enzyme that makes a second messenger is not a regulator of the virus.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-10"
  },
  {
   "id": "MO-11",
   "title": "Keep mutualistic programmes separate from defence.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-11"
  },
  {
   "id": "MO-12",
   "title": "Check taxon fit before accepting an inferred multi-organism or immune annotation.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-12"
  },
  {
   "id": "MO-13",
   "title": "Annotate the mature, functional RNA, identified by an RNAcentral or MOD identifier.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-13"
  },
  {
   "id": "MO-14",
   "title": "Give an RNA an RNA-specific function term; bare `RNA binding` and `protein binding` are not functions for an ncRNA.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-14"
  },
  {
   "id": "MO-15",
   "title": "Annotate a miRNA target with BP plus `has input`; add the MF only from the paper that shows binding.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-15"
  },
  {
   "id": "MO-16",
   "title": "For RNA experiments, adding the RNA is IDA, removing or blocking it is IMP, a reporter assay is IDA, and expression change is never evidence of function.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-16"
  },
  {
   "id": "MO-17",
   "title": "Choose the silencing child term from what was measured.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-17"
  },
  {
   "id": "MO-18",
   "title": "Downstream processes of a miRNA are regulation terms and non-core; context extensions need evidence of endogenous expression.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-18"
  },
  {
   "id": "MO-19",
   "title": "Annotate proteins that change miRNA levels to the step they act on; the core processing machinery carries no specific miRNA or mRNA in extensions.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-19"
  },
  {
   "id": "MO-20",
   "title": "For a lncRNA, establish the mechanism class first, and distinguish the RNA's activity from the act of transcribing the locus.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-20"
  },
  {
   "id": "MO-21",
   "title": "A guide RNA's family supports its guide activity; its target-specific process needs the target.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/multi-organism-and-ncrna.html#mo-21"
  },
  {
   "id": "ONT-1",
   "title": "Read the definition and the parents, not the label",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-1"
  },
  {
   "id": "ONT-2",
   "title": "Establish a term's state against a named release, from two independent services",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-2"
  },
  {
   "id": "ONT-3",
   "title": "Treat `replaced_by` as a mechanical redirect that you must check",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-3"
  },
  {
   "id": "ONT-4",
   "title": "Treat `consider` as a list of options and triage annotations by mechanism",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-4"
  },
  {
   "id": "ONT-5",
   "title": "A replacement in another aspect is a `consider`, never a `replaced_by`",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-5"
  },
  {
   "id": "ONT-6",
   "title": "When nothing replaces the term, put the content on what the gene does, or on its partner",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-6"
  },
  {
   "id": "ONT-7",
   "title": "Migrate an obsolete term in a review with `MODIFY`, everywhere it occurs",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-7"
  },
  {
   "id": "ONT-8",
   "title": "Merges are now obsoletions with `replaced_by`; read old secondary ids accordingly",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-8"
  },
  {
   "id": "ONT-9",
   "title": "Fix a wrong annotation at its source; fix a wrong term in the ontology; do not confuse the two",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-9"
  },
  {
   "id": "ONT-10",
   "title": "Track upstream changes as inbound work, and argue disagreement in writing",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-10"
  },
  {
   "id": "ONT-11",
   "title": "Request a new term only when real evidence for a real gene needs it",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-11"
  },
  {
   "id": "ONT-12",
   "title": "Do not request terms that GO has decided not to have",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-12"
  },
  {
   "id": "ONT-13",
   "title": "In a review, propose a missing term with an NTR placeholder, never an ill-fitting id",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-13"
  },
  {
   "id": "ONT-14",
   "title": "An ontology gap is not a knowledge gap",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-14"
  },
  {
   "id": "ONT-15",
   "title": "Propose an obsoletion only for a term whose meaning is broken, with a remapping for every curated row",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-15"
  },
  {
   "id": "ONT-16",
   "title": "Know what a taxon constraint says and how it propagates",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-16"
  },
  {
   "id": "ONT-17",
   "title": "When an annotation violates a constraint, decide which of the two is wrong",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-17"
  },
  {
   "id": "ONT-18",
   "title": "A pathway named for a component does not exist where the component is absent",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-18"
  },
  {
   "id": "ONT-19",
   "title": "Propose a taxon constraint only with evidence of absence and a measured payoff",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-19"
  },
  {
   "id": "ONT-20",
   "title": "Do not annotate new rows to flagged terms, and read existing rows on them as review prompts",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/ontology-change-and-taxa.html#ont-20"
  },
  {
   "id": "PC-1",
   "title": "Annotate `part_of` a complex only with evidence that the complex exists as a stable unit and that this gene product is an intrinsic member.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-1"
  },
  {
   "id": "PC-2",
   "title": "Use the most specific complex term that the evidence supports; treat bare `GO:0032991` protein-containing complex as a placeholder to refine; record the organelle separately.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-2"
  },
  {
   "id": "PC-3",
   "title": "A gene product that binds a complex without being part of it gets `GO:0044877` protein-containing complex binding or a specific child, not `part_of` or `located_in` the complex.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-3"
  },
  {
   "id": "PC-4",
   "title": "Do not infer a molecular function from complex membership, co-purification or loss of complex activity on knockout.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-4"
  },
  {
   "id": "PC-5",
   "title": "The subunit that performs the activity `enables` it, with no qualifier, even when it works inside a complex; homomultimers also `enable`.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-5"
  },
  {
   "id": "PC-6",
   "title": "Use `contributes_to` only when no single subunit has the activity and the activity is that of an irreducible molecular machine, and give it only to the subunits whose part is in the mechanism.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-6"
  },
  {
   "id": "PC-7",
   "title": "Accessory, structural and regulatory subunits get their own MF or none; do not give them `contributes_to` the complex's catalytic activity.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-7"
  },
  {
   "id": "PC-8",
   "title": "Annotate subunits to the complex-level activity, not to its substeps; a subunit that catalyses a half-reaction on its own may `enable` the parent term.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-8"
  },
  {
   "id": "PC-9",
   "title": "When the active subunit of a complex is not known, give no subunit the complex's MF; use CC membership and BP.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-9"
  },
  {
   "id": "PC-10",
   "title": "Assembly factors get assembly processes and their own activity; they are not `part_of` the mature complex and never receive its activity.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-10"
  },
  {
   "id": "PC-11",
   "title": "Do not annotate a subunit to the assembly of its own complex because the complex fails to form without it; require evidence that it acts on the assembly of other parts.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-11"
  },
  {
   "id": "PC-12",
   "title": "Treat oligomeric state as out of scope: do not propose oligomerization or homodimerization terms, and review existing ones by their evidence.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-12"
  },
  {
   "id": "PC-13",
   "title": "Review Complex Portal-derived subunit rows as claims about the subunit; never propagate the complex's MF to its subunits.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-13"
  },
  {
   "id": "PC-14",
   "title": "In GO-CAM, use a complex as the enabler only for an emergent activity, list as `has_part` only the subunits that take part, and link subunits to complexes with `part_of`, never MF `occurs_in` a complex.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-14"
  },
  {
   "id": "PC-15",
   "title": "In a review's `core_functions`, state the attribution level: the subunit's own activity in `molecular_function`, the machine's activity in `contributes_to_molecular_function` only for direct participants.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-15"
  },
  {
   "id": "PC-16",
   "title": "Check propagated complex-activity rows (IBA, ISS, InterPro2GO) for transfer to non-catalytic subunits or paralogs.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/protein-complexes.html#pc-16"
  },
  {
   "id": "PH-1",
   "title": "Review an IBA by its node placement, not by its donor count",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-1"
  },
  {
   "id": "PH-2",
   "title": "Seed an IBD only from experimental annotations that make the claim the term makes",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-2"
  },
  {
   "id": "PH-3",
   "title": "Use high-throughput seeds and single seeds only with an independent second line",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-3"
  },
  {
   "id": "PH-4",
   "title": "Place the IBD at the deepest node the evidence supports, and no deeper",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-4"
  },
  {
   "id": "PH-5",
   "title": "Do not propagate binding-only, redundant, indirect or contextual terms",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-5"
  },
  {
   "id": "PH-6",
   "title": "Propagate substrate and cargo specificity only within a duplication-free clade",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-6"
  },
  {
   "id": "PH-7",
   "title": "Do not propagate a cellular component across a node whose members live in different compartments",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-7"
  },
  {
   "id": "PH-8",
   "title": "Ignore seed qualifiers except NOT; carry `contributes_to` only where the subunit's role is conserved",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-8"
  },
  {
   "id": "PH-9",
   "title": "Record a loss with IKR or IRD, and choose IKR when a key residue explains it",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-9"
  },
  {
   "id": "PH-10",
   "title": "NOT propagates only to the term annotated; a positive general term still descends",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-10"
  },
  {
   "id": "PH-11",
   "title": "The target in its own `WITH/FROM` is not circular",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-11"
  },
  {
   "id": "PH-12",
   "title": "Read the `WITH/FROM` first, and count donors correctly",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-12"
  },
  {
   "id": "PH-13",
   "title": "Stop propagation at duplications that changed function, at pseudo-enzymes, and at lineage boundaries",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-13"
  },
  {
   "id": "PH-14",
   "title": "Before REMOVE on an IBA, complete the checklist and route the fix to the node",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-14"
  },
  {
   "id": "PH-15",
   "title": "Treat an IBA-only leaf as under-annotated, and check for orthologs split across families",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-15"
  },
  {
   "id": "PH-16",
   "title": "ISO needs a current experimental donor, the right orthology edge, and every co-ortholog named",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-16"
  },
  {
   "id": "PH-17",
   "title": "Move conserved activity by orthology; do not move context",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-17"
  },
  {
   "id": "PH-18",
   "title": "ISS and ISA need an experimentally characterised match, a reviewed alignment, and no binding-only terms",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-18"
  },
  {
   "id": "PH-19",
   "title": "Do not add back what a phylogenetic curator deliberately removed",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-19"
  },
  {
   "id": "PH-20",
   "title": "Keep IBA, TreeGrafter and automated orthology distinct in review and in tickets",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/phylogenetic-propagation.html#ph-20"
  },
  {
   "id": "QN-1",
   "title": "Every annotation must carry an explicit relation that matches its aspect and term type.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-1"
  },
  {
   "id": "QN-2",
   "title": "Use `contributes_to` only when no single subunit, or smaller subset of subunits, can be said to carry out the activity. Annotate every catalytic-core subunit this way, and no accessory subunit.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-2"
  },
  {
   "id": "QN-3",
   "title": "Use `involved_in` only when the gene product's own activity is a step in the process. Use an `acts_upstream_of...` relation for every other causal link, and treat a BP row with no stated relation as `acts_upstream_of_or_within`.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-3"
  },
  {
   "id": "QN-4",
   "title": "Use `is_active_in` only when the evidence places the activity, not just the protein, in the location. Otherwise use `located_in`.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-4"
  },
  {
   "id": "QN-5",
   "title": "Do not make new `colocalizes_with` annotations. When reviewing one, convert it to `is_active_in` or `located_in` if the evidence supports that, or remove it.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-5"
  },
  {
   "id": "QN-6",
   "title": "Judge the relation together with the term. Positive annotations entail ancestors only through relations that carry up.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-6"
  },
  {
   "id": "QN-7",
   "title": "When reviewing, correct a wrong relation as a structured relation change. Do not REMOVE a right term because its relation is wrong.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-7"
  },
  {
   "id": "QN-8",
   "title": "Make a NOT annotation only when an experiment tested for the property and found it absent, or when the key residues for it are lost (IKR), and only when a reader would otherwise expect the property.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-8"
  },
  {
   "id": "QN-9",
   "title": "A NOT negates the term and all its descendants. Place it on the most general term the evidence excludes, and never on an ancestor of a term the gene product positively has.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-9"
  },
  {
   "id": "QN-10",
   "title": "A positive and a NOT annotation to the same term may coexist only when the literature genuinely conflicts or the claims concern different gene products (isoforms). The reviewer must reconcile each pair in writing and narrow the NOT where the conflict is only apparent.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-10"
  },
  {
   "id": "QN-11",
   "title": "A NOT to a molecular function is the strongest use of the qualifier. A NOT to a process needs evidence that the gene product was unable to do the process's work.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-11"
  },
  {
   "id": "QN-12",
   "title": "Do not attach an annotation extension to a NOT annotation.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-12"
  },
  {
   "id": "QN-13",
   "title": "Do not make NOT annotations to binding terms.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-13"
  },
  {
   "id": "QN-14",
   "title": "A NOT needs a positive annotation in the same aspect, the ND root if nothing else is known. A NOT row does not make an ND row stale.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-14"
  },
  {
   "id": "QN-15",
   "title": "Use NOT to stop propagation of a lost activity, and know how PAINT treats NOT.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-15"
  },
  {
   "id": "QN-16",
   "title": "Review an existing NOT row as a claim of absence: ACCEPT, MODIFY (narrow the term or fix the isoform), REMOVE or UNDECIDED. Do not mark it non-core, over-annotated or too general.",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/qualifiers-and-negation.html#qn-16"
  },
  {
   "id": "REV-1",
   "title": "Judge the claim, not the row; rows sharing a term get consistent actions",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-1"
  },
  {
   "id": "REV-2",
   "title": "Choose the action by what it says about the claim",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-2"
  },
  {
   "id": "REV-3",
   "title": "A correct but general term is `MODIFY` only when this row's evidence supports the specific term",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-3"
  },
  {
   "id": "REV-4",
   "title": "Separate core from peripheral before deciding anything else",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-4"
  },
  {
   "id": "REV-5",
   "title": "The conclusion, not the assay; the direct role, not its downstream effects",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-5"
  },
  {
   "id": "REV-6",
   "title": "Catalytic rows on pseudoenzymes, substrates and accessory subunits",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-6"
  },
  {
   "id": "REV-7",
   "title": "Measured activity is not automatically function",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-7"
  },
  {
   "id": "REV-8",
   "title": "Do not overrule an experimental curator from evidence you have not seen",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-8"
  },
  {
   "id": "REV-9",
   "title": "Challenge an electronic or phylogenetic row by arguing with its source",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-9"
  },
  {
   "id": "REV-10",
   "title": "Necessity is not participation",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-10"
  },
  {
   "id": "REV-11",
   "title": "`NEW` is the one action that manufactures a claim; hold it to a higher bar",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-11"
  },
  {
   "id": "REV-12",
   "title": "An ND row is a statement about the literature",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-12"
  },
  {
   "id": "REV-13",
   "title": "Remove bare protein binding; look for the informative function behind it",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-13"
  },
  {
   "id": "REV-14",
   "title": "A NOT must exclude the function; propose NOTs where errors will recur",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-14"
  },
  {
   "id": "REV-15",
   "title": "A retraction is a source failure; scope the response to the evidence line",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-15"
  },
  {
   "id": "REV-16",
   "title": "A miscitation is a defect in the citation, not in the biology; key it on the citation",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-16"
  },
  {
   "id": "REV-17",
   "title": "Record upstream errors as structured source defects, addressed to whoever can fix them",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-17"
  },
  {
   "id": "REV-18",
   "title": "Every row needs term-specific reasoning and independent, verbatim support",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-18"
  },
  {
   "id": "REV-19",
   "title": "Know what the gorules already enforce, and do not mistake passing them for review",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-19"
  },
  {
   "id": "REV-20",
   "title": "An obsoletion-driven review ticket is a review of claims, not a find-and-replace",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/reviewing-annotations.html#rev-20"
  },
  {
   "id": "RS-1",
   "title": "Decide between \"part of X\" and \"regulation of X\" by locating the gene product's activity relative to the process boundaries",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-1"
  },
  {
   "id": "RS-2",
   "title": "Annotate regulation of X only when the gene product modulates X, and name the target",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-2"
  },
  {
   "id": "RS-3",
   "title": "Limiting quantities, constitutive prerequisites and substrate supply are not regulation",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-3"
  },
  {
   "id": "RS-4",
   "title": "Pathway members that activate the next member are part of the pathway, not regulators of it; feedback is the exception",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-4"
  },
  {
   "id": "RS-5",
   "title": "Judge sign in vivo, from the gene product's effect, and correct a wrong sign rather than tolerating it",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-5"
  },
  {
   "id": "RS-6",
   "title": "A signalling pathway runs from ligand–receptor engagement to the last effector; annotate its members, not its targets",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-6"
  },
  {
   "id": "RS-7",
   "title": "Intracellular signalling cassettes are part of pathways; cassette members may carry both terms",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-7"
  },
  {
   "id": "RS-8",
   "title": "Protein ligands are part of the pathway they start; annotate them with receptor ligand activity, not receptor-specific binding terms",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-8"
  },
  {
   "id": "RS-9",
   "title": "Receptors, G proteins and second-messenger enzymes: annotate the specific pathway the evidence shows, with the right coupling and sign",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-9"
  },
  {
   "id": "RS-10",
   "title": "Regulation does not cross transcription, and general machinery is not a pathway regulator",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-10"
  },
  {
   "id": "RS-11",
   "title": "Use \"response to X\" for gene products that detect X, transduce it, or carry out a response specific to X",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-11"
  },
  {
   "id": "RS-12",
   "title": "IEP supports \"response to\" and other BP terms only for normal expression, and usually only as a non-core role",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-12"
  },
  {
   "id": "RS-13",
   "title": "Do not use MF regulator terms when the regulatory activity is unknown, and do not give a regulator the activity it regulates",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-13"
  },
  {
   "id": "RS-14",
   "title": "Annotate regulation at the level where it acts, not at every enclosing process",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/regulation-and-signaling.html#rs-14"
  },
  {
   "id": "TR-1",
   "title": "Classify the activity first: polymerase, GTF, dbTF, coTF, or regulator of a regulator",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-1"
  },
  {
   "id": "TR-2",
   "title": "Annotate dbTF activity only when the protein's own sequence-specific DNA binding and its regulation of targets are both supported",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-2"
  },
  {
   "id": "TR-3",
   "title": "Read each DNA-binding assay for what it shows: location, binding, or direct sequence-specific binding",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-3"
  },
  {
   "id": "TR-4",
   "title": "Require a genomic address: non-specific, structure-specific and modification-specific DNA binders are not dbTFs",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-4"
  },
  {
   "id": "TR-5",
   "title": "Annotate coTF activity for locus-specific action through a dbTF, and protect proteins with a real DNA-binding domain from it",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-5"
  },
  {
   "id": "TR-6",
   "title": "Separate GTFs from coTFs by where they are recruited, and annotate GTFs to transcription itself",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-6"
  },
  {
   "id": "TR-7",
   "title": "Proteins that act on transcription regulators away from chromatin are regulator-of-regulator, not coTFs",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-7"
  },
  {
   "id": "TR-8",
   "title": "Use RNA polymerase II terms for eukaryotic protein-coding genes; name Pol I or III only when shown",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-8"
  },
  {
   "id": "TR-9",
   "title": "State activator or repressor when the direction at a target is shown; allow both when context changes it",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-9"
  },
  {
   "id": "TR-10",
   "title": "For dbTF DNA binding use the cis-regulatory sequence-specific terms; put region and motif in extensions",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-10"
  },
  {
   "id": "TR-11",
   "title": "Annotate regulation of transcription only from evidence of a transcriptional effect; use regulation of gene expression for mRNA-level changes",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-11"
  },
  {
   "id": "TR-12",
   "title": "Give chromatin enzymes, readers and chaperones their own activity; add transcription regulation only on gene-specific evidence",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-12"
  },
  {
   "id": "TR-13",
   "title": "Treat an enzyme activity plus dbTF activity on one protein as a probable error",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-13"
  },
  {
   "id": "TR-14",
   "title": "Name the direct target gene with `has_input`, one target per annotation; a coTF's input is the dbTF",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-14"
  },
  {
   "id": "TR-15",
   "title": "Bacterial and plant regulators follow the same evidence standard with their own terms",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-15"
  },
  {
   "id": "TR-16",
   "title": "Review electronic and propagated dbTF rows against the family and the member",
   "page": "../../pages/projects/GO_GUIDELINES/guidelines/transcription-regulation.html#tr-16"
  }
 ]
};
