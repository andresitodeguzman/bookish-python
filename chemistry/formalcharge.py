def formalCharge(valence, nonbonding, bonding):
    v = int(valence)
    n = int(nonbonding)
    b = int(bonding)
    compute = int(v-n-((1/2)*b))
    return compute

valence = input("Valence Electrons: ")
nonbonding = input("Non-bonding Electrons: ")
bonding = input("Bonding Electrons: ")
solve = formalCharge(valence, nonbonding, bonding)
print(solve)
