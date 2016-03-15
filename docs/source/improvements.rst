.. _improvements:

************
Improvements
************

.. toctree::
   :maxdepth: 2

=======================
Short term improvements
=======================

Change after 321 course finishes

- Set the default view to be the model selection pane (problem viewer)
- Initialise the problem type string in the simulation results pane (currently defaults to "None" and can only be changed if the user runs a model other than model 1)
- In the problem view, replace the string "parameters" with "Model selection", and remove the text "boundary condition"
- Move 3D model window to left of the simulation results pane, and the tensors etc to the right of the pane.
- Allow the tensors etc  in the simulation results pane to be hidden.
- Change axes in the 3D model window from x,y,z to x1,x2,x3 

======================
Long term improvements
======================

For next year:

Lab 1
-----

- allow the user to either:

  - specify the deformation gradient and dynamically udpate the simulation results

  - solve a model with a specific set of boundary conditions (eg. uniaxial/shear) i.e. a partially kinematically constrainted model. Then allow the user to pull on a node/face and dynamically solve for the unconstrained dofs such that resulting deformation is incompressible.


Lab 2
-----

- take the stress analysis out of lab 1 and make that the start of lab 2, as a warm exercise.

- allow two independent models with the same boundary conditions to be solved and viewed simultaneously with a vertical split screen in the simulation results window. Make the model on the left and right side of the screen isotropic and anisotropic, respectively. Add a slider to change the fibre angle and dynamically update the simulation results to help highlight which deformation/stress tensors change and which do not. Link the cameras in the two graphical windows to simplify visualisation.

==============================
Cool but would they be useful?
==============================

  - perturb the nodes of the model and dynamically update the tensors describing the deformation (this needs to be a fully kinematically constrained model). Simplify the space of possible purturbations by allowing motion only on a 3D grid of points which align with the x, y, and z axes. This will allow the user to recreate different modes of deformation e.g. extension shear etc (note that the deformation may not be homogeneous, and in such cases the tensors describing the deformation would be different for different material points within the element).


