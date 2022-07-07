# Bindings using C++ and Eigen:
import sys
import os
try:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../build/')))
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../build-linux/')))
    from gpytoolbox_eigen_bindings import mesh_union
    from gpytoolbox_eigen_bindings import mesh_difference
    from gpytoolbox_eigen_bindings import mesh_intersection
    from gpytoolbox_eigen_bindings import upper_envelope
    from gpytoolbox_eigen_bindings import ray_mesh_intersect
    from gpytoolbox_eigen_bindings import in_element_aabb
    from gpytoolbox_eigen_bindings import remove_duplicate_vertices
    from gpytoolbox_eigen_bindings import decimate
    from .lazy_cage import lazy_cage
except:
    print("-------------------------------------------------------------------")
    print("WARNING: You are using only the pure-python gpytoolbox functionality. Some functions will be unavailable. \n See https://github.com/sgsellan/gpytoolbox for full installation instructions.")
    print("-------------------------------------------------------------------")

# Things that do not need my bindings
# These functions require igl official bindings (and they shouldn't)
from .linear_elasticity_stiffness import linear_elasticity_stiffness
from .linear_elasticity import linear_elasticity

# This function depends on skimage and imageio (should it?)
from .png2poly import png2poly

# These functions depend ONLY on numpy and scipy and each other
from .edge_indeces import edge_indeces
from .regular_square_mesh import regular_square_mesh
from .regular_cube_mesh import regular_cube_mesh
from .signed_distance_polygon import signed_distance_polygon
from .metropolis_hastings import metropolis_hastings
from .ray_polyline_intersect import ray_polyline_intersect
from .poisson_surface_reconstruction import poisson_surface_reconstruction
from .fd_interpolate import fd_interpolate
from .fd_grad import fd_grad
from .fd_partial_derivative import fd_partial_derivative
from .random_points_on_polyline import random_points_on_polyline
from .normalize_points import normalize_points
from .write_ply import write_ply
from .initialize_quadtree import initialize_quadtree
from .subdivide_quad import subdivide_quad
from .in_quadtree import in_quadtree
from .quadtree_gradient import quadtree_gradient
from .quadtree_laplacian import quadtree_laplacian
from .quadtree_boundary import quadtree_boundary
from .bad_quad_mesh_from_quadtree import bad_quad_mesh_from_quadtree