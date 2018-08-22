* Created: Fri Aug 11 13:47:14 2017
* Basado en ejemplo dado por Weste-Harris. Fig 8.10, 8.9. Cuarta edicion

* curvas 
*----------------------------------------------------------------------
* Parameters and models
*----------------------------------------------------------------------
* XT018, Low Power MOS, 1.8V
* Se incluye la biblioteca tipica de LP5MOS
* Ojo: verifiquen que apunten a donde esta instalado el PDK
*.option search='$HOME/Proyectos-Actuales/chip-design/imd/v_2_0_1/design/Hspice/lpmos'
.option search='/mnt/vol_NFS_Zener/WD_ESPEC/esolera/tutorial_xfab_xh018_v2_0_2/design/Hspice/lpmos'
.lib './xh018.lib' tm
.lib './param.lib' 3s
.option PARHIER = LOCAL

.option ARTIST=2 PSF=2
.temp 25
.param SUPPLY=1.8

* Crea la variable suply



.option post
*.option scale=0.18u post
.param lmin=0.36u
.param wmin_n=2.52u
.param wmin_p=wmin_n*4.41

*--------------------------------------------------------------------------------------------------------
*Stimulation netlist
*------------------------------------------------------------------------------------------------------
*nmos

Vgs	g	gnd	1.8
Vds	d	gnd	1.8
Vmed    d	a	0
xM1	a	g	gnd	gnd	ne	W=wmin_n	L=lmin	

*----------------------------------------------------------------------------------------------
*Stimulus
*----------------------------------------------------------------------------------------------
.dc Vgs 0 1.8 1m
.end	
