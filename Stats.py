def battingAve(total_hits, at_bats):
    if at_bats == 0:
        return 0.0 #input validation
    return total_hits / at_bats

def sluggingPercentage(singles, doubles, triples, home_runs, at_bats):
    if at_bats == 0:
        return 0.0 #input validation
    total_bases = singles + (2 * doubles) + (3 * triples) + (4 * home_runs)
    return total_bases / at_bats
