*****************************
Lab 1: Deformation and Stress
*****************************
   
.. toctree::
   :maxdepth: 2
    
The following list describes what a student can do/expect to see in Neon (**All output at 4 DP.**).

============
Model labels
============
- Model 1 (Uniaxial extension of unit cube)
- Model 2 (Equibiaxial extension of unit cube)
- Model 3 (Simple shear of unit cube)
- Model 4 (Shear of unit cube)
- Model 5 (Extension and shear of unit cube)

===============
Strain analysis
===============
    - **Select and solve a model**
    - **Visualise**:

      - **model** (white background, undeformed=red, deformed=green)
      - **x,y,z axes**
      - **deformed coordinate of model** (reference coordinates do not need to be shown as it is a unit cube, and node numbers not required)
      - they will use this infomation to write down coordinate equations describing deformation (in the form x=f(X) eg x=3X etc)

    - **Show** (4 DP with Tensors in bold).:

      - **Deformation gradient tensor (F)**
      - IGNORE: Determinant of F (for incompressible problems, they should know that det(F)=J=1 and det(C)=I3=1 so only showing I3 sufficient)
      - **Right Cauchy-Green deformation tensor (C)**
      - **I1=trace(C), I2, I3=det(C)** (I2 not really needed)
      - **Green-Lagrange strain tensor (E)**

===============
Stress analysis
===============
    - **Show** (4 DP with Tensors in bold).:

      - **Second Piola-Kirchhoff tensor (T)** (they will use this to calculate Cauchy Stress tensor without needing to calculate distorsional/hydrostatic pressure related terms)
      - **Cauchy stress tensor** ( :math:`\mathbf{\sigma}` ) (don't need to show J)
      - **Hydrostatic pressure** (not really needed for lab 1 but best to show consistent output across labs where possible) 

