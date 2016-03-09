
.. |vspace| raw:: latex

   \vspace{5mm}

.. _lab1:

****************************************************
Lab 1: Deformation and stress in isotropic materials
****************************************************

.. toctree::
   :maxdepth: 2

The objective of this lab is to analyse large deformation kinematics and stress with respect to reference coordinates in isotropic materials. The deformations you will be analysing include:

  - Model 1 (Uniaxial extension of a unit cube)
  - Model 2 (Equibiaxial extension of a unit cube)
  - Model 3 (Simple shear of a unit cube)
  - Model 4 (Shear of a unit cube)
  - Model 5 (Extension and shear of a unit cube)

Before starting this lab, please read the :ref:`Using OpenCMISS <using-opencmiss>` section to familiarise yourself with the software used in this lab.

|vspace|

========================
Solving mechanics models
========================

1. Start Neon and load lab1 (described in the :ref:`Starting Neon <starting-neon>` section).

|vspace|

2. Select "Model 1 (uniaxial extension of a unit cube)" from the drop down menu and click the "run" button (screenshots of this procedure are shown in the :ref:`Running models in Neon <running-models-in-Neon>` section).

|vspace|

3. After a short time, the model should have solved and the simulation results pane will open as shown in the screenshot below.

  .. image:: images/lab1_model1.png

  |vspace|

  The left side of the pane shows the stress and strain tensors associated with the simulation. The simulation results are shown in the 3D graphics window on the right side of the pane. In this graphical window:

      - the undeformed (reference) configuration of the unit cube is shown in red, and
      - the deformed (current) configuration is shown in green (x, y, z components of the deformed coordinates are shown at the corners of the model).

  The model in the 3D graphics window can be rotated (click-drag-left-mouse button), translated (click-drag-middle-mouse button), or zoomed (click-drag-middle-mouse button).

|vspace|

==========================
Section 1: Strain analysis
==========================

4. Write down the coordinate equations that describe this deformation in the form :math:`\boldsymbol{x}=f(\boldsymbol{X})`, i.e.:

  .. math::

    x_1 &= aX_1 + bX_2 + cX_3\\
    x_2 &= dX_1 + eX_2 + fX_3\\
    x_3 &= gX_1 + hX_2 + iX_3

  where the constants a-i need to be identified from the undeformed and deformed coordinates of the model shown in the graphics window.


|vspace|

5. Determine the deformation gradient tensor :math:`(\boldsymbol{F}=d\boldsymbol{x}/d\boldsymbol{X})`, and evaluate the determinant of :math:`\boldsymbol{F}` to see whether the material is incompressible (i.e. maintains constant volume).

|vspace|

6. Determine:

  - right Cauchy-Green deformation tensor :math:`(\boldsymbol{C})`,
  - :math:`I_1=trace(\boldsymbol{C})`,
  - :math:`I_3=det(\boldsymbol{C})`, and the
  - Green-Lagrange strain tensor :math:`(\boldsymbol{E})`.

|vspace|

7. Check your answers to 5 and 6 against the simulation results.

  .. Note::

      Some of the numbers are not identically=0 due to Round-off error. Assume any number less than 1E-10=0.

|vspace|

8. Select View->Problem from the menu and repeat steps 2-7 for the remaining models in the lab:

    - Model 2 (Equibiaxial extension of a unit cube)
    - Model 3 (Simple shear of a unit cube)
    - Model 4 (Shear of a unit cube)
    - Model 5 (Extension and shear of a unit cube)

|vspace|


.. note::

  By the end of section 1 you should be able to:

    - analyse large deformation kinematics with respect to reference coordinates, i.e. by determining :math:`\boldsymbol{F}`, :math:`\boldsymbol{C}`, invariants of :math:`\boldsymbol{C}`, and :math:`\boldsymbol{E}`.

    - relate the components of the deformation gradient tensor to the underlying deformation.

    - determine if a material is incompressible.


==========================
Section 2: Stress analysis
==========================

9. Select "Model 1 (uniaxial extension of a unit cube)" from the drop down menu and click the "run" button.

|vspace|

10. Using the components of the 2nd Piola-Kirchhoff stress tensor :math:`(\boldsymbol{T})` and your :math:`(\boldsymbol{F})` from step 5, determine the Cauchy components of the stress tensor :math:`(\boldsymbol{\Sigma})` (Don't forget the Jacobian :math:`(J)`).

|vspace|

11. Select View->Problem from the menu and repeat step 9 for the remaining models in the lab.

|vspace|

12. In model 1, why are :math:`\Sigma_{22}` and :math:`\Sigma_{33}` zero, and how do they relate to the deformation seen in the graphical window?

|vspace|

13. In model 3, why is :math:`\Sigma_{33}` negative? 

|vspace|

14. In model 3, why are the off-diagonal components of :math:`\boldsymbol{\Sigma}` nonzero? 

.. note::

  By the end of section 2 you should be able to:

    - derive the Cauchy stress tensor from the second Piola-Kirchhoff stress tensor.

    - relate the components of the Cauchy stress tensor to the underlying deformation.

