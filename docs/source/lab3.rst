
.. |vspace| raw:: latex

   \vspace{5mm}

.. _lab2b:

***************************************************
Lab 2b: Analysing stresses in anisotropic materials
***************************************************

.. toctree::
   :maxdepth: 2

The objective of this lab is to analyse stresses in anisotropic materials.

===================
Section 1: Revision
===================
Before starting this lab, please be sure to have completed :ref:`Lab 1: Analysing deformation and stresses in isotropic materials <lab1>` and :ref:`Lab 2a: Transforming stresses and strains between different coordinate systems <lab2a>`.

.. to familiarise yourself with stress and strain analysis techniques and the transformation of these quantities between fibre and reference coordinates, which will be used in this lab.

In :ref:`Section 3 of Lab 2a <isotropic_biaxial_extension_of_unit_cube>`, you investigated how rotating the fibre axes with respect to reference axes influenced the values of the stress and strain tensors for an isotropic material undergoing a equibiaxial deformation. Summarise your results i.e.:

  - did the strain tensor change when the fibre axis was rotated? Why?
  - did the stress tensor change when the fibre axis was rotated? Why?

===================================================
Section 2: Deriving components of the stress tensor
===================================================

1. The exponential constitutive relation (shown below) will be used to describe the behaviour of the material considered in this lab. Analytically differentiate this relation with respect to the strain components :math:`E_{ff}` and :math:`E_{ss}`. Thus determine analytic expressions for the **distortional components** of the second Piola-Kirchhoff stress tensor.

  .. math::

    W_{I} = \frac{c_{1}}{2}(e^{Q}-1)

  where

  .. math::

    Q = & c_{ff}E^{2}_{ff} +
        & c_{ss}E^{2}_{ss} + 
        & c_{nn}E^{2}_{nn} + \\
        & 2c_{fs}(\frac{1}{2}(E_{fs}+E_{sf}))^{2} + 
        & 2c_{fn}(\frac{1}{2}(E_{fn}+E_{nf}))^{2} + 
        & 2c_{ns}(\frac{1}{2}(E_{ns}+E_{sn}))^{2}

  .. Note::

      - Note the similarity of terms and derivatives.

      - No need to consider the shear terms, since there are no shear strains in the biaxial deformations that will be considered in this lab.

|vspace|

2. Write down the expression for the total stresses: :math:`T^{ff}` and :math:`T^{ss}` (see Eqn 38 of `Nash and Hunter (2007) <https://canvas.auckland.ac.nz/courses/14750/files/27954/download?wrap=1>`_, or Eqn 15 of `Nash and Hunter (2000) <http://link.springer.com/article/10.1023%2FA%3A1011084330767>`_).

  .. Note::

      - :math:`C^{MN}` is not the same as :math:`C_{MN}`. They are inversely related: :math:`C^{MN}=\{C_{MN}\}^{-1}`.

      - It is easy to invert a diagonal tensor - check that :math:`C^{MN}C_{MN}=\boldsymbol{I}`.


|vspace|

==========================================================================
Section 3: Analysing stresses in a material undergoing biaxial deformation
==========================================================================

Stresses with respect to the reference axes
-------------------------------------------

3. Run Model 1 in OpenCMISS (the procedure for running the simulation in OpenCMISS was outlined in :ref:`steps 1:3 of Section 3 of Lab 2a <isotropic_biaxial_extension_of_unit_cube>`).

4. The material constants for this model are defined below:

  .. math::

    c_{1} &= 0.0475~kPa \\
    c_{ff} = c_{ss} = c_{nn} &= c_{fs} = c_{fn} = c_{ns} = 15.25 \\

  Substitute the Green-Lagrange strain components (:math:`\boldsymbol{E}_{ref}`) from the simulation results into your analytic expression from Step 1 of this lab to determine values for the **distortional components** of the second Piola-Kirchhoff stress tensor. Verify that these distortional stresses are:

  .. math::

    T_{ref}^{ff\_dist} = T_{ref}^{ss\_dist} = 8.590~kPa ~~~~ (\text{note}~Q=3.74)

|vspace|

5. Determine the total stresses: :math:`T_{ref}^{ff}` and :math:`T_{ref}^{ss}` using the equation you wrote down in Step 2. This requires determining the value for the **hydrostatic pressure**, :math:`p`, which is provided from the simulation results. Check your answers against the simulation results.

|vspace|

6. Based on the values of the total stresses, what can you infer about the structural properties of the material? Why? 

|vspace|

7. Now, run Model 2. This model is similar to model 1, except that the exponential material constants are now:

  .. math::

    c_{1} &= 0.0475~kPa\\
    c_{ff} &= 15.25 ~~~~
    c_{ss} &= 6.8 ~~~~
    c_{nn} &= 8.9 \\
    c_{fs} &= 6.95 ~~~~
    c_{fn} &= 6.05 ~~~~
    c_{ns} &= 4.93

  Determine the distortional second Piola-Kirchhoff stress components :math:`T_{ref}^{ff\_dist}` and :math:`T_{ref}^{ss\_dist}`.

|vspace|

8.  Determine the total stresses: :math:`T_{ref}^{ff}` and :math:`T_{ref}^{ss}` (use the **hydrostatic pressure** value, :math:`p`, from the simulation results). Check your answers against the simulation results.

|vspace|

9. How have the total second Piola-Kirchhoff stress components changed compared with Step 5. Why? Based on the values of the total stresses, what can you infer about the structural properties of the material?

|vspace|

Stresses with respect to rotated (material-fibre) axes
------------------------------------------------------

10. Now run Model 5. This model uses the same material constants as Model 2, except that the fibre angle has now changed from 0 to 45 degrees with respect to the :math:`x_{1}`-axis (in the :math:`x_{1}`-:math:`x_{2}` plane). 

|vspace|

11. Substitute the fibre strains (:math:`\boldsymbol{E}_{fib}`) from the simulation results and the exponential material constants from Step 7 into your analytic stress expressions from Section 1 to determine the total second Piola-Kirchhoff stress components with respect to the fibre (material) coordinates (:math:`\boldsymbol{T}_{fib}`) (use the **hydrostatic pressure** value, :math:`p`, from the simulation results).

|vspace|

12. Determine the second Piola-Kirchhoff stress components with respect to the reference coordinate axes (:math:`\boldsymbol{T}_{ref}`) via an appropriate tensor transformation outlined in :ref:`Step 3 of Section 2 of Lab 2a <tensor_transformations>`. Check your answers against the simulation results.

|vspace|

13. How do the stress components of :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` compare to Step 5. Explain similarities and differences.

|vspace|

14. Now run Model 6, where the fibre angle has been rotated 90 degrees with respect to the :math:`x_{1}`-axis (in the :math:`x_{1}`-:math:`x_{2}` plane). Repeat the analysis in Steps 11-12.

|vspace|

15. How do the stress components of :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` compare to Step 5. Explain similarities and differences.

|vspace|

.. ====================
.. Section 4: Questions
.. ====================

.. After you have completed the above exercises in Section 2 and Section 3, consider the following questions: 

.. a. What do you notice about the stress tensors, :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}`, in the above analysis for an isotropic or anisotropic material undergoing equibiaxial deformation? Why?

.. b. Under what deformations would you expect these stress tensors be different?

|vspace|

.. note::

  By the end of this lab you should be able to:

    - derive components of the second Piola-Kirchhoff stress tensor.

    - evaluate the second Piola-Kirchhoff stress tensor with respect to spatial or material coordinates.

