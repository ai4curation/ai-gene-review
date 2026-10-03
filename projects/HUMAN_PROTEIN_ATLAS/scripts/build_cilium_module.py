#!/usr/bin/env python3
"""Build modules/primary_cilium_life_cycle.yaml from a compact curated spec.

The spec below is the curated content (stages, roles, GO terms, citations).
UniProt accessions and names are NOT typed here: they are read from
cilium_life_cycle/candidate_members.tsv, which was populated from the UniProt
REST API. GO ids in the spec were checked against OLS (2026-10-03); PMIDs were
checked against PubMed.

Usage (from repo root):
    uv run python projects/HUMAN_PROTEIN_ATLAS/scripts/build_cilium_module.py
"""

import csv
import re
from pathlib import Path

import yaml

WORK = Path("projects/HUMAN_PROTEIN_ATLAS/cilium_life_cycle")
OUT = Path("modules/primary_cilium_life_cycle.yaml")

MEMBERS = {r["gene"]: r for r in csv.DictReader((WORK / "candidate_members.tsv").open(), delimiter="\t")}

GO = {
    "GO:0044782": "cilium organization",
    "GO:0060271": "cilium assembly",
    "GO:1905515": "non-motile cilium assembly",
    "GO:0061523": "cilium disassembly",
    "GO:1905349": "ciliary transition zone assembly",
    "GO:1905556": "ciliary vesicle assembly",
    "GO:0042073": "intraciliary transport",
    "GO:0035720": "intraciliary anterograde transport",
    "GO:0035721": "intraciliary retrograde transport",
    "GO:0061512": "protein localization to cilium",
    "GO:1902017": "regulation of cilium assembly",
    "GO:1902018": "negative regulation of cilium assembly",
    "GO:0007019": "microtubule depolymerization",
    "GO:0003924": "GTPase activity",
    "GO:0004674": "protein serine/threonine kinase activity",
    "GO:0004439": "phosphatidylinositol-4,5-bisphosphate 5-phosphatase activity",
    "GO:0005085": "guanyl-nucleotide exchange factor activity",
    "GO:0005096": "GTPase activator activity",
    "GO:0008574": "plus-end-directed microtubule motor activity",
    "GO:0008569": "minus-end-directed microtubule motor activity",
    "GO:0042903": "tubulin deacetylase activity",
    "GO:0030992": "intraciliary transport particle B",
    "GO:0030991": "intraciliary transport particle A",
    "GO:0016939": "kinesin II complex",
    "GO:0036038": "MKS complex",
    "GO:0035869": "ciliary transition zone",
    "GO:0036064": "ciliary basal body",
    "GO:0097721": "ciliary vesicle",
    "GO:0060170": "ciliary membrane",
    "GO:0005930": "axoneme",
    "GO:0097542": "ciliary tip",
    "GO:0097730": "non-motile cilium",
    "GO:0034451": "centriolar satellite",
}

HPA_ATLAS = {
    "source_id": "PMID:41005307",
    "title": "Intrinsic heterogeneity of primary cilia revealed through spatial proteomics.",
}


def term(go_id):
    return {"id": go_id, "label": GO[go_id]}


def concept(go_id, description=None):
    d = {"preferred_term": GO[go_id], "term": term(go_id)}
    if description:
        d["description"] = description
    return d


def protein(gene):
    m = MEMBERS[gene]
    name = re.split(r" \(|\s\[", m["protein_name"])[0]
    return {"preferred_term": gene, "term": {"id": f"UniProtKB:{m['uniprot']}", "label": name}}


def gp(gene):
    return {"selector_type": "GENE_PRODUCT", "gene_product": protein(gene)}


def ev(pmid, statement, title=None):
    d = {"source_id": pmid}
    if title:
        d["title"] = title
    d["statement"] = statement
    return d


def annoton(aid, label, participant, role, fn=None, fn_label=None, fn_desc=None,
            processes=(), locations=(), evidence=()):
    a = {"id": aid, "label": label, "participant": participant}
    if fn:
        a["function"] = {"preferred_term": fn_label or GO[fn], "term": term(fn)}
    elif fn_label:
        a["function"] = {"preferred_term": fn_label}
        if fn_desc:
            a["function"]["description"] = fn_desc
    if processes:
        a["processes"] = [concept(p) for p in processes]
    if locations:
        a["locations"] = [concept(loc) for loc in locations]
    a["role_description"] = role
    if evidence:
        a["evidence"] = list(evidence)
    return a


def complex_sel(name, desc, genes, role, go_id=None):
    pc = {"preferred_term": name}
    if go_id:
        pc["term"] = term(go_id)
    return {
        "selector_type": "PROTEIN_COMPLEX",
        "protein_complex": {
            **pc,
            "description": desc,
            "active_units": [
                {"id": f"{g.lower()}_unit", "label": f"{g} subunit", "participant": gp(g), "role": role}
                for g in genes
            ],
        },
    }


# ---------------------------------------------------------------- stages
TANOS = ev("PMID:23348840", "Identifies CEP83, CEP89, SCLT1, FBF1 and CEP164 as distal appendage components, "
           "defines their assembly hierarchy, and shows that undocked centrioles fail to recruit TTBK2 or release CP110.",
           "Centriole distal appendages promote membrane docking, leading to cilia initiation.")
GOETZ = ev("PMID:23141541", "TTBK2 acts at the distal end of the basal body, promotes removal of the CP110 cap and "
           "recruitment of IFT proteins, and is required to initiate ciliogenesis.",
           "The spinocerebellar ataxia-associated gene Tau tubulin kinase 2 controls the initiation of ciliogenesis.")
KOBAYASHI = ev("PMID:21620453", "KIF24 binds CP110 and CEP97 at the mother centriole, depolymerizes microtubules in vitro, "
               "and restrains cilia assembly in cycling cells.",
               "Centriolar kinesin Kif24 interacts with CP110 to remodel microtubules and regulate ciliogenesis.")
LU = ev("PMID:25686250", "EHD1 and EHD3 tubulate membranes to fuse distal appendage vesicles into the ciliary vesicle, "
        "acting with the Rab11-Rab8 cascade; Rab8 is activated only after ciliary vesicle assembly.",
        "Early steps in primary cilium assembly require EHD1/EHD3-dependent ciliary vesicle formation.")
WU = ev("PMID:29335527", "Myosin-Va transports preciliary vesicles to the mother centriole, the earliest known step of "
        "ciliary vesicle formation.",
        "Myosin-Va is required for preciliary vesicle transportation to the mother centriole during ciliogenesis.")
NACHURY = ev("PMID:17574030", "Rab8-GTP, produced by the Rab8 GEF Rabin8 at the basal body, enters the cilium and "
             "promotes ciliary membrane extension.",
             "A core complex of BBS proteins cooperates with the GTPase Rab8 to promote ciliary membrane biogenesis.")
GARCIA = ev("PMID:21725307", "TCTN1 forms a transition zone complex with MKS1, TMEM216, TMEM67, CEP290, B9D1, TCTN2 and "
            "CC2D2A that controls ciliogenesis and ciliary membrane composition in a tissue-specific manner.",
            "A transition zone complex regulates mammalian ciliogenesis and ciliary membrane composition.")
PAZOUR = ev("PMID:11062270", "IFT88 and its mouse homologue Tg737 are required for cilium and flagellum assembly.",
            "Chlamydomonas IFT88 and its mouse homologue, polycystic kidney disease gene tg737, are required for "
            "assembly of cilia and flagella.")
TASCHNER = ev("PMID:36354106", "Biochemically validated structural model of the 15-subunit IFT-B complex.",
              "Biochemically validated structural model of the 15-subunit intraflagellar transport complex IFT-B.")
IFTA = ev("PMID:36775821", "Structures of the human IFT-A complex provide the molecular basis of IFT-A in ciliary transport.",
          "Human IFT-A complex structures provide molecular insights into ciliary transport.")
TOROPOVA = ev("PMID:31451806", "Structure of the dynein-2 complex and its assembly onto IFT trains for retrograde transport.",
              "Structure of the dynein-2 complex and its assembly with intraflagellar transport trains.")
GOTTHARDT = ev("PMID:26551564", "ARL13B is the guanine nucleotide exchange factor for ARL3, creating a G-protein cascade "
               "that releases lipidated cargo from PDE6D and UNC119 inside the cilium.",
               "A G-protein activation cascade from Arl13B to Arl3 and implications for ciliary targeting of lipidated proteins.")
TULP3 = ev("PMID:20889716", "TULP3 bridges the IFT-A complex and membrane phosphoinositides to traffic G protein-coupled "
           "receptors into cilia.",
           "TULP3 bridges the IFT-A complex and membrane phosphoinositides to promote trafficking of G protein-coupled "
           "receptors into primary cilia.")
INPP5E_EV = ev("PMID:19668215", "INPP5E localizes to cilia; its loss causes ciliary signaling defects and ciliary instability.",
               "INPP5E mutations cause primary cilium signaling defects, ciliary instability and ciliopathies in human "
               "and mouse.")
ICK = ev("PMID:24853502", "Intestinal cell kinase (CILK1) is a key regulator of cilia length and signaling.",
         "Intestinal cell kinase, a protein associated with endocrine-cerebro-osteodysplasia syndrome, is a key "
         "regulator of cilia length and Hedgehog signaling.")
ICK_MOK = ev("PMID:25243405", "The RCK kinases ICK and MOK regulate cilium length and intraflagellar transport in renal "
             "epithelial cells.",
             "Regulation of cilium length and intraflagellar transport by the RCK-kinases ICK and MOK in renal epithelial cells.")
PUGACHEVA = ev("PMID:17604723", "NEDD9/HEF1 activates Aurora A at the basal body, which phosphorylates and activates the "
               "tubulin deacetylase HDAC6 to drive ciliary disassembly.",
               "HEF1-dependent Aurora A activation induces disassembly of the primary cilium.")
MIYAMOTO = ev("PMID:25660017", "PLK1-activated KIF2A depolymerizes microtubules at the basal body to drive primary cilium "
              "disassembly.",
              "The Microtubule-Depolymerizing Activity of a Mitotic Kinesin Protein KIF2A Drives Primary Cilia Disassembly "
              "Coupled with Cell Proliferation.")
KINZEL = ev("PMID:20643351", "Pitchfork (CIMAP3) activates Aurora A at the basal body to regulate primary cilia disassembly.",
            "Pitchfork regulates primary cilia disassembly and left-right asymmetry.")
TCTEX = ev("PMID:21394082", "Phosphorylated Tctex-1 (DYNLT1) at the transition zone controls ciliary resorption before "
           "S-phase entry.",
           "Ciliary transition zone activation of phosphorylated Tctex-1 controls ciliary resorption, S-phase entry and "
           "fate of neural progenitors.")


def part(order, role, node):
    return {"order": order, "role": role, "node": node}


parts = [
    part(1, "mother centriole licensing", {
        "id": "mother_centriole_licensing",
        "label": "Mother centriole licensing and basal body conversion",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:1905515")],
        "description": (
            "The mother centriole becomes competent to template a cilium. Distal appendages, assembled in the order "
            "CEP83 then SCLT1 and CEP89 then FBF1 and CEP164, dock the centriole to membrane and recruit TTBK2. TTBK2 "
            "removes the CP110-CEP97 cap, which together with KIF24 otherwise suppresses axoneme growth."),
        "evidence": [TANOS, GOETZ, KOBAYASHI],
        "annotons": [
            annoton("distal_appendage_assembly", "Distal appendage (transition fiber) complex",
                    complex_sel("centriole distal appendage complex",
                                "Distal appendage proteins assembled hierarchically on the mother centriole.",
                                ["CEP83", "SCLT1", "CEP89", "FBF1", "CEP164"], "distal appendage component"),
                    "Docks the mother centriole to vesicles and membrane and recruits TTBK2.",
                    fn_label="distal appendage scaffold",
                    fn_desc="Structural scaffold role; no specific GO molecular-function term is asserted.",
                    processes=["GO:1905515"], locations=["GO:0036064"], evidence=[TANOS]),
            annoton("ttbk2_cap_removal", "TTBK2 removes the CP110 cap", gp("TTBK2"),
                    "Kinase recruited by CEP164 that triggers CP110-CEP97 removal and IFT recruitment.",
                    fn="GO:0004674", processes=["GO:1905515"], locations=["GO:0036064"], evidence=[GOETZ]),
            annoton("cp110_cep97_cap", "CP110-CEP97 distal cap suppresses ciliogenesis",
                    complex_sel("CP110-CEP97 distal centriole cap",
                                "Cap on the distal end of the mother centriole that blocks axoneme extension until removed.",
                                ["CCP110", "CEP97", "KIF24"], "distal cap component"),
                    "Inhibitory cap; its removal licenses axoneme growth.",
                    fn_label="ciliogenesis suppressor cap",
                    fn_desc="KIF24 contributes microtubule-depolymerizing activity; no single MF term covers the cap.",
                    processes=["GO:1902018"], locations=["GO:0036064"], evidence=[KOBAYASHI, GOETZ]),
        ],
        "connections": [
            {"source": "distal_appendage_assembly", "target": "ttbk2_cap_removal", "connection_type": "PROVIDES_INPUT_FOR",
             "description": "CEP164 at the distal appendages recruits TTBK2 to the mother centriole."},
            {"source": "ttbk2_cap_removal", "target": "cp110_cep97_cap", "connection_type": "NEGATIVELY_REGULATES",
             "description": "TTBK2 promotes removal of the CP110-CEP97 cap."},
        ],
    }),
    part(2, "ciliary vesicle formation", {
        "id": "ciliary_vesicle_formation",
        "label": "Ciliary vesicle formation at the distal appendages",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:1905556")],
        "description": (
            "Myosin-Va delivers preciliary vesicles to the distal appendages. EHD1 and EHD3 tubulate the docked "
            "distal appendage vesicles so they fuse into a single ciliary vesicle. The Rab11-Rabin8-Rab8 cascade then "
            "supplies membrane for ciliary growth."),
        "evidence": [WU, LU, NACHURY],
        "annotons": [
            annoton("myo5a_vesicle_delivery", "Myosin-Va preciliary vesicle delivery", gp("MYO5A"),
                    "Actin-based motor that carries preciliary vesicles to the mother centriole.",
                    fn_label="actin-based vesicle transport motor",
                    fn_desc="Motor role; MF term not asserted pending review of MYO5A.",
                    processes=["GO:1905556"], evidence=[WU]),
            annoton("ehd_vesicle_tubulation", "EHD1/EHD3 membrane tubulation",
                    complex_sel("EHD1/EHD3 membrane-shaping proteins",
                                "Membrane-tubulating EH-domain ATPases acting on distal appendage vesicles.",
                                ["EHD1", "EHD3"], "membrane-shaping ATPase"),
                    "Tubulate distal appendage vesicles to form the ciliary vesicle.",
                    fn_label="membrane tubulation",
                    fn_desc="Membrane-shaping role; no GO MF term asserted.",
                    processes=["GO:1905556"], locations=["GO:0097721"], evidence=[LU]),
            annoton("rabin8_rab8_gef", "Rabin8 activates Rab8", gp("RAB3IP"),
                    "RAB8 guanine nucleotide exchange factor, recruited downstream of RAB11.",
                    fn="GO:0005085", processes=["GO:0060271"], evidence=[NACHURY]),
            annoton("rab8_membrane_supply", "Rab8 ciliary membrane delivery", gp("RAB8A"),
                    "GTP-bound RAB8A enters the cilium and promotes ciliary membrane extension.",
                    fn="GO:0003924", processes=["GO:0060271"], locations=["GO:0060170"], evidence=[NACHURY, LU]),
        ],
        "connections": [
            {"source": "myo5a_vesicle_delivery", "target": "ehd_vesicle_tubulation", "connection_type": "PRECEDES",
             "description": "Delivered vesicles are remodeled by EHD1/EHD3 into the ciliary vesicle."},
            {"source": "rabin8_rab8_gef", "target": "rab8_membrane_supply", "connection_type": "POSITIVELY_REGULATES",
             "description": "Rabin8 loads RAB8A with GTP."},
        ],
    }),
    part(3, "transition zone assembly", {
        "id": "transition_zone_assembly",
        "label": "Transition zone assembly",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:1905349")],
        "description": (
            "The transition zone forms between basal body and axoneme and gates ciliary membrane composition. "
            "It is built from the MKS module, the NPHP module and CEP290. GO has merged the former basal body-plasma "
            "membrane docking and transition fiber assembly terms into this process."),
        "evidence": [GARCIA],
        "annotons": [
            annoton("mks_module", "MKS module",
                    complex_sel("MKS complex", "Tectonic/MKS ciliopathy protein complex at the transition zone.",
                                ["MKS1", "TMEM67", "CC2D2A", "B9D1", "B9D2", "TCTN1", "TCTN2", "TMEM216", "TMEM231"],
                                "MKS module component", "GO:0036038"),
                    "Transition zone gate that controls entry of ciliary membrane proteins.",
                    fn_label="ciliary diffusion barrier",
                    fn_desc="Barrier/gating role; no GO MF term asserted.",
                    processes=["GO:1905349"], locations=["GO:0035869"], evidence=[GARCIA]),
            annoton("nphp_module", "NPHP module",
                    complex_sel("NPHP module", "Nephronophthisis proteins at the transition zone.",
                                ["NPHP1", "NPHP4", "RPGRIP1L"], "NPHP module component"),
                    "Second transition zone module, partly redundant with the MKS module.",
                    fn_label="transition zone scaffold",
                    processes=["GO:1905349"], locations=["GO:0035869"]),
            annoton("cep290_tz_scaffold", "CEP290 transition zone scaffold", gp("CEP290"),
                    "Links the transition zone to the axoneme and membrane; part of the TCTN1 complex.",
                    fn_label="transition zone scaffold",
                    processes=["GO:1905349"], locations=["GO:0035869"], evidence=[GARCIA]),
        ],
    }),
    part(4, "axoneme extension by IFT", {
        "id": "axoneme_extension_ift",
        "label": "Axoneme extension by intraflagellar transport",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:0042073")],
        "description": (
            "IFT trains carry axoneme precursors and membrane proteins to the ciliary tip and back. Kinesin-2 drives "
            "anterograde trains carrying IFT-B; dynein-2 drives retrograde trains, with IFT-A required for retrograde "
            "transport and membrane-protein entry."),
        "evidence": [PAZOUR, TASCHNER, IFTA, TOROPOVA],
        "annotons": [
            annoton("ift_b_complex", "IFT-B complex",
                    complex_sel("IFT-B complex", "Anterograde IFT adaptor complex.",
                                ["IFT88", "IFT52", "IFT81", "IFT74", "IFT172"], "IFT-B subunit", "GO:0030992"),
                    "Anterograde train adaptor; IFT81-IFT74 bind tubulin cargo.",
                    fn_label="IFT cargo adaptor",
                    processes=["GO:0035720", "GO:0060271"], locations=["GO:0097730"], evidence=[PAZOUR, TASCHNER]),
            annoton("ift_a_complex", "IFT-A complex",
                    complex_sel("IFT-A complex", "Retrograde IFT and membrane-protein import complex.",
                                ["IFT140", "IFT122", "WDR35", "TTC21B"], "IFT-A subunit", "GO:0030991"),
                    "Retrograde train component and adaptor for membrane-protein entry with TULP3.",
                    fn_label="IFT cargo adaptor",
                    processes=["GO:0035721"], locations=["GO:0097730"], evidence=[IFTA]),
            annoton("kinesin2_anterograde", "Heterotrimeric kinesin-2",
                    complex_sel("kinesin-2 (KIF3A/KIF3B/KAP3)", "Heterotrimeric kinesin II motor.",
                                ["KIF3A", "KIF3B", "KIFAP3"], "kinesin-2 subunit", "GO:0016939"),
                    "Anterograde IFT motor.",
                    fn="GO:0008574", processes=["GO:0035720"], locations=["GO:0005930"]),
            annoton("dynein2_retrograde", "Dynein-2",
                    complex_sel("cytoplasmic dynein-2", "Retrograde IFT motor complex.",
                                ["DYNC2H1", "DYNC2LI1", "DYNC2I1", "DYNC2I2"], "dynein-2 subunit"),
                    "Retrograde IFT motor, carried to the tip in an autoinhibited state on anterograde trains.",
                    fn="GO:0008569", processes=["GO:0035721"], locations=["GO:0005930"], evidence=[TOROPOVA]),
        ],
        "connections": [
            {"source": "kinesin2_anterograde", "target": "ift_b_complex", "connection_type": "PROVIDES_INPUT_FOR",
             "description": "Kinesin-2 moves IFT-B trains toward the ciliary tip."},
            {"source": "dynein2_retrograde", "target": "ift_a_complex", "connection_type": "PROVIDES_INPUT_FOR",
             "description": "Dynein-2 returns IFT-A trains to the base."},
        ],
    }),
    part(5, "ciliary membrane composition", {
        "id": "ciliary_membrane_composition",
        "label": "Ciliary membrane identity and protein targeting",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:0061512")],
        "description": (
            "Mature cilia keep a distinct membrane. ARL13B activates ARL3, which releases lipidated cargo from PDE6D "
            "and UNC119B inside the cilium; RP2 inactivates ARL3. INPP5E keeps PI(4,5)P2 low in the ciliary membrane, "
            "and TULP3 couples IFT-A to phosphoinositides to import GPCRs. BBSome-mediated export is modeled in "
            "modules/bbsome.yaml."),
        "evidence": [GOTTHARDT, TULP3, INPP5E_EV],
        "annotons": [
            annoton("arl13b_arl3_gef", "ARL13B activates ARL3", gp("ARL13B"),
                    "Ciliary membrane GTPase that acts as GEF for ARL3.",
                    fn="GO:0005085", processes=["GO:0061512"], locations=["GO:0060170"], evidence=[GOTTHARDT]),
            annoton("arl3_cargo_release", "ARL3 releases lipidated cargo", gp("ARL3"),
                    "ARL3-GTP displaces lipidated cargo from PDE6D and UNC119B inside the cilium.",
                    fn="GO:0003924", processes=["GO:0061512"], evidence=[GOTTHARDT]),
            annoton("lipid_cargo_carriers", "Lipidated cargo carriers",
                    complex_sel("lipid-binding cargo carriers", "Solubilizing carriers for prenylated and myristoylated cargo.",
                                ["PDE6D", "UNC119B"], "lipidated-cargo carrier"),
                    "Carry lipidated proteins to the cilium for ARL3-dependent release.",
                    fn_label="lipidated protein carrier", processes=["GO:0061512"], evidence=[GOTTHARDT]),
            annoton("rp2_arl3_gap", "RP2 inactivates ARL3", gp("RP2"),
                    "GTPase-activating protein for ARL3.", fn="GO:0005096", processes=["GO:0061512"]),
            annoton("inpp5e_pip2_hydrolysis", "INPP5E sets ciliary phosphoinositides", gp("INPP5E"),
                    "Hydrolyzes PI(4,5)P2 in the ciliary membrane.",
                    fn="GO:0004439", locations=["GO:0060170"], evidence=[INPP5E_EV]),
            annoton("tulp3_gpcr_import", "TULP3 links IFT-A to membrane cargo", gp("TULP3"),
                    "Adaptor bridging IFT-A and phosphoinositides for GPCR import.",
                    fn_label="IFT-A membrane cargo adaptor", processes=["GO:0061512"], evidence=[TULP3]),
        ],
        "connections": [
            {"source": "arl13b_arl3_gef", "target": "arl3_cargo_release", "connection_type": "POSITIVELY_REGULATES",
             "description": "ARL13B loads ARL3 with GTP."},
            {"source": "rp2_arl3_gap", "target": "arl3_cargo_release", "connection_type": "NEGATIVELY_REGULATES",
             "description": "RP2 stimulates ARL3 GTP hydrolysis."},
            {"source": "lipid_cargo_carriers", "target": "arl3_cargo_release", "connection_type": "PROVIDES_INPUT_FOR",
             "description": "Carrier-bound cargo is released by ARL3-GTP."},
        ],
    }),
    part(6, "length control", {
        "id": "cilium_length_control",
        "label": "Cilium length control",
        "module_type": "REGULATORY_STEP",
        "concepts": [concept("GO:1902017")],
        "description": (
            "Steady-state length reflects the balance of assembly and turnover at the tip. The RCK kinases CILK1 and "
            "MAK limit length by regulating IFT turnaround; KIF7 organizes the ciliary tip. GO has no specific "
            "cilium-length term, so the regulation-of-assembly term is used."),
        "evidence": [ICK, ICK_MOK],
        "annotons": [
            annoton("rck_kinases", "RCK kinases restrict cilium length",
                    complex_sel("RCK kinases", "Ciliary length-control kinases (not a stable complex).",
                                ["CILK1", "MAK"], "length-control kinase"),
                    "Phosphorylate kinesin-2 and IFT components to control IFT turnaround and length.",
                    fn="GO:0004674", processes=["GO:1902017"], locations=["GO:0097542"], evidence=[ICK, ICK_MOK]),
            annoton("kif7_tip_organizer", "KIF7 ciliary tip organizer", gp("KIF7"),
                    "Kinesin that organizes the ciliary tip compartment and limits axoneme length.",
                    fn_label="ciliary tip organization", processes=["GO:1902017"], locations=["GO:0097542"]),
        ],
    }),
    part(7, "cilium disassembly", {
        "id": "cilium_disassembly",
        "label": "Cilium disassembly before cell-cycle re-entry",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:0061523")],
        "description": (
            "On cell-cycle re-entry the cilium is resorbed so the centrioles can act at the spindle poles. NEDD9 and "
            "Pitchfork activate Aurora A at the basal body; Aurora A activates the tubulin deacetylase HDAC6. PLK1 "
            "activates KIF2A, which depolymerizes microtubules at the base. Phosphorylated Tctex-1 at the transition "
            "zone also promotes resorption."),
        "evidence": [PUGACHEVA, MIYAMOTO, KINZEL, TCTEX],
        "annotons": [
            annoton("aurka_disassembly_kinase", "Aurora A drives disassembly", gp("AURKA"),
                    "Basal body kinase activated by NEDD9 and Pitchfork; phosphorylates HDAC6.",
                    fn="GO:0004674", processes=["GO:0061523"], locations=["GO:0036064"], evidence=[PUGACHEVA]),
            annoton("aurka_activators", "Aurora A activators",
                    complex_sel("Aurora A activators", "Basal-body activators of Aurora A (not a stable complex).",
                                ["NEDD9", "CIMAP3"], "Aurora A activator"),
                    "Scaffold and activator proteins that switch on Aurora A at the basal body.",
                    fn_label="kinase activator", processes=["GO:0061523"], evidence=[PUGACHEVA, KINZEL]),
            annoton("hdac6_deacetylation", "HDAC6 deacetylates axonemal tubulin", gp("HDAC6"),
                    "Tubulin deacetylase activated by Aurora A.",
                    fn="GO:0042903", processes=["GO:0061523"], evidence=[PUGACHEVA]),
            annoton("plk1_kinase", "PLK1 activates KIF2A", gp("PLK1"),
                    "Kinase that activates KIF2A at the basal body.",
                    fn="GO:0004674", processes=["GO:0061523"], evidence=[MIYAMOTO]),
            annoton("kif2a_depolymerization", "KIF2A depolymerizes microtubules", gp("KIF2A"),
                    "Kinesin-13 microtubule depolymerase acting at the base of the cilium.",
                    fn_label="microtubule depolymerase",
                    fn_desc="No GO MF term for microtubule depolymerase activity; process asserted instead.",
                    processes=["GO:0007019", "GO:0061523"], locations=["GO:0036064"], evidence=[MIYAMOTO]),
            annoton("tctex1_resorption", "Phosphorylated Tctex-1 promotes resorption", gp("DYNLT1"),
                    "Phospho-Tctex-1 at the transition zone promotes ciliary resorption.",
                    fn_label="resorption promoter", processes=["GO:0061523"], locations=["GO:0035869"],
                    evidence=[TCTEX]),
        ],
        "connections": [
            {"source": "aurka_activators", "target": "aurka_disassembly_kinase", "connection_type": "POSITIVELY_REGULATES",
             "description": "NEDD9 and Pitchfork activate Aurora A."},
            {"source": "aurka_disassembly_kinase", "target": "hdac6_deacetylation", "connection_type": "POSITIVELY_REGULATES",
             "description": "Aurora A phosphorylates and activates HDAC6."},
            {"source": "plk1_kinase", "target": "kif2a_depolymerization", "connection_type": "POSITIVELY_REGULATES",
             "description": "PLK1 activates KIF2A."},
        ],
    }),
]

doc = {
    "id": "MODULE:primary_cilium_life_cycle",
    "title": "Primary cilium life cycle module",
    "description": (
        "The primary cilium is a microtubule-based sensory organelle templated by the mother centriole. Its life "
        "cycle runs from licensing of the mother centriole as a basal body, through ciliary vesicle formation, "
        "transition zone assembly and IFT-driven axoneme extension, to maintenance of a distinct ciliary membrane, "
        "control of cilium length, and disassembly when the cell re-enters the cell cycle. This module captures the "
        "ordered stages and the protein roles that carry out each stage, using human proteins as concrete members."),
    "status": "DRAFT",
    "scope": "CONCRETE",
    "evidence": [
        {**HPA_ATLAS, "statement": (
            "HPA primary-cilium atlas: antibody-based sub-ciliary localization of 715 proteins in three cell lines. "
            "Used here as localization evidence for module members; most calls are graded Approved or Uncertain.")},
        TANOS, GOETZ, LU, GARCIA, TOROPOVA, PUGACHEVA, MIYAMOTO,
    ],
    "notes": (
        "Draft built in the HUMAN_PROTEIN_ATLAS project. Members and UniProt accessions come from "
        "projects/HUMAN_PROTEIN_ATLAS/cilium_life_cycle/candidate_members.tsv (UniProt REST). Several roles have no "
        "GO molecular-function term (distal appendage scaffold, transition zone barrier, IFT adaptor, microtubule "
        "depolymerase) and carry preferred_term only. BBSome cargo export is a separate module (modules/bbsome.yaml). "
        "Motile cilia, centriole duplication and the ciliary pocket are outside this boundary."),
    "module": {
        "id": "primary_cilium_life_cycle",
        "label": "Primary cilium life cycle",
        "module_type": "ORGANELLE_LIFECYCLE",
        "concepts": [
            concept("GO:0044782", "Assembly, arrangement and disassembly of a cilium."),
            concept("GO:0097730"),
        ],
        "context": {
            "taxa": [{"preferred_term": "Homo sapiens", "term": {"id": "NCBITaxon:9606", "label": "Homo sapiens"}}],
            "conditions": [{"preferred_term": "quiescent or differentiated cells that form a primary cilium",
                            "description": "Cilia assemble in G0/G1 and are resorbed before mitosis."}],
        },
        "parts": parts,
        "connections": [
            {"source": "mother_centriole_licensing", "target": "ciliary_vesicle_formation", "connection_type": "PRECEDES"},
            {"source": "ciliary_vesicle_formation", "target": "transition_zone_assembly", "connection_type": "PRECEDES"},
            {"source": "transition_zone_assembly", "target": "axoneme_extension_ift", "connection_type": "PRECEDES"},
            {"source": "axoneme_extension_ift", "target": "ciliary_membrane_composition", "connection_type": "PRECEDES"},
            {"source": "ciliary_membrane_composition", "target": "cilium_disassembly", "connection_type": "PRECEDES",
             "description": "A mature cilium is resorbed when the cell re-enters the cell cycle."},
            {"source": "cilium_length_control", "target": "axoneme_extension_ift", "connection_type": "NEGATIVELY_REGULATES",
             "description": "RCK kinases and KIF7 limit axoneme length."},
        ],
    },
    "knowledge_gaps": [
        {"gap_statement": "GO has no term for regulation of cilium length or for a cytoplasmic dynein-2 complex.",
         "boundary": "Length control is modeled with regulation of cilium assembly; dynein-2 is located to the axoneme.",
         "gap_kind": ["ONTOLOGY"], "status": "OPEN",
         "significance": "Length-control kinases and the retrograde motor cannot be annotated precisely.",
         "resolution": "Propose 'regulation of cilium length' and 'cytoplasmic dynein-2 complex' to GO."},
        {"gap_statement": "Distal appendage, transition zone and IFT adaptor proteins lack a molecular-function term.",
         "boundary": "These annotons carry preferred_term functions without GO ids.",
         "gap_kind": ["ONTOLOGY", "BIOLOGY"], "status": "OPEN",
         "significance": "Most structural ciliogenesis proteins are MF-dark.",
         "resolution": "Review member genes and consider structural-constituent or adaptor MF terms case by case."},
        {"gap_statement": "Many module members have only Approved or Uncertain HPA cilium-atlas calls.",
         "boundary": "HPA grades reflect antibody validation and literature agreement, not biological truth.",
         "gap_kind": ["CURATION"], "status": "OPEN",
         "significance": "HPA cilium localizations for core members are mostly absent from GOA.",
         "resolution": "Use module membership plus literature to decide which atlas calls should become annotations."},
    ],
}


class Dumper(yaml.SafeDumper):
    pass


def str_presenter(dumper, data):
    if len(data) > 100:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=">")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


Dumper.add_representer(str, str_presenter)
OUT.write_text(yaml.dump(doc, Dumper=Dumper, sort_keys=False, width=100, allow_unicode=True))
print(f"wrote {OUT}")
