import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import plotly.express as px
import plotly.io as pio

import markdown

import argparse

# Read data from CSV file
data = pd.read_csv('data.csv')

# Extract columns
sports = data['sport']
objectivity = data['objectivity']
physical_exertion = data['physical_exertion']
mental_exertion = data['mental_exertion']

# Create a new figure for plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
scatter = ax.scatter(objectivity, physical_exertion, mental_exertion, c='r', marker='o')

# Labels
ax.set_xlabel('Objectivity')
ax.set_ylabel('Physical Exertion')
ax.set_zlabel('Mental Exertion')

# Title
ax.set_title('3D Scatter Plot of Sports')

# Annotate each point with its sport name
for i, sport in enumerate(sports):
    ax.text(objectivity[i], physical_exertion[i], mental_exertion[i], sport)


def render_plot_html(data, outfile="index.html"):
    # Extract columns
    fig = px.scatter_3d(
        data,
        x='objectivity',
        y='physical_exertion',
        z='mental_exertion',
        text='sport',
        title='3D Scatter Plot of Sports',
        labels={'objectivity': 'Objectivity', 'physical_exertion': 'Physical Exertion', 'mental_exertion': 'Mental Exertion'}
    )

    # Save interactive plot to HTML
    pio.write_html(fig, file=outfile, auto_open=False)

# Function to extract specific parts of the README
def extract_parts(content, start_marker, end_marker):
    start_index = content.find(start_marker)
    end_index = content.find(end_marker, start_index)
    if start_index != -1 and end_index != -1:
        return content[start_index:end_index]
    return ""

# Function to remove specific parts of the README
def remove_parts(content, start_marker, end_marker):
    start_index = content.find(start_marker)
    end_index = content.find(end_marker, start_index)
    if start_index != -1 and end_index != -1:
        return content[:start_index] + content[end_index+len(end_marker):]
    return ""

def build_html_page():

    # Define markers for the parts you want to extract
    start_marker = "# Introduction"
    end_marker = "# Installation"

    # Extract the desired part
    extracted_content = extract_parts(readme_content, start_marker, end_marker)

    # Convert extracted part to HTML
    html_content = markdown.markdown(extracted_content)

    # Save to an HTML file
    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot 3D scatter plot of sports data.')
    parser.add_argument('--html', action='store_true', help='whether to build an html file for deployment')
    args = parser.parse_args()

    if args.html:
        # Save interactive plot to HTML
        render_plot_html(data)

        # build page around the plot data
        # Read the README file
        with open('README.md', 'r', encoding='utf-8') as file:
            readme_content = file.read()
    else:
        # Show plot
        plt.show()



