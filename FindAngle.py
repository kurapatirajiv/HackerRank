# Enter your code here. Read input from STDIN. Print output to STDOUT
# Angle MBC is same as MCB because the median from hypotenuse makes two isocles traingles ABM MBC, where AM=BM=MC
# Math.degree returns float value
import math;
side1,side2 = int(raw_input()),int(raw_input());
print str(int(round(math.degrees(math.atan2(side1,side2)))))+"°";