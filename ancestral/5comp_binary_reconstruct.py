var.nexus_allowAllDigitNames = True   # put it somewhere else
var.doCheckForDuplicateSequences = False

t = var.trees[0]
a = var.alignments[0]
t.data = Data()

t.model.dump()

print('\nAfter optimizing, the composition of the model for the non-root nodes is:') 
print(t.model.parts[0].comps[0].val)
print('...and:')
print(t.model.parts[0].comps[1].val)
print('and ...')
print(t.model.parts[0].comps[2].val)
print('and root comp...')
print(t.model.parts[0].comps[3].val)
print(t.model.parts[0].comps[4].val)
t.write()
t.draw()
func.reseedCRandomizer(os.getpid())
# The char "symbols", AAs in this case, are available as a.symbols; that is why
# I gave a name to var.alignments[0].  Also available as
# d.parts[partNum].symbols, so d.parts[0].symbols are also 'arndcqeghilkmfpstwyv'

print("Node-to-comp mapping:")
for n in t.iterNodes():
    print(n.nodeNum,n.parts[0].compNum)

counts = [0] * 2
for rep in range(1000):
    ancSt = t.ancestralStateDraw()
    for i in range(2):
        ch = a.symbols[i] # '01'
        cnt = ancSt.count(ch)
        counts[i] += cnt
        mySum = float(sum(counts))
print("\nsymbol optimized      draws")
for i in range(2):
    print("  %s      %.5f     %.4f" % (a.symbols[i], t.model.parts[0].comps[2].val[i], counts[i]/mySum))

#calculate predicted OGT according to Zeldovich
for i in range(5):
    print("For composition " + str(i))
    print(t.model.parts[0].comps[i].nNodes)
    f_ivywrel = 0
    f_ivywrel = t.model.parts[0].comps[i].val[1]
    print("F(IVYWREL) = " + str(f_ivywrel))
    print("T_opt estimate according to Zeldovich: " + str(937.0*float(f_ivywrel) - 335.0))
