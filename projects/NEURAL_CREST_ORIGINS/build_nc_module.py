"""Build modules/neural_crest_gene_regulatory_network.yaml from validated gene reviews.

Every evidence quote is copied verbatim from a review's core_functions.supported_by
(already validated against the cached publication), and every title from the
publication cache, so nothing is retyped by hand.
"""
import re, yaml, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]

def review(org, gene):
    return yaml.safe_load(open(ROOT / f"genes/{org}/{gene}/{gene}-ai-review.yaml"))

def recname(org, gene):
    txt = open(ROOT / f"genes/{org}/{gene}/{gene}-uniprot.txt").read()
    m = re.search(r"^DE   RecName: Full=([^;{]+)", txt, re.M)
    return m.group(1).strip()

def title(ref):
    if not ref.startswith("PMID:"):
        return None
    p = ROOT / f"publications/PMID_{ref.split(':')[1]}.md"
    text = open(p).read()
    if text.startswith("---"):
        front = text.split("---", 2)[1]
        return (yaml.safe_load(front) or {}).get("title")
    return None

def evidence(org, gene, bp_id, statement, n=2, refs=None):
    """Pull up to n supported_by quotes from the core function carrying bp_id."""
    d = review(org, gene)
    out = []
    if bp_id in ("NPB", "NPM"):
        wanted = "neural plate border formation" if bp_id == "NPB" else "neural crest progenitor maintenance"
        for pt in d.get("proposed_new_terms") or []:
            if pt.get("proposed_name") == wanted:
                for sb in pt.get("supported_by") or []:
                    ref = sb["reference_id"]
                    if refs and ref not in refs:
                        continue
                    item = {"source_id": ref}
                    t = title(ref)
                    if t:
                        item["title"] = t
                    item["statement"] = statement
                    item["supporting_text"] = sb["supporting_text"]
                    out.append(item)
                    if len(out) >= n:
                        return out
        assert out, (gene, bp_id)
        return out
    for cf in d.get("core_functions") or []:
        bps = [p.get("id") for p in cf.get("directly_involved_in") or []]
        if bp_id not in bps:
            continue
        for sb in cf.get("supported_by") or []:
            ref = sb["reference_id"]
            if not ref.startswith("PMID:"):
                continue
            if refs and ref not in refs:
                continue
            item = {"source_id": ref}
            t = title(ref)
            if t:
                item["title"] = t
            item["statement"] = statement
            item["supporting_text"] = sb["supporting_text"]
            if item not in out:
                out.append(item)
            if len(out) >= n:
                return out
    assert out, (gene, bp_id)
    return out

def term(i, l):
    return {"id": i, "label": l}

def annoton(aid, label, org, gene, mf, procs, role, ev_bp, statement, refs=None, n=2):
    d = review(org, gene)
    return {
        "id": aid,
        "label": label,
        "participant": {
            "selector_type": "GENE_PRODUCT",
            "gene_product": {
                "preferred_term": d["gene_symbol"],
                "term": term(f"UniProtKB:{d['id']}", recname(org, gene)),
                "description": f"{d['taxon']['label']} {d['gene_symbol']}; reviewed in genes/{org}/{gene}/.",
            },
        },
        "function": {"preferred_term": mf[1], "term": term(*mf)},
        "processes": [{"preferred_term": p[1], "term": term(*p)} if p[0] else {"preferred_term": p[1]} for p in procs],
        "locations": [{"preferred_term": "nucleus", "term": term("GO:0005634", "nucleus")}],
        "role_description": role,
        "evidence": evidence(org, gene, ev_bp, statement, n=n, refs=refs),
    }

ACT = ("GO:0001228", "DNA-binding transcription activator activity, RNA polymerase II-specific")
REP = ("GO:0001227", "DNA-binding transcription repressor activity, RNA polymerase II-specific")
TF = ("GO:0000981", "DNA-binding transcription factor activity, RNA polymerase II-specific")
INH = ("GO:0140416", "transcription regulator inhibitor activity")
NCF = ("GO:0014029", "neural crest formation")
# Proposed replacement for GO:0014029 in the border layer (projects/NEURAL_CREST_FORMATION_OBSOLETION.md)
NPB = (None, "neural plate border formation (proposed new term; replaces GO:0014029, proposed for obsoletion)")
NPM = (None, "neural crest progenitor maintenance (proposed new term; replaces GO:0014029, proposed for obsoletion)")
NCC = ("GO:0014034", "neural crest cell fate commitment")
NCS = ("GO:0014036", "neural crest cell fate specification")
MIG = ("GO:0001755", "neural crest cell migration")
DEL = ("GO:0036032", "neural crest cell delamination")
CSK = ("GO:0048701", "embryonic cranial skeleton morphogenesis")

border = {
    "id": "neural_plate_border_specification",
    "label": "Neural plate border specification",
    "module_type": "DEVELOPMENTAL_PROCESS",
    "description": (
        "Wnt, intermediate BMP and FGF signals at the edge of the neural plate are read out by a set of "
        "transcription factors that define the neural plate border, a competence territory that gives rise "
        "to neural crest, preplacodal ectoderm, dorsal neural tube and epidermis. Border specifiers act "
        "upstream of, and are required for, crest specifier expression, but individually do not impose crest "
        "fate; Pax3 and Zic1 together are necessary and sufficient to do so."
    ),
    "concepts": [{"preferred_term": "neural plate border formation (proposed new term)",
                  "description": "No GO term exists. GO:0014029 neural crest formation is defined as forming this ectodermal region but is placed under epithelial to mesenchymal transition; it is proposed for obsoletion, with this new term as one replacement (projects/NEURAL_CREST_FORMATION_OBSOLETION.md)."}],
    "variant_sets": [{
        "id": "pax37_paralogs",
        "label": "Pax3/7 border specifier (paralog deployment differs by lineage)",
        "axis": "Pax3/7 paralog / vertebrate lineage",
        "selection": "ONE_OR_MORE",
        "notes": "Frog leads with Pax3, chick with Pax7, and mouse uses both redundantly; amphioxus has a single Pax3/7 at the border.",
        "variants": [
            {"id": "pax3_variant", "label": "Pax3 (lead paralog in frog)", "module_type": "DEVELOPMENTAL_PROCESS",
             "annotons": [annoton("pax3_border", "Pax3 border specifier", "XENLA", "pax3-a", ACT, [NPB, NCC],
                "Paired-box activator at the border; with Zic1 directly activates crest specifier genes.",
                "GO:0014034", "Pax3 and Zic1 directly activate the crest specifier genes.", refs=["PMID:24360906"])]},
            {"id": "pax7_variant", "label": "Pax7 (lead paralog in chick)", "module_type": "DEVELOPMENTAL_PROCESS",
             "annotons": [annoton("pax7_border", "Pax7 border specifier", "human", "PAX7", ACT, [NPB],
                                  "Paired-box border factor required for crest specifier expression in chick; binds the FoxD3 NC1 enhancer with Msx1 and Ets1.",
                                  "NPB", "Pax7 is required for crest formation and binds the FoxD3 NC1 enhancer.")]},
        ],
    }],
    "annotons": [
        annoton("gbx2_border", "Gbx2 border specifier", "XENLA", "gbx2", REP, [NPB],
                "Wnt-responsive repressor acting upstream of the border factors Pax3 and Msx1; required for crest and limits the preplacodal domain.",
                "NPB", "Gbx2 is required for neural crest and acts upstream of the border factors Pax3 and Msx1."),
        annoton("msx1_border", "Msx1 border specifier", "human", "MSX1", TF, [NPB],
                "BMP-responsive homeodomain factor at the neural fold; induces Pax3 and Zic cell-autonomously.",
                "NPB", "Intermediate BMP specifies Msx expression at the border, and Msx1 induces Pax3 and Zic."),
        annoton("tfap2a_border", "AP-2alpha border initiator", "human", "TFAP2A", ACT, [NPB],
                "Earliest known border specifier; mediates Wnt input to initiate the border and activate pax3.",
                "NPB", "AP-2alpha initiates neural plate border patterning and activates pax3.", refs=["PMID:21169220"]),
        annoton("tfap2c_border", "AP-2gamma (TFAP2A–TFAP2C) border inducer", "human", "TFAP2C", ACT, [NPB],
                "Partners TFAP2A as a heterodimer during border induction; lost from crest at specification, when TFAP2B replaces it.",
                "NPB", "TFAP2A/C heterodimers mediate neural plate border induction.", refs=["PMID:31848212"]),
        annoton("zic1_border", "Zic1 border specifier", "XENLA", "zic1", ACT, [NPB, NCC],
                "Zinc-finger activator at the border; with Pax3 commits cells to crest, alone promotes preplacodal or neural fates.",
                "NPB", "Pax3 and Zic1 are early border factors, necessary and sufficient to promote crest fate."),
    ],
}

competence = {
    "id": "progenitor_competence_maintenance",
    "label": "Maintenance of border/crest progenitor competence",
    "module_type": "DEVELOPMENTAL_PROCESS",
    "description": (
        "Factors shared with the pluripotent blastula keep border and premigratory crest progenitors "
        "proliferative and undifferentiated, preserving the broad potential that crest cells later deploy. "
        "Loss causes progenitor arrest or death rather than a switch to another fate, so these factors "
        "support crest formation without specifying crest identity. No GO process term captures this role; "
        "a new term, neural crest progenitor maintenance, is proposed for it."
    ),
    "concepts": [{"preferred_term": "neural crest progenitor maintenance (proposed new term)",
                  "description": "Proposed as a child of GO:0019827 stem cell population maintenance, replacing GO:0014029 for competence factors (projects/NEURAL_CREST_FORMATION_OBSOLETION.md)."}],
    "annotons": [
        annoton("myc_competence", "c-Myc competence factor", "XENLA", "myc-a", TF, [NPM],
                "Blastula-inherited Myc/Max E-box factor at the border before slug; required for crest precursors.",
                "NPM", "c-Myc is at the border before slug and is required for crest precursors."),
        annoton("id3_competence", "Id3 bHLH inhibitor", "XENLA", "id3-a", INH,
                [NPM, ("GO:0045596", "negative regulation of cell differentiation")],
                "Dominant-negative HLH protein that keeps crest progenitors cycling and undifferentiated.",
                "NPM", "Id3 maintains the cycling crest progenitor pool rather than specifying crest fate."),
        annoton("pou5f3_competence", "Oct25 (Pou5f3) competence factor", "XENLA", "pou5f1.1", TF, [NPM],
                "POU-V blastula pluripotency factor retained at the neural plate border; required (with its paralog) for snai2 and foxd3, and its gain expands border and crest markers.",
                "NPM", "Pou5f3 is expressed at the border and is required for crest specifier expression.", refs=["PMID:39060477"]),
        annoton("hes4_competence", "Hairy2 border repressor", "XENLA", "hes4-a", REP,
                [NPM, ("GO:0030514", "negative regulation of BMP signaling pathway")],
                "bHLH-Orange repressor that holds border cells undifferentiated and tunes Bmp4 levels at the border.",
                "NPM", "Hairy2 keeps border cells undifferentiated and tunes Bmp4 at the border."),
    ],
}

soxe = {
    "id": "soxe_paralogs",
    "label": "SoxE crest specifier (paralog deployment differs by lineage)",
    "axis": "SoxE paralog / vertebrate lineage",
    "selection": "ONE_OR_MORE",
    "notes": (
        "Which SoxE paralog leads crest specification varies: Sox8 in frog, Sox9 in chick and mouse, "
        "sox9a/b in zebrafish, independently duplicated SoxE1/2 in lamprey. The specifier role belongs to "
        "the SoxE group; paralog-specific crest roles should not be transferred by orthology."
    ),
    "variants": [
        {"id": "sox8_variant", "label": "Sox8 (first-wave SoxE in frog)", "module_type": "DEVELOPMENTAL_PROCESS",
         "annotons": [annoton("sox8_spec", "Sox8 crest specifier", "XENLA", "sox8", TF, [NCS],
                              "Earliest SoxE at the lateral neural plate edge; knockdown delays crest induction.",
                              "GO:0014036", "Sox8 knockdown delays crest progenitor induction.")]},
        {"id": "sox9_variant", "label": "Sox9", "module_type": "DEVELOPMENTAL_PROCESS",
         "annotons": [annoton("sox9_spec", "Sox9 crest specifier", "XENLA", "sox9-a", ACT, [NCS],
                              "SoxE activator required for crest specification but not migration.",
                              "GO:0014036", "Sox9 is an activator required for crest specification, not migration.")]},
        {"id": "sox10_variant", "label": "Sox10", "module_type": "DEVELOPMENTAL_PROCESS",
         "annotons": [annoton("sox10_spec", "Sox10 crest specifier", "XENLA", "sox10", TF, [NCS],
                              "SoxE factor acting in the earliest steps of crest specification; later drives pigment and glial lineages.",
                              "GO:0014036", "Sox10 acts early in crest specification and expands the Slug domain.")]},
    ],
}

specification = {
    "id": "neural_crest_fate_specification",
    "label": "Neural crest fate specification",
    "module_type": "DEVELOPMENTAL_PROCESS",
    "description": (
        "Border inputs switch on a set of crest specifier transcription factors in the prospective crest. "
        "They act within the crest domain, cross-regulate one another, and are required for, and in "
        "combination sufficient for, crest identity."
    ),
    "concepts": [{"preferred_term": NCS[1], "term": term(*NCS)}],
    "annotons": [
        annoton("foxd3_spec", "FoxD3 crest specifier", "XENLA", "foxd3-a", REP, [NCC],
                "Forkhead repressor recruiting Groucho/TLE; induces crest markers when overexpressed.",
                "GO:0014034", "FoxD3 is expressed in the presumptive crest and induces crest markers."),
        annoton("snai1_spec", "Snail1 early crest specifier", "XENLA", "snai1", REP, [NCS],
                "Earliest crest specifier, activated in the first wave with sox8 and myc and directly by Zic1; acts upstream of Snai2. Also expressed in pluripotent blastula cells.",
                "GO:0014036", "Snail1 is an early, Zic1-responsive crest specifier activated with sox8 and myc."),
        annoton("snai2_spec", "Snai2 crest specifier", "XENLA", "snai2", REP, [NCS],
                "E-box repressor required to form crest precursors; acts downstream of the border factors.",
                "GO:0014036", "Snai2 is required to form crest precursors and acts downstream of Zic1/Pax3."),
        annoton("tfap2b_spec", "AP-2beta (TFAP2A–TFAP2B) crest specifier", "human", "TFAP2B", ACT, [NCS],
                "Comes on at the onset of specification, heterodimerises with TFAP2A and recruits it to specification enhancers; represses TFAP2C.",
                "GO:0014036", "TFAP2B is required for crest specification but not the border, and recruits TFAP2A to specification enhancers.", refs=["PMID:31848212"]),
        annoton("tfap2a_spec", "AP-2alpha crest specifier", "human", "TFAP2A", ACT, [NCS],
                "Second, crest-intrinsic deployment of AP-2alpha after its border role.",
                "NPB", "AP-2alpha acts again as a crest specifier after initiating the border.", refs=["PMID:21169220"], n=1),
        annoton("twist1_snai2_inhibition", "Twist1 restraint of Snai2", "XENLA", "twist1", INH, [NCS],
                "Twist binds Snai2 directly and reduces its chromatin occupancy, restraining Snai2-driven crest expansion.",
                "GO:0014036", "Twist binds Snai2 directly and reduces its recruitment to chromatin.", refs=["PMID:23443570"]),
    ],
    "variant_sets": [soxe],
}

emigration = {
    "id": "neural_crest_emigration",
    "label": "Neural crest delamination and migration",
    "module_type": "DEVELOPMENTAL_PROCESS",
    "description": (
        "Specified crest cells lose adhesion to the neural tube, delaminate and migrate along stereotyped "
        "routes. Some specifier factors are redeployed here as effectors."
    ),
    "concepts": [{"preferred_term": DEL[1], "term": term(*DEL)}, {"preferred_term": MIG[1], "term": term(*MIG)}],
    "annotons": [
        annoton("ets1_emigration", "Ets1 delamination effector", "XENLA", "ets1-a", ACT, [DEL, MIG],
                "Ets activator required in the crest for delamination and migration; part of the cranial crest circuit in jawed vertebrates.",
                "GO:0036032", "Ets1 knockdown in the crest disrupts delamination and migration.", refs=["PMID:25691536"], n=1),
        annoton("snai2_migration", "Snai2 migration effector", "XENLA", "snai2", REP, [MIG],
                "Later Snai2 activity, recruiting PRC2 to the E-cadherin promoter, is required for crest migration.",
                "GO:0001755", "Late Snai2 activity is required for crest migration."),
    ],
}

ectomesenchyme = {
    "id": "cranial_ectomesenchyme",
    "label": "Cranial crest ectomesenchyme and skeletogenesis",
    "module_type": "DEVELOPMENTAL_PROCESS",
    "description": (
        "Cranial crest cells adopt an ectomesenchymal, skeletogenic fate and build the cartilage and bone "
        "of the head. This is the vertebrate-specific output most associated with the 'new head'."
    ),
    "concepts": [{"preferred_term": CSK[1], "term": term(*CSK)}],
    "annotons": [
        annoton("twist1_ectomesenchyme", "Twist1 ectomesenchyme driver", "XENLA", "twist1", TF, [CSK],
                "bHLH factor that steers cranial crest to cartilage-forming ectomesenchyme; without it, cells lose Sox9 and drift toward glial fates.",
                "GO:0048701", "Twist depletion loses Sox9 in the branchial arches and head cartilage."),
        annoton("sox9_chondrogenesis", "Sox9 crest chondrogenesis", "XENLA", "sox9-a", ACT,
                [("GO:0002062", "chondrocyte differentiation")],
                "SoxE activator required for crest-derived cranial cartilage.",
                "GO:0002062", "Sox9 knockdown removes crest-derived skeletal elements.", refs=["PMID:11807034"], n=1),
        annoton("tfap2a_craniofacial", "AP-2alpha craniofacial morphogenesis", "human", "TFAP2A", ACT, [CSK],
                "AP-2alpha in crest is required for face, skull and palate morphogenesis.",
                "GO:0048701", "Tfap2a loss, including crest-specific loss, causes craniofacial and palate defects."),
    ],
}

DR = "file:modules/neural_crest_gene_regulatory_network-deep-research-falcon.md"
DR_EDGE_QUOTES = {
    ("gbx2_border", "pax3_border"): "Gbx2 is positioned upstream of *msx1* and *pax3* by epistasis",
    ("gbx2_border", "msx1_border"): "Gbx2 is positioned upstream of *msx1* and *pax3* by epistasis",
    ("tfap2a_border", "pax3_border"): "A stronger direct edge is AP-2α → *pax3*",
    ("twist1_snai2_inhibition", "snai2_spec"): "a permanently activating or permanently inhibiting “TWIST → SNAI2” arrow misstates the mechanism",
}


def conn(s, t, ct, desc):
    c = {"source": s, "target": t, "connection_type": ct, "description": desc}
    q = DR_EDGE_QUOTES.get((s, t))
    if q:
        c["evidence"] = [{"source_id": DR, "statement": "Module deep research (falcon) assessment of this edge.", "supporting_text": q}]
    return c

connections = [
    conn("neural_plate_border_specification", "neural_crest_fate_specification", "PRECEDES",
         "Border specifiers are expressed first and are required for crest specifier expression."),
    conn("progenitor_competence_maintenance", "neural_crest_fate_specification", "PROVIDES_INPUT_FOR",
         "Competence factors keep border progenitors undifferentiated so that specifier inputs can act."),
    conn("neural_crest_fate_specification", "neural_crest_emigration", "PRECEDES",
         "Specified crest cells delaminate and migrate."),
    conn("neural_crest_emigration", "cranial_ectomesenchyme", "PRECEDES",
         "Migrating cranial crest populates the pharyngeal arches and forms skeletogenic ectomesenchyme."),
    conn("gbx2_border", "pax3_border", "POSITIVELY_REGULATES",
         "Gbx2 acts upstream of Pax3, placed by epistasis; direct binding to the pax3 locus is not demonstrated."),
    conn("gbx2_border", "msx1_border", "POSITIVELY_REGULATES",
         "Gbx2 acts upstream of Msx1, placed by epistasis; direct binding to the msx1 locus is not demonstrated."),
    conn("tfap2a_border", "pax3_border", "POSITIVELY_REGULATES",
         "AP-2alpha activates pax3 directly: translation-independent induction, promoter-reporter, site mutation and EMSA/supershift (frog)."),
    conn("msx1_border", "pax3_border", "POSITIVELY_REGULATES", "Msx1 induces Pax3 cell-autonomously."),
    conn("msx1_border", "zic1_border", "POSITIVELY_REGULATES", "Msx1 induces ZicR1/Zic cell-autonomously."),
    conn("pax3_border", "snai2_spec", "POSITIVELY_REGULATES", "Pax3 binds and activates snail2 directly."),
    conn("pax3_border", "foxd3_spec", "POSITIVELY_REGULATES",
         "Pax3/Zic1 activate foxd3 without new protein synthesis (immediate-response target); enhancer occupancy in frog not shown."),
    conn("zic1_border", "foxd3_spec", "POSITIVELY_REGULATES",
         "Pax3/Zic1 activate foxd3 without new protein synthesis (immediate-response target); enhancer occupancy in frog not shown."),
    conn("zic1_border", "snai1_spec", "POSITIVELY_REGULATES",
         "Zic1 binds a snail1 element (EMSA) and activates snail1 without new protein synthesis."),
    conn("snai1_spec", "snai2_spec", "POSITIVELY_REGULATES", "Snail1 acts upstream of Slug/Snai2 in crest specification."),
    conn("tfap2c_border", "tfap2b_spec", "POSITIVELY_REGULATES",
         "TFAP2A/C occupies the TFAP2B locus and is required for its activation at the onset of specification (chick)."),
    conn("tfap2b_spec", "tfap2c_border", "NEGATIVELY_REGULATES",
         "TFAP2B represses TFAP2C cell-autonomously, stabilising the switch from the A/C to the A/B heterodimer (chick)."),
    conn("pax3_border", "tfap2b_spec", "POSITIVELY_REGULATES",
         "Pax3/Zic1 activate tfap2b without new protein synthesis (frog immediate-response target)."),
    conn("zic1_border", "tfap2b_spec", "POSITIVELY_REGULATES",
         "Pax3/Zic1 activate tfap2b without new protein synthesis (frog immediate-response target)."),
    conn("pax7_border", "foxd3_spec", "POSITIVELY_REGULATES",
         "Pax7 binds the FoxD3 NC1 enhancer in vivo (ChIP) with Msx1 and Ets1; its knockdown abolishes NC1/NC2 activity (chick)."),
    conn("pou5f3_competence", "pax3_border", "POSITIVELY_REGULATES",
         "Pou5f3 gain of function expands pax3 (and zic1, snai2) expression."),
    conn("pax3_border", "sox8_spec", "POSITIVELY_REGULATES", "Pax3/Zic1 activate sox8 with snail1 and myc."),
    conn("pax3_border", "twist1_ectomesenchyme", "POSITIVELY_REGULATES", "Pax3 activates twist1 directly."),
    conn("twist1_snai2_inhibition", "snai2_spec", "NEGATIVELY_REGULATES",
         "Twist binds Snai2 and reduces its chromatin occupancy. Stage-specific: Twist later promotes mesenchymal outputs, so this is not a permanent inhibitory edge."),
    conn("hes4_competence", "id3_competence", "PROVIDES_INPUT_FOR",
         "Hairy2 and Id3 act together (with Stat3) to keep progenitors undifferentiated."),
]

doc = {
    "id": "MODULE:neural_crest_gene_regulatory_network",
    "title": "Neural crest gene regulatory network module",
    "description": (
        "The vertebrate neural crest gene regulatory network: the transcriptional program by which signals "
        "at the edge of the neural plate are converted, through a neural plate border layer and a crest "
        "specifier layer, into migratory multipotent crest cells, of which the cranial population forms "
        "skeletogenic ectomesenchyme. A parallel competence layer, shared with pluripotent blastula cells, "
        "keeps progenitors undifferentiated. Border specifiers (Gbx2, Msx1, AP-2alpha, Pax3, Zic1) are "
        "largely ancestral chordate genes already expressed at the amphioxus neural plate border; most crest "
        "specifiers were recruited at the base of vertebrates, mainly by changes in where they are expressed, "
        "and some cranial circuit components (Ets1) were added later in jawed vertebrates. Inducing signals "
        "(Wnt, BMP, FGF) are covered by the wnt_signaling, bmp_signaling and FGF modules and are treated here "
        "as upstream context."
    ),
    "status": "DRAFT",
    "scope": None,
    "evidence": [
        {"source_id": "PMID:25564621", "title": title("PMID:25564621") or "Establishing neural crest identity: a gene regulatory recipe",
         "statement": "Review of the layered neural crest gene regulatory network (border, specifier, effector layers)."},
        {"source_id": "PMID:18562679", "title": title("PMID:18562679"),
         "statement": "Amphioxus has border patterning genes at the neural plate border but lacks most crest specifier expression there.",
         "supporting_text": "neural plate border patterning genes, and melanocyte differentiation genes appear conserved"},
        {"source_id": DR, "statement": "Module deep research supports treating inducing signals as upstream inputs rather than network members.",
         "supporting_text": "WNT, BMP and FGF signaling are upstream inputs"},
        {"source_id": "PMID:31645763", "title": title("PMID:31645763"),
         "statement": "The cranial crest circuit was assembled gradually in gnathostomes; the ancestral crest was trunk-like."},
    ],
    "notes": (
        "Concrete members are the gene products reviewed in projects/NEURAL_CREST_ORIGINS.md: Xenopus laevis "
        "proteins where reviewed Swiss-Prot entries exist, human proteins otherwise. Process terms follow "
        "the replacement rule of projects/NEURAL_CREST_FORMATION_OBSOLETION.md: border genes at the proposed "
        "'neural plate border formation' term (plus GO:0014034 where they directly induce crest fate), crest "
        "specifiers at GO:0014036, and competence factors at the proposed 'neural crest progenitor "
        "maintenance' term. Genes with "
        "roles in more than one layer (AP-2alpha, Snai2, Twist1, Sox9) have one annoton per role, which is "
        "how roles that are non-core at gene level (e.g. Twist1 in ectomesenchyme) become explicit parts here. "
        "Sox10-driven melanocyte and glial differentiation are downstream derivative programs and are out of scope."
    ),
    "module": {
        "id": "neural_crest_gene_regulatory_network",
        "label": "Neural crest gene regulatory network",
        "module_type": "DEVELOPMENTAL_PROCESS",
        "concepts": [{"preferred_term": "neural crest cell differentiation", "term": term("GO:0014033", "neural crest cell differentiation"),
                      "description": "Umbrella term: GO:0014034 fate commitment, GO:0014032 development and GO:0001755 migration all fall under it."}],
        "context": {
            "taxa": [{"preferred_term": "Vertebrata", "term": term("NCBITaxon:7742", "Vertebrata"),
                      "description": "The neural crest is a vertebrate innovation; the border layer is shared with other chordates."}],
            "cellular_components": [{"preferred_term": "nucleus", "term": term("GO:0005634", "nucleus")}],
        },
        "parts": [
            {"order": 1, "role": "define the neural plate border competence territory", "node": border},
            {"order": 1, "role": "keep border and crest progenitors undifferentiated and proliferative", "node": competence},
            {"order": 2, "role": "specify neural crest identity", "node": specification},
            {"order": 3, "role": "delaminate and migrate", "node": emigration},
            {"order": 4, "role": "form cranial skeletogenic ectomesenchyme", "node": ectomesenchyme},
        ],
        "connections": connections,
    },
}
doc["knowledge_gaps"] = [
    {
        "gap_statement": "GO has no term for neural plate border formation or specification, so border specifiers are annotated to GO:0014029 neural crest formation.",
        "boundary": "Affects the neural_plate_border_specification part and every border-specifier gene (Gbx2, Msx1, AP-2alpha, Pax3, Zic1, Hairy2).",
        "gap_kind": ["ONTOLOGY"],
        "status": "OPEN",
        "significance": "The border is a competence territory that also gives rise to placodes, dorsal neural tube and epidermis; annotating it as crest formation conflates the ancestral border layer with the vertebrate crest.",
        "resolution": "Propose a neural plate border formation term to GO and re-place border-specifier annotations under it.",
        "provenance": [
            {"reference_id": "PMID:21169220", "supporting_text": "NB-like pattern in neuralized ectoderm"},
            {"reference_id": "PMID:25564621", "supporting_text": "neural plate border is established by the combined action of distinct signaling pathways"},
        ],
        "proposed_terms": [{
            "proposed_name": "neural plate border formation",
            "proposed_definition": "The formation of the region of ectoderm at the boundary between the neural plate and the non-neural ectoderm, competent to give rise to neural crest, preplacodal ectoderm, dorsal neural tube and epidermis.",
            "justification": "Six reviewed border specifiers have no specific term; the territory is conserved in non-vertebrate chordates that lack neural crest.",
            "supported_by": [
                {"reference_id": "PMID:18562679", "supporting_text": "neural plate border patterning genes, and melanocyte differentiation genes appear conserved"},
                {"reference_id": "PMID:21169220", "supporting_text": "NB-like pattern in neuralized ectoderm"},
            ],
        }],
    },
    {
        "gap_statement": "No GO process term describes maintaining border and crest progenitors in an undifferentiated, proliferative, competent state.",
        "boundary": "Affects the progenitor_competence_maintenance part (c-Myc, Id3, Hairy2).",
        "gap_kind": ["ONTOLOGY", "CURATION"],
        "status": "NARROWING",
        "significance": "Without such a term these factors are annotated to neural crest formation, although loss causes arrest or death rather than a change of fate.",
        "resolution": "Proposed: a new term 'neural crest progenitor maintenance' under GO:0019827 (decided 2026-10-09; projects/NEURAL_CREST_FORMATION_OBSOLETION.md).",
        "provenance": [{"reference_id": "PMID:15769946", "supporting_text": "rather than a cell fate switch"}],
        "proposed_terms": [{
            "proposed_name": "neural crest progenitor maintenance",
            "proposed_definition": "The process by which neural plate border and premigratory neural crest progenitor cells are kept in an undifferentiated, proliferative and multipotent state until neural crest specification.",
            "justification": "Myc, Id3, Hairy2 and Pou5f3/Oct25 are required for crest to form, but their loss causes progenitor arrest or death rather than a change of fate; neither crest cell differentiation nor fate specification describes them.",
            "proposed_parent": {"id": "GO:0019827", "label": "stem cell population maintenance"},
            "supported_by": [{"reference_id": "PMID:15769946", "supporting_text": "rather than a cell fate switch"}],
        }],
    },
    {
        "gap_statement": "Parts of the network are lineage-specific: the cranial circuit (including Ets1) is absent from lamprey crest, Twist1's early specifier role is reported only in anamniotes, and the leading SoxE paralog differs by lineage.",
        "boundary": "Affects the neural_crest_fate_specification and neural_crest_emigration parts; the module is drawn from frog and human members.",
        "gap_kind": ["BIOLOGY"],
        "status": "OPEN",
        "significance": "A pan-vertebrate module would overstate the conservation of these components; taxon-specific variants may be needed.",
        "resolution": "Model taxon variants (cyclostome vs gnathostome; anamniote vs amniote) once lamprey and amniote members are reviewed.",
        "provenance": [
            {"reference_id": "PMID:31645763", "supporting_text": "lamprey lacks most components of a transcriptional circuit that is specific to"},
            {"reference_id": "file:modules/neural_crest_gene_regulatory_network-deep-research-falcon.md",
             "supporting_text": "ETS1 is a strong cranial regulator in chick but is not a universal vertebrate delamination factor"},
        ],
    },
]
doc["knowledge_gaps"] += [
    {
        "gap_statement": "Several components supported by the literature are not yet reviewed members: Hairy2 acting through an FGFR4–STAT3 complex, OCT4–SOX2 redeployed to TFAP2A-bound crest enhancers, and Twist1's chromatin partners (CHD7/CHD8/WHSC1). The TFAP2 partner switch and Pax7 were added after review (2026-10-08).",
        "boundary": "Affects the border, competence, specification and ectomesenchyme parts; members are limited to the genes reviewed in projects/NEURAL_CREST_ORIGINS.md.",
        "gap_kind": ["CURATION"],
        "status": "OPEN",
        "significance": "Without these the module under-represents protein assemblies and the chick/amniote implementation of the network.",
        "resolution": "Review FGFR4/STAT3 and the Twist1 chromatin partners and add annotons where supported. The OCT4–SOX2–TFAP2A finding is from chick/human; in frog the Oct–Sox pair acting at genome activation is Pou5f3 with Sox3, and Sox3 is absent from crest by neurula, so any crest Oct partner is more likely SoxE.",
        "provenance": [
            {"reference_id": DR, "supporting_text": "it promotes assembly of a membrane-associated FGFR4–STAT3 complex"},
            {"reference_id": DR, "supporting_text": "OCT4–SOX2 is redirected from NANOG toward TFAP2A-bound crest enhancers"},
            {"reference_id": DR, "supporting_text": "TWIST1 BioID identified CHD7/CHD8/WHSC1"},
        ],
    },
    {
        "gap_statement": "The hand-off from SoxB1 (Sox2/Sox3) to SoxE is a required step in moving from pluripotent blastula cells to crest, but SoxB1 factors are not members: they must be switched off for crest to form and do none of its work.",
        "boundary": "SoxB1 is treated as an upstream blastula/neural-plate state, outside the module; the hand-off sits between the competence and specification parts.",
        "gap_kind": ["ONTOLOGY", "BIOLOGY"],
        "status": "OPEN",
        "significance": "The module cannot express a required repression of an upstream state; GO has no term for this kind of state transition, and adding a negative-regulation crest term to SoxB1 would fail the participation test.",
        "resolution": "Model the hand-off explicitly (e.g. a NEGATIVELY_REGULATES edge from a crest specifier to an upstream SoxB1 node) once a repressor of SoxB1 in the crest is established; record SoxB1 in the reviews as non-participants.",
        "provenance": [
            {"reference_id": "PMID:30144418", "supporting_text": "A transition from SoxB1 to SoxE transcription factors is essential for"},
            {"reference_id": "PMID:39060477", "supporting_text": "soxB1a, soxB1b, brd4 were all expressed in lamprey animal pole cells, analogous to Xenopus"},
        ],
    },
    {
        "gap_statement": "Lin28 is a candidate competence factor, but its crest requirement is shown only in chick; the frog lin28a review found no frog crest evidence.",
        "boundary": "Affects the progenitor_competence_maintenance part; Lin28 is not included as an annoton.",
        "gap_kind": ["BIOLOGY", "CURATION"],
        "status": "OPEN",
        "significance": "Lin28/let-7 would link developmental timing and Myc to crest competence, but frog and chick may differ.",
        "resolution": "Review chick LIN28A (Q45KJ5) and test lin28a/lin28b at the frog neural plate border.",
        "provenance": [{"reference_id": "PMID:30520734", "supporting_text": "Changes in Lin28a levels impact neural crest development in vivo"}],
    },
]
doc.pop("scope")
for e in doc["evidence"]:
    if e.get("title") is None:
        e.pop("title", None)

out = ROOT / "modules/neural_crest_gene_regulatory_network.yaml"
yaml.safe_dump(doc, open(out, "w"), sort_keys=False, width=110, allow_unicode=True)
print("wrote", out)
