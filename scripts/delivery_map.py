"""Assign each result to a delivery model, from remote training to tools and finance."""
ORDER = ["Remote training without a human mentor", "AI mentor", "Human mentoring, advice or services",
         "Training bundled with tools, platforms or finance", "Tools, platforms or finance on their own"]
def delivery(paper):
    p = paper.split(",")[0]
    if p in ("De Oliveira", "Cole et al.", "Mehmood", "Fuchs et al.", "de Barros et al.", "Rodriguez-Lesmes et al.", "Davies et al."): return ORDER[0]
    if p == "Otis et al.": return ORDER[1]
    if p in ("Estefan et al.", "Cusolito et al.", "McKenzie et al.", "Asiedu") or (p == "Anderson et al." and "Uganda" in paper): return ORDER[2]
    if p in ("Desai", "Jin & Sun", "Batista et al.", "Bastian et al.", "Alhorr", "Mukherjee") or (p == "Dalton et al." and "2020" in paper): return ORDER[3]
    return ORDER[4]
