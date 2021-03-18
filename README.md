# Empirical estimation of thermal conductivity
Estimate the thermal conductivity using empirical models including the Clarke’s, Cahill–Pohl’s, and  Slack's models.

# The basic equations

* Clarke model<sup>[1](https://doi.org/10.1016/S0257-8972(02)00593-5),[2](https://doi.org/10.1016/j.jeurceramsoc.2014.03.013)</sup>

&#954;<sub>min</sub>  = 0.87  k<sub>B</sub>(N<sub>A</sub> n &#961; /M<sub>avg</sub>)<sup>2/3</sup>  (E/&#961;)<sup>1/2</sup>,  

where **k<sub>B</sub>** is Boltzmann constant,  **M<sub>avg</sub>** and **n** are the mean atomic mass and the number of the atoms in the unit cell, respectively, **E** is Young’s modulus, **&#961;** is the density and **N<sub>A</sub>** is Avogadro’s number.

* Cahill–Pohl model<sup>[3](https://doi.org/10.1146/annurev.pc.39.100188.000521),[4](https://doi.org/10.1063/1.4832615),[5](https://doi.org/10.1103/PhysRevB.46.6131)</sup>

&#954;<sub>min</sub>  =  k<sub>B</sub>/2.48 (n/&#937;)<sup>2/3</sup>  (v<sub>l</sub>+2v<sub>t</sub>),              

or 

&#954;<sub>min</sub>  = 1/2 (&#960;/6)<sup>1/3</sup>k<sub>B</sub> (n/&#937;)<sup>2/3</sup>  (v<sub>l</sub>+2v<sub>t</sub>),

where **k<sub>B</sub>** is Boltzmann constant, **&#937;**  and **n** are the volume of unit cell and the number of the atoms in the unit cell, respectively. **v<sub>l</sub>** and **v<sub>t</sub>** and the longitudinal and  transverse sound  velocities, respectively, which are estimated from the bulk modulus **B** and shear modulus **G** as follows:

v<sub>l</sub>= ((B+4G/3)/&#961;)<sup>1/2</sup>,                  

v<sub>t</sub>=(G/&#961;)<sup>1/2</sup>.                 

* Slack model<sup>[6](https://doi.org/10.1016/0022-3697(73)90092-9)</sup>

&#954; = 3.1 &#8727; 10<sup>-6</sup> M<sub>avg</sub> &#920;<sub>D</sub><sup>3</sup>&#948; /(&#947;<sup>2</sup>n<sup>2/3</sup>T), 

where **M<sub>avg</sub>**  is the mean atomic mass (in amu), **&#920;<sub>D</sub>**  is the Debye temperature (in K), **n** and the number of the atoms in the unit cell, **&#948;<sup>3</sup>** is the volume per atom (in &#197;<sup>3</sup>), and **&#947;** is the average Gr&#252;neisen parameter. The Debye temperature<sup>[7](https://doi.org/10.1002/andp.19123441404)</sup> and Gr&#252;neisen parameter can be evaluated from the sound velocities, which can be measured experimentally, or can be obtained by the theoretically-calculated elastic modulus.

&#920;<sub>D</sub> = h/k<sub>B</sub> (3n/(4&#960;&#937;))<sup>1/3</sup>v<sub>a</sub>,  

where **h** and **k<sub>B</sub>** are Planck and Boltzmann constants, respectively, **n** is the number of atoms in the unit cell, **&#937;** is the cell volume, and **v<sub>a</sub>** is the average sound wave velocity. The **v<sub>a</sub>**  is given in terms of **v<sub>l</sub>** and **v<sub>t</sub>** as

v<sub>a</sub> = [(1/3)(1/v<sub>l</sub><sup>3</sup>+2/v<sub>t</sub><sup>3</sup>)]<sup>-1/3</sup>.  

The Gr&#252;neisen parameter **&#947;**  is calculated from the relation proposed by Belomestnykh<sup>[8](https://doi.org/10.1134/1.1666949)</sup>:

&#947; = [9-12(v<sub>t</sub>/v<sub>l</sub>)<sup>2</sup>]/[2+4(v<sub>t</sub>/v<sub>l</sub>)<sup>2</sup>],  

which takes into account the contribution of acoustic sound velocities only.

# Usage

## Input parameters

1. natoms_list:  number of atoms for each species in the primitive unit cell. For example, Al<sub>2</sub>Fe<sub>3</sub>Si<sub>3</sub> in the primitive unit cell of its triclinic structure, the number of  Fe, Al, and Si are 6, 4, and 6, respectively. So  define:   natoms_list = [6, 4, 6].
2. atomic_weight_list: the atomic weight (in amu) for each atom species. For example:  the atomic weights of Fe, Al, and Si are 55.845, 26.982, and 28.086, respectively. So define:  atomic_weight_list = [55.845, 26.982, 28.086].
3. vol: the volume of primitive unit cell (in in &#197;<sup>3</sup>).  For example, the volume of the primitive unit cell of   Al<sub>2</sub>Fe<sub>3</sub>Si<sub>3</sub>  is  196.489731295 &#197;<sup>3</sup>. So define: vol = 196.489731295.
4. K: bulk modulus (in GPa).  For example, K = 173.121
5. G: shear modulus (in GPa). For example, G = 173.121
6. E: Young's modulus (in GPa). For example,  E= 286.239.
7. t: temperature (in K). t= 679.334852747

## Call function

- kappa_Clarke=thermal_cond_clarke(natoms_list, atomic_weight_list, vol, E)

- kappa_Chill=thermal_cond_cahill(natoms_list, atomic_weight_list, vol, K, G)

- kappa_Slack=thermal_cond_slack(natoms_list, atomic_weight_list, vol, K, G, t)

- kappa_mixed=thermal_cond_latt_mixed(natoms_list, atomic_weight_list, vol, K)

print(kappa_Clarke)

print(kappa_Chill)

print(kappa_Slack)

print(kappa_mixed)

All the calculated thermal conductivities are given in the unit of W m<sup>-1</sup>K<sup>-1</sup>.  Meanwhile, the other physics quantities such as Debye temperature, Gr&#252;neisen parameter, and sound velocities are also printed out. 

We have used the Slack model to estimate of Al<sub>2</sub>Fe<sub>3</sub>Si<sub>3</sub>. If you are interested in it, please refer to our paper:

1. Zhufeng Hou, Yoshiki Takagiwa, Yoshikazu Shinohara, Yibin Xu, and Koji Tsuda, Machine-learning-assisted development and theoretical consideration for the Al<sub>2</sub>Fe<sub>3</sub>Si<sub>3</sub>  thermoelectric material, *ACS Appl. Mater. Interfaces* **11**, 11545–11554(2019). DOI: [10.1021/acsami.9b02381](https://doi.org/10.1021/acsami.9b02381).


# References

1. D. R. Clarke, Materials selection guidelines for low thermal conductivity thermal barrier coatings, *Surf. Coat. Technol.* **163–164**, 67–74(2003). DOI: [10.1016/S0257-8972(02)00593-5](https://doi.org/10.1016/S0257-8972(02)00593-5).
2. A. M. Limarga, S. Shian, R. M. Leckie, C. G. Levi, and D. R. Clarke, Thermal conductivity of single- and multi-phase compositions in the ZrO<sub>2</sub>–Y<sub>2</sub>O<sub>3</sub>–Ta<sub>2</sub>O<sub>5</sub> system, *J. Eur. Ceram. Soc.*, **34**, 3085-3094(2014). DOI: [10.1016/j.jeurceramsoc.2014.03.013](https://doi.org/10.1016/j.jeurceramsoc.2014.03.013).
3. D. G. Cahill and R. O. Pohl, Lattice vibrations and heat transport in crystals and glasses,  *Annu. Rev. Phys. Chem.*, **39**, 93–121(1988). DOI: [10.1146/annurev.pc.39.100188.000521](https://doi.org/10.1146/annurev.pc.39.100188.000521).
4. D. G. Cahill, P. V. Braun, G. Chen, D. R. Clarke, S. Fan, K. E. Goodson, P. Keblinski, W. P. King, G. D. Mahan, A. Majumdar, H. J. Maris, S. R. Phillpot, E. Pop and L. Shi, *Appl. Phys. Rev.*, **1**, 011305(2014). DOI: [10.1063/1.4832615](https://doi.org/10.1063/1.4832615).
5. D. G. Cahill, S. K. Watson, and R. O. Pohl, Lower limit to the thermal conductivity of disordered crystals, *Phys. Rev. B* **46**, 6131(1992). DOI: [10.1103/PhysRevB.46.6131](https://doi.org/10.1103/PhysRevB.46.6131).
6. G. A. Slack, Nonmetallic crystals with high thermal conductivity, *J. Phys. Chem. Solids*
   **34**, 321–335 (1973). DOI: [10.1016/0022-3697(73)90092-9](https://doi.org/10.1016/0022-3697(73)90092-9).
7. P. Debye, Zur theorie der spezifischen w&#228;rmen,  *Annalen der Physik* **344**, 789–839 (1912). DOI: [10.1002/andp.19123441404](https://doi.org/10.1002/andp.19123441404).
8. V. N. Belomestnykh, The acoustical Gr&#252;neisen constants of solids, *Tech. Phys. Lett.* **30**,
   91–93 (2004). DOI: [10.1134/1.1666949](https://doi.org/10.1134/1.1666949).
