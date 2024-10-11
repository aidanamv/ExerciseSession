import imageio
import os
import pandas as pd
import pyvista as pv
import numpy as np
def read_csv(csv_file_path):
    """
    Task 1: Read the CSV file and extract data for the specified objects.

    Parameters:
        csv_file_path (str): Path to the CSV file.

    Returns:
        DataFrame: Data for object 1 and object 2.
    """
    # Step 1: Read the CSV file into a DataFrame

    # Step 2:Extract data for both objects based on their indices

    return object1_data, object2_data


def transform_mesh(mesh, transformation_matrix):
    """
    Task 2: Extract the rotation and translation from pandas series.
    Apply a transformation matrix to a mesh.

    Parameters:
        mesh (pyvista.PolyData): The mesh to transform.
        transformation_matrix (pandas.Series): The transformation matrix as a pandas Series.

    Returns:
        pyvista.PolyData: The transformed mesh.
    """
    # Step 1: Initialize a 4x4 identity matrix

    # Step 2: Extract position (translation) from the Series (assumed to be in indices 2, 3, and 4)

    # Step 3: Extract rotation matrix from the Series (assumed to be in indices 5 to 13 and reshape to 3x3)

    # Step 4: Fill the transformation matrix with position and rotation data


    # Step 5: Apply the transformation to the mesh

    return transformed_mesh

def extract_camera_parameters(obj1, obj2):
    """
        Task 3: Extract camera parameters based on two objects.

        Parameters:
            obj1 (pyvista.PolyData): Transformed object 1.
            obj2 (pyvista.PolyData): Transformed object 2.

        Returns:
            tuple: Camera position, focal point, up direction, and view angle.
        """
    # Step 1: Initialize a PyVista plotter and add the meshes to it



    # Step 2: Show the plot


    # Step 3: Extract camera parameters


    return camera_position, focal_point, up_direction, view_angle


def create_gif(frame_dir,num_frames):
    """
        Task 4: Create a GIF from saved frames and save it.

        Parameters:
            frame_dir (str): Directory where the frames are saved.
            num_frames (int): The number of frames to include in the GIF.

        Returns:
            None
        """
    # Step 1: Use `imageio` to write a GIF from saved frames
