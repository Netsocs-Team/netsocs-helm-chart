import sys
import os
import re

def update_version_in_file(file_path, new_version):
    try:
        # Read the file
        with open(file_path, 'r') as file:
            content = file.read()
            
        # Update main version (only if it's at the top level)
        pattern = r'^(version: )([^\"]+)$'  # Matches version at the start of a line
        content = re.sub(pattern, f'\\g<1>{new_version}', content, flags=re.MULTILINE)
        
        # Update appVersion
        pattern = r'^(appVersion: \")([^"]+)\"$'  # Matches appVersion at the start of a line
        content = re.sub(pattern, f'\\g<1>{new_version}\"', content, flags=re.MULTILINE)
        
        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(content)
            
        print(f"Successfully updated version in {os.path.basename(file_path)} to {new_version}")
        
    except Exception as e:
        print(f"Error updating {os.path.basename(file_path)}: {str(e)}")
        sys.exit(1)

def update_all_versions(new_version):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Update Chart.yaml
    chart_path = os.path.join(script_dir, '../Chart.yaml')
    update_version_in_file(chart_path, new_version)
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python set-app-version.py <new-version>")
        sys.exit(1)
        
    new_version = sys.argv[1]
    update_all_versions(new_version)