import os

def rename_videos_in_video_folder():
    # Specify the directory
    directory = 'video'
    
    # Check if the directory exists
    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return
    
    # List all video files in the directory (.mp4, .avi, .mov, etc.)
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv')  # Add more extensions if needed
    files = [f for f in os.listdir(directory) if f.lower().endswith(video_extensions)]
    
    # Sort files to maintain consistent order
    files.sort()

    # Rename each file
    for index, filename in enumerate(files, start=1):
        # Construct the new filename
        new_name = f"{index}.mp4"
        
        # Get the full path of the old and new file names
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {old_file} to {new_file}')

# Example usage
rename_videos_in_video_folder()
