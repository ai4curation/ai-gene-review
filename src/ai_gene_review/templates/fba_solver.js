// Browser port of ai_gene_review.module_fba.simulate_fba.
//
// It takes one compiled model (the JSON form of an FBAModel, as emitted by
// fba_model_payload) and follows the Python steps exactly: GPR capacities,
// regulatory gating, reaction and edge upper bounds, then the exact two-stage
// pFBA optimum as a min-cost maximum flow, arc for arc in the same order.
// tests/test_module_fba.py runs this file under Node and checks it against the
// Python solver, so a change to one must be made to the other.

const FBA_EPS = 1e-6;

function fbaHas(obj, key) {
    return Object.prototype.hasOwnProperty.call(obj, key);
}

function fbaRound(v, digits) {
    const f = Math.pow(10, digits);
    return Math.round(v * f) / f;
}

function fbaLevel(v) {
    return typeof v === "boolean" ? (v ? 1.0 : 0.0) : Math.max(0.0, Number(v));
}

function evalGprAst(expr, rawLevels, resolvedOut) {
    if (!expr || typeof expr !== "object") return 1.0;
    if (expr.element !== undefined && expr.element !== null) {
        const eid = String(expr.element);
        const direct = fbaHas(rawLevels, eid) ? rawLevels[eid] : 1.0;
        const subCap = expr.sub_logic && typeof expr.sub_logic === "object"
            ? evalGprAst(expr.sub_logic, rawLevels, resolvedOut)
            : 1.0;
        const val = Math.max(0.0, direct * subCap);
        resolvedOut[eid] = val;
        return val;
    }
    if (fbaHas(expr, "all_of")) {
        const subs = (expr.all_of || []).map(s => evalGprAst(s, rawLevels, resolvedOut));
        return subs.length ? Math.min(...subs) : 1.0;
    }
    if (fbaHas(expr, "any_of")) {
        const subs = (expr.any_of || []).map(s => evalGprAst(s, rawLevels, resolvedOut));
        return subs.length ? Math.min(1.0, subs.reduce((a, b) => a + b, 0.0)) : 1.0;
    }
    return 1.0;
}

function evalFbaLogic(expr, active, flowInputs, competingInhibitors) {
    if (expr.element !== undefined && expr.element !== null) {
        const v = String(expr.element);
        if (competingInhibitors.includes(v)) return false;
        if (flowInputs.includes(v)) return true;
        return Boolean(active[v]);
    }
    const op = ["all_of", "any_of", "none_of"].find(k => expr[k] && expr[k].length);
    if (op === undefined) return true;
    const subs = expr[op]
        .filter(sub => sub && typeof sub === "object")
        .map(sub => evalFbaLogic(sub, active, flowInputs, competingInhibitors));
    if (op === "none_of") return !subs.some(Boolean);
    if (op === "all_of") return subs.every(Boolean);
    return subs.some(Boolean);
}

function resolveFbaActive(model, settings, gprCapacities) {
    const active = {};
    for (const r of model.reactions) {
        if (fbaHas(settings, r.id)) {
            const v = settings[r.id];
            active[r.id] = typeof v === "boolean" ? v : Number(v) > FBA_EPS;
        } else if (r.is_flow_stage && (fbaHas(gprCapacities, r.id) ? gprCapacities[r.id] : 1.0) <= FBA_EPS) {
            active[r.id] = false;
        } else {
            active[r.id] = Boolean(r.default_active);
        }
    }
    let converged = false;
    for (let iter = 0; iter < model.reactions.length + 1; iter++) {
        let changed = false;
        for (const r of model.reactions) {
            if (fbaHas(settings, r.id)) continue;
            let next;
            if (r.is_flow_stage && (fbaHas(gprCapacities, r.id) ? gprCapacities[r.id] : 1.0) <= FBA_EPS) {
                next = false;
            } else {
                let gatedOff = false;
                if (r.activation_logic) {
                    gatedOff = !evalFbaLogic(r.activation_logic, active, r.flow_inputs, r.competing_inhibitors);
                } else {
                    if (r.gate_activators.some(g => fbaHas(active, g) && !active[g])) gatedOff = true;
                    if (r.gate_inhibitors.some(g => Boolean(active[g]))) gatedOff = true;
                }
                next = gatedOff ? false : Boolean(r.default_active);
            }
            if (active[r.id] !== next) {
                active[r.id] = next;
                changed = true;
            }
        }
        if (!changed) {
            converged = true;
            break;
        }
    }
    return { active, converged };
}

function minCostMaxFlow(nNodes, arcs, source, sink) {
    const head = [];
    const residual = [];
    const cost = [];
    const adjacency = [];
    for (let i = 0; i < nNodes; i++) adjacency.push([]);
    for (const [tail, hd, cap, c] of arcs) {
        adjacency[tail].push(head.length);
        head.push(hd);
        residual.push(cap);
        cost.push(c);
        adjacency[hd].push(head.length);
        head.push(tail);
        residual.push(0.0);
        cost.push(-c);
    }
    for (;;) {
        const dist = new Array(nNodes).fill(Infinity);
        const via = new Array(nNodes).fill(-1);
        dist[source] = 0.0;
        for (let iter = 0; iter < nNodes - 1; iter++) {
            let changed = false;
            for (let u = 0; u < nNodes; u++) {
                if (dist[u] === Infinity) continue;
                for (const a of adjacency[u]) {
                    if (residual[a] > FBA_EPS && dist[u] + cost[a] < dist[head[a]]) {
                        dist[head[a]] = dist[u] + cost[a];
                        via[head[a]] = a;
                        changed = true;
                    }
                }
            }
            if (!changed) break;
        }
        if (dist[sink] === Infinity) break;
        let push = Infinity;
        let v = sink;
        while (v !== source) {
            const a = via[v];
            push = Math.min(push, residual[a]);
            v = head[a ^ 1];
        }
        v = sink;
        while (v !== source) {
            const a = via[v];
            residual[a] -= push;
            residual[a ^ 1] += push;
            v = head[a ^ 1];
        }
    }
    return arcs.map((_arc, i) => residual[2 * i + 1]);
}

function solvePfba(flowRxns, entryIds, terminalIds, reactionBounds, edges, uptakeRate, params) {
    const index = {};
    flowRxns.forEach((r, k) => { index[r.id] = k; });
    const source = 0;
    const sink = 2 * flowRxns.length + 1;
    const inNode = id => 2 * index[id] + 1;
    const outNode = id => 2 * index[id] + 2;
    const supply = sink + 1;
    const arcs = [[supply, source, Math.max(0.0, uptakeRate), 0.0]];
    for (const eid of entryIds) {
        if (fbaHas(index, eid)) arcs.push([source, inNode(eid), Infinity, 0.0]);
    }
    const rxnArc = {};
    for (const r of flowRxns) {
        rxnArc[r.id] = arcs.length;
        const c = r.is_optional_branch ? params.optional_branch_flux_cost : params.core_flux_cost;
        arcs.push([inNode(r.id), outNode(r.id), reactionBounds[r.id], c]);
    }
    const edgeArc = {};
    edges.forEach(([src, tgt, ub], idx) => {
        if (ub > FBA_EPS && fbaHas(index, src) && fbaHas(index, tgt)) {
            edgeArc[idx] = arcs.length;
            arcs.push([outNode(src), inNode(tgt), ub, 0.0]);
        }
    });
    for (const tid of terminalIds) {
        if (fbaHas(index, tid)) arcs.push([outNode(tid), sink, Infinity, 0.0]);
    }
    const flows = minCostMaxFlow(sink + 2, arcs, supply, sink);
    const rxnFlux = {};
    for (const id of Object.keys(rxnArc)) rxnFlux[id] = flows[rxnArc[id]];
    const edgeFlux = edges.map((_e, i) => (fbaHas(edgeArc, i) ? flows[edgeArc[i]] : 0.0));
    return { rxnFlux, edgeFlux };
}

function simulateFba(model, params, settings, uptakeRate) {
    const pinned = settings || {};

    const rawGprLevels = {};
    for (const g of model.gpr_elements) {
        rawGprLevels[g.id] = fbaHas(pinned, g.id) ? fbaLevel(pinned[g.id]) : (g.default_active ? 1.0 : 0.0);
    }
    const gprCapacities = {};
    for (const r of model.reactions) {
        if (!r.is_flow_stage) continue;
        let cap = r.gpr_logic ? evalGprAst(r.gpr_logic, rawGprLevels, gprCapacities) : 1.0;
        if (fbaHas(pinned, r.id)) cap *= fbaLevel(pinned[r.id]);
        gprCapacities[r.id] = fbaRound(cap, 6);
    }
    for (const g of model.gpr_elements) {
        if (!fbaHas(gprCapacities, g.id)) gprCapacities[g.id] = fbaRound(rawGprLevels[g.id], 6);
    }

    const { active, converged } = resolveFbaActive(model, pinned, gprCapacities);

    const reactionBounds = {};
    for (const r of model.reactions) {
        if (!r.is_flow_stage || !active[r.id]) {
            reactionBounds[r.id] = 0.0;
            continue;
        }
        let ub = r.upper_bound * (fbaHas(gprCapacities, r.id) ? gprCapacities[r.id] : 1.0);
        for (const inh of r.competing_inhibitors) {
            if (active[inh]) ub *= params.competing_inhibitor_factor;
        }
        for (const mod of r.positive_modulators) {
            if (active[mod]) ub *= params.positive_regulator_boost;
            else if (!r.activation_logic) ub = 0.0;
        }
        reactionBounds[r.id] = Math.max(0.0, ub);
    }

    const outgoingBySrc = {};
    const incomingByTgt = {};
    for (const r of model.reactions) {
        outgoingBySrc[r.id] = [];
        incomingByTgt[r.id] = [];
    }
    const edgeUbs = model.transitions.map((t, idx) => {
        if (!active[t.source] || !active[t.target]) return 0.0;
        if (t.activation_logic) {
            if (!evalFbaLogic(t.activation_logic, active, t.flow_inputs, t.competing_inhibitors)) return 0.0;
        } else {
            if (t.gate_activators.some(g => fbaHas(active, g) && !active[g])) return 0.0;
            if (t.gate_inhibitors.some(g => Boolean(active[g]))) return 0.0;
        }
        let eUb = Math.min(reactionBounds[t.source], reactionBounds[t.target]);
        for (const inh of t.competing_inhibitors) {
            if (active[inh]) eUb *= params.competing_inhibitor_factor;
        }
        for (const mod of t.positive_modulators) {
            if (active[mod]) eUb *= params.positive_regulator_boost;
            else if (!t.activation_logic) eUb = 0.0;
        }
        eUb = Math.max(0.0, eUb);
        if (eUb > FBA_EPS) {
            outgoingBySrc[t.source].push(idx);
            incomingByTgt[t.target].push(idx);
        }
        return eUb;
    });

    const flowRxns = model.reactions.filter(r => r.is_flow_stage);
    const termSet = new Set(model.effective_terminals);
    const entrySet = new Set(model.entry_reactions);
    const { rxnFlux, edgeFlux } = solvePfba(
        flowRxns,
        model.entry_reactions,
        model.effective_terminals,
        reactionBounds,
        model.transitions.map((t, i) => [t.source, t.target, edgeUbs[i]]),
        uptakeRate,
        params
    );
    for (const r of model.reactions) {
        if (!fbaHas(rxnFlux, r.id)) rxnFlux[r.id] = 0.0;
    }

    let maxResidual = 0.0;
    for (const r of flowRxns) {
        const incSum = entrySet.has(r.id)
            ? rxnFlux[r.id]
            : incomingByTgt[r.id].reduce((acc, idx) => acc + edgeFlux[idx], 0.0);
        const outSum = termSet.has(r.id)
            ? rxnFlux[r.id]
            : outgoingBySrc[r.id].reduce((acc, idx) => acc + edgeFlux[idx], 0.0);
        maxResidual = Math.max(maxResidual, Math.abs(incSum - outSum));
    }

    return {
        elementActive: active,
        gprCapacities,
        reactionBounds,
        reactionFluxes: rxnFlux,
        transitionFluxes: model.transitions.map((t, idx) => ({ ...t, upper_bound: edgeUbs[idx], flux: edgeFlux[idx] })),
        totalUptake: model.entry_reactions.reduce((acc, id) => acc + (rxnFlux[id] || 0.0), 0.0),
        totalExport: model.effective_terminals.reduce((acc, id) => acc + (rxnFlux[id] || 0.0), 0.0),
        totalL1: Object.values(rxnFlux).reduce((a, b) => a + b, 0.0),
        maxResidual,
        converged
    };
}
