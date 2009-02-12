"""This demo program demonstrates how to extract matching sub meshes
from a common mesh."""

__author__ = "Anders Logg (logg@simula.no)"
__date__ = "2009-02-11 -- 2009-02-09"
__copyright__ = "Copyright (C) 2009 Anders Logg"
__license__  = "GNU LGPL Version 2.1"

from dolfin import *

# Structure sub domain
class Structure(SubDomain):
    def inside(self, x, on_boundary):
        return x[0] > 1.4 - DOLFIN_EPS and x[0] < 1.6 + DOLFIN_EPS and x[1] < 0.6 + DOLFIN_EPS

# Create mesh
mesh = Rectangle(0.0, 0.0, 3.0, 1.0, 60, 20)
  
# Create sub domain markers and mark everaything as 0
sub_domains = MeshFunction("uint", mesh, mesh.topology().dim())
sub_domains.set_all(0)

# Mark structure domain as 1
structure = Structure()
structure.mark(sub_domains, 1)
  
# Extract sub meshes
fluid_mesh = SubMesh(mesh, sub_domains, 0)
structure_mesh = SubMesh(mesh, sub_domains, 1)
  
# Plot meshes
plot(fluid_mesh, title="Fluid")
plot(structure_mesh, title="Structure")
interactive()

# Not working, want a dictionary
global_vertex_indices = fluid_mesh.data().mapping("global vertex indices")
print global_vertex_indices
