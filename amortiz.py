import numpy_financial as npf

def amortize(principle, ir, term):
    
    #total interest paid, total principle paid
    tip = 0
    tpp = 0

    for month in range(1, term + 1):
        
    #monthly payment, interest payment, principle payment
        pmt = npf.pmt(ir/12, term, -principle)
        ipmt = npf.ipmt(ir/12, month, term, -principle)
        ppmt = npf.ppmt(ir/12, month, term, -principle)
        tip += ipmt
        tpp += ppmt

        print(month, f" {pmt:15,.2f} {ipmt:15,.2f} {ppmt:15,.2f} {tip:15,.2f} {tpp:15,.2f}")

#principle, interest rate, number of payments
principle = 10000
ir = .02
term = 36
amortize(principle, ir, term)
