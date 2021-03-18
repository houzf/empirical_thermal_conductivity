#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import e, pi, sin, exp, cos
import numpy as np
from numpy import math

def molecular_weight(natoms_list, atomic_weight_list):
    #atomic_weight_list in  atomic mass units (u)
    # 1 u = 1 g/mol/(N_A)
    mol_weight=0.0
    for i in range(len(natoms_list)):
        mol_weight += natoms_list[i] * atomic_weight_list[i]

    #molecular weight in unit of atomic mass units (u)
    return mol_weight


def mass(natoms_list, atomic_weight_list):
    #atomic_weight_list in  atomic mass units (u)
    # 1 u = 1 g/mol/(N_A)
    #  Avogadro's number, in unit of mol^{-1}.
    NA = 6.02214085774e+23
    molw = molecular_weight(natoms_list, atomic_weight_list)
    print('Average atomic mass [g/mol]:{:12.5f}'.format(molw/sum(natoms_list)))
    mass_in_kg = (molw/NA)*0.001
    #print 'Average atomic mass [kg/atom]:', mass_in_kg/sum(natoms_list)
    #print 'Total mass [kg]:', mass_in_kg
    return mass_in_kg

def mass_density(natoms_list, atomic_weight_list, vol):
    # volume in unit of angstrom^{-3}.
    #atomic_weight_list in  atomic mass units (u)
    # 1 u = 1 g/mol/(N_A)
    # density in unit of kg/m^3.
    mass_in_kg = mass(natoms_list, atomic_weight_list)
    rho = mass_in_kg/(vol*1.0e-30)
    print('Density [kg/m^3]:{:12.5f}'.format(rho))
    return rho

def thermal_cond_clarke(natoms_list, atomic_weight_list, vol, E):
    #Boltzmann constant (J/K = W*s/K)
    kb = 1.3806485279e-23
    #  Avogadro's number
    NA = 6.02214085774e+23
    # volume in unit of angstrom^{-3}.
    #Young's modulus E in GPa
    # 1GPa = 10^9 N/m^2 = 10^9 kg/(m*s^2).
    GPa2SI = 1.0e9
    E = E*GPa2SI
    rho = mass_density(natoms_list, atomic_weight_list, vol)
    v_s = np.sqrt(E/rho)
    print("Velocity estimated from Young's modulus [m/s]:{:12.5f}".format(v_s))
    natoms = sum(natoms_list)
    molw = molecular_weight(natoms_list, atomic_weight_list)
    kappa_clarke = 0.87 * kb * (NA*natoms*rho/molw)**(2.0/3.0) * v_s
    # in unit of W/(m.K)
    return kappa_clarke

def thermal_cond_cahill(natoms_list, atomic_weight_list, vol, K, G):
    # volume in unit of angstrom^{-3}.
    #Boltzmann constant (J/K = W*s/K)
    kb = 1.3806485279e-23
    # 1GPa = 10^9 N/m^2 = 10^9 kg/(m*s^2).
    GPa2SI = 1.0e9
    K = K*GPa2SI
    G = G*GPa2SI
    rho = mass_density(natoms_list, atomic_weight_list, vol)
    v_l = np.sqrt((K+4.0*G/3.0)/rho)
    v_t = np.sqrt(G/rho)
    natoms = sum(natoms_list)
    n = float(natoms)/(vol*1.0e-30)
    print('Longitudinal sound velocity estimated from bulk and shear moduli [m/s]:{:12.5f}'.format(v_l))
    print('Transverse sound velocity estimated from shear modulus [m/s]:{:12.5f}'.format(v_t))
    #kappa_cahill = 1.0/2.48 * kb *n**(2.0/3.0)*(v_l+v_t)
    kappa_cahill = 0.5*(np.pi/6.0)**(1.0/3.0)*kb*n**(2.0/3.0)*(v_l+v_t)
    return kappa_cahill

def thermal_cond_latt_mixed(natoms_list, atomic_weight_list, vol, K):
    #Boltzmann constant (J/K = W*s/K)
    kb = 1.3806485279e-23
    #Avogadro's number
    NA = 6.02214085774e+23
    ang2m = 1.0e-10
    # 1GPa = 10^9 N/m^2 = 10^9 kg/(m*s^2).
    GPa2SI = 1.0e9
    K = K*GPa2SI
    a1 = 2.7e-4
    a2 = 1.5e-23
    rho = mass_density(natoms_list, atomic_weight_list, vol)
    v_s = np.sqrt(K/rho)
    print('Speed of sound estimated from bulk modulus [m/s]:{:12.5f}'.format(v_s))
    mass_in_kg = mass(natoms_list, atomic_weight_list)
    natoms = sum(natoms_list)
    mean_mass = mass_in_kg/float(natoms)
    print(mean_mass)
    vol = vol*ang2m**3
    print('vol:{:12.5e}'.format(vol))
    mean_vol = vol/float(natoms)
    print('mean_vol:{:12.5e}'.format(mean_vol))
    print(a1, mean_vol, mean_vol**(2.0/3.0), natoms**(1.0/3.0))
    kappa_ac = a1*mean_mass*v_s**3/(mean_vol**(2.0/3.0)*natoms**(1.0/3.0))
    kappa_op = a2*v_s*mean_vol**(-2.0/3.0)*(1.0-float(natoms)**(-2.0/3.0))
    print('Lattice thermal conducivity contribued by acoustic phonons:{:12.5f}'.format(
          kappa_ac))
    print('Lattice thermal conducivity contribued by optical phonons:{:12.5f}'.format(
        kappa_op))

    #print((6*np.pi**2)**(2.0/3.0)*0.25*np.pi**(-2))
    #print(1.5*kb*(np.pi/6.0)*(1.0/3.0)*v_s*mean_vol**(-2.0/3.0)*(1.0-natoms**(-2.0/3.0)))
    #print(1.5*kb*(np.pi/6.0)*(1.0/3.0))
    kappa_lat = kappa_ac + kappa_op

    return kappa_lat

def thermal_cond_slack(natoms_list, atomic_weight_list, vol, K, G, t):
    # volume in unit of angstrom^{-3}.
    # Planck constant: (J.s)
    h = 6.62607004e-34
    #Boltzmann constant (J/K = W*s/K)
    kb = 1.38064852e-23
    # 1GPa = 10^9 N/m^2 = 10^9 kg/(m*s^2).
    GPa2SI = 1.0e9
    K = K*GPa2SI
    G = G*GPa2SI
    rho = mass_density(natoms_list, atomic_weight_list, vol)
    v_l = np.sqrt((K+4.0*G/3.0)/rho)
    v_t = np.sqrt(G/rho)
    v_a = ((1.0/3.0)*(v_l**(-3.0)+2.0*v_t**(-3.0)))**(-1.0/3.0)
    x = v_t/v_l
    gamma = (9.0-12.0*x**2)/(2.0+4.0*x**2)
    print('gamma:{:12.5f}'.format(gamma))
    natoms = sum(natoms_list)
    n = float(natoms)/(vol*1.0e-30)
    t_Debye = h/kb*(3.0*natoms/(4.0*np.pi*vol*1.0e-30))**(1.0/3.0)*v_a
    print('Longitudinal sound velocity estimated from bulk and shear moduli [m/s]:{:12.5f}'.format(v_l))
    print('Transverse sound velocity estimated from shear modulus [m/s]:{:12.5f}'.format(v_t))
    print('Averaged sound velocity [m/s]:{:12.5f}'.format(v_a))
    print('Debye temperature [K]:{:12.5f}'.format(t_Debye))
    print('Gruneisen parameter gamma:{:12.5f}'.format(gamma))
    #A = 2.43e-8/(1.0-0.514/gamma + 0.228/(gamma**2))
    #print 'A=',A
    mass_in_kg = mass(natoms_list, atomic_weight_list)
    #Ma= mass_in_kg/float(natoms)
    #Ma in unit of amu
    Ma = molecular_weight(natoms_list, atomic_weight_list)/float(natoms)
    #delta= (vol*1.0e-30/float(natoms))**(1.0/3.0)
    # delta in angstrom
    delta = (vol/float(natoms))**(1.0/3.0)
    A = 3.1e-6
    kappa_slack = A*Ma*delta*natoms**(-2.0/3.0)*t_Debye**3.0/(gamma**2*t)
    return kappa_slack

def calc_volume_trilinic(a, b, c, alpha, beta, gamma):

    alpha = math.pi * alpha/180.0
    beta = math.pi * beta/180.0
    gamma = math.pi * gamma/180.0
    ca = math.cos(alpha)
    cb = math.cos(beta)
    cg = math.cos(gamma)
    vol = a*b*c*math.sqrt(1.0+2*ca*cb*cg-ca**2-cb**2-cg**2)
    return vol

def cal_modulus(v_l, v_t, rho):
    ## v_t: transverse velocity, in m/s
    ## rho: in kg/m^3
    # 1GPa = 10^9 N/m^2 = 10^9 kg/(m*s^2).
    GPa2SI = 1.0e9
    B = rho*(v_l**2 - 4.0/3.0 * v_t**2)/GPa2SI
    G = rho*v_t**2/GPa2SI
    # G, B in GPa
    E = rho*v_t**2*(3.0*v_l**2 -
         4.0*v_t**2)/(v_l**2-v_t**2)*1.0/GPa2SI
    #E2 = 9 *B*G/(3.0*B+G)
    #print(E, E2)
    nu = (3.0*B-2.0*G)/(6.0*B+2.0*G)
    return B, G, E, nu


if __name__ == "__main__":
    a = [6, 4, 6]
    am=[55.845, 26.982, 28.086]
    #vol = 196.48
    vol = 196.489731295
    E = 286.239
    K = 173.121
    G = 116.886
    T = 679.334852747
    #T = 300.0
    """
    vol=198.6
    E=249
    G=102
    K=152
    T=640
    """

    print('Clarke model:')
    print(thermal_cond_clarke(a, am, vol, E))
    print('\n')
    print('Cahil model')
    print(thermal_cond_cahill(a, am, vol, K, G))
    print('\n')
    print('Mixed model')
    print(thermal_cond_latt_mixed(a, am, vol,  K))
    print('\n')
    print('Slack model:')
    print(thermal_cond_slack(a, am, vol, K, G, T))

    """
    print('experiment: x=0\n')
    print('Clarke model:')
    print(thermal_cond_clarke(a, am, vol, E))
    print('\n')
    print('Cahil model')
    print(thermal_cond_cahill(a, am, vol, K, G))
    print('\n')
    print('Mixed model')
    print(thermal_cond_latt_mixed(a, am, vol,  K))
    print('\n')
    print('Slack model:')
    print(thermal_cond_slack(a, am, vol, K, G, T))
    """

    bka=[1, 1, 3]
    bkm=[39.098, 180.948, 15.999]
    kka=186.9
    vka=3.988**3
    #print vka
    #print thermal_cond_latt_mixed(bka, bkm, vka,  kka)
    
    #BiCuSeO
    ccu=[2, 2 , 2, 2]
    cmcu=[63.546, 208.9804, 78.96, 15.999]
    vcu=3.9029*3.9029*8.9186
    Ecu=91.8
    Kcu=87.06
    Gcu=34.67
    #Ecu=94.02
    #Kcu=89.32
    #Gcu=35.49
    """
    Ecu=89.60
    Kcu=84.80
    Gcu=33.84
    Tcu=923
    print('Slack model:')
    print(thermal_cond_slack(ccu, cmcu, vcu, Kcu, Gcu, Tcu))
    print('Clarke model:')
    print(thermal_cond_clarke(ccu, cmcu, vcu, Ecu))
    print('Cahil model')
    print thermal_cond_cahill(ccu,cmcu, vcu, Kcu, Gcu)
    print('mixed model')
    print(thermal_cond_latt_mixed(ccu, cmcu, vcu,  Kcu))
    #print(mass(ccu,cmcu))
    #print((Gcu*1e+9)/2090**2)
    #print((Kcu+0.75*Gcu)*1e+9/(3366**2))
    """
