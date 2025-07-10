from pytest import approx
import math
print(0.1 + 0.2 == 0.3) #This doesn't work
print(0.1 + 0.2 == approx(0.3)) #This will work

print(0.1 + 0.2 == approx(0.3, abs=0.001)) #abs is an actual value it's checking for
print(0.1 + 0.2 == approx(0.3, rel=0.00000000000001)) #rel means within a percent