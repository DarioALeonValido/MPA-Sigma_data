import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
from matplotlib.cm import get_cmap

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)


Na_iGN_k16=np.array([1,2,3,4,5,6,7,8,9]) #bcc
Na_iNGN_k16=np.concatenate((Na_iGN_k16[-1:0:-1],Na_iGN_k16))
Na_kGN_k16=np.linspace(0, 1, len(Na_iGN_k16))
Na_kNGN_k16=np.linspace(-1, 1, len(Na_iNGN_k16))

fcc_iGL_k16=np.array([1,2,3,4,5,6,7,8,9]) #fcc
fcc_iGX_k16=np.array([1,10,25,38,49,58,65,70,73]) #fcc

fcc_iLGX_k16=np.concatenate((fcc_iGL_k16[-1:0:-1],fcc_iGX_k16))
fcc_kLG_k16=np.linspace(-np.sqrt(3/2), 0, len(fcc_iGL_k16))
fcc_kGX_k16=np.linspace(0, 1, len(fcc_iGX_k16))
fcc_kLGX_k16=np.concatenate((fcc_kLG_k16[:-1],fcc_kGX_k16))

#---------- plots -----------------------------------------

plt.rcParams['font.size'] = '11.5'
plt.rcParams['lines.linewidth'] = 1.5

cmap_S = 'PuOr_r'
cmap_num = get_cmap(cmap_S)

panels = ['(a)','(b)','(c)','(d)','(e)','(f)','(g)','(h)']

f=0.95
fx=4;fy=2
figNaSiMoS2Cu, axsNaSiMoS2Cu = plt.subplots(fy, fx, sharey='row', width_ratios=[0.4,1,1.64275/1.41421,1])
figNaSiMoS2Cu.set_size_inches(f*3*fx, f*4*fy*1.1* (1+1.64275/1.41421+1+0.4)/(1+1.64275/1.41421+1) )
figNaSiMoS2Cu.subplots_adjust(left=0.06, bottom=0.055, right=0.99, top=1.02, wspace=None, hspace=0.1)

path = 'databases/'

for m in range(4):
  axsNaSiMoS2Cu[0,m].set_title(panels[m],weight='bold',c='k',loc='center')
  axsNaSiMoS2Cu[1,m].set_title(panels[4+m],weight='bold',c='k',loc='center')

#axsNaSiMoS2Cu[3].set_xticks([fcc_kLG_k16[0],0,1], labels=["$L$","$\Gamma$","$X$"])
#axsNaSiMoS2Cu[3].set_xlim(fcc_kLG_k16[0],1)

pad=0.08
aspect=25

ylim1 = 45; ylim2 = 40
axsNaSiMoS2Cu[0,0].set_ylim(-ylim1,ylim1)
axsNaSiMoS2Cu[1,0].set_ylim(-ylim2,ylim2)

axsNaSiMoS2Cu[0,0].set_ylabel("$\omega~$(eV)")
axsNaSiMoS2Cu[1,0].set_ylabel("$\omega~$(eV)")


#------------------------ Na

grid_k, grid_w, map_imSc_shifted_tot, map_imG_shifted_tot = np.load(f'{path}spectral_Na.npy')

vmax=np.max(map_imSc_shifted_tot)
vmin=-vmax
pcm = axsNaSiMoS2Cu[0,0].pcolor(grid_k, grid_w, map_imSc_shifted_tot, cmap=cmap_S, vmin=vmin, vmax=vmax)
cbar = figNaSiMoS2Cu.colorbar(pcm, ax=axsNaSiMoS2Cu[0,0],location='top', extend='max',aspect=aspect*0.4,pad=pad)
cbar.ax.xaxis.set_tick_params(color='r')
plt.setp(plt.getp(cbar.ax.axes, 'xticklabels'), color='r')
cbar.ax.xaxis.set_minor_locator(AutoMinorLocator(2))
vmax=0.8
vmin=-vmax
pcm = axsNaSiMoS2Cu[1,0].pcolor(grid_k, grid_w, map_imG_shifted_tot, cmap=cmap_S, vmin=vmin, vmax=vmax)
cbar = figNaSiMoS2Cu.colorbar(pcm, ax=axsNaSiMoS2Cu[1,0],location='top', extend='max',aspect=aspect*0.4,pad=pad)
cbar.ax.xaxis.set_tick_params(color='b')
plt.setp(plt.getp(cbar.ax.axes, 'xticklabels'), color='b')
cbar.ax.xaxis.set_minor_locator(AutoMinorLocator(2))

axsNaSiMoS2Cu[0,0].set_xticks([0,1], labels=["$\Gamma$","$N$"])
axsNaSiMoS2Cu[1,0].set_xticks([0,1], labels=["$\Gamma$","$N$"])

axsNaSiMoS2Cu[0,0].annotate('Na', [0.95,ylim1-2],verticalalignment='top',horizontalalignment='right',
                                 bbox=dict(boxstyle="square,pad=0.25", fc="w", ec="gray", lw=2))
axsNaSiMoS2Cu[0,0].annotate("$Im \Sigma$", [0.05,ylim1-2],verticalalignment='top',horizontalalignment='left', color='r')

axsNaSiMoS2Cu[1,0].annotate('Na', [0.95,-ylim2+2],verticalalignment='bottom',horizontalalignment='right',
                                 bbox=dict(boxstyle="square,pad=0.25", fc="w", ec="gray", lw=2))
axsNaSiMoS2Cu[1,0].annotate("$Im G$", [0.05,-ylim2+2],verticalalignment='bottom',horizontalalignment='left', color='b')


#------------------------ Si

grid_k, grid_w, map_imSc_shifted_tot, map_imG_shifted_tot = np.load(f'{path}spectral_Si.npy')

vmax=np.max(map_imSc_shifted_tot)
vmin=-vmax
pcm = axsNaSiMoS2Cu[0,1].pcolor(grid_k, grid_w, map_imSc_shifted_tot, cmap=cmap_S, vmin=vmin, vmax=vmax)
cbar = figNaSiMoS2Cu.colorbar(pcm, ax=axsNaSiMoS2Cu[0,1],location='top', extend='max',aspect=aspect,pad=pad)
cbar.ax.xaxis.set_tick_params(color='r')
plt.setp(plt.getp(cbar.ax.axes, 'xticklabels'), color='r')
cbar.ax.xaxis.set_minor_locator(AutoMinorLocator(2))
vmax=0.3
vmin=-vmax
pcm = axsNaSiMoS2Cu[1,1].pcolor(grid_k, grid_w, map_imG_shifted_tot, cmap=cmap_S, vmin=vmin, vmax=vmax)
cbar = figNaSiMoS2Cu.colorbar(pcm, ax=axsNaSiMoS2Cu[1,1],location='top', extend='max',aspect=aspect,pad=pad)
cbar.ax.xaxis.set_tick_params(color='b')
plt.setp(plt.getp(cbar.ax.axes, 'xticklabels'), color='b')
cbar.ax.xaxis.set_minor_locator(AutoMinorLocator(2))

axsNaSiMoS2Cu[0,1].set_xticks([fcc_kLG_k16[0],0,1], labels=["$L$","$\Gamma$","$X$"])
axsNaSiMoS2Cu[1,1].set_xticks([fcc_kLG_k16[0],0,1], labels=["$L$","$\Gamma$","$X$"])

axsNaSiMoS2Cu[0,1].annotate('Si', [0.95,ylim1-2],verticalalignment='top',horizontalalignment='right',
                                 bbox=dict(boxstyle="square,pad=0.25", fc="w", ec="gray", lw=2))
axsNaSiMoS2Cu[0,1].annotate("$Im \Sigma$", [fcc_kLG_k16[0]+0.05,ylim1-2],verticalalignment='top',horizontalalignment='left', color='r')

axsNaSiMoS2Cu[1,1].annotate('Si', [0.95,-ylim2+2],verticalalignment='bottom',horizontalalignment='right',
                                 bbox=dict(boxstyle="square,pad=0.25", fc="w", ec="gray", lw=2))
axsNaSiMoS2Cu[1,1].annotate("$Im G$", [fcc_kLG_k16[0]+0.05,-ylim2+2],verticalalignment='bottom',horizontalalignment='left', color='b')


#------------------------ MoS2

grid_k, grid_w, map_imSc_shifted_tot, map_imG_shifted_tot = np.load(f'{path}spectral_MoS2.npy')

vmax=np.max(map_imSc_shifted_tot)
vmin=-vmax
pcm = axsNaSiMoS2Cu[0,2].pcolor(grid_k, grid_w, map_imSc_shifted_tot, cmap=cmap_S, vmin=vmin, vmax=vmax)
cbar = figNaSiMoS2Cu.colorbar(pcm, ax=axsNaSiMoS2Cu[0,2],location='top', extend='max',aspect=aspect*1.64275/1.41421,pad=pad)
cbar.ax.xaxis.set_tick_params(color='r')
plt.setp(plt.getp(cbar.ax.axes, 'xticklabels'), color='r')
cbar.ax.xaxis.set_minor_locator(AutoMinorLocator(2))
vmax=0.5
vmin=-vmax
pcm = axsNaSiMoS2Cu[1,2].pcolor(grid_k, grid_w, map_imG_shifted_tot, cmap=cmap_S, vmin=vmin, vmax=vmax)
cbar = figNaSiMoS2Cu.colorbar(pcm, ax=axsNaSiMoS2Cu[1,2],location='top', extend='max',aspect=aspect*1.64275/1.41421,pad=pad)
cbar.ax.xaxis.set_tick_params(color='b')
plt.setp(plt.getp(cbar.ax.axes, 'xticklabels'), color='b')
cbar.ax.xaxis.set_minor_locator(AutoMinorLocator(2))

axsNaSiMoS2Cu[0,2].set_xlim(0,1.5+2/3**0.5)
axsNaSiMoS2Cu[1,2].set_xlim(0,1.5+2/3**0.5)

axsNaSiMoS2Cu[0,2].set_xticks([0,1,1.5,1.5+2/3**0.5], labels=["$\Gamma$","$M$","$K$","$\Gamma$"])
axsNaSiMoS2Cu[1,2].set_xticks([0,1,1.5,1.5+2/3**0.5], labels=["$\Gamma$","$M$","$K$","$\Gamma$"])

axsNaSiMoS2Cu[0,2].annotate('MoS2', [1.5+2/3**0.5-0.05,ylim1-2],verticalalignment='top',horizontalalignment='right',
                                 bbox=dict(boxstyle="square,pad=0.25", fc="w", ec="gray", lw=2))
axsNaSiMoS2Cu[0,2].annotate("$Im \Sigma$", [0.05,ylim1-2],verticalalignment='top',horizontalalignment='left', color='r')

axsNaSiMoS2Cu[1,2].annotate('MoS2', [1.5+2/3**0.5-0.05,-ylim2+2],verticalalignment='bottom',horizontalalignment='right',
                                 bbox=dict(boxstyle="square,pad=0.25", fc="w", ec="gray", lw=2))
axsNaSiMoS2Cu[1,2].annotate("$Im G$", [0.05,-ylim2+2],verticalalignment='bottom',horizontalalignment='left', color='b')


#------------------------ Cu

grid_k, grid_w, map_imSc_shifted_tot, map_imG_shifted_tot = np.load(f'{path}spectral_Cu.npy')

vmax=np.max(map_imSc_shifted_tot)
vmin=-vmax
pcm = axsNaSiMoS2Cu[0,3].pcolor(grid_k, grid_w, map_imSc_shifted_tot, cmap=cmap_S, vmin=vmin, vmax=vmax)
cbar = figNaSiMoS2Cu.colorbar(pcm, ax=axsNaSiMoS2Cu[0,3],location='top', extend='max',aspect=aspect,pad=pad)
cbar.ax.xaxis.set_tick_params(color='r')
plt.setp(plt.getp(cbar.ax.axes, 'xticklabels'), color='r')
cbar.ax.xaxis.set_minor_locator(AutoMinorLocator(2))
vmax=0.7
vmin=-vmax
pcm = axsNaSiMoS2Cu[1,3].pcolor(grid_k, grid_w, map_imG_shifted_tot, cmap=cmap_S, vmin=vmin, vmax=vmax)
cbar = figNaSiMoS2Cu.colorbar(pcm, ax=axsNaSiMoS2Cu[1,3],location='top', extend='max',aspect=aspect,pad=pad)
cbar.ax.xaxis.set_tick_params(color='b')
plt.setp(plt.getp(cbar.ax.axes, 'xticklabels'), color='b')
cbar.ax.xaxis.set_minor_locator(AutoMinorLocator(2))

axsNaSiMoS2Cu[0,3].set_xticks([fcc_kLG_k16[0],0,1], labels=["$L$","$\Gamma$","$X$"])
axsNaSiMoS2Cu[1,3].set_xticks([fcc_kLG_k16[0],0,1], labels=["$L$","$\Gamma$","$X$"])

axsNaSiMoS2Cu[0,3].annotate('Cu', [0.95,ylim1-2],verticalalignment='top',horizontalalignment='right',
                                 bbox=dict(boxstyle="square,pad=0.25", fc="w", ec="gray", lw=2))
axsNaSiMoS2Cu[0,3].annotate("$Im \Sigma$", [fcc_kLG_k16[0]+0.05,ylim1-2],verticalalignment='top',horizontalalignment='left', color='r')

axsNaSiMoS2Cu[1,3].annotate('Cu', [0.95,-ylim2+2],verticalalignment='bottom',horizontalalignment='right',
                                 bbox=dict(boxstyle="square,pad=0.25", fc="w", ec="gray", lw=2))
axsNaSiMoS2Cu[1,3].annotate("$Im G$", [fcc_kLG_k16[0]+0.05,-ylim2+2],verticalalignment='bottom',horizontalalignment='left', color='b')


###################
figNaSiMoS2Cu.savefig('spectral_NaSiMoS2Cu.png',dpi=300)
plt.show()