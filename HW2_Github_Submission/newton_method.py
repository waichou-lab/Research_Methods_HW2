#!/usr/bin/env python3
import math
from math import log, cos, sin
import sys

def f(t): return math.log(t) + math.cos(t)   # t = x-1, domain t>0
def df(t): return 1.0/t - math.sin(t)

def newton_with_brackets(t0, tol=1e-5, maxit=200):
    t = t0
    for k in range(maxit):
        ft = f(t)
        dft = df(t)
        if abs(ft) < tol:
            return t, k, True
        if dft == 0:
            break
        step = ft / dft
        t_new = t - step
        # keep t positive
        if t_new <= 0 or math.isinf(t_new) or math.isnan(t_new):
            break
        # damping
        if abs(step) > 1.0:
            step *= 0.5
            t_new = t - step
        t = t_new
    return t, maxit, False

def find_roots(scan_min=1e-4, scan_max=100, nsteps=1000, tol=1e-5):
    xs = [scan_min + i*(scan_max-scan_min)/nsteps for i in range(nsteps+1)]
    signs = [math.copysign(1, f(x)) if f(x)!=0 else 0 for x in xs]
    roots = []
    # find sign changes to bracket
    for i in range(len(xs)-1):
        a, b = xs[i], xs[i+1]
        fa, fb = f(a), f(b)
        if fa==0:
            roots.append(a); continue
        if fa*fb < 0:
            # bisection to get initial guess
            lo, hi = a, b
            for _ in range(60):
                mid = 0.5*(lo+hi)
                if f(lo)*f(mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            guess = 0.5*(lo+hi)
            t, iters, ok = newton_with_brackets(guess, tol=tol)
            if ok and t>0:
                # deduplicate
                if not any(abs(t - r) < 1e-6 for r in roots):
                    roots.append(t)
    # attempt to find remaining isolated roots via many inits
    for init in [0.5,1.0,2.0,3.0,5.0,10.0]:
        t, iters, ok = newton_with_brackets(init, tol=tol)
        if ok and t>0 and not any(abs(t - r) < 1e-6 for r in roots):
            roots.append(t)
    roots.sort()
    # convert t -> x = t+1
    return [r+1.0 for r in roots]

if __name__ == '__main__':
    roots = find_roots(scan_max=200, nsteps=20000)
    print('Found roots x (x>1) of ln(x-1)+cos(x-1)=0:')
    for r in roots:
        print('x = {:.8f}, check f(x-1) = {:.3e}'.format(r, f(r-1)))
