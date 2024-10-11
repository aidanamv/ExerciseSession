from utils import *
import pyvista as pv

def main():
    # Load the object data from CSV
    object1_data, object2_data = read_csv("./data/tracking_data.csv")
    # Create a directory to store the frames
    frame_dir = "./frames"
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)
    # Load the STL files
    obj1 = pv.read("./data/vertebra.stl")
    obj2 = pv.read("./data/tool.stl")

    # Create a PyVista plotter
    plotter = pv.Plotter()

    # Add the meshes to the plotter
    plotter.add_mesh(obj1, color="red", show_edges=True)
    plotter.add_mesh(obj2, color="blue", show_edges=True)

    # Apply the first transformation
    obj1_initial_transformed = transform_mesh(obj1, object1_data.iloc[0])
    obj2_initial_transformed = transform_mesh(obj2, object2_data.iloc[0])
    # Extract camera parameters by visualizing and manually manipulating the view
    camera_position, camera_focal_point, camera_up, camera_view_angle = extract_camera_parameters(obj1_initial_transformed, obj2_initial_transformed)
    plotter.camera.position = camera_position
    plotter.camera.focal_point = camera_focal_point
    plotter.camera.view_angle = camera_view_angle
    plotter.camera.up = camera_up
    plotter.show(window_size=(1024, 1024), interactive_update=True)
    # Set the number of frames and start the animation loop
    num_frames = 1000
    # Task 5: Create animation loop
    for n in range(500, num_frames):
        # Step 1: Clear previous meshes and reload STL files

        # Step 2: Apply transformations for the current frame

        # Step 3: Add transformed meshes to the plotter

        # Step 4: Update the plot and save the frame as a PNG

    #GIF file creation
    create_gif(frame_dir, num_frames)


if __name__ == "__main__":
    main()
