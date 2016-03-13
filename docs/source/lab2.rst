
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

2. Select "Model 1 (Equibiaxial extension of unit cube, isotropic, 0 degree fibre rotation)" from the drop down menu and click the "run" button (screenshots of this procedure are shown in the :ref:`Running models in OpenCMISS <running-models-in-OpenCMISS>` section).

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

  - the deformation gradient tensor (:math:`\boldsymbol{F}=\frac{\partial\boldsymbol{x}}{\partial\boldsymbol{X}}`),
  - the right Cauchy-Green deformation tensor (:math:`\boldsymbol{C}`), and
  - Green-Lagrange strain tensor (:math:`\boldsymbol{E}`) (label this :math:`\boldsymbol{E}_{ref}`).

  .. Note::

      This is the same deformation used in model 2 in Lab1, so you should not need to re-do these calculations.

6. Check your answers to 4 and 5 against the simulation results.

|vspace|

==========================
Section 2: Stress analysis
==========================

1. Analytically differentiate the Costa constitutive relation (shown below) with respect to the strain components :math:`E_{ff}` and :math:`E_{ss}`. Thus determine analytic expressions for the **distortional components** of the second Piola-Kirchhoff stress tensor.

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

Isotropic material properties with fibre axes aligned with the reference axes
-----------------------------------------------------------------------------

2. The material parameters defined for model 1 are isotropic (equal in the 3 axial directions), i.e.

  .. math::

    c_{1} &= 0.0475 \\
    c_{ff} = c_{ss} = c_{nn} &= 15.25 \\
    c_{fs} = c_{fn} = c_{sn} &= 6.05

  Substitute the Green-Lagrange strain components (:math:`\boldsymbol{E}`) from Section 1 into your analytic expression from step 1 to determine values for the **distortional components** of the second Piola-Kirchhoff stress tensor. Verify that these distortional stresses are:

  .. math::

    T^{ff\_dist} = T^{ss\_dist} = 8.590~kPa

  .. Note::

      - For this exercise :math:`Q=3.74`.

|vspace|

3. Determine the total stresses: :math:`T^{ff}` and :math:`T^{ss}` using equation 38 in `Nash and Hunter (2000) <http://link.springer.com/article/10.1023%2FA%3A1011084330767>`_. This requires determining the value for the **hydrostatic pressure**, :math:`p`, which is provided from the simulation results.

  .. Note::

      - :math:`C^{MN}` is not the same as :math:`C_{MN}`. They are inversely related: :math:`C^{MN}=\{C_{MN}\}^{-1}`.

      - It is easy to invert a diagonal tensor - check that :math:`C^{MN}C_{MN}=\boldsymbol{I}`.

|vspace|

4. Check your answers to 3 against the simulation results.

|vspace|

Orthotropic material properties with fibre axes aligned with the reference axes
-------------------------------------------------------------------------------

5. Return to the model selection drop down menu by clicking Select View->Problem from the menu. Select and run model 2 (Equibiaxial extension of unit cube). This model and its boundary conditions are similar to the previous model, except that the Costa relation parameters are now fully orthotropic:

  .. math::

    c_{1} &= 0.0475 \\
    c_{ff} &= 15.25
    c_{ss} &= 6.8
    c_{nn} &= 8.9 \\
    c_{fs} &= 6.95
    c_{fn} $= 6.05
    c_{sn} &= 4.93

  Determine the distortional second Piola-Kirchhoff stress components :math:`T^{ff\_dist}` and :math:`T^{ss\_dist}`.

|vspace|

6.  Determine the total stresses: :math:`T^{ff}` and :math:`T^{ss}`.

|vspace|

7. How have the total second Piola-Kirchhoff stress components changed compared with step 3. Why?

|vspace|


Isotropic material properties with rotated fibre axes
-----------------------------------------------------

8. Return to the model selection drop down menu and select and run model 3 (Equibiaxial extension of unit cube, isotropic, 30 degree fibre rotation). This model is similar to the previous models, except that the fibre (material) axes are no longer aligned with the reference axes. They are now rotated anticlockwise by an angle of :math:`\theta=30` degrees from the :math:`x_{1}` axis (in the :math:`x_{1}`-:math:`x_{2}` plane). When visualising the model, the gold arrows in the graphics window indicate the direction of the fibre axis (along which the first material coordinate is defined), and the :math:`x_{1}`-:math:`x_{2}` plane indicates the orientation of the flat laminar sheet.

|vspace|

9. Determine the Green-Lagrange strain tensor components with respect to the fibre axes (:math:`\boldsymbol{E}_{fib}`) using the tensor transformation:

  .. math::

    \boldsymbol{E}_{fib} = \boldsymbol{Q}^{T} \boldsymbol{E}_{ref} \boldsymbol{Q}

  where :math:`\boldsymbol{E}_{ref}` is the Green-Lagrange strain tensor with respect to the reference axes which were calculated in step 5 of section 1, and :math:`\boldsymbol{Q}` is the orthogonal rotation matrix:

  .. math::

      \boldsymbol{Q} = 
      \begin{bmatrix}
        \cos(\theta) & -\sin(\theta) & 0  \\
        \sin(\theta) &  \cos(\theta) & 0  \\
        0              &  0              & 1
      \end{bmatrix}

|vspace|

10. Check your answers to 9 against the simulation results.

|vspace|

11. Explain similarities/differences between :math:`\boldsymbol{E}_{fib}` and :math:`\boldsymbol{E}_{ref}` for this model.

|vspace|

12. Substitute your fibre strains (:math:`\boldsymbol{E}_{fib}`) from step 9 and the isotropic Costa material constants from step 2 into your analytic stress expressions from step 1 to determine the total second Piola-Kirchhoff stress components with respect to the fibre (material) coordinates (:math:`\boldsymbol{T}_{fib}`). 

|vspace|

13. Transform the second Piola-Kirchhoff stress tensor (:math:`\boldsymbol{T}_{fib}`) from step 12  using:

  .. math::

    \boldsymbol{T}_{ref} = \boldsymbol{Q}^{T} \boldsymbol{T}_{fib} \boldsymbol{Q}

  to determine the second Piola-Kirchhoff stress components with respect to the reference coordinate axes.

|vspace|

14. Check your answers to 13 against the simulation results.

|vspace|

15. Explain similarities/differences between :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` for this model.

|vspace|

16. What would you expect from the analysis in steps 8-15 if the fibre angle was changed from 30 to 45 degrees for this isotropic model?  What do you notice about the stress tensors :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` for this isotropic model subject to the equibiaxial deformation? Explain.

  .. note::

   You should not need to solve the model to answer this questions, but if you need the extra practice, apply steps 8-15 to model 4 (Equibiaxial extension of unit cube, isotropic, 45 degree fibre rotation).

|vspace|

Orthotropic material properties with rotated fibre axes
-------------------------------------------------------

17. Now run model 5. This is an othotropic similar to that described in step 5 above, except that the fibre angle is changed from 0 to 45 degrees with respect to the :math:`x_{1}`-axis (in the :math:`x_{1}`-:math:`x_{2}` plane). Repeat the analysis in steps 8-15.

|vspace|

18. How do the stress components of :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` compare to step 7.  Explain similarities and differences.

|vspace|

19. Now run model 6. This is an othotropic similar to that described in step 5 above, except that the fibre angle is changed from 0 to 90 degrees with respect to the :math:`x_{1}`-axis (in the :math:`x_{1}`-:math:`x_{2}` plane). Repeat the analysis in steps 8-15.

|vspace|

20. How do the stress components of :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` compare to step 7.  Explain similarities and differences.

|vspace|

Questions
---------

After you have completed the above exercises, answer the following questions: 

a. Will the invariants of :math:`\boldsymbol{C}` be different when calculated with respect to fibre or reference coordinates?

|vspace|

.. note::

  By the end of this lab you should be able to:

    - compare and contrast spatial versus material coordinates.

    - analyse large deformation kinematics with respect to reference or material coordinates.

    - define stress tensors with respect to spatial or material coordinates.

