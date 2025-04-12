import os

def rename_images():
    # Get the directory path
    image_dir = "images"
    
    # Get list of image files
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
    
    # Sort files to ensure consistent ordering
    image_files.sort()
    
    # Rename files
    for i, old_name in enumerate(image_files, 1):
        # Get file extension from original file
        file_ext = os.path.splitext(old_name)[1]
        # Create new name
        new_name = f"image{i}{file_ext}"
        
        # Full paths
        old_path = os.path.join(image_dir, old_name)
        new_path = os.path.join(image_dir, new_name)
        
        # Rename file
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")

if __name__ == "__main__":
    rename_images() 