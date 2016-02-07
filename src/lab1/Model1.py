#!/usr/bin/env python
#> \file
#> \author Thiranja Babarenda Gamage
#> \brief 
#>
#> \section LICENSE
#>
#> Version: MPL 1.1/GPL 2.0/LGPL 2.1
#>
#> The contents of this file are subject to the Mozilla Public License
#> Version 1.1 (the "License"); you may not use this file except in
#> compliance with the License. You may obtain a copy of the License at
#> http://www.mozilla.org/MPL/
#>
#> Software distributed under the License is distributed on an "AS IS"
#> basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
#> License for the specific language governing rights and limitations
#> under the License.
#>
#> The Original Code is openCMISS
#>
#> The Initial Developer of the Original Code is University of Auckland,
#> Auckland, New Zealand and University of Oxford, Oxford, United
#> Kingdom. Portions created by the University of Auckland and University
#> of Oxford are Copyright (C) 2007 by the University of Auckland and
#> the University of Oxford. All Rights Reserved.
#>
#> Contributor(s): 
#>
#> Alternatively, the contents of this file may be used under the terms of
#> either the GNU General Public License Version 2 or later (the "GPL"), or
#> the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
#> in which case the provisions of the GPL or the LGPL are applicable instead
#> of those above. if you wish to allow use of your version of this file only
#> under the terms of either the GPL or the LGPL, and not to allow others to
#> use your version of this file under the terms of the MPL, indicate your
#> decision by deleting the provisions above and replace them with the notice
#> and other provisions required by the GPL or the LGPL. if you do not delete
#> the provisions above, a recipient may use your version of this file under
#> the terms of any one of the MPL, the GPL or the LGPL.
#>
#> Main script

import numpy

# Intialise OpenCMISS
from opencmiss.iron import iron

# Set problem parameters
width = 1.0
length = 1.0
height = 1.0

UsePressureBasis = False
NumberOfGaussXi = 2

coordinateSystemUserNumber = 1
regionUserNumber = 1
basisUserNumber = 1
pressureBasisUserNumber = 2
generatedMeshUserNumber = 1
meshUserNumber = 1
decompositionUserNumber = 1
geometricFieldUserNumber = 1
fibreFieldUserNumber = 2
materialFieldUserNumber = 3
dependentFieldUserNumber = 4
strainFieldUserNumber = 5
equationsSetFieldUserNumber = 6
equationsSetUserNumber = 1
problemUserNumber = 1

# Set all diganostic levels on for testing
#iron.DiagnosticsSetOn(iron.DiagnosticTypes.All,[1,2,3,4,5],"Diagnostics",["FINITE_ELASTICITY_GAUSS_CAUCHY_TENSOR"])

numberOfLoadIncrements = 1
numberGlobalXElements = 1
numberGlobalYElements = 1
numberGlobalZElements = 1
InterpolationType = 1
numberOfXi = 3

# Get the number of computational nodes and this computational node number
numberOfComputationalNodes = iron.ComputationalNumberOfNodesGet()
computationalNodeNumber = iron.ComputationalNodeNumberGet()

# Create a 3D rectangular cartesian coordinate system
coordinateSystem = iron.CoordinateSystem()
coordinateSystem.CreateStart(coordinateSystemUserNumber)
coordinateSystem.DimensionSet(3)
coordinateSystem.CreateFinish()

# Create a region and assign the coordinate system to the region
region = iron.Region()
region.CreateStart(regionUserNumber,iron.WorldRegion)
region.LabelSet("Region")
region.coordinateSystem = coordinateSystem
region.CreateFinish()

# Define basis
basis = iron.Basis()
basis.CreateStart(basisUserNumber)
if InterpolationType in (1,2,3,4):
    basis.type = iron.BasisTypes.LAGRANGE_HERMITE_TP
elif InterpolationType in (7,8,9):
    basis.type = iron.BasisTypes.SIMPLEX
basis.numberOfXi = numberOfXi
basis.interpolationXi = [iron.BasisInterpolationSpecifications.LINEAR_LAGRANGE]*numberOfXi
if(NumberOfGaussXi>0):
    basis.quadratureNumberOfGaussXi = [NumberOfGaussXi]*numberOfXi
basis.CreateFinish()

if(UsePressureBasis):
    # Define pressure basis
    pressureBasis = iron.Basis()
    pressureBasis.CreateStart(pressureBasisUserNumber)
    if InterpolationType in (1,2,3,4):
        pressureBasis.type = iron.BasisTypes.LAGRANGE_HERMITE_TP
    elif InterpolationType in (7,8,9):
        pressureBasis.type = iron.BasisTypes.SIMPLEX
    pressureBasis.numberOfXi = numberOfXi
    pressureBasis.interpolationXi = [iron.BasisInterpolationSpecifications.LINEAR_LAGRANGE]*numberOfXi
    if(NumberOfGaussXi>0):
        pressureBasis.quadratureNumberOfGaussXi = [NumberOfGaussXi]*numberOfXi
    pressureBasis.CreateFinish()

# Start the creation of a generated mesh in the region
generatedMesh = iron.GeneratedMesh()
generatedMesh.CreateStart(generatedMeshUserNumber,region)
generatedMesh.type = iron.GeneratedMeshTypes.REGULAR
if(UsePressureBasis):
    generatedMesh.basis = [basis,pressureBasis]
else:
    generatedMesh.basis = [basis]
    generatedMesh.extent = [width,length,height]
    generatedMesh.numberOfElements = [numberGlobalXElements,numberGlobalYElements,numberGlobalZElements]
# Finish the creation of a generated mesh in the region
mesh = iron.Mesh()
generatedMesh.CreateFinish(meshUserNumber,mesh)

# Create a decomposition for the mesh
decomposition = iron.Decomposition()
decomposition.CreateStart(decompositionUserNumber,mesh)
decomposition.type = iron.DecompositionTypes.CALCULATED
decomposition.numberOfDomains = numberOfComputationalNodes
decomposition.CreateFinish()

# Create a field for the geometry
geometricField = iron.Field()
geometricField.CreateStart(geometricFieldUserNumber,region)
geometricField.MeshDecompositionSet(decomposition)
geometricField.TypeSet(iron.FieldTypes.GEOMETRIC)
geometricField.VariableLabelSet(iron.FieldVariableTypes.U,"Geometry")
geometricField.ComponentMeshComponentSet(iron.FieldVariableTypes.U,1,1)
geometricField.ComponentMeshComponentSet(iron.FieldVariableTypes.U,2,1)
geometricField.ComponentMeshComponentSet(iron.FieldVariableTypes.U,3,1)
if InterpolationType == 4:
    geometricField.fieldScalingType = iron.FieldScalingTypes.ARITHMETIC_MEAN
geometricField.CreateFinish()

# Update the geometric field parameters from generated mesh
generatedMesh.GeometricParametersCalculate(geometricField)

# Create a fibre field and attach it to the geometric field
fibreField = iron.Field()
fibreField.CreateStart(fibreFieldUserNumber,region)
fibreField.TypeSet(iron.FieldTypes.FIBRE)
fibreField.MeshDecompositionSet(decomposition)
fibreField.GeometricFieldSet(geometricField)
fibreField.VariableLabelSet(iron.FieldVariableTypes.U,"Fibre")
if InterpolationType == 4:
    fibreField.fieldScalingType = iron.FieldScalingTypes.ARITHMETIC_MEAN
fibreField.CreateFinish()

# Create the equations_set
equationsSetField = iron.Field()
equationsSet = iron.EquationsSet()

problemSpecification = [iron.ProblemClasses.ELASTICITY,
    iron.ProblemTypes.FINITE_ELASTICITY,
    iron.ProblemSubtypes.NONE]
equationsSet.CreateStart(equationsSetUserNumber,region,fibreField,problemSpecification,
    equationsSetFieldUserNumber, equationsSetField)
equationsSet.CreateFinish()

# Create the dependent field
dependentField = iron.Field()
equationsSet.DependentCreateStart(dependentFieldUserNumber,dependentField)
dependentField.VariableLabelSet(iron.FieldVariableTypes.U,"Dependent")
dependentField.ComponentInterpolationSet(iron.FieldVariableTypes.U,4,iron.FieldInterpolationTypes.ELEMENT_BASED)
dependentField.ComponentInterpolationSet(iron.FieldVariableTypes.DELUDELN,4,iron.FieldInterpolationTypes.ELEMENT_BASED)
if(UsePressureBasis):
    # Set the pressure to be nodally based and use the second mesh component
    if InterpolationType == 4:
        dependentField.ComponentInterpolationSet(iron.FieldVariableTypes.U,4,iron.FieldInterpolationTypes.NODE_BASED)
        dependentField.ComponentInterpolationSet(iron.FieldVariableTypes.DELUDELN,4,iron.FieldInterpolationTypes.NODE_BASED)
    dependentField.ComponentMeshComponentSet(iron.FieldVariableTypes.U,4,2)
    dependentField.ComponentMeshComponentSet(iron.FieldVariableTypes.DELUDELN,4,2)
if InterpolationType == 4:
    dependentField.fieldScalingType = iron.FieldScalingTypes.ARITHMETIC_MEAN
equationsSet.DependentCreateFinish()

# Initialise dependent field from undeformed geometry and displacement bcs and set hydrostatic pressure
iron.Field.ParametersToFieldParametersComponentCopy(
    geometricField,iron.FieldVariableTypes.U,iron.FieldParameterSetTypes.VALUES,1,
    dependentField,iron.FieldVariableTypes.U,iron.FieldParameterSetTypes.VALUES,1)
iron.Field.ParametersToFieldParametersComponentCopy(
    geometricField,iron.FieldVariableTypes.U,iron.FieldParameterSetTypes.VALUES,2,
    dependentField,iron.FieldVariableTypes.U,iron.FieldParameterSetTypes.VALUES,2)
iron.Field.ParametersToFieldParametersComponentCopy(
    geometricField,iron.FieldVariableTypes.U,iron.FieldParameterSetTypes.VALUES,3,
    dependentField,iron.FieldVariableTypes.U,iron.FieldParameterSetTypes.VALUES,3)
iron.Field.ComponentValuesInitialiseDP(
    dependentField,iron.FieldVariableTypes.U,iron.FieldParameterSetTypes.VALUES,4,0.)

# Create the material field
materialField = iron.Field()
equationsSet.MaterialsCreateStart(materialFieldUserNumber,materialField)
materialField.VariableLabelSet(iron.FieldVariableTypes.U,"Material")
equationsSet.MaterialsCreateFinish()

# Set Mooney-Rivlin constants c10 and c01 respectively.
materialField.ComponentValuesInitialiseDP(
    iron.FieldVariableTypes.U,iron.FieldParameterSetTypes.VALUES,1,1.0)
materialField.ComponentValuesInitialiseDP(
    iron.FieldVariableTypes.U,iron.FieldParameterSetTypes.VALUES,2,0.2)

# Create a Guass point based field for calculated strain
strainField = iron.Field()
strainField.CreateStart(strainFieldUserNumber, region)
strainField.MeshDecompositionSet(decomposition)
strainField.TypeSet(iron.FieldTypes.GENERAL)
strainField.GeometricFieldSet(geometricField)
strainField.DependentTypeSet(iron.FieldDependentTypes.DEPENDENT)
strainField.VariableTypesSet([iron.FieldVariableTypes.U])
strainField.VariableLabelSet(iron.FieldVariableTypes.U, "Strain")
strainField.NumberOfComponentsSet(iron.FieldVariableTypes.U, 6)
for component in range(1, 7):
    strainField.ComponentInterpolationSet(
            iron.FieldVariableTypes.U, component,
            iron.FieldInterpolationTypes.GAUSS_POINT_BASED)
strainField.CreateFinish()

equationsSet.DerivedCreateStart(strainFieldUserNumber, strainField)
equationsSet.DerivedVariableSet(iron.EquationsSetDerivedTypes.STRAIN, iron.FieldVariableTypes.U)
equationsSet.DerivedCreateFinish()

# Create equations
equations = iron.Equations()
equationsSet.EquationsCreateStart(equations)
equations.sparsityType = iron.EquationsSparsityTypes.SPARSE
equations.outputType = iron.EquationsOutputTypes.NONE
equationsSet.EquationsCreateFinish()

# Define the problem
problem = iron.Problem()
problemSpecification = [iron.ProblemClasses.ELASTICITY,
        iron.ProblemTypes.FINITE_ELASTICITY,
        iron.ProblemSubtypes.NONE]
problem.CreateStart(problemUserNumber, problemSpecification)
problem.CreateFinish()

# Create the problem control loop
problem.ControlLoopCreateStart()
controlLoop = iron.ControlLoop()
problem.ControlLoopGet([iron.ControlLoopIdentifiers.NODE],controlLoop)
controlLoop.MaximumIterationsSet(numberOfLoadIncrements)
problem.ControlLoopCreateFinish()

# Create problem solver
nonLinearSolver = iron.Solver()
linearSolver = iron.Solver()
problem.SolversCreateStart()
problem.SolverGet([iron.ControlLoopIdentifiers.NODE],1,nonLinearSolver)
nonLinearSolver.outputType = iron.SolverOutputTypes.PROGRESS
nonLinearSolver.NewtonJacobianCalculationTypeSet(iron.JacobianCalculationTypes.EQUATIONS)
nonLinearSolver.NewtonLinearSolverGet(linearSolver)
linearSolver.linearType = iron.LinearSolverTypes.DIRECT
#linearSolver.libraryType = iron.SolverLibraries.LAPACK
problem.SolversCreateFinish()

# Create solver equations and add equations set to solver equations
solver = iron.Solver()
solverEquations = iron.SolverEquations()
problem.SolverEquationsCreateStart()
problem.SolverGet([iron.ControlLoopIdentifiers.NODE],1,solver)
solver.SolverEquationsGet(solverEquations)
solverEquations.sparsityType = iron.SolverEquationsSparsityTypes.SPARSE
equationsSetIndex = solverEquations.EquationsSetAdd(equationsSet)
problem.SolverEquationsCreateFinish()

# Prescribe boundary conditions (absolute nodal parameters)
boundaryConditions = iron.BoundaryConditions()
solverEquations.BoundaryConditionsCreateStart(boundaryConditions)
# Set x=0 nodes to no x displacment
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,1,iron.BoundaryConditionsTypes.FIXED,0.0)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,1,iron.BoundaryConditionsTypes.FIXED,0.0)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,1,iron.BoundaryConditionsTypes.FIXED,0.0)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,7,1,iron.BoundaryConditionsTypes.FIXED,0.0)

# Set x=1 nodes to x=1.5
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,1,iron.BoundaryConditionsTypes.FIXED,0.5)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,4,1,iron.BoundaryConditionsTypes.FIXED,0.5)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,1,iron.BoundaryConditionsTypes.FIXED,0.5)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,8,1,iron.BoundaryConditionsTypes.FIXED,0.5)

# Set y=0 nodes to no y displacement
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,2,iron.BoundaryConditionsTypes.FIXED,0.0)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,2,iron.BoundaryConditionsTypes.FIXED,0.0)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,2,iron.BoundaryConditionsTypes.FIXED,0.0)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,2,iron.BoundaryConditionsTypes.FIXED,0.0)

# Set z=0 nodes to no y displacement
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,3,iron.BoundaryConditionsTypes.FIXED,0.0)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,3,iron.BoundaryConditionsTypes.FIXED,0.0)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,3,iron.BoundaryConditionsTypes.FIXED,0.0)
boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,4,3,iron.BoundaryConditionsTypes.FIXED,0.0)
solverEquations.BoundaryConditionsCreateFinish()

# Solve the problem
problem.Solve()

# Export results
fields = iron.Fields()
fields.CreateRegion(region)
fields.NodesExport("cube","FORTRAN")
fields.ElementsExport("cube","FORTRAN")
fields.Finalise()

elementNumber = 1
xiPosition = [0., 0., 0.]
deformationGradientTensor = equationsSet.TensorInterpolateXi(
    iron.EquationsSetTensorEvaluateTypes.DEFORMATION_GRADIENT,
    elementNumber, xiPosition,(3,3))
print("Deformation Gradient Tensor")
print(deformationGradientTensor)

rightCauchyGreenDeformationTensor = equationsSet.TensorInterpolateXi(
    iron.EquationsSetTensorEvaluateTypes.R_CAUCHY_GREEN_DEFORMATION,
    elementNumber, xiPosition,(3,3))
print("Right Cauchy-Green Deformation Tensor")
print(rightCauchyGreenDeformationTensor)

I1=numpy.trace(rightCauchyGreenDeformationTensor)
I2=0.5*(numpy.trace(rightCauchyGreenDeformationTensor)**2.
        -numpy.tensordot(rightCauchyGreenDeformationTensor,
                rightCauchyGreenDeformationTensor))
I3=numpy.linalg.det(rightCauchyGreenDeformationTensor)
print("Invariants")
print("I1={0}, I2={1}, I3={2}".format(I1,I2,I3))

GreenLagrangeStrainTensor = equationsSet.TensorInterpolateXi(
    iron.EquationsSetTensorEvaluateTypes.GREEN_LAGRANGE_STRAIN,
    elementNumber, xiPosition,(3,3))
print("Green-Lagrange Strain Tensor")
print(GreenLagrangeStrainTensor)

CauchyStressTensor = equationsSet.TensorInterpolateXi(
    iron.EquationsSetTensorEvaluateTypes.CAUCHY_STRESS,
    elementNumber, xiPosition,(3,3))
print("Cauchy Stress Tensor")
print(CauchyStressTensor)

secondPiolaStressTensor = equationsSet.TensorInterpolateXi(
    iron.EquationsSetTensorEvaluateTypes.SECOND_PK_STRESS,
    elementNumber, xiPosition,(3,3))
print("Second Piola-Kirchhoff Stress Tensor")
print(secondPiolaStressTensor)



