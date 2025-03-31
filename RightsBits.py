# CAUTION: NO error checking, will accept nonsense strings and return a valid but harmless rightsByte

# Construction of the rightsByte:
def buildRightsByte(convertible=0, redeemable=0, revenue_sharing=False, collaterizable=False, inheritance=False):
    '''
    buildRightsByte sets the RightsByte on a per Investor basis 
        Every coin issued by a specific Controller has DLO rights associated with them
        Status of these rights is stored in a single byte as follows: 
        convertibility 3 lsb, redeemability 4,5 lsb, revenue sharing 3 msb, and 
        collateralizability 2 msb.  Most significant bit is inheritance.
    '''
    # initialize to zero, i.e. no rights
    RightsByte = 0
    if convertible != 0:
        RightsByte = convertible
    if redeemable != 0:
        RightsByte = RightsByte + (redeemable*8) # redeemable will be either 2 (Market) 0r 1 (Par)
    if revenue_sharing:
        RightsByte = RightsByte + 32 
    if collaterizable:
        RightsByte = RightsByte + 64
    if inheritance:
        RightsByte = RightsByte + 128
    RightsByte = bin(RightsByte)
    print(f"RightsByte is {RightsByte}")
    return RightsByte

def rightsByte(InvestorLevel):
    if InvestorLevel == "GP":
        #  set to most rights 
        convertible = 5         # binary 00000101
        redeemable =  2         # binary 00010000
        revenue_sharing = True  # binary 00100000
        collaterizable = True   # binary 01000000
        inheritance = True      # binary 10000000
        RightsByte = buildRightsByte(convertible, redeemable, revenue_sharing, collaterizable, inheritance)

    elif InvestorLevel == "LP":
        #  set to most rights for example purposes
        convertible = 4         # binary 00000100
        redeemable =  2         # binary 00010000
        revenue_sharing = True  # binary 00100000
        collaterizable = False  # binary 00000000
        inheritance = True      # binary 10000000
        RightsByte = buildRightsByte(convertible, redeemable, revenue_sharing, collaterizable, inheritance)

    elif InvestorLevel == "10000":
        convertible = 0            # binary 00000000
        redeemable =  1            # binary 00001000
        revenue_sharing = False    # binary 00000000
        collaterizable = False     # binary 00000000
        inheritance = False        # binary 00000000
        RightsByte = buildRightsByte(convertible, redeemable, revenue_sharing, collaterizable, inheritance)

    elif InvestorLevel == "100":
        convertible = 0            # binary 00000000
        redeemable =  1            # binary 00001000
        revenue_sharing = False    # binary 00000000
        collaterizable = False     # binary 00000000
        inheritance = False        # binary 00000000
        RightsByte = buildRightsByte(convertible, redeemable, revenue_sharing, collaterizable, inheritance)

    else:
        convertible = 0            # binary 00000000
        redeemable =  0            # binary 00000000
        revenue_sharing = False    # binary 00000000
        collaterizable = False     # binary 00000000
        inheritance = False        # binary 00000000
        RightsByte = buildRightsByte(convertible, redeemable, revenue_sharing, collaterizable, inheritance)
