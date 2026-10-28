# Outputs for GROMACS Set Up workflow

This workflow performs a simulation setup of a protein system, compatible with the GROMACS MD package.

Below there is a short description for all the **GROMACS Set Up** workflow outputs:

* **biobb.MDsetup.top.zip:** Replace solvent molecules with ions to neutralize the system.
* **biobb.MDsetup.tpr:** Portable binary run file to run a free MD simulation.
* **biobb.MDsetup.gro:** GRO for short free MD simulation.
* **biobb.MDsetup.cpt:** CPT for short free MD simulation.
* **biobb.MDsetup.xtc:** Imaged MD trajectory.
* **biobb.MDsetup.top.pdb:** Output dry structure.
* **biobb.MDsetup.energy.xvg:** Checking Energy Minimization results.
* **biobb.MDsetup.rgyr.xvg:** Radius of Gyration to measure the protein compactness during the free MD simulation .
* **biobb.MDsetup.rmsd_first.xvg:** RMSd against minimized and equilibrated snapshot (backbone atoms).
* **biobb.MDsetup.rmsd_exp.xvg:** RMSd against experimental structure (backbone atoms).
* **biobb.MDsetup.prod.tpr:** Portable binary run file to run a long MD (production) simulation.


For more information about this workflow, please visit the [workflows section](https://mmb.irbbarcelona.org/biobb-wfs/workflows#setup) in our website.
