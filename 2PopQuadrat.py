#!/usr/bin/python3

import pandas as pan 
import scipy.stats as st

#
# Filename: 2PopQuadrat.py
# Author: Saverio Simonelli <saverio.simonelli.95@gmail.com>
# Copyright: 2020 Saverio Simonelli 
# License: MIT license
#

def get_data_a_between(datafile, xname, yname, limit):
	df = pan.read_csv(datafile, sep = ";")
	df[yname] = df[yname].apply(lambda x: float(x.replace(',','.')))
	

	df = df[df[xname] > 100]
	df = df[abs(df[yname]) < limit]
    #change region name or comment following instruction of interested in full pattern from two files
	df = df[df['region'] == 'Intron']

	x = df[xname].values
	#y = abs(df[yname].values)
	y = df[yname].values
	df = pan.DataFrame([x, y], index = ['x', 'y'])
	return df.T

def get_data_b_between(datafile, xname, yname, limit):
	df = pan.read_csv(datafile, sep = ";")
	df[yname] = df[yname].apply(lambda x: float(x.replace(',','.')))
	

	df = df[df[xname] > 100]
	df = df[abs(df[yname]) < limit]

	df = df[df['region'] != 'Intron']

	x = df[xname].values
	#y = abs(df[yname].values)
	y = df[yname].values
	df = pan.DataFrame([x, y], index = ['x', 'y'])
	return df.T
	
def get_data_a_external(datafile, xname, yname, limit):
	df = pan.read_csv(datafile, sep = ";")
	df[yname] = df[yname].apply(lambda x: float(x.replace(',','.')))
	

	df = df[df[xname] > 100]
	df = df[abs(df[yname]) > limit]

	df = df[df['region'] == 'Intron']

	x = df[xname].values
	#y = abs(df[yname].values)
	y = df[yname].values
	df = pan.DataFrame([x, y], index = ['x', 'y'])
	return df.T

def get_data_b_external(datafile, xname, yname, limit):
	df = pan.read_csv(datafile, sep = ";")
	df[yname] = df[yname].apply(lambda x: float(x.replace(',','.')))
	

	df = df[df[xname] > 100]
	df = df[abs(df[yname]) > limit]

	df = df[df['region'] != 'Intron']

	x = df[xname].values
	#y = abs(df[yname].values)
	y = df[yname].values
	df = pan.DataFrame([x, y], index = ['x', 'y'])
	return df.T


def quadrat_external(dfa, dfb, limit):
    
    cab = 0
    c0b = 0
    ca0 = 0
    c00 = 0
    
    xmax = dfa['x'].max()
    if xmax < dfb['x'].max(): xmax = dfb['x'].max()
    
    xmin = dfa['x'].min()
    if xmin > dfb['x'].min(): xmin = dfb['x'].min()
    
    ymax = dfa['y'].max()
    if ymax < dfb['y'].max(): ymax = dfb['y'].max()
    
    y = limit
    
    dx = (xmax - xmin)/10
    dy = (ymax - y)/5
    xflag = False 
    yflag = False
    while y <= ymax:
        x = xmin
        while x <= xmax:
            #if dfa['x'] > x : 
            dfbb = dfb[dfb['x'] > x]
            dfbb = dfbb[dfbb['x'] <= x + dx]
            dfbb = dfbb[dfbb['y'] > y]
            dfbb = dfbb[dfbb['y'] <= y + dy]
            dfaa = dfa[dfa['x'] > x]
            dfaa = dfaa[dfaa['x'] <= x + dx]
            dfaa = dfaa[dfaa['y'] > y]
            dfaa = dfaa[dfaa['y'] <= y + dy]
            #print(x, x+dx, y, y+dy, dfaa.shape[0])
            a = dfaa.shape[0]
            b = dfbb.shape[0]
            #if a>0 or b >0: print(x, x+dx, y, y+dy, a, b)
            if a > 0 and b > 0: cab = cab + 1
            elif b > 0: c0b = c0b + 1
            elif a > 0: ca0 = ca0 + 1
            else: c00 = c00 + 1
            x = x + dx
            if x > xmax and xflag == False: 
                x = xmax
                xflag = True
        y = y + dy 
        if y > ymax and yflag == False: 
            y = ymax
            yflag = True
    
    #x = 0
    y = -limit
    xflag = False 
    yflag = False
    ymin = dfa['y'].min()
    if ymin > dfb['y'].min(): ymin = dfb['y'].min()
    dy = (y - ymin)/5
    while y >= ymin:
        x = xmin
        while x <= xmax:
            dfbb = dfb[dfb['x'] > x]
            dfbb = dfbb[dfbb['x'] <= x + dx]
            dfbb = dfbb[dfbb['y'] < y]
            dfbb = dfbb[dfbb['y'] >= y - dy]
            dfaa = dfa[dfa['x'] > x]
            dfaa = dfaa[dfaa['x'] <= x + dx]
            dfaa = dfaa[dfaa['y'] < y]
            dfaa = dfaa[dfaa['y'] >= y - dy]
            a = dfaa.shape[0]
            b = dfbb.shape[0]
            #if a>0 or b >0: print(x, x+dx, y, y-dy, a, b)
            if a > 0 and b > 0: cab = cab + 1
            elif b > 0: c0b = c0b + 1
            elif a > 0: ca0 = ca0 + 1
            else: c00 = c00 + 1
            x = x + dx
            if x > xmax and xflag == False: 
                x = xmax
                xflag = True
        y = y - dy
        if y < ymin and yflag == False: 
            y = ymin
            yflag = True
    
          
        
    print(cab, c0b, ca0, c00)
    return cab, c0b, ca0, c00


def quadrat_between(dfa, dfb):
	cab = 0
	c0b = 0
	ca0 = 0
	c00 = 0
	xmin = dfa['x'].min()
	if xmin > dfb['x'].min(): xmin = dfb['x'].min()
	xmax = dfa['x'].max()
	if xmax < dfb['x'].max(): xmax = dfb['x'].max()
	ymax = dfa['y'].max()
	if ymax < dfb['y'].max(): ymax = dfb['y'].max()
	x = xmin
	ymin = dfa['y'].min()
	if ymin > dfb['y'].min(): ymin = dfb['y'].min()
	dx = (xmax - xmin)/10
	dy = (ymax - ymin)/10
	xflag = False 
	yflag = False
	print(xmin, xmax, ymin, ymax, dx, dy)
	y = ymin
	while y <= ymax:
		x = xmin
		while x <= xmax:
			#if dfa['x'] > x : 
			dfbb = dfb[dfb['x'] > x]
			dfbb = dfbb[dfbb['x'] <= x + dx]
			dfbb = dfbb[dfbb['y'] > y]
			dfbb = dfbb[dfbb['y'] <= y + dy]
			dfaa = dfa[dfa['x'] > x]
			dfaa = dfaa[dfaa['x'] <= x + dx]
			dfaa = dfaa[dfaa['y'] > y]
			dfaa = dfaa[dfaa['y'] <= y + dy]
			#print(x, x+dx, y, y+dy, dfaa.shape[0])
			a = dfaa.shape[0]
			b = dfbb.shape[0]
			#if a>0 or b >0: print(x, x+dx, y, y+dy, a, b)
			if a > 0 and b > 0: cab = cab + 1
			elif b > 0: c0b = c0b + 1
			elif a > 0: ca0 = ca0 + 1
			else: c00 = c00 + 1
			x = x + dx
			if x > xmax and xflag == False: 
				x = xmax
				xflag = True
		y = y + dy 
		if y > ymax and yflag == False: 
			y = ymax
			yflag = True
			
	print(cab, c0b, ca0, c00)
	return cab, c0b, ca0, c00


def test(datafiles, xname, yname):
	#a  = get_data_a_between(datafiles[0], xname, yname, 10)
	#b  = get_data_b_between(datafiles[1], xname, yname, 10)
	#cab, c0b, ca0, c00 = quadrat_between(a, b)
    a  = get_data_a_external(datafiles[0], xname, yname, limit = 4)
    b  = get_data_b_external(datafiles[1], xname, yname, limit = 4)
    cab, c0b, ca0, c00 = quadrat_external(a, b, limit = 4)
    test = st.chi2_contingency([[cab, c0b], [ca0, c00]])
    print(test)
    return


xname = "G-Score"
yname = "log2FoldChange"
datafile1 =	 ""
#directory + file name

datafile2 = ""
# = datafile1 when comparing different regions from same point pattern or != datafile 1 when comparing two patterns

datafile1 =  "C:/Users/Utente/Desktop/MacsBio/data/MCF7_BreastCancerCells/6_CoCulturedMCF7_LGvsCoCulturedMCF7_HG/6red_dist_QgrsWebReverseComplement_MCF7_BreastCancerCells_6_CoCulturedMCF7_LGvsCoCulturedMCF7_HG_20200213.csv"

#datafile1 =  "C:/Users/Utente/Desktop/MacsBio/data/MCF7_BreastCancerCells/5_CoCulturedMCF7_HGvsMCF7_HG/5red_dist_QgrsWebReverseComplement_MCF7_BreastCancerCells_5_CoCulturedMCF7_HGvsMCF7_HG_20200215.csv"

datafile2 = "C:/Users/Utente/Desktop/MacsBio/data/Adipocytes/8_CoCulturedADIPO_LGvsADIPO_LG/8red_dist_QgrsWebReverseComplement_Adipocytes_8_CoCulturedADIPO_LGvsADIPO_LG_20200215.csv"

print(datafile1, datafile2)
test([datafile1, datafile2], xname, yname)
