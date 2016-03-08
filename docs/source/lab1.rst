
.. |vspace| raw:: latex

   \vspace{5mm}

*****************************
Lab 1: Deformation and Stress
*****************************

.. toctree::
   :maxdepth: 2


This lab aims to analyse large deformation kinematics with respect to material coordinates.
Before starting this lab, please read the :ref:`Using OpenCMISS <using-opencmiss>` section to familiarise yourself with the software used in this lab.

|vspace|

========================
Solving mechanics models
========================

1. Start Neon and load lab1 (described in the :ref:`Starting Neon <starting-neon>` section).

|vspace|

2. Select "Model 1 (uniaxial extension of a unit cube)" from the drop down menu and click the "run" button (screenshots of this procedure are shown in the :ref:`Running models in Neon <running-models-in-Neon>` section).

|vspace|

3. After a short time, the model should have solved and the simulation results pane wil open as shown in the screenshot below.

  .. image:: images/lab1_model1.png

  |vspace|

  The left side of the pane shows the stress and strain tensors associated with the simulation. The simulation results are shown in the 3D graphics window on the right side of the pane. In this graphical window:

      - the undeformed (reference) configuration of the unit cube is shown in red, and
      - the deformed (current) configuration is shown in green (x,y,z components of the deformed coordinates are shown at the corners of the model).

  The model in the 3D graphics window can be rotated (click-drag-left-mouse button), translated (click-drag-middle-mouse button), or zoomed (click-drag-middle-mouse button).

|vspace|

===============
Strain analysis
===============

4. Write down the coordinate equations that describe this deformation in the form :math:`x=f(X)`, e.g:

  .. math::

    x = 3X + 2Y + 4Z

    y = 5X - 4Y

    z = 2X + 3Y - 2Z

  .. Note::

      This is not the answer!

|vspace|

5. Determine the deformation gradient tensor :math:`(\boldsymbol{F}=dx/dX)`, and evaluate the determinant of :math:`\boldsymbol{F}` to see whether the deformation is incompressible (i.e. constant volume).

|vspace|

6. Determine:

  - right Cauchy-Green deformation tensor :math:`(\boldsymbol{C})`,
  - :math:`I1=trace(\boldsymbol{C})`,
  - :math:`I3=det(\boldsymbol{C})`, and the
  - Green-Lagrange strain tensor :math:`(\boldsymbol{E})`.

|vspace|

7. Check your answers to 5 and 6 against the simulation results.

  .. Note::

      Some of the numbers are not identically=0 due to Round-off error . Assume any number less than 1E-10=0.

|vspace|

8. Select View->Problem from the menu and repeat steps 2-7 for the remaining models in the lab:

    - Model 2 (Equibiaxial extention of a unit cube)
    - Model 3 (Simple shear of a unit cube)
    - Model 4 (Shear of a unit cube)
    - Model 5 (Extention and shear of a unit cube)

|vspace|


===============
Stress analysis
===============

9. Select "Model 1 (uniaxial extension of a unit cube)" from the drop down menu and click the "run" button.

|vspace|

10. Using the values of the 2nd Piola Kirchhoff tensor components :math:`(\boldsymbol{T})` and your :math:`(\boldsymbol{F})` tensor from step 5, determine the Cauchy components of stress :math:`(\Sigma)` (Don't forget the Jacobian :math:`(J)`)

|vspace|

11. Select View->Problem from the menu and repeat step 9 for the remaining models in the lab:
