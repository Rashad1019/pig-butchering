import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

def create_composite_dashboard():
    # Define the input image paths
    images = {
        'primary': 'primary_financial_flow_sankey.png',
        'regional': 'regional_flow_sankey.png',
        'crypto': 'crypto_conversion_network.png',
        'temporal': 'temporal_pattern_analysis.png'
    }
    
    # Create figure with 2x2 grid
    fig, axes = plt.subplots(2, 2, figsize=(20, 20))
    
    # Load and display each image in its respective position
    for (title, path), ax in zip(images.items(), axes.flat):
        # Read image
        img = mpimg.imread(path)
        
        # Display image
        ax.imshow(img)
        ax.set_title(title.replace('_', ' ').title(), pad=20, fontsize=14)
        
        # Remove axes
        ax.axis('off')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the composite image
    output_path = 'financial_flow_composite.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return output_path

if __name__ == "__main__":
    output_file = create_composite_dashboard()
    print(f"Created composite dashboard: {output_file}")