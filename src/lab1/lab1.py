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

# Set constants
X, Y, Z = (1, 2, 3)

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
equationsSetFieldUserNumber = 5
equationsSetUserNumber = 1
problemUserNumber = 1

# Set all diganostic levels on for testing
#iron.DiagnosticsSetOn(iron.DiagnosticTypes.ALL,[1,2,3,4,5],"diagnostics.txt",[])

numberOfLoadIncrements = 1
numberGlobalXElements = 1
numberGlobalYElements = 1
numberGlobalZElements = 1
InterpolationType = 1
numberOfXi = 3

def solve_model(model=1):
    print("Solving model {0}".format(model))
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
        dependentField,iron.FieldVariableTypes.U,iron.FieldParameterSetTypes.VALUES,4,0.0)

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
    nonLinearSolver.NewtonJacobianCalculationTypeSet(
            iron.JacobianCalculationTypes.EQUATIONS)
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
    if model == 1:
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,7,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,X,iron.BoundaryConditionsTypes.FIXED,0.5)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,4,X,iron.BoundaryConditionsTypes.FIXED,0.5)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,X,iron.BoundaryConditionsTypes.FIXED,0.5)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,8,X,iron.BoundaryConditionsTypes.FIXED,0.5)

        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,Y,iron.BoundaryConditionsTypes.FIXED,0.0)

        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,4,Z,iron.BoundaryConditionsTypes.FIXED,0.0)

    elif model == 2:
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,7,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,X,iron.BoundaryConditionsTypes.FIXED,0.25)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,4,X,iron.BoundaryConditionsTypes.FIXED,0.25)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,X,iron.BoundaryConditionsTypes.FIXED,0.25)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,8,X,iron.BoundaryConditionsTypes.FIXED,0.25)

        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,Y,iron.BoundaryConditionsTypes.FIXED,0.25)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,4,Y,iron.BoundaryConditionsTypes.FIXED,0.25)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,7,Y,iron.BoundaryConditionsTypes.FIXED,0.25)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,8,Y,iron.BoundaryConditionsTypes.FIXED,0.25)


        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,4,Z,iron.BoundaryConditionsTypes.FIXED,0.0)

    elif model == 3:
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,X,iron.BoundaryConditionsTypes.FIXED,0.5)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,7,X,iron.BoundaryConditionsTypes.FIXED,0.5)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,4,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,X,iron.BoundaryConditionsTypes.FIXED,0.5)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,8,X,iron.BoundaryConditionsTypes.FIXED,0.5)

        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,Y,iron.BoundaryConditionsTypes.FIXED,0.0)

        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,4,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,7,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,8,Z,iron.BoundaryConditionsTypes.FIXED,0.0)

    elif model == 4:
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,X,iron.BoundaryConditionsTypes.FIXED,0.5)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,8,X,iron.BoundaryConditionsTypes.FIXED,0.5)

        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,Y,iron.BoundaryConditionsTypes.FIXED,0.0)

        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,Z,iron.BoundaryConditionsTypes.FIXED,0.5)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,8,Z,iron.BoundaryConditionsTypes.FIXED,0.5)

    elif model == 5:
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,X,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,X,iron.BoundaryConditionsTypes.FIXED,0.5)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,7,X,iron.BoundaryConditionsTypes.FIXED,0.5)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,X,iron.BoundaryConditionsTypes.FIXED,0.25)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,4,X,iron.BoundaryConditionsTypes.FIXED,0.25)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,X,iron.BoundaryConditionsTypes.FIXED,0.75)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,8,X,iron.BoundaryConditionsTypes.FIXED,0.75)

        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,Y,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,Y,iron.BoundaryConditionsTypes.FIXED,0.0)

        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,1,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,2,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,3,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,4,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,5,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,6,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,7,Z,iron.BoundaryConditionsTypes.FIXED,0.0)
        boundaryConditions.AddNode(dependentField,iron.FieldVariableTypes.U,1,1,8,Z,iron.BoundaryConditionsTypes.FIXED,0.0)

    solverEquations.BoundaryConditionsCreateFinish()

    # Solve the problem
    problem.Solve()

    # Export results
    fields = iron.Fields()
    fields.CreateRegion(region)
    fields.NodesExport("model{0}".format(model),"FORTRAN")
    fields.ElementsExport("model{0}".format(model),"FORTRAN")
    fields.Finalise()

    elementNumber = 1
    xiPosition = [0.5, 0.5, 0.5]
    F = equationsSet.TensorInterpolateXi(
        iron.EquationsSetTensorEvaluateTypes.DEFORMATION_GRADIENT,
        elementNumber, xiPosition,(3,3))
    print("Deformation Gradient Tensor")
    print(F)

    C = equationsSet.TensorInterpolateXi(
        iron.EquationsSetTensorEvaluateTypes.R_CAUCHY_GREEN_DEFORMATION,
        elementNumber, xiPosition,(3,3))
    print("Right Cauchy-Green Deformation Tensor")
    print(C)

    E = equationsSet.TensorInterpolateXi(
        iron.EquationsSetTensorEvaluateTypes.GREEN_LAGRANGE_STRAIN,
        elementNumber, xiPosition,(3,3))
    print("Green-Lagrange Strain Tensor")
    print(E)

    I1=numpy.trace(C)
    I2=0.5*(numpy.trace(C)**2.-numpy.tensordot(C,C))
    I3=numpy.linalg.det(C)
    print("Invariants")
    print("I1={0}, I2={1}, I3={2}".format(I1,I2,I3))

    TC = equationsSet.TensorInterpolateXi(
        iron.EquationsSetTensorEvaluateTypes.CAUCHY_STRESS,
        elementNumber, xiPosition,(3,3))
    print("Cauchy Stress Tensor")
    print(TC)

    # Output of Second Piola-Kirchhoff Stress Tensor not implemented. It is
    # instead, calculated from TG=J*F^(-1)*TC*F^(-T), where T indicates the
    # transpose fo the matrix.
    #TG = equationsSet.TensorInterpolateXi(
    #    iron.EquationsSetTensorEvaluateTypes.SECOND_PK_STRESS,
    #    elementNumber, xiPosition,(3,3))
    J=1. #Assumes J=1
    TG = numpy.dot(numpy.linalg.inv(F),numpy.dot(
            TC,numpy.linalg.inv(numpy.matrix.transpose(F))))
    print("Second Piola-Kirchhoff Stress Tensor")
    print(TG)

    # Note that the hydrostatic pressure value is different from the value quoted
    # in the original lab instructions. This is because the stress has been
    # evaluated using modified invariants (isochoric invariants)
    p = dependentField.ParameterSetGetElement(
        iron.FieldVariableTypes.U,
        iron.FieldParameterSetTypes.VALUES,elementNumber,4)
    print("Hydrostatic pressure")
    print(p)
    
    problem.Destroy()


if __name__ == "__main__":

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
    basis.interpolationXi = (
        [iron.BasisInterpolationSpecifications.LINEAR_LAGRANGE]*numberOfXi)
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
        pressureBasis.interpolationXi = (
            [iron.BasisInterpolationSpecifications.LINEAR_LAGRANGE]*numberOfXi)
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
        generatedMesh.numberOfElements = (
            [numberGlobalXElements,numberGlobalYElements,numberGlobalZElements])
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
        iron.EquationsSetSubtypes.MOONEY_RIVLIN]
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

    # Create equations
    equations = iron.Equations()
    equationsSet.EquationsCreateStart(equations)
    equations.sparsityType = iron.EquationsSparsityTypes.SPARSE
    equations.outputType = iron.EquationsOutputTypes.NONE
    equationsSet.EquationsCreateFinish()

    solve_model(model=1)
    solve_model(model=2)
    solve_model(model=3)
    solve_model(model=4)
    solve_model(model=5)

