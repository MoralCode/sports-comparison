import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import plotly.express as px
import plotly.io as pio

import markdown
from pathlib import Path

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
    end_index = content.find(end_marker, max(start_index, 0))
    if start_index != -1 and end_index != -1:
        return content[start_index:end_index]
    elif start_index == -1 and end_index != -1:
        return content[:end_index]
    elif start_index != -1 and end_index == -1:
        return content[start_index:]
    return ""

# Function to remove specific parts of the README
def remove_parts(content, start_marker, end_marker):
    start_index = content.find(start_marker)
    end_index = content.find(end_marker, start_index)
    if start_index != -1 and end_index != -1:
        return content[:start_index] + content[end_index+len(end_marker):]
    return ""

def create_markdown_tag(identifier="NONEXISTENT"):
    """converts a tag name into a literal string to search for in the markdown to separate certain blocks
    """
    return f"<!-- tag:{identifier} -->"


def build_html_page(readme_file="README.md"):
    # build page around the plot data
    # Read the README file

    readme_content = Path(readme_file).read_text()

    # Extract the intro
    extracted_intro = extract_parts(
        readme_content,
        create_markdown_tag(),
        create_markdown_tag("END_INTRO")
    )

    # remove the image from that intro
    extracted_intro = remove_parts(
        extracted_intro,
        create_markdown_tag("BEGIN_IMAGE"),
        create_markdown_tag("END_IMAGE")
    )

    # Extract the scoring section
    extracted_scoring = extract_parts(
        readme_content,
        create_markdown_tag("END_INTRO"),
        create_markdown_tag("END_SCORING")
    )

    intro_html = markdown.markdown(extracted_intro)

    plot_embed = '<iframe src="./3dplot.html"></iframe>'
    scoring_html = markdown.markdown(extracted_scoring)


    # Convert extracted part to HTML
    html_content = intro_html + plot_embed + scoring_html

    # Save to an HTML file
    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot 3D scatter plot of sports data.')
    parser.add_argument('--html', action='store_true', help='whether to build an html file for deployment')
    args = parser.parse_args()

    if args.html:
        # Save interactive plot to HTML
        render_plot_html(data, outfile="3dplot.html")
        build_html_page()
        
    else:
        # Show plot
        plt.show()



