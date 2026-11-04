import csv, re, collections, json
def load_dirs(D):
    tomaster={}
    for r in csv.DictReader(open(f"{D}/rhea-directions.tsv"),delimiter="\t"):
        for k in ("RHEA_ID_MASTER","RHEA_ID_LR","RHEA_ID_RL","RHEA_ID_BI"): tomaster[r[k]]=r["RHEA_ID_MASTER"]
    return tomaster
def load_sp(D):
    sp=collections.defaultdict(set)
    for r in csv.DictReader(open(f"{D}/rhea2uniprot_sprot.tsv"),delimiter="\t"): sp[r["MASTER_ID"]].add(r["ID"])
    return sp
def load_rhea(D):
    eq={}
    for r in csv.DictReader(open(f"{D}/rhea_all.tsv"),delimiter="\t"):
        eq[r["Reaction identifier"].split(":")[1]]=r["Equation"]
    ec=collections.defaultdict(set)
    for r in csv.DictReader(open(f"{D}/rhea2ec.tsv"),delimiter="\t"): ec[r["MASTER_ID"]].add(r["ID"])
    return eq,ec
def parse_obo(path):
    terms={}; cur=None
    for line in open(path):
        line=line.rstrip("\n")
        if line.startswith("["):
            cur={"stanza":line,"xrefs":[],"isa":[],"obs":False,"ns":None,"def":""}; continue
        if cur is None or cur["stanza"]!="[Term]": continue
        if line.startswith("id: "): cur["id"]=line[4:]; terms[cur["id"]]=cur
        elif line.startswith("name: "): cur["name"]=line[6:]
        elif line.startswith("namespace: "): cur["ns"]=line[11:]
        elif line.startswith("def: "): cur["def"]=line[5:]
        elif line.startswith("is_obsolete: true"): cur["obs"]=True
        elif line.startswith("is_a: "): cur["isa"].append(line[6:16])
        elif line.startswith("intersection_of: GO:"): cur["isa"].append(line[17:27])
        elif line.startswith("xref: "):
            m=re.match(r"xref: (RHEA|EC):([\d.\-n]+)(?: \{source=\"([^\"]+)\"\})?",line)
            if m: cur["xrefs"].append((m.group(1),m.group(2),m.group(3)))
    return terms
def ancestors(terms):
    memo={}
    def anc(t):
        if t in memo: return memo[t]
        memo[t]=set()
        s={t}
        for p in terms.get(t,{}).get("isa",[]): s|=anc(p)
        memo[t]=s; return s
    return anc
