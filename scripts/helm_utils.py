import os
import subprocess
import yaml
from datetime import datetime

def package_chart(chart_dir):
    """
    Package a Helm chart directory
    """
    os.chdir(chart_dir)
    result = subprocess.run(['helm', 'package', '.'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error packaging chart: {result.stderr}")
        return None
    
    # Get the chart name and version from Chart.yaml
    with open(os.path.join(chart_dir, 'Chart.yaml')) as f:
        chart_info = yaml.safe_load(f)
    
    return f"{chart_info['name']}-{chart_info['version']}.tgz"

def update_index(chart_dir):
    """
    Update the Helm repository index
    """
    os.chdir(chart_dir)
    result = subprocess.run(['helm', 'repo', 'index', '.', '--merge', 'index.yaml'], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error updating index: {result.stderr}")
        return False
    
    print("Index updated successfully")
    return True

def package_and_index_charts():
    """
    Package all charts and update the index
    """
    charts_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    charts = [d for d in os.listdir(charts_dir) if os.path.isdir(os.path.join(charts_dir, d))]
    
    print(f"Processing charts in {charts_dir}")
    
    # Package each chart
    for chart in charts:
        chart_path = os.path.join(charts_dir, chart)
        if os.path.exists(os.path.join(chart_path, 'Chart.yaml')):
            print(f"\nPackaging chart: {chart}")
            package_result = package_chart(chart_path)
            if package_result:
                print(f"Successfully packaged: {package_result}")
    
    # Update index
    print("\nUpdating index.yaml...")
    update_index(charts_dir)

if __name__ == "__main__":
    package_and_index_charts()
