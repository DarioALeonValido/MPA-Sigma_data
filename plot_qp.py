import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

databaseV_Na = 'databases/qp_v_Na.dat'
databaseV_Si = 'databases/qp_v_Si.dat'
databaseV_Cu = 'databases/qp_v_Cu.dat'
databaseV_MoS2 = 'databases/qp_v_MoS2.dat'
databaseV_NaCl = 'databases/qp_v_NaCl.dat'
databaseV_F2 = 'databases/qp_v_F2.dat'

databaseC_Na = 'databases/qp_c_Na.dat'
databaseC_Si = 'databases/qp_c_Si.dat'
databaseC_Cu = 'databases/qp_c_Cu.dat'
databaseC_MoS2 = 'databases/qp_c_MoS2.dat'
databaseC_NaCl = 'databases/qp_c_NaCl.dat'
databaseC_F2 = 'databases/qp_c_F2.dat'

#---------- plots -----------------------------------------

plt.rcParams['font.size'] = '11.5'
plt.rcParams['lines.linewidth'] = 1.5

f=0.9
fx=3;fy=3
figSiNaCu, axsSiNaCu = plt.subplots(fy, fx, sharex='col', sharey='row', tight_layout=True)
figSiNaCu.set_size_inches(f*4*fx, f*3*fy)

f=0.9
fx=3;fy=3
figMoS2NaClF2, axsMoS2NaClF2 = plt.subplots(fy, fx, sharex='col', sharey='row', tight_layout=True)
figMoS2NaClF2.set_size_inches(f*4*fx, f*3*fy)


cmap_S = mpl.cm.get_cmap('PuOr_r')
colors = [cmap_S(0.75),cmap_S(0.25)]
cmpa = 'k'
cmpaVC = ['k','grey']
lsVC = [':','-.']
labelsVC = ['val (FF)', 'con (FF)']
labelMPA = 'MPA-$\Sigma$'
labelMPAg = 'MPA-$G$'

labelsSi = ['Fermi', '$+0.7~$eV']
labelsNa = ['$-3.3~$eV', '$+0.8~$eV']
labelsCu = ['$-9.3~$eV', '$+7.1~$eV']
labelsMoS2 = ['Fermi', '$+1.7~$eV']
labelsNaCl = ['Fermi', '$+3.1~$eV']
labelsF2 = ['Fermi', '$+3.5~$eV']

panels = ['(a)','(b)','(c)','(d)','(e)','(f)','(g)','(h)','(i)']
panels = np.reshape(panels,(3,3))
labelsNaSiCu = ['Si','Na','Cu']
labelsMoS2NaClF2 = ['MoS2','NaCl','F2']

#------------------------ Si
SimaxReS0 = 1.153296; SiminReS0 = -0.569141
SimaxImS0 = 3.573639; SiminImS0 = 0.168896
SimaxImG = 0.04
SimaxReS = 2.; SiminReS = -5.0
SimaxImS = 7.0; SiminImS = -4.5

fReS = 1.
fImS = 1.
fImG = 1.

v_ener, v_ReS, v_ImS, v_ImG, v_ReSmpa, v_ImSmpa, v_ImGmpa = np.loadtxt(databaseV_Si, unpack=True)
c_ener, c_ReS, c_ImS, c_ImG, c_ReSmpa, c_ImSmpa, c_ImGmpa = np.loadtxt(databaseC_Si, unpack=True)

axsSiNaCu[0,0].plot(v_ener, v_ReS *fReS, c=colors[0])
axsSiNaCu[0,0].plot(v_ener, v_ReSmpa *fReS, c=cmpa, ls=lsVC[0])
axsSiNaCu[0,0].plot(c_ener, c_ReS *fReS, c=colors[1])
axsSiNaCu[0,0].plot(c_ener, c_ReSmpa *fReS, c=cmpa, ls=lsVC[1])

axsSiNaCu[1,0].plot(v_ener, v_ImS *fImS, c=colors[0])
axsSiNaCu[1,0].plot(v_ener, v_ImSmpa *fImS, c=cmpa, ls=lsVC[0])
axsSiNaCu[1,0].plot(c_ener, c_ImS *fImS, c=colors[1])
axsSiNaCu[1,0].plot(c_ener, c_ImSmpa *fImS, c=cmpa, ls=lsVC[1])

axsSiNaCu[2,0].plot(v_ener, v_ImG *fImG, c=colors[0], label = labelsSi[0])
axsSiNaCu[2,0].plot(v_ener, v_ImGmpa *fImG, c=cmpa, ls=lsVC[0])
axsSiNaCu[2,0].plot(c_ener, c_ImG *fImG, c=colors[1], label = labelsSi[1])
axsSiNaCu[2,0].plot(c_ener, c_ImGmpa *fImG, c=cmpa, ls=lsVC[1])

axsSiNaCu[0,0].set_title(r"$\times$"+str(round(1/fReS,1)),loc='left',size='medium')
axsSiNaCu[1,0].set_title(r"$\times$"+str(round(1/fImS,1)),loc='left',size='medium')
axsSiNaCu[2,0].set_title(r"$\times$"+str(round(1/fImG,1)),loc='left',size='medium')


#------------------------ Na
fReS = 0.1021370658849681
fImS = 0.12037609641650913
fImG = 0.02666666666666667

v_ener, v_ReS, v_ImS, v_ImG, v_ReSmpa, v_ImSmpa, v_ImGmpa = np.loadtxt(databaseV_Na, unpack=True)
c_ener, c_ReS, c_ImS, c_ImG, c_ReSmpa, c_ImSmpa, c_ImGmpa = np.loadtxt(databaseC_Na, unpack=True)

axsSiNaCu[0,1].plot(v_ener, v_ReS *fReS, c=colors[0])
axsSiNaCu[0,1].plot(v_ener, v_ReSmpa *fReS, c=cmpa, ls=lsVC[0])
axsSiNaCu[0,1].plot(c_ener, c_ReS *fReS, c=colors[1])
axsSiNaCu[0,1].plot(c_ener, c_ReSmpa *fReS, c=cmpa, ls=lsVC[1])

axsSiNaCu[1,1].plot(v_ener, v_ImS *fImS, c=colors[0])
axsSiNaCu[1,1].plot(v_ener, v_ImSmpa *fImS, c=cmpa, ls=lsVC[0])
axsSiNaCu[1,1].plot(c_ener, c_ImS *fImS, c=colors[1])
axsSiNaCu[1,1].plot(c_ener, c_ImSmpa *fImS, c=cmpa, ls=lsVC[1])

axsSiNaCu[2,1].plot(v_ener, v_ImG *fImG, c=colors[0], label = labelsNa[0])
axsSiNaCu[2,1].plot(v_ener, v_ImGmpa *fImG, c=cmpa, ls=lsVC[0])
axsSiNaCu[2,1].plot(c_ener, c_ImG *fImG, c=colors[1], label = labelsNa[1])
axsSiNaCu[2,1].plot(c_ener, c_ImGmpa *fImG, c=cmpa, ls=lsVC[1])

axsSiNaCu[0,1].set_title(r"$\times$"+str(round(1/fReS,1)),loc='left',size='medium')
axsSiNaCu[1,1].set_title(r"$\times$"+str(round(1/fImS,1)),loc='left',size='medium')
axsSiNaCu[2,1].set_title(r"$\times$"+str(round(1/fImG,1)),loc='left',size='medium')


#------------------------ Cu
fReS = 0.1779474882593287
fImS = 0.3023057157540113
fImG = 0.39999999999999997

v_ener, v_ReS, v_ImS, v_ImG, v_ReSmpa, v_ImSmpa, v_ImGmpa = np.loadtxt(databaseV_Cu, unpack=True)
c_ener, c_ReS, c_ImS, c_ImG, c_ReSmpa, c_ImSmpa, c_ImGmpa = np.loadtxt(databaseC_Cu, unpack=True)

axsSiNaCu[0,2].plot(v_ener, v_ReS *fReS, c=colors[0], label = labelsVC[0])
axsSiNaCu[0,2].plot(v_ener, v_ReSmpa *fReS, c=cmpa, ls=lsVC[0], label = labelMPA)
axsSiNaCu[0,2].plot(c_ener, c_ReS *fReS, c=colors[1], label = labelsVC[1])
axsSiNaCu[0,2].plot(c_ener, c_ReSmpa *fReS, c=cmpa, ls=lsVC[1], label = labelMPA)

axsSiNaCu[1,2].plot(v_ener, v_ImS *fImS, c=colors[0])
axsSiNaCu[1,2].plot(v_ener, v_ImSmpa *fImS, c=cmpa, ls=lsVC[0])
axsSiNaCu[1,2].plot(c_ener, c_ImS *fImS, c=colors[1])
axsSiNaCu[1,2].plot(c_ener, c_ImSmpa *fImS, c=cmpa, ls=lsVC[1])

axsSiNaCu[2,2].plot(v_ener, v_ImG *fImG, c=colors[0], label = labelsCu[0])
axsSiNaCu[2,2].plot(v_ener, v_ImGmpa *fImG, c=cmpa, ls=lsVC[0])
axsSiNaCu[2,2].plot(c_ener, c_ImG *fImG, c=colors[1], label = labelsCu[1])
axsSiNaCu[2,2].plot(c_ener, c_ImGmpa *fImG, c=cmpa, ls=lsVC[1])

axsSiNaCu[0,2].set_title(r"$\times$"+str(round(1/fReS,1)),loc='left',size='medium')
axsSiNaCu[1,2].set_title(r"$\times$"+str(round(1/fImS,1)),loc='left',size='medium')
axsSiNaCu[2,2].set_title(r"$\times$"+str(round(1/fImG,1)),loc='left',size='medium')


#-----------------------
axsSiNaCu[0,0].set_ylim(SiminReS,SimaxReS)
axsSiNaCu[1,0].set_ylim(SiminImS,SimaxImS)
axsSiNaCu[2,0].set_ylim(-SimaxImG,SimaxImG)

axsSiNaCu[2,0].set_xlim(-50.5,50.5)
axsSiNaCu[2,1].set_xlim(-50.5,50.5)
axsSiNaCu[2,2].set_xlim(-101.0,101.0)

axsSiNaCu[0,0].yaxis.set_minor_locator(AutoMinorLocator(5))
axsSiNaCu[1,0].yaxis.set_minor_locator(AutoMinorLocator(5))
axsSiNaCu[2,0].yaxis.set_minor_locator(AutoMinorLocator(5))

axsSiNaCu[2,0].xaxis.set_minor_locator(AutoMinorLocator(5))
axsSiNaCu[2,1].xaxis.set_minor_locator(AutoMinorLocator(5))
axsSiNaCu[2,2].xaxis.set_minor_locator(AutoMinorLocator(5))

axsSiNaCu[0,0].set_ylabel("Re$[\Sigma]~$(eV)")
axsSiNaCu[1,0].set_ylabel("Im$[\Sigma]~$(eV)")
axsSiNaCu[2,0].set_ylabel("Im$[G]~$(eV$^{-1}$)")

for m in range(3):
  axsSiNaCu[2,m].set_xlabel("$\omega - \epsilon^{KS}~$(eV)")
  for m2 in range(3):
    axsSiNaCu[m,m2].set_title(panels[m,m2],weight='bold',c='k',loc='center')

FZ = 15
axsSiNaCu[2,0].annotate(labelsNaSiCu[0], [-48,SimaxImG-(SimaxImG+SimaxImG)*0.05],verticalalignment='top',horizontalalignment='left', fontsize = FZ) 
axsSiNaCu[2,1].annotate(labelsNaSiCu[1], [-48,SimaxImG-(SimaxImG+SimaxImG)*0.05],verticalalignment='top',horizontalalignment='left', fontsize = FZ) 
axsSiNaCu[2,2].annotate(labelsNaSiCu[2], [-95,SimaxImG-(SimaxImG+SimaxImG)*0.05],verticalalignment='top',horizontalalignment='left', fontsize = FZ)  

axsSiNaCu[0,2].legend(frameon=False, loc=4, borderaxespad=0.45)
axsSiNaCu[2,0].legend(frameon=False)
axsSiNaCu[2,1].legend(frameon=False)
axsSiNaCu[2,2].legend(frameon=False)

#-----------------------

#------------------------ MoS2
MoS2maxReS0 = 6.002289; MoS2minReS0 = -4.92205
MoS2maxImS0 = 7.918444; MoS2minImS0 = -8.534949
MoS2maxImG = 0.1
MoS2maxReS = 6.5; MoS2minReS = -6.5
MoS2maxImS = 8.9; MoS2minImS = -8.9

fReS = 1.
fImS = 1.
fImG = 1.

v_ener, v_ReS, v_ImS, v_ImG, v_ReSmpa, v_ImSmpa, v_ImGmpa = np.loadtxt(databaseV_MoS2, unpack=True)
c_ener, c_ReS, c_ImS, c_ImG, c_ReSmpa, c_ImSmpa, c_ImGmpa = np.loadtxt(databaseC_MoS2, unpack=True)

axsMoS2NaClF2[0,0].plot(v_ener, v_ReS *fReS, c=colors[0])
axsMoS2NaClF2[0,0].plot(v_ener, v_ReSmpa *fReS, c=cmpa, ls=lsVC[0])
axsMoS2NaClF2[0,0].plot(c_ener, c_ReS *fReS, c=colors[1])
axsMoS2NaClF2[0,0].plot(c_ener, c_ReSmpa *fReS, c=cmpa, ls=lsVC[1])

axsMoS2NaClF2[1,0].plot(v_ener, v_ImS *fImS, c=colors[0])
axsMoS2NaClF2[1,0].plot(v_ener, v_ImSmpa *fImS, c=cmpa, ls=lsVC[0])
axsMoS2NaClF2[1,0].plot(c_ener, c_ImS *fImS, c=colors[1])
axsMoS2NaClF2[1,0].plot(c_ener, c_ImSmpa *fImS, c=cmpa, ls=lsVC[1])

axsMoS2NaClF2[2,0].plot(v_ener, v_ImG *fImG, c=colors[0], label = labelsMoS2[0])
axsMoS2NaClF2[2,0].plot(v_ener, v_ImGmpa *fImG, c=cmpa, ls=lsVC[0])
axsMoS2NaClF2[2,0].plot(c_ener, c_ImG *fImG, c=colors[1], label = labelsMoS2[1])
axsMoS2NaClF2[2,0].plot(c_ener, c_ImGmpa *fImG, c=cmpa, ls=lsVC[1])

axsMoS2NaClF2[0,0].set_title(r"$\times$"+str(round(1/fReS,1)),loc='left',size='medium')
axsMoS2NaClF2[1,0].set_title(r"$\times$"+str(round(1/fImS,1)),loc='left',size='medium')
axsMoS2NaClF2[2,0].set_title(r"$\times$"+str(round(1/fImG,1)),loc='left',size='medium')


#------------------------ NaCl
fReS = 0.5913585221674876
fImS = 3.2320179591836733
fImG = 0.5

v_ener, v_ReS, v_ImS, v_ImG, v_ReSmpa, v_ImSmpa, v_ImGmpa = np.loadtxt(databaseV_NaCl, unpack=True)
c_ener, c_ReS, c_ImS, c_ImG, c_ReSmpa, c_ImSmpa, c_ImGmpa = np.loadtxt(databaseC_NaCl, unpack=True)

axsMoS2NaClF2[0,1].plot(v_ener, v_ReS *fReS, c=colors[0])
axsMoS2NaClF2[0,1].plot(v_ener, v_ReSmpa *fReS, c=cmpa, ls=lsVC[0])
axsMoS2NaClF2[0,1].plot(c_ener, c_ReS *fReS, c=colors[1])
axsMoS2NaClF2[0,1].plot(c_ener, c_ReSmpa *fReS, c=cmpa, ls=lsVC[1])

axsMoS2NaClF2[1,1].plot(v_ener, v_ImS *fImS, c=colors[0])
axsMoS2NaClF2[1,1].plot(v_ener, v_ImSmpa *fImS, c=cmpa, ls=lsVC[0])
axsMoS2NaClF2[1,1].plot(c_ener, c_ImS *fImS, c=colors[1])
axsMoS2NaClF2[1,1].plot(c_ener, c_ImSmpa *fImS, c=cmpa, ls=lsVC[1])

axsMoS2NaClF2[2,1].plot(v_ener, v_ImG *fImG, c=colors[0], label = labelsNaCl[0])
axsMoS2NaClF2[2,1].plot(v_ener, v_ImGmpa *fImG, c=cmpa, ls=lsVC[0])
axsMoS2NaClF2[2,1].plot(c_ener, c_ImG *fImG, c=colors[1], label = labelsNaCl[1])
axsMoS2NaClF2[2,1].plot(c_ener, c_ImGmpa *fImG, c=cmpa, ls=lsVC[1])

axsMoS2NaClF2[0,1].set_title(r"$\times$"+str(round(1/fReS,1)),loc='left',size='medium')
axsMoS2NaClF2[1,1].set_title(r"$\times$"+str(round(1/fImS,1)),loc='left',size='medium')
axsMoS2NaClF2[2,1].set_title(r"$\times$"+str(round(1/fImG,1)),loc='left',size='medium')


#------------------------ F2
fReS = 0.4612625012103523
fImS = 0.7167861394115225
fImG = 1.0

v_ener, v_ReS, v_ImS, v_ImG, v_ReSmpa, v_ImSmpa, v_ImGmpa = np.loadtxt(databaseV_F2, unpack=True)
c_ener, c_ReS, c_ImS, c_ImG, c_ReSmpa, c_ImSmpa, c_ImGmpa = np.loadtxt(databaseC_F2, unpack=True)

axsMoS2NaClF2[0,2].plot(v_ener, v_ReS *fReS, c=colors[0], label = labelsVC[0])
axsMoS2NaClF2[0,2].plot(v_ener, v_ReSmpa *fReS, c=cmpa, ls=lsVC[0], label = labelMPA)
axsMoS2NaClF2[0,2].plot(c_ener, c_ReS *fReS, c=colors[1], label = labelsVC[1])
axsMoS2NaClF2[0,2].plot(c_ener, c_ReSmpa *fReS, c=cmpa, ls=lsVC[1], label = labelMPA)

axsMoS2NaClF2[1,2].plot(v_ener, v_ImS *fImS, c=colors[0])
axsMoS2NaClF2[1,2].plot(v_ener, v_ImSmpa *fImS, c=cmpa, ls=lsVC[0])
axsMoS2NaClF2[1,2].plot(c_ener, c_ImS *fImS, c=colors[1])
axsMoS2NaClF2[1,2].plot(c_ener, c_ImSmpa *fImS, c=cmpa, ls=lsVC[1])

axsMoS2NaClF2[2,2].plot(v_ener, v_ImG *fImG, c=colors[0], label = labelsF2[0])
axsMoS2NaClF2[2,2].plot(v_ener, v_ImGmpa *fImG, c=cmpa, ls=lsVC[0])
axsMoS2NaClF2[2,2].plot(c_ener, c_ImG *fImG, c=colors[1], label = labelsF2[1])
axsMoS2NaClF2[2,2].plot(c_ener, c_ImGmpa *fImG, c=cmpa, ls=lsVC[1])

axsMoS2NaClF2[0,2].set_title(r"$\times$"+str(round(1/fReS,1)),loc='left',size='medium')
axsMoS2NaClF2[1,2].set_title(r"$\times$"+str(round(1/fImS,1)),loc='left',size='medium')
axsMoS2NaClF2[2,2].set_title(r"$\times$"+str(round(1/fImG,1)),loc='left',size='medium')


#-----------------------
axsMoS2NaClF2[0,0].set_ylim(MoS2minReS,MoS2maxReS)
axsMoS2NaClF2[1,0].set_ylim(MoS2minImS,MoS2maxImS)
axsMoS2NaClF2[2,0].set_ylim(-MoS2maxImG,MoS2maxImG)

axsMoS2NaClF2[2,0].set_xlim(-50.5,50.5)
axsMoS2NaClF2[2,1].set_xlim(-50.5,50.5)
axsMoS2NaClF2[2,2].set_xlim(-101.0,101.0)

axsMoS2NaClF2[0,0].yaxis.set_minor_locator(AutoMinorLocator(5))
axsMoS2NaClF2[1,0].yaxis.set_minor_locator(AutoMinorLocator(5))
axsMoS2NaClF2[2,0].yaxis.set_minor_locator(AutoMinorLocator(5))

axsMoS2NaClF2[2,0].xaxis.set_minor_locator(AutoMinorLocator(5))
axsMoS2NaClF2[2,1].xaxis.set_minor_locator(AutoMinorLocator(5))
axsMoS2NaClF2[2,2].xaxis.set_minor_locator(AutoMinorLocator(5))

axsMoS2NaClF2[0,0].set_ylabel("Re$[\Sigma]~$(eV)")
axsMoS2NaClF2[1,0].set_ylabel("Im$[\Sigma]~$(eV)")
axsMoS2NaClF2[2,0].set_ylabel("Im$[G]~$(eV$^{-1}$)")

for m in range(3):
  axsMoS2NaClF2[2,m].set_xlabel("$\omega - \epsilon^{KS}~$(eV)")
  for m2 in range(3):
    axsMoS2NaClF2[m,m2].set_title(panels[m,m2],weight='bold',c='k',loc='center')

FZ = 15
axsMoS2NaClF2[2,0].annotate(labelsMoS2NaClF2[0], [-48,MoS2maxImG-(MoS2maxImG+MoS2maxImG)*0.05],verticalalignment='top',horizontalalignment='left', fontsize = FZ) 
axsMoS2NaClF2[2,1].annotate(labelsMoS2NaClF2[1], [-48,MoS2maxImG-(MoS2maxImG+MoS2maxImG)*0.05],verticalalignment='top',horizontalalignment='left', fontsize = FZ) 
axsMoS2NaClF2[2,2].annotate(labelsMoS2NaClF2[2], [-95,MoS2maxImG-(MoS2maxImG+MoS2maxImG)*0.05],verticalalignment='top',horizontalalignment='left', fontsize = FZ)  

axsMoS2NaClF2[0,2].legend(frameon=False, loc=(0.59,0.2), borderaxespad=0.45)
axsMoS2NaClF2[2,0].legend(frameon=False)
axsMoS2NaClF2[2,1].legend(frameon=False)
axsMoS2NaClF2[2,2].legend(frameon=False)


figSiNaCu.savefig('qp_SiNaCu.pdf')
figMoS2NaClF2.savefig('qp_MoS2NaClF2.pdf')
###################
plt.show()