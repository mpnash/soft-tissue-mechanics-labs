
.. |vspace| raw:: latex

   \vspace{5mm}

.. _lab3:

******************************************************
Lab 3: Deformation and stress in anisotropic materials
******************************************************

.. toctree::
   :maxdepth: 2

The objective of this lab is to analyse large deformation kinematics and stress in anisotropic materials. 

.. The deformations you will be analysing include:
..  - Model 2 (Equibiaxial extension of unit cube, orthotropic, 0 degree fibre rotation)
..  - Model 5 (Equibiaxial extension of unit cube, orthotropic, 45 degree fibre rotation)
..  - Model 6 (Equibiaxial extension of unit cube, orthotropic, 90 degree fibre rotation)

===================
Section 1: Revision
===================
Before starting this lab, please be sure to have completed :ref:`Lab 1: Deformation and stress in isotropic materials <lab1>` and :ref:`Lab 2: Transforming stresses and strains between different coordinate systems <lab2>` to familiarise yourself with stress and strain analysis techniques and the transformation of these quantities between fibre and reference coordinates, which will be used in this lab.

===================================================
Section 2: Deriving components of the stress tensor
===================================================

1. The Costa constitutive relation (shown below) will be used to describe the behaviour of the material considered in this lab. Analytically differentiate the Costa constitutive relation with respect to the strain components :math:`E_{ff}` and :math:`E_{ss}`. Thus determine analytic expressions for the **distortional components** of the second Piola-Kirchhoff stress tensor.

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

      - No need to consider the shear terms, since there are no shear strains in the biaxial deformations that will be considered in this lab.

|vspace|

2. Write down the expression for the total stresses: :math:`T^{ff}` and :math:`T^{ss}` (see `Nash and Hunter (2000) <http://link.springer.com/article/10.1023%2FA%3A1011084330767>`_).

|vspace|

===========================================
Section 3: Biaxial extension of a unit cube
===========================================

In this lab we will revisit the isotropic biaxial extension of a unit cube problem that was previously considered in :ref:`Section 3 of Lab2 <isotropic_biaxial_extension_of_unit_cube>`. Use the  Green-Lagrange strain tensor (:math:`\boldsymbol{E}`) that you previously derived in Step 5 of Section 3 in Lab 2 to answer the following questions.

Isotropic material properties with fibre axes aligned with the reference axes
-----------------------------------------------------------------------------

1. The isotropic material parameters defined for the isotropic biaxial extension of a unit cube problem are defined below:

  .. math::

    c_{1} &= 0.0475 \\
    c_{ff} = c_{ss} = c_{nn} &= c_{fs} = c_{fn} = c_{sn} = 15.25 \\

  Substitute the Green-Lagrange strain components (:math:`\boldsymbol{E}`) into your analytic expression from step 1 of Section 1 of this lab to determine values for the **distortional components** of the second Piola-Kirchhoff stress tensor. Verify that these distortional stresses are:

  .. math::

    T^{ff\_dist} = T^{ss\_dist} = 8.590~kPa

  .. Note::

      - For this exercise :math:`Q=3.74`.

|vspace|

2. Determine the total stresses: :math:`T^{ff}` and :math:`T^{ss}` using the equation you wrote down in Section 2. This requires determining the value for the **hydrostatic pressure**, :math:`p`, which is provided from the simulation results.

  .. Note::

      - :math:`C^{MN}` is not the same as :math:`C_{MN}`. They are inversely related: :math:`C^{MN}=\{C_{MN}\}^{-1}`.

      - It is easy to invert a diagonal tensor - check that :math:`C^{MN}C_{MN}=\boldsymbol{I}`.

|vspace|

3. Run Model 1 (Equibiaxial extension of unit cube, isotropic, 0 degree fibre rotation) from Lab2 in OpenCMISS and check your answers to Step 2 against the simulation results (the procedure for running the simulation in OpenCMISS was outlined in :ref:`steps 1:3 of Section 3 of Lab2 <isotropic_biaxial_extension_of_unit_cube>`).

|vspace|

Isotropic material properties with respect to rotated fibre axes
----------------------------------------------------------------

4. In Section 3 of Lab 2, you investigated how rotating the fibre axes with respect to reference axes influenced the values of the stress and strain tensors for an isotropic material undergoing a equibiaxial deformation. Summarise your results i.e.:
  - did the strain tensor change when the fibre axis was rotated? Why?
  - did the stress tensor change when the fibre axis was rotated? Why?

|vspace|

Orthotropic material properties with fibre axes aligned with the reference axes
-------------------------------------------------------------------------------

5. Now consider a similar model where the fibres align with the reference axes, except that now the Costa relation parameters are fully orthotropic:

  .. math::

    c_{1} &= 0.0475 \\
    c_{ff} &= 15.25 \\
    c_{ss} &= 6.8 \\
    c_{nn} &= 8.9 \\
    c_{fs} &= 6.95 \\
    c_{fn} &= 6.05 \\
    c_{sn} &= 4.93

  Determine the distortional second Piola-Kirchhoff stress components :math:`T^{ff\_dist}` and :math:`T^{ss\_dist}`.

|vspace|

6.  Determine the total stresses: :math:`T^{ff}` and :math:`T^{ss}`.

|vspace|

7. Run Model 1 (Equibiaxial extension of unit cube, orthotropic, 0 degree fibre rotation) from Lab2 in OpenCMISS and check your answers against the simulation results.

|vspace|

8. How have the total second Piola-Kirchhoff stress components changed compared with step 2. Why?

|vspace|

Orthotropic material properties with respect to rotated fibre axes
------------------------------------------------------------------

9. Now run Model 5 (Equibiaxial extension of unit cube, orthotropic, 45 degree fibre rotation). This is an othotropic material similar to that described in step 5 above, except that the fibre angle is changed from 0 to 45 degrees with respect to the :math:`x_{1}`-axis (in the :math:`x_{1}`-:math:`x_{2}` plane). 

|vspace|

10. Substitute the fibre strains (:math:`\boldsymbol{E}_{fib}`) from the simulation results and the othotropic Costa material constants from step 5 into your analytic stress expressions from Section 1 to determine the total second Piola-Kirchhoff stress components with respect to the fibre (material) coordinates (:math:`\boldsymbol{T}_{fib}`).

|vspace|

11. Determine the second Piola-Kirchhoff stress components with respect to the reference coordinate axes (:math:`\boldsymbol{T}_{ref}`) via an appropriate tensor transformation outlined in :ref:`step 3 of Section 2 of Lab2 <tensor_transformations>`. Check your answers against the simulation results.

|vspace|

12. How do the stress components of :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` compare to step 2. Explain similarities and differences.

|vspace|

13. Now run Model 6 (Equibiaxial extension of unit cube, orthotropic, 90 degree fibre rotation), where the fibre angle has been rotated 90 degrees with respect to the :math:`x_{1}`-axis (in the :math:`x_{1}`-:math:`x_{2}` plane). Repeat the analysis in steps 10-11.

|vspace|

14. How do the stress components of :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` compare to step 2. Explain similarities and differences.

|vspace|

====================
Section 4: Questions
====================

After you have completed the above exercises in Section 2 and Section 3, answer the following questions: 

b. What do you notice about the strain tensors, :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}`, in the above analysis for an isotropic or anisotropic material undergoing equibiaxial deformation?

a. Under what deformations would you expect these strain tensors be different?

|vspace|

.. note::

  By the end of this lab you should be able to:

    - derive components of the second Piola-Kirchhoff stress tensor.

    - evaluate the second Piola-Kirchhoff stress tensor with respect to spatial or material coordinates.


