
.. |vspace| raw:: latex

   \vspace{5mm}

.. _lab2:

*****************************************************************
Lab 2: Relating stress and strain in different coordinate systems
*****************************************************************

.. toctree::
   :maxdepth: 2

The objective of this lab is to analyse large deformation kinematics and stress with respect to both fibre and reference coordinates in isotropic materials. The deformations you will be analysing include equibiaxial extension and uniaxial extension.

Before starting this lab, please complete :ref:`Lab 1: Deformation and stress in isotropic materials <lab1>` to familiarise yourself with stress and strain analysis techniques that will be used in this lab.

===========================================
Section 1: Biaxial extension of a unit cube
===========================================

1. Start OpenCMISS and load Lab2 (described in the :ref:`Starting OpenCMISS <starting-OpenCMISS>` section).

|vspace|

2. Select "Model 1 (Equibiaxial extension of unit cube, isotropic, 0 degree fibre rotation)" from the drop down menu and click the "run" button (screenshots of this procedure are shown in the :ref:`Running models in OpenCMISS <running-models-in-OpenCMISS>` section).

|vspace|

3. After a short time, the model should have solved and the simulation results pane will open as shown in the screenshot below.

  .. image:: images/lab2_model1.png

  |vspace|

  The left side of the pane shows the stress and strain tensors associated with the simulation in fibre and reference coordinates. The simulation results are shown in the 3D graphics window on the right side of the pane. In this graphical window:

      - the undeformed (reference) configuration of the unit cube is shown in red, and
      - the deformed (current) configuration is shown in green (:math:`x_{1}`, :math:`x_{2}`, :math:`x_{3}` components of the deformed coordinates are shown at the corners of the model, (note that in the graphical window, these components are labelled x, y, and z, respectively).
      - **ignore the gold arrows for now - important later.**

  The model in the 3D graphics window can be rotated (click-drag-left-mouse button), translated (click-drag-middle-mouse button), or zoomed (click-drag-middle-mouse button).

|vspace|


4. This equibiaxial deformation is incompressible (i.e. maintains constant volume) described by the equations:

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

|vspace|


Isotropic material properties with rotated fibre axes
-----------------------------------------------------

6. Return to the model selection drop down menu and select and run model 3 (Equibiaxial extension of unit cube, isotropic, 30 degree fibre rotation). This model is similar to the previous models, except that the fibre (material) axes are no longer aligned with the reference axes. They are now rotated anticlockwise by an angle of :math:`\theta=30` degrees from the :math:`x_{1}` axis (in the :math:`x_{1}`-:math:`x_{2}` plane). When visualising the model, the gold arrows in the graphics window indicate the direction of the fibre axis (along which the first material coordinate is defined), and the :math:`x_{1}`-:math:`x_{2}` plane indicates the orientation of the flat laminar sheet.

|vspace|

7. Determine the Green-Lagrange strain tensor components with respect to the fibre axes (:math:`\boldsymbol{E}_{fib}`) by selecting and using an appropriate tensor transformation from the two options listed below:

  .. math::

    \boldsymbol{E}_{fib} = \boldsymbol{Q}^{T} \boldsymbol{E}_{ref} \boldsymbol{Q}~(option~1)

    \boldsymbol{E}_{fib} =  \boldsymbol{Q} \boldsymbol{E}_{ref} \boldsymbol{Q}^{T}~(option~2)

  where :math:`\boldsymbol{E}_{ref}` is the Green-Lagrange strain tensor with respect to the reference axes that is shown in the simulation results, and :math:`\boldsymbol{Q}` is the orthogonal rotation matrix:

  .. math::

      \boldsymbol{Q} = 
      \begin{bmatrix}
        \cos(\theta) & -\sin(\theta) & 0  \\
        \sin(\theta) &  \cos(\theta) & 0  \\
        0              &  0              & 1
      \end{bmatrix}

|vspace|

8. Check your answers to 7 against the simulation results.

|vspace|

9. Explain similarities/differences between :math:`\boldsymbol{E}_{fib}` and :math:`\boldsymbol{E}_{ref}` for this model.

|vspace|

10. Determine the second Piola-Kirchhoff stress components with respect to the reference coordinate axes (:math:`\boldsymbol{T}_{ref}`) by selecting and using an appropriate tensor transformation from the two options listed below:

  .. math::

    \boldsymbol{T}_{ref} = \boldsymbol{Q}^{T} \boldsymbol{T}_{fib} \boldsymbol{Q}~(option~1)

    \boldsymbol{T}_{ref} =  \boldsymbol{Q} \boldsymbol{T}_{fib} \boldsymbol{Q}^{T}~(option~2)

  where :math:`\boldsymbol{T}_{fib}` is the second Piola-Kirchhoff stress tensor with respect to the fibre axes that is shown in the simulation results, and :math:`\boldsymbol{Q}` is the orthogonal rotation matrix defined in step 7.

|vspace|

11. Check your answers to 10 against the simulation results.

|vspace|

12. Explain similarities/differences between :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` for this model.

|vspace|

13. What would you expect from the analysis in steps 7-12 if the fibre angle was changed from 30 degrees to 45 degrees or 90 degrees for this isotropic model?  What do you notice about the stress tensors :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` for this isotropic model subject to the equibiaxial deformation? Explain.

  .. note::

    You should not need to do any calculations to answer this questions, but if you need the extra practice, perform steps 7-12 with :math:`\theta=45` degrees, and/or :math:`\theta=90` degrees.

|vspace|

============================================
Section 2: Uniaxial extension of a unit cube
============================================

1. Consider the uniaxial deformation shown in the figure below, where the fibre (material) axes are aligned with the reference axes (:math:`\theta=0` degrees):

  .. image:: images/uniaxial_0_degrees_fibres.png

  |vspace|

  This deformation is described by the following equations:

  .. math::

    x_1 &= \frac{3}{2}X_1\\
    x_2 &= \sqrt{\frac{2}{3}}X_2\\
    x_3 &= \sqrt{\frac{2}{3}}X_3

|vspace|

2. Write down:

  - the deformation gradient tensor (:math:`\boldsymbol{F}=\frac{\partial\boldsymbol{x}}{\partial\boldsymbol{X}}`),
  - the right Cauchy-Green deformation tensor (:math:`\boldsymbol{C}`), and
  - Green-Lagrange strain tensor (:math:`\boldsymbol{E}`) (label this :math:`\boldsymbol{E}_{ref}`).

  .. Note::

      This is the same deformation used in model 1 in Lab1, so you should not need to re-do these calculations.

      For this model, the second Piola-Kirchhoff stress tensor with respect to both the reference and fibre axes is:

      .. math::

        \boldsymbol{T_{ref}} = \boldsymbol{T_{fib}} = 
        \begin{bmatrix}
          440.5  & 0       & 0 \\
          0      & 0       & 0 \\
          0      & 0       & 0
        \end{bmatrix}

|vspace|

Isotropic material properties with rotated fibre axes
-----------------------------------------------------

3. Now consider the same deformation, except that the fibre (material) axes are no longer aligned with the reference axes. They are now rotated anticlockwise by an angle of :math:`\theta=30` degrees from the :math:`x_{1}` axis (in the :math:`x_{1}`-:math:`x_{2}` plane), as shown in the figure below.

  .. image:: images/uniaxial_30_degrees_fibres.png

|vspace|

4. Determine the Green-Lagrange strain tensor components with respect to the fibre axes (:math:`\boldsymbol{E}_{fib}`) by selecting and using an appropriate tensor transformation from the two options listed below:

  .. math::

    \boldsymbol{E}_{fib} = \boldsymbol{Q}^{T} \boldsymbol{E}_{ref} \boldsymbol{Q}~(option~1)

    \boldsymbol{E}_{fib} =  \boldsymbol{Q} \boldsymbol{E}_{ref} \boldsymbol{Q}^{T}~(option~2)

  where :math:`\boldsymbol{E}_{ref}` is the Green-Lagrange strain tensor with respect to the reference axes that you derived in step 2, and :math:`\boldsymbol{Q}` is the orthogonal rotation matrix defined in step 7 of Section 1.

|vspace|

5. Explain similarities/differences between :math:`\boldsymbol{E}_{fib}` and :math:`\boldsymbol{E}_{ref}` for this model.

|vspace|

6. Determine the second Piola-Kirchhoff stress components with respect to the reference coordinate axes (:math:`\boldsymbol{T}_{ref}`) by selecting and using an appropriate tensor transformation from the two options listed below:

  .. math::

    \boldsymbol{T}_{ref} = \boldsymbol{Q}^{T} \boldsymbol{T}_{fib} \boldsymbol{Q}~(option~1)

    \boldsymbol{T}_{ref} =  \boldsymbol{Q} \boldsymbol{T}_{fib} \boldsymbol{Q}^{T}~(option~2)

  where :math:`\boldsymbol{Q}` is the orthogonal rotation matrix defined in step 7 of Section 1. and :math:`\boldsymbol{T}_{fib}` is the second Piola-Kirchhoff stress tensor with respect to the fibre axes defined below:

  .. math::

    \boldsymbol{T_{fib}} = 
    \begin{bmatrix}
      38.01   & -6.404  & 0 \\
      -6.404  & 12.67   & 0 \\
      0       & 0       & 0
    \end{bmatrix}

|vspace|

7. Explain similarities/differences between :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` for this model.

|vspace|


8. What would you expect from the analysis in steps 7-13 if the fibre angle was changed from 30 degrees to 45 degrees or 90 degrees for this isotropic model?  What do you notice about the stress tensors :math:`\boldsymbol{T}_{fib}` and :math:`\boldsymbol{T}_{ref}` for this isotropic model subject to the uniaxial deformation? Explain.

  .. note::

    You should not need to do any calculations to answer this questions, but if you need the extra practice, perform steps 4-7 with:

    :math:`\theta=45` degrees, where the second Piola-Kirchhoff stress tensor with respect to the fibre axes is:

      .. math::

        \boldsymbol{T_{fib}} = 
        \begin{bmatrix}
          12.33   & -3.597  & 0 \\
          -3.597  & 12.33   & 0 \\
          0       & 0       & 0
        \end{bmatrix}

    and/or :math:`\theta=90` degrees, where the second Piola-Kirchhoff stress tensor with respect to the fibre axes is:

      .. math::

        \boldsymbol{T_{fib}} = 
        \begin{bmatrix}
          0      & 0       & 0 \\
          0      & 440.5   & 0 \\
          0      & 0       & 0
        \end{bmatrix}

|vspace|

====================
Section 3: Questions
====================

After you have completed the above exercises in section 1 and section 2, answer the following questions: 

a. How do changes in :math:`\boldsymbol{E}_{ref}` for different fibre angles (:math:`\theta`) in the biaxial deformation compare with the changes seen in the uniaxial deformation.

b. How do changes in :math:`\boldsymbol{E}_{fib}` for different fibre angles (:math:`\theta`) in the biaxial deformation compare with the changes seen in the uniaxial deformation.

c. How do changes in :math:`\boldsymbol{T}_{ref}` for different fibre angles (:math:`\theta`) in the biaxial deformation compare with the changes seen in the uniaxial deformation.

d. How do changes in :math:`\boldsymbol{T}_{fib}` for different fibre angles (:math:`\theta`) in the biaxial deformation compare with the changes seen in the uniaxial deformation.

e. Will the invariants of :math:`\boldsymbol{C}` be different when calculated with respect to fibre or reference coordinates?

|vspace|

.. note::

  By the end of this lab you should be able to:

    - analyse large deformation kinematics with respect to reference or material coordinates for isotropic materials.

    - analyse stress tensors with respect to spatial or material coordinates for isotropic materials.


See this :ref:`link <lab2_section1_solutions>` and this :ref:`link <lab2_section2_solutions>` for the solutions to step 13 of Section 1 and step 8 of Section 2, respectively.

