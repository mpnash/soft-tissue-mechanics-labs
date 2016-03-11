
.. |vspace| raw:: latex

   \vspace{5mm}

.. _lab2:

******************************************************
Lab 2: Deformation and stress in anisotropic materials
******************************************************

.. toctree::
   :maxdepth: 2

The objective of this lab is to analyse large deformation kinematics and stress with respect to both fibre and reference coordinates in anisotropic materials. The deformations you will be analysing include:

  - Model 1 (Equibiaxial extension of unit cube, isotropic, 0 degree fibre rotation)
  - Model 2 (Equibiaxial extension of unit cube, orthotropic, 0 degree fibre rotation)
  - Model 3 (Equibiaxial extension of unit cube, isotropic, 30 degree fibre rotation)
  - Model 4 (Equibiaxial extension of unit cube, isotropic, 45 degree fibre rotation)
  - Model 5 (Equibiaxial extension of unit cube, orthotropic, 45 degree fibre rotation)
  - Model 6 (Equibiaxial extension of unit cube, orthotropic, 90 degree fibre rotation)

Before starting this lab, please complete :ref:`Lab 1: Deformation and stress in isotropic materials <lab1>` to familiarise yourself with stress and strain analysis techniques that will be used in this lab.

========================
Solving mechanics models
========================

1. Start OpenCMISS and load Lab2 (described in the :ref:`Starting OpenCMISS <starting-OpenCMISS>` section).

|vspace|

2. Select "Model 1 (Equibiaxial extension of unit cube)" from the drop down menu and click the "run" button (screenshots of this procedure are shown in the :ref:`Running models in OpenCMISS <running-models-in-OpenCMISS>` section).

|vspace|

3. After a short time, the model should have solved and the simulation results pane will open as shown in the screenshot below.

  .. image:: images/lab2_model1.png

  |vspace|

  The left side of the pane shows the stress and strain tensors associated with the simulation in fibre and reference coordinates. The simulation results are shown in the 3D graphics window on the right side of the pane. In this graphical window:

      - the undeformed (reference) configuration of the unit cube is shown in red, and
      - the deformed (current) configuration is shown in green (x, y, z components of the deformed coordinates are shown at the corners of the model).
      - **ignore the gold arrows for now - important later.**

  The model in the 3D graphics window can be rotated (click-drag-left-mouse button), translated (click-drag-middle-mouse button), or zoomed (click-drag-middle-mouse button).

|vspace|

==========================
Section 1: Strain analysis
==========================

4. This equibiaxial deformation is incompressible (i.e. maintains constant volume) described by the equations

  .. math::

    x_1 &= \frac{5}{4}X_1\\
    x_2 &= \frac{5}{4}X_2\\
    x_3 &= \frac{16}{25}X_3

|vspace|

5. Write down:

  - the deformation gradient tensor :math:`(\boldsymbol{F}=\frac{\partial\boldsymbol{x}}{\partial\boldsymbol{X}})`,
  - the right Cauchy-Green deformation tensor :math:`(\boldsymbol{C})`, and
  - Green-Lagrange strain tensor :math:`(\boldsymbol{E})` (label this :math:`\boldsymbol{E}_{ref}`).

  .. Note::

      This is the same deformation used in model 2 in Lab1, so you should not need to re-do these calculations.

6. Check your answers to 4 and 5 against the simulation results.

7. Analytically differentiate the Costa constitutive relation (shown below) with respect to the strain components :math:`(E_{ff})` and :math:`(E_{ss})`. Thus determine analytic expressions for the **distortional components** of the second Piola-Kirchhoff stress tensor.

  .. math::

    W_{I} = \frac{c_{1}}{2}(e^{Q}-1)

  where

  .. math::

    Q = & c_{ff}E^{2}_{ff} + \\
        & c_{ss}E^{2}_{ss} + \\ 
        & c_{nn}E^{2}_{nn} + \\
        & 2c_{fs}(\frac{1}{2}(E_{fs}+E_{sf}))^{2} + \\
        & 2c_{fn}(\frac{1}{2}(E_{fn}+E_{fn}))^{2} + \\ 
        & 2c_{ns}(\frac{1}{2}(E_{ns}+E_{ns}))^{2}

  .. Note::

      - Note the similarity of terms and derivatives.

      - No need to consider the shear terms, since there are no shear strains in the models considered in this lab.

|vspace|

==========================
Section 2: Stress analysis
==========================

Isotropic material properties
-----------------------------

1. The material parameters defined for model 1 are isotropic (equal in the 3 axial directions), i.e.

  .. math::

    c_{1} &= 0.0475 \\
    c_{ff} = c_{ss} = c_{nn} &= 15.25 \\
    c_{fs} = c_{fn} = c_{sn} &= 6.05

  Substitute the Green-Lagrange strain components :math:`(\boldsymbol{E})` from Section 1 into your analytic expression from step 7 to determine values for the **distortional components** of the second Piola-Kirchhoff stress tensor. Verify that these distortional stresses are:

  .. math::

    T^{ff\_dist} = T^{ss\_dist} = 8.590~kPa

  .. Note::

      - For this exercise :math:`Q=3.74`.

2. Determine the total stresses: :math:`T^{ff}` and :math:`T^{ss}` using equation 38 in `Nash and Hunter (2000) <http://link.springer.com/article/10.1023%2FA%3A1011084330767>`_. This requires determining the value for the **hydrostatic pressure**, :math:`p`, which is provided from the simulation results.

  .. Note::

      - :math:`C^{MN}` is not the same as :math:`C_{MN}`. They are inversely related: :math:`C^{MN}=\{C_{MN}\}^{-1}`.

      - It is easy to invert a diagonal tensor - check that :math:`C^{MN}C_{MN}=\boldsymbol{I}`.

3. Check your answers to 2 against the simulation results.

Anisotropic material properties
-------------------------------

4. Return to the model selection drop down menu by clicking Select View->Problem from the menu. Select and run model 2 (Equibiaxial extension of unit cube). This model and boundary conditions are similar to the previous model, except that the Costa relation parameters are now fully orthotropic:

  .. math::

    c_{1} &= 0.0475 \\
    c_{ff} &= 15.25
    c_{ss} &= 6.8
    c_{nn} &= 8.9 \\
    c_{fs} &= 6.95
    c_{fn} $= 6.05
    c_{sn} &= 4.93

  Determine the distortional second Piola-Kirchhoff stress components :math:`T^{ff\_dist}` and :math:`T^{ss\_dist}`.

5.  Determine the total stresses: :math:`T^{ff}` and :math:`T^{ss}`.

6. How have the total second Piola-Kirchhoff stress components changed compared with step 2. Why?

7. Now consider a model similar to model 2 

Questions
---------



Will the invariants be different between fibre and reference coordinates?
