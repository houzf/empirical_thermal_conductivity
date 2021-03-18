# Empirical estimation of thermal conductivity
Estimate the thermal conductivity using empirical models including the Clarke’s, Cahill’s, and  Slack's models.

# The basic equations

* Clarke model

&#954;<sub>min</sub>  = 0.85  k<sub>B</sub>(N<sub>A</sub> n &#961; /M<sub>avg</sub>)<sup>2/3</sup>  (E/&#961;)<sup>1/2</sup>,  Eq.(1)

where **k<sub>B</sub>** is Boltzmann constant,  **M<sub>avg</sub>** and **n** are the mean atomic mass and the number of the atoms in the unit cell, respectively, **E** is Young’s modulus, **&#961;** is the density and **N<sub>A</sub>** is Avogadro’s number.

* Cahill model
* 
&#954;<sub>min</sub>  =  k<sub>B</sub>/2.48 (n/&#937;)<sup>2/3</sup>  (v<sub>l</sub>+2v<sub>t</sub>),                Eq.(2)

or 

&#954;<sub>min</sub>  = 1/2 (&#960;/6)<sup>1/3</sup>k<sub>B</sub> (n/&#937;)<sup>2/3</sup>  (v<sub>l</sub>+2v<sub>t</sub>),  Eq.(3)

where **k<sub>B</sub>** is Boltzmann constant, **&#937;**  and **n** are the volume of unit cell and the number of the atoms in the unit cell, respectively. **v<sub>l</sub>** and **v<sub>t</sub>** and the longitudinal and  transverse sound  velocities, respectively, which are estimated from the bulk modulus **B** and shear modulus **G** as follows:

v<sub>l</sub>= ((B+4G/3)/&#961;)<sup>1/2</sup>,                   Eq.(4)

v<sub>t</sub>=(G/&#961;)<sup>1/2</sup>.                           Eq.(5)

* Slack model

&#954; = 3.1 &#8727; 10<sup>-6</sup> M<sub>avg</sub> &#920;<sub>D</sub><sup>3</sup>&#948; /(&#947;<sup>2</sup>n<sup>2/3</sup>T),  Eq.(6)

where **M<sub>avg</sub>**  is the mean atomic mass (in amu), **&#920;<sub>D</sub>**  is the Debye temperature (in K), **n** and the number of the atoms in the unit cell, **&#948;<sup>3</sup>** is the volume per atom (in &#197;<sup>3</sup>), and **&#947;** is the average Gr&#252;neisen parameter. The Debye temperature and Gr&#252;neisen parameter can be evaluated from the sound velocities, which can be measured experimentally, or can be obtained by the theoretically-calculated elastic modulus.

&#920;<sub>D</sub> = h/k<sub>B</sub> (3n/(4&#960;&#937;))<sup>1/3</sup>v<sub>a</sub>,   Eq.(7)

where **h** and **k_<sub>B</sub>** are Planck and Boltzmann constants, respectively, **n** is the number of atoms in the unit cell, **&#937;** is the cell volume, and **v<sub>a</sub>** is the average sound wave velocity. The **v<sub>a</sub>**  is given in terms of **v<sub>l</sub>** and **v<sub>t</sub>** as

v<sub>a</sub> = [(1/3)(1/v<sub>l</sub><sup>3</sup>+2/v<sub>t</sub><sup>3</sup>)]<sup>-1/3</sup>.  Eq.(8)

The Gr&#252;neisen parameter **&#947;**  is calculated from the relation proposed by Belomestnykh:

&#947; = [9-12(v<sub>t</sub>/v<sub>l</sub>)<sup>2</sup>]/[2+4(v<sub>t</sub>/v<sub>l</sub>)<sup>2</sup>],  Eq.(9)

which takes into account the contribution of acoustic sound velocities only.
