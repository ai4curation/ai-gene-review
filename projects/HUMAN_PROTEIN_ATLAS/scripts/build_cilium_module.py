#!/usr/bin/env python3
"""Build modules/primary_cilium_life_cycle.yaml from a compact curated spec.

The spec below is the curated content (stages, roles, GO terms, citations).
UniProt accessions and names are NOT typed here: they are read from
cilium_life_cycle/candidate_members.yaml, which was populated from the UniProt
REST API. GO ids in the spec were checked against OLS (2026-10-03); PMIDs were
checked against PubMed.

Usage (from repo root):
    uv run python projects/HUMAN_PROTEIN_ATLAS/scripts/build_cilium_module.py
"""

import re
from pathlib import Path

import yaml

WORK = Path("projects/HUMAN_PROTEIN_ATLAS/cilium_life_cycle")
OUT = Path("modules/primary_cilium_life_cycle.yaml")

MEMBERS = {r["gene"]: r for r in yaml.safe_load((WORK / "candidate_members.yaml").read_text())["members"]}

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
    "GO:0003925": "G protein activity",
    "GO:0001918": "farnesylated protein binding",
    "GO:0043539": "protein serine/threonine kinase activator activity",
    "GO:0030295": "protein kinase activator activity",
    "GO:0008289": "lipid binding",
    "GO:1903441": "protein localization to ciliary membrane",
    "GO:0030674": "protein-macromolecule adaptor activity",
    "GO:0015631": "tubulin binding",
    "GO:0140597": "protein carrier activity",
    "GO:0051010": "microtubule plus-end binding",
    "GO:0019894": "kinesin binding",
    "GO:0005814": "centriole",
    "GO:0030050": "vesicle transport along actin filament",
    "GO:0000146": "microfilament motor activity",
    "GO:0016887": "ATP hydrolysis activity",
    "GO:0031115": "negative regulation of microtubule polymerization",
    "GO:1902856": "negative regulation of non-motile cilium assembly",
    "GO:0005868": "cytoplasmic dynein complex",
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

KANIE = ev("PMID:39882855", "CEP89 positions myristoylated NCS1 at the distal appendages, where it captures preciliary "
           "vesicles for ciliary vesicle formation.")
TTBK2_KIF2A = ev("PMID:39930500", "TTBK2 restrains the microtubule depolymerizer KIF2A at the mother centriole to "
                 "support primary cilia growth.")
HEF1_AURA = ev("PMID:16184168", "HEF1/NEDD9 activates Aurora A in vitro and is required for its activation at the "
               "centrosome.")
ISMAIL = ev("PMID:22002721", "PDE6D is a GDI-like carrier for farnesylated cargo whose release is triggered by "
            "ARL2-GTP or ARL3-GTP.")
WRIGHT = ev("PMID:22085962", "An ARL3-UNC119-RP2 GTPase cycle targets myristoylated NPHP3 to the primary cilium.")
KIF7_TIP = ev("PMID:24952464", "KIF7 organizes the cilium tip compartment by limiting microtubule growth at the tip.")
MAK_RET = ev("PMID:39293864", "Ccrk-Mak/Ick signaling regulates ciliary transport and is essential for retinal "
             "photoreceptor survival.")
RPGRIP1L_TZ = ev("PMID:26392567", "Mks5/RPGRIP1L is required to form the transition zone and its ciliary zone of "
                 "exclusion.")
MKS_NPHP = ev("PMID:21422230", "MKS and NPHP modules cooperate to establish basal body/transition zone membrane "
              "associations and ciliary gate function.")


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
            "CEP83 then SCLT1 and CEP89 then FBF1 and CEP164, dock the centriole to membrane. CEP164 recruits TTBK2, "
            "which triggers removal of the CP110-CEP97 cap by phosphorylating cap-anchoring proteins (MPHOSPH9, "
            "CEP83); CP110 itself is not a known TTBK2 substrate. KIF24 recruits the cap and depolymerizes centriolar "
            "microtubules, restraining ciliogenesis in cycling cells. CEP89 also positions NCS1 to capture "
            "preciliary vesicles, linking this stage to ciliary vesicle formation. FBF1 is not needed for licensing "
            "itself (cap removal and TTBK2 recruitment are normal without it) but gates IFT and membrane-protein entry "
            "at the ciliary base."),
        "evidence": [TANOS, GOETZ, KOBAYASHI, KANIE],
        "annotons": [
            annoton("distal_appendage_assembly", "Distal appendage (transition fiber) complex",
                    complex_sel("centriole distal appendage complex",
                                "Distal appendage proteins assembled hierarchically on the mother centriole.",
                                ["CEP83", "SCLT1", "CEP89", "FBF1", "CEP164"], "distal appendage component"),
                    "Docks the mother centriole to vesicles and membrane and recruits TTBK2.",
                    fn_label="distal appendage scaffold",
                    fn_desc=("Structural scaffold role; no specific GO molecular-function term is asserted. CEP89 "
                             "additionally acts as an adaptor for NCS1-mediated vesicle capture."),
                    processes=["GO:1905515"], locations=["GO:0036064"], evidence=[TANOS, KANIE]),
            annoton("ttbk2_cap_removal", "TTBK2 triggers CP110 cap removal", gp("TTBK2"),
                    "Kinase recruited by CEP164 that triggers CP110-CEP97 cap removal and IFT recruitment, and "
                    "restrains KIF2A during cilium growth.",
                    fn="GO:0004674", processes=["GO:1905515"], locations=["GO:0036064"],
                    evidence=[GOETZ, TTBK2_KIF2A]),
            annoton("cp110_cep97_cap", "CP110-CEP97 distal cap suppresses ciliogenesis",
                    complex_sel("CP110-CEP97 distal centriole cap",
                                "Cap on the distal end of the mother centriole that blocks axoneme extension until removed.",
                                ["CCP110", "CEP97"], "distal cap component"),
                    "Inhibitory cap; its removal licenses axoneme growth. CEP97 is the adaptor that stabilizes CP110.",
                    fn_label="ciliogenesis suppressor cap",
                    fn_desc="CP110 caps microtubule plus ends; CEP97 acts as a protein-macromolecule adaptor.",
                    processes=["GO:1902018"], locations=["GO:0005814"], evidence=[KOBAYASHI, GOETZ]),
            annoton("kif24_cap_recruitment", "KIF24 recruits the cap and remodels centriolar microtubules", gp("KIF24"),
                    "Kinesin-13 that recruits MPHOSPH9 and the CP110-CEP97 cap to the mother centriole and "
                    "depolymerizes centriolar microtubules, suppressing ciliogenesis in cycling cells.",
                    fn_label="microtubule depolymerase",
                    fn_desc="No GO MF term for microtubule depolymerase activity.",
                    processes=["GO:1902018"], locations=["GO:0005814"], evidence=[KOBAYASHI]),
        ],
        "connections": [
            {"source": "distal_appendage_assembly", "target": "ttbk2_cap_removal", "connection_type": "PROVIDES_INPUT_FOR",
             "description": "CEP164 at the distal appendages recruits TTBK2 to the mother centriole."},
            {"source": "ttbk2_cap_removal", "target": "cp110_cep97_cap", "connection_type": "NEGATIVELY_REGULATES",
             "description": "TTBK2 triggers removal of the CP110-CEP97 cap."},
            {"source": "kif24_cap_recruitment", "target": "cp110_cep97_cap", "connection_type": "POSITIVELY_REGULATES",
             "description": "KIF24 recruits and maintains the cap at the mother centriole."},
        ],
    }),
    part(2, "ciliary vesicle formation", {
        "id": "ciliary_vesicle_formation",
        "label": "Ciliary vesicle formation at the distal appendages",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:1905556")],
        "description": (
            "Myosin-Va delivers preciliary vesicles to the distal appendages, upstream of ciliary vesicle formation. "
            "EHD1 and EHD3 tubulate the docked distal appendage vesicles so they fuse into a single ciliary vesicle; "
            "EHD1 is the dominant paralog in RPE1 cells. CEP290 also acts here, at centriolar satellites, in ciliary "
            "vesicle maturation and RAB8A recruitment."),
        "evidence": [WU, LU],
        "annotons": [
            annoton("myo5a_vesicle_delivery", "Myosin-Va preciliary vesicle delivery", gp("MYO5A"),
                    "Processive actin motor that carries preciliary vesicles to the mother centriole; its dominant "
                    "roles (melanosome and secretory vesicle transport) lie outside cilia.",
                    fn="GO:0000146", processes=["GO:0030050", "GO:0060271"], evidence=[WU]),
            annoton("ehd_vesicle_tubulation", "EHD1/EHD3 membrane tubulation",
                    complex_sel("EHD1/EHD3 membrane-shaping proteins",
                                "Membrane-tubulating EH-domain ATPases acting on distal appendage vesicles.",
                                ["EHD1", "EHD3"], "membrane-shaping ATPase"),
                    "Tubulate distal appendage vesicles to form the ciliary vesicle.",
                    fn="GO:0016887", fn_label="ATP hydrolysis activity",
                    processes=["GO:1905556"], locations=["GO:0097721"], evidence=[LU]),
        ],
        "connections": [
            {"source": "myo5a_vesicle_delivery", "target": "ehd_vesicle_tubulation", "connection_type": "PRECEDES",
             "description": "Delivered vesicles are remodeled by EHD1/EHD3 into the ciliary vesicle."},
        ],
    }),
    part(3, "ciliary membrane extension", {
        "id": "ciliary_membrane_extension",
        "label": "Ciliary membrane supply and extension",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:0060271")],
        "description": (
            "Once the ciliary vesicle has formed, the RAB11-Rabin8-RAB8 cascade supplies membrane for the growing "
            "ciliary sheath; RAB8 is activated only after ciliary vesicle assembly. RAB8A is pleiotropic and also acts "
            "in exocytosis and endocytic recycling."),
        "evidence": [NACHURY, LU],
        "annotons": [
            annoton("rabin8_rab8_gef", "Rabin8 activates Rab8", gp("RAB3IP"),
                    "RAB8 guanine nucleotide exchange factor, delivered to the mother centriole downstream of RAB11.",
                    fn="GO:0005085", processes=["GO:0060271"], evidence=[NACHURY]),
            annoton("rab8_membrane_supply", "Rab8 ciliary membrane delivery", gp("RAB8A"),
                    "GTP-bound RAB8A enters the cilium and promotes ciliary membrane extension.",
                    fn="GO:0003924", processes=["GO:0060271"], locations=["GO:0060170"], evidence=[NACHURY, LU]),
        ],
        "connections": [
            {"source": "rabin8_rab8_gef", "target": "rab8_membrane_supply", "connection_type": "POSITIVELY_REGULATES",
             "description": "Rabin8 loads RAB8A with GTP."},
        ],
    }),
    part(4, "transition zone assembly", {
        "id": "transition_zone_assembly",
        "label": "Transition zone assembly",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:1905349")],
        "description": (
            "The transition zone forms between basal body and axoneme and gates ciliary membrane composition. "
            "RPGRIP1L acts upstream as the foundational assembly factor for both the MKS and NPHP modules and CEP290. "
            "In the NPHP module, NPHP4 is the adaptor hub bridging RPGRIP1L and NPHP1; NPHP1 depends on both to reach "
            "the transition zone. MKS1-B9D2-B9D1 form a linear core of the MKS module. CEP290 is its own transition "
            "zone component, not an MKS subunit. GO has merged the former basal body-plasma membrane docking and "
            "transition fiber assembly terms into this process."),
        "evidence": [GARCIA, RPGRIP1L_TZ, MKS_NPHP],
        "annotons": [
            annoton("rpgrip1l_tz_foundation", "RPGRIP1L founds the transition zone", gp("RPGRIP1L"),
                    "Foundational transition zone assembly factor upstream of the MKS and NPHP modules and CEP290.",
                    fn_label="transition zone scaffold",
                    processes=["GO:1905349"], locations=["GO:0035869"], evidence=[RPGRIP1L_TZ]),
            annoton("mks_module", "MKS module",
                    complex_sel("MKS complex", "Tectonic/MKS ciliopathy protein complex at the transition zone.",
                                ["MKS1", "TMEM67", "CC2D2A", "B9D1", "B9D2", "TCTN1", "TCTN2", "TMEM216", "TMEM231"],
                                "MKS module component", "GO:0036038"),
                    "Transition zone gate that controls entry of ciliary membrane proteins.",
                    fn_label="ciliary diffusion barrier",
                    fn_desc="Barrier/gating role; no GO MF term asserted.",
                    processes=["GO:1905349"], locations=["GO:0035869"], evidence=[GARCIA]),
            annoton("nphp_module", "NPHP module",
                    complex_sel("NPHP module", "Nephronophthisis proteins at the transition zone; NPHP4 is the hub.",
                                ["NPHP4", "NPHP1"], "NPHP module component"),
                    "Second transition zone module, partly redundant with the MKS module.",
                    fn="GO:0030674",
                    processes=["GO:1905349"], locations=["GO:0035869"], evidence=[MKS_NPHP]),
            annoton("cep290_tz_scaffold", "CEP290 transition zone scaffold", gp("CEP290"),
                    "Builds the microtubule-to-membrane Y-links of the transition zone; also acts at centriolar "
                    "satellites in ciliary vesicle maturation.",
                    fn_label="transition zone scaffold",
                    processes=["GO:1905349"], locations=["GO:0035869"], evidence=[GARCIA]),
        ],
        "connections": [
            {"source": "rpgrip1l_tz_foundation", "target": "mks_module", "connection_type": "PRECEDES",
             "description": "RPGRIP1L is required to assemble the MKS module."},
            {"source": "rpgrip1l_tz_foundation", "target": "nphp_module", "connection_type": "PRECEDES",
             "description": "RPGRIP1L is required to recruit the NPHP module."},
            {"source": "rpgrip1l_tz_foundation", "target": "cep290_tz_scaffold", "connection_type": "PRECEDES",
             "description": "RPGRIP1L is required for CEP290 localization."},
        ],
    }),
    part(5, "axoneme extension by IFT", {
        "id": "axoneme_extension_ift",
        "label": "Axoneme extension by intraflagellar transport",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:0042073")],
        "description": (
            "IFT trains carry axoneme precursors and membrane proteins to the ciliary tip and back. Kinesin-2 "
            "(KIF3A/KIF3B motors with the KIFAP3 cargo adaptor) drives anterograde trains carrying IFT-B. Within "
            "IFT-B, IFT81-IFT74 bind tubulin cargo, and IFT88, IFT52 and IFT172 are scaffolds. Dynein-2 drives "
            "retrograde trains. IFT-A acts in retrograde transport and, with TULP3, imports membrane proteins; loss "
            "of IFT-A subunits other than IFT122 has only mild effects on ciliogenesis."),
        "evidence": [PAZOUR, TASCHNER, IFTA, TOROPOVA],
        "annotons": [
            annoton("ift_b_scaffold", "IFT-B scaffold subunits",
                    complex_sel("IFT-B complex (scaffold subunits)", "Structural core and peripheral IFT-B subunits.",
                                ["IFT88", "IFT52", "IFT172"], "IFT-B subunit", "GO:0030992"),
                    "Backbone of anterograde IFT trains.",
                    fn_label="IFT-B structural scaffold",
                    fn_desc="No GO MF term asserted; cargo binding is shown only for IFT81-IFT74.",
                    processes=["GO:0035720", "GO:0060271"], locations=["GO:0097730"], evidence=[PAZOUR, TASCHNER]),
            annoton("ift81_ift74_tubulin", "IFT81-IFT74 tubulin module",
                    complex_sel("IFT81-IFT74 tubulin-binding module", "IFT-B subcomplex that binds tubulin cargo.",
                                ["IFT81", "IFT74"], "tubulin-binding IFT-B subunit", "GO:0030992"),
                    "Binds tubulin for delivery to the growing axoneme tip.",
                    fn="GO:0015631", processes=["GO:0035720", "GO:0060271"], locations=["GO:0097730"],
                    evidence=[TASCHNER]),
            annoton("ift_a_complex", "IFT-A complex",
                    complex_sel("IFT-A complex", "Retrograde IFT and membrane-protein import complex.",
                                ["IFT140", "IFT122", "WDR35", "TTC21B"], "IFT-A subunit", "GO:0030991"),
                    "Retrograde train component and, with TULP3, carrier for membrane-protein entry into cilia.",
                    fn="GO:0140597", processes=["GO:0035721", "GO:0061512"], locations=["GO:0097730"],
                    evidence=[IFTA, TULP3]),
            annoton("kinesin2_anterograde", "Kinesin-2 motor subunits",
                    complex_sel("kinesin-2 (KIF3A/KIF3B)", "Motor subunits of heterotrimeric kinesin II.",
                                ["KIF3A", "KIF3B"], "kinesin-2 motor subunit", "GO:0016939"),
                    "Anterograde IFT motor.",
                    fn="GO:0008574", processes=["GO:0035720"], locations=["GO:0005930"]),
            annoton("kifap3_cargo_adaptor", "KIFAP3 kinesin-2 cargo adaptor", gp("KIFAP3"),
                    "Non-motor subunit of kinesin II that binds the KIF3A/KIF3B motor and links it to cargo.",
                    fn="GO:0019894", processes=["GO:0035720"]),
            annoton("dynein2_retrograde", "Dynein-2",
                    complex_sel("cytoplasmic dynein-2", "Retrograde IFT motor complex; DYNC2H1 is the motor, the "
                                "intermediate and light intermediate chains contribute.",
                                ["DYNC2H1", "DYNC2LI1", "DYNC2I1", "DYNC2I2"], "dynein-2 subunit", "GO:0005868"),
                    "Retrograde IFT motor, carried to the tip in an autoinhibited state on anterograde trains.",
                    fn="GO:0008569", processes=["GO:0035721"], locations=["GO:0005930"], evidence=[TOROPOVA]),
        ],
        "connections": [
            {"source": "kinesin2_anterograde", "target": "ift_b_scaffold", "connection_type": "PROVIDES_INPUT_FOR",
             "description": "Kinesin-2 moves IFT-B trains toward the ciliary tip."},
            {"source": "kifap3_cargo_adaptor", "target": "kinesin2_anterograde", "connection_type": "PROVIDES_INPUT_FOR",
             "description": "KIFAP3 links cargo to the kinesin-2 motor."},
            {"source": "dynein2_retrograde", "target": "ift_a_complex", "connection_type": "PROVIDES_INPUT_FOR",
             "description": "Dynein-2 returns IFT-A trains to the base."},
        ],
    }),
    part(6, "ciliary membrane composition", {
        "id": "ciliary_membrane_composition",
        "label": "Ciliary membrane identity and protein targeting",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:0061512")],
        "description": (
            "Mature cilia keep a distinct membrane. ARL13B activates ARL3, a GTP-dependent switch whose GTP-bound form "
            "releases lipidated cargo from PDE6D (farnesylated/prenylated cargo) and UNC119B (myristoylated cargo) "
            "inside the cilium; RP2 inactivates ARL3. INPP5E keeps PI(4,5)P2 low in the ciliary membrane, and TULP3 "
            "couples IFT-A to phosphoinositides to import GPCRs. PDE6D also solubilizes farnesylated RAS outside "
            "cilia. BBSome-mediated export is modeled in modules/bbsome.yaml."),
        "evidence": [GOTTHARDT, TULP3, INPP5E_EV, ISMAIL, WRIGHT],
        "annotons": [
            annoton("arl13b_arl3_gef", "ARL13B activates ARL3", gp("ARL13B"),
                    "Ciliary membrane GTPase that acts as GEF for ARL3.",
                    fn="GO:0005085", processes=["GO:0061512"], locations=["GO:0060170"], evidence=[GOTTHARDT]),
            annoton("arl3_cargo_release", "ARL3 releases lipidated cargo", gp("ARL3"),
                    "ARL3-GTP binds PDE6D and UNC119B and displaces their lipidated cargo inside the cilium; its intrinsic "
                    "GTP hydrolysis is negligible without RP2.",
                    fn="GO:0003925", processes=["GO:0061512"], evidence=[GOTTHARDT]),
            annoton("pde6d_prenyl_carrier", "PDE6D carries farnesylated cargo", gp("PDE6D"),
                    "GDI-like carrier for farnesylated and prenylated cargo such as INPP5E and PDE6 subunits.",
                    fn="GO:0001918", processes=["GO:0061512"], evidence=[ISMAIL]),
            annoton("unc119b_myristoyl_carrier", "UNC119B carries myristoylated cargo", gp("UNC119B"),
                    "Binds the myristoyl group of cargo such as NPHP3 and delivers it to the ciliary membrane.",
                    fn="GO:0008289", processes=["GO:1903441"], evidence=[WRIGHT]),
            annoton("rp2_arl3_gap", "RP2 inactivates ARL3", gp("RP2"),
                    "GTPase-activating protein for ARL3; a regulator, not a cargo carrier.",
                    fn="GO:0005096", processes=["GO:1903441"], evidence=[WRIGHT]),
            annoton("inpp5e_pip2_hydrolysis", "INPP5E sets ciliary phosphoinositides", gp("INPP5E"),
                    "Hydrolyzes PI(4,5)P2 (and PI(3,4,5)P3) in the ciliary membrane.",
                    fn="GO:0004439", locations=["GO:0060170"], evidence=[INPP5E_EV]),
            annoton("tulp3_gpcr_import", "TULP3 links IFT-A to membrane cargo", gp("TULP3"),
                    "Adaptor bridging IFT-A and phosphoinositides for GPCR import.",
                    fn="GO:0030674", processes=["GO:0061512"], evidence=[TULP3]),
        ],
        "connections": [
            {"source": "arl13b_arl3_gef", "target": "arl3_cargo_release", "connection_type": "POSITIVELY_REGULATES",
             "description": "ARL13B loads ARL3 with GTP."},
            {"source": "rp2_arl3_gap", "target": "arl3_cargo_release", "connection_type": "NEGATIVELY_REGULATES",
             "description": "RP2 stimulates ARL3 GTP hydrolysis."},
            {"source": "pde6d_prenyl_carrier", "target": "arl3_cargo_release", "connection_type": "PROVIDES_INPUT_FOR",
             "description": "PDE6D-bound cargo is released by ARL3-GTP."},
            {"source": "unc119b_myristoyl_carrier", "target": "arl3_cargo_release", "connection_type": "PROVIDES_INPUT_FOR",
             "description": "UNC119B-bound cargo is released by ARL3-GTP."},
        ],
    }),
    part(7, "length control", {
        "id": "cilium_length_control",
        "label": "Cilium length control",
        "module_type": "REGULATORY_STEP",
        "concepts": [concept("GO:1902856")],
        "description": (
            "Steady-state length reflects the balance of assembly and turnover at the tip. The RCK kinases CILK1 and "
            "MAK limit length by regulating IFT turnaround; CILK1 is the better-supported length kinase in most cells, "
            "while MAK evidence comes mainly from the photoreceptor connecting cilium. KIF7, a non-motile kinesin-4, "
            "binds growing microtubule plus ends and slows their growth at the tip. GO has no cilium-length term, so "
            "negative regulation of non-motile cilium assembly is used."),
        "evidence": [ICK, ICK_MOK, MAK_RET, KIF7_TIP],
        "annotons": [
            annoton("rck_kinases", "RCK kinases restrict cilium length",
                    complex_sel("RCK kinases", "Ciliary length-control kinases (not a stable complex).",
                                ["CILK1", "MAK"], "length-control kinase"),
                    "Phosphorylate kinesin-2 and IFT components to control IFT turnaround and length.",
                    fn="GO:0004674", processes=["GO:1902856"], locations=["GO:0097542"],
                    evidence=[ICK, ICK_MOK, MAK_RET]),
            annoton("kif7_tip_organizer", "KIF7 limits microtubule growth at the tip", gp("KIF7"),
                    "Non-motile kinesin-4 that binds microtubule plus ends at the ciliary tip and slows their growth; "
                    "also a core Hedgehog-pathway regulator.",
                    fn="GO:0051010", processes=["GO:0031115", "GO:1902856"], locations=["GO:0097542"],
                    evidence=[KIF7_TIP]),
        ],
    }),
    part(8, "cilium disassembly", {
        "id": "cilium_disassembly",
        "label": "Cilium disassembly before cell-cycle re-entry",
        "module_type": "BIOLOGICAL_PROCESS",
        "concepts": [concept("GO:0061523")],
        "description": (
            "On cell-cycle re-entry the cilium is resorbed so the centrioles can act at the spindle poles. NEDD9 and "
            "Pitchfork (CIMAP3) activate Aurora A at the basal body; Aurora A activates the tubulin deacetylase "
            "HDAC6. PLK1 activates KIF2A, which depolymerizes microtubules at the base and is held back by TTBK2 "
            "while the cilium grows. Phosphorylated Tctex-1 (DYNLT1) at the transition zone promotes resorption "
            "independently of dynein. AURKA, PLK1, KIF2A and NEDD9 are pleiotropic: their dominant roles are mitotic "
            "or adhesion-related, and ciliary disassembly is a secondary function."),
        "evidence": [PUGACHEVA, MIYAMOTO, KINZEL, TCTEX, HEF1_AURA, TTBK2_KIF2A],
        "annotons": [
            annoton("aurka_disassembly_kinase", "Aurora A drives disassembly", gp("AURKA"),
                    "Basal body kinase activated by NEDD9 and Pitchfork; phosphorylates HDAC6.",
                    fn="GO:0004674", processes=["GO:0061523"], locations=["GO:0036064"], evidence=[PUGACHEVA]),
            annoton("nedd9_aurka_activation", "NEDD9 activates Aurora A", gp("NEDD9"),
                    "Cas-family scaffold that activates Aurora A at the basal body.",
                    fn="GO:0043539", processes=["GO:0061523"], evidence=[PUGACHEVA, HEF1_AURA]),
            annoton("pitchfork_aurka_activation", "Pitchfork activates Aurora A", gp("CIMAP3"),
                    "Activates Aurora A at the basal body to drive cilium disassembly.",
                    fn="GO:0030295", processes=["GO:0061523"], evidence=[KINZEL]),
            annoton("hdac6_deacetylation", "HDAC6 deacetylates axonemal tubulin", gp("HDAC6"),
                    "Tubulin deacetylase activated by Aurora A.",
                    fn="GO:0042903", processes=["GO:0061523"], evidence=[PUGACHEVA]),
            annoton("plk1_kinase", "PLK1 activates KIF2A", gp("PLK1"),
                    "Kinase that activates KIF2A at the basal body.",
                    fn="GO:0004674", processes=["GO:0061523"], evidence=[MIYAMOTO]),
            annoton("kif2a_depolymerization", "KIF2A depolymerizes microtubules", gp("KIF2A"),
                    "Kinesin-13 ATP-dependent microtubule depolymerase acting at the mother centriole.",
                    fn_label="ATP-dependent microtubule depolymerase activity",
                    fn_desc="No GO MF term exists; proposed as a new term in the KIF2A review.",
                    processes=["GO:0007019", "GO:0061523"], locations=["GO:0036064"],
                    evidence=[MIYAMOTO, TTBK2_KIF2A]),
            annoton("tctex1_resorption", "Phosphorylated Tctex-1 promotes resorption", gp("DYNLT1"),
                    "Phospho-Tctex-1 at the transition zone promotes ciliary resorption, independently of dynein.",
                    fn_label="resorption promoter", processes=["GO:0061523"], locations=["GO:0035869"],
                    evidence=[TCTEX]),
        ],
        "connections": [
            {"source": "nedd9_aurka_activation", "target": "aurka_disassembly_kinase", "connection_type": "POSITIVELY_REGULATES",
             "description": "NEDD9 activates Aurora A."},
            {"source": "pitchfork_aurka_activation", "target": "aurka_disassembly_kinase", "connection_type": "POSITIVELY_REGULATES",
             "description": "Pitchfork activates Aurora A."},
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
        "Revised 2026-10-03 after gene reviews of all 60 members (genes/human/<GENE>/). "
        "Draft built in the HUMAN_PROTEIN_ATLAS project. Members and UniProt accessions come from "
        "projects/HUMAN_PROTEIN_ATLAS/cilium_life_cycle/candidate_members.yaml (UniProt REST). Several roles have no "
        "GO molecular-function term (distal appendage scaffold, transition zone barrier, IFT adaptor, microtubule "
        "depolymerase) and carry preferred_term only. BBSome cargo export is a separate module (modules/bbsome.yaml). "
        "Motile cilia, centriole duplication and the ciliary pocket are outside this boundary. "
        "Ontology gaps: GO has no term for regulation of cilium length (negative regulation of non-motile cilium "
        "assembly is used), no cytoplasmic dynein-2 complex term (the generic cytoplasmic dynein complex is used) and "
        "no microtubule depolymerase activity term (KIF2A, KIF24); these are candidate GO term requests. Curation "
        "note: many members have only Approved or Uncertain HPA cilium-atlas calls, which are not exported to GOA; "
        "whether those calls should become annotations is tracked in the HUMAN_PROTEIN_ATLAS project."),
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
            {"source": "ciliary_vesicle_formation", "target": "ciliary_membrane_extension", "connection_type": "PRECEDES",
             "description": "RAB8 is activated only after the ciliary vesicle has formed."},
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
        {"gap_statement": ("The molecular activities of the distal appendage proteins (CEP83, SCLT1, FBF1, CEP164), "
                           "the transition zone MKS-module proteins and the IFT-B scaffold subunits (IFT88, IFT52, "
                           "IFT172) are unknown beyond 'structural scaffold'."),
         "boundary": ("Their requirement for ciliogenesis and their positions are well established; what each "
                      "protein does mechanistically (binding partners, membrane contacts, gating chemistry) is not."),
         "gap_kind": ["BIOLOGY"], "status": "OPEN",
         "significance": ("Most structural ciliogenesis proteins have no defined molecular function, so the module "
                          "can say where they act but not how."),
         "resolution": ("Reconstitution and structure-function work, for example in vitro membrane-binding and "
                        "barrier assays with purified MKS-module and distal appendage subcomplexes.")},
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
