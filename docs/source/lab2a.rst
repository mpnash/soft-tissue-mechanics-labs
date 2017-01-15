
.. |vspace| raw:: latex

   \vspace{5mm}

.. _lab2a:

****************************************************************
Lab 2a: Transforming stresses from 2nd Piola-Kirchhoff to Cauchy
****************************************************************

.. toctree::
   :maxdepth: 2

The objective of this lab is to transform 2nd Piola-Kirchhoff stresses to Cauchy stresses. The deformations that will be considered in this lab include uniaxial and equi-biaxial extension of an isotropic unit cube.

=====================
Transforming stresses
=====================

1. Select "Model 1 (uniaxial extension of a unit cube)" from the drop down menu and click the "run" button.

|vspace|

2. Using the components of the 2nd Piola-Kirchhoff stress tensor :math:`(\boldsymbol{T})` and your deformation gradient tensor :math:`(\boldsymbol{F})` from step 5, determine the Cauchy components of the stress tensor :math:`(\boldsymbol{\Sigma})` (Don't forget the Jacobian :math:`(J)`).

|vspace|

3. Select View->Problem from the menu and repeat step 1-2 for the remaining models in the lab.

|vspace|

Questions
---------

After you have completed the above exercises, answer the following questions:

a. In model 1, why are :math:`\Sigma_{22}` and :math:`\Sigma_{33}` zero. How do they relate to the deformation seen in the graphical window?

|vspace|

b. In model 3, why is :math:`\Sigma_{33}` negative?

|vspace|

c. In model 3, why are the off-diagonal components of :math:`\boldsymbol{\Sigma}` nonzero?

|vspace|

.. note::

  By the end of section 2 you should be able to:

    - derive the Cauchy stress tensor from the second Piola-Kirchhoff stress tensor.

    - relate the components of the Cauchy stress tensor to the underlying deformation.

