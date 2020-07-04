2PopQuadrat Created by Saverio Simonelli MIT license 2020

This program implements a spatial independence test: 
a two-population quadrat method as explained by Bianca Capuano in IB Biology for the Diploma Programme, chapter 4.2[53]. 
It follows the algorithm provided by B. Capuano and Y. Sadahiro in its lessons, available at the link:
http://ua.t.u-tokyo.ac.jp/okabelab/sada/docs/pdf_class/Ch06_2c.pdf [55]. 

According to this algorithm, the subarea of interest, S, is divided into rectangular cells. 

Subsequently, the rectangles containing points of both populations, Cab, the cells containing points of a single population, Ca0 and C0b, and the empty ones, C00, are counted. 

These values are organized as a contingency matrix, to which a chi-square test can be applied to verify independence.
<pre>
Be
S region of interest
Pa set of points from population A
Pb set of points from population B
T contingency matrix
Q set of squares that divide the region of interest
q single cell of Q
χ2 test
p p-value

Algorithm: QUADRAT METHOD
INPUT: Pa, Pb, S
OUTPUT: p
1. set T := empty set
2. divide S in cells to generate Q
3. for each cell q belonging to Q do
4.      add in T info about Pa, Pb in q
5. end for
6. do chi-square test about T
7. extract p from chi-square value
8. return p

</pre>

