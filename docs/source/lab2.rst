Lab 2: Anisotropy and fibre (material) coordinates
==================================================
   
.. toctree::
   :maxdepth: 2
    

The following list describes what a student can do/expect to see in Neon 

============
Model labels
============
- Model 1 (Equibiaxial extension of unit cube, isotropic, 0 degree fibre rotation)
- Model 2 (Equibiaxial extension of unit cube, orthotropic, 0 degree fibre rotation)
- Model 3 (Equibiaxial extension of unit cube, isotropic, 30 degree fibre rotation)
- Model 4 (Equibiaxial extension of unit cube, isotropic, 45 degree fibre rotation)
- Model 5 (Equibiaxial extension of unit cube, orthotropic, 45 degree fibre rotation)
- Model 6 (Equibiaxial extension of unit cube, orthotropic, 90 degree fibre rotation)

==========================
Isotropy versus anisotropy
==========================

    - **Select and solve a model**
    - **Visualise**:

      - model (white background, undeformed=red, deformed=green)
      - **fibre axis** (gold)
      - x,y,z axes
      - deformed coordinate of model (reference coordinates do not need to be shown as it is a unit cube, and node numbers not required)
      - they will use this infomation to write down coordinate equations describing deformation (in the form x=f(X) eg x=3X etc)

    - **Show** (4 DP with Tensors in bold).:

      - **Deformation gradient tensor (F)**
      - **Right Cauchy-Green deformation tensor (C)**
      - I1=trace(**C**), I2, I3=det(**C**) (I2 not really needed)
      - **Green-Lagrange strain tensor with respect to reference coordinates (Eref)**
      - **Green-Lagrange strain tensor with respect to fibre coordinates (Efib)**
      - **Second Piola-Kirchhoff tensor with respect to reference coordinates (Tref)** (they will calcualte this using the constitutive equation/hydrostatic pressure term)
      - **Second Piola-Kirchhoff tensor with respect to fibre coordinates (Tfib)**
      - **Hydrostatic pressure** (p) (not really needed for lab 1 but best to show consistent output across labs where possible) 
      - IGNORE Cauchy stress tensor ( :math:`\mathbf{\sigma}` )



