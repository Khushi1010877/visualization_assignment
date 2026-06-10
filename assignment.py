# ====================================================
# IMPORT ALL REQUIRED LIBRARIES
# ====================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import plotly.graph_objects as go
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import LinearColorMapper, ColorBar
from bokeh.transform import transform

# If you are using Jupyter Notebook, uncomment the next line to display Bokeh plots inline
# output_notebook()

# ====================================================
# MATPLOTLIB ASSIGNMENT
# ====================================================

# Question 1: Using the given dataset, generate a 3D scatter plot to visualize the distribution of data points in a three-dimensional space.
np.random.seed(30)
data_3d = {
    'X': np.random.uniform(-10, 10, 300),
    'Y': np.random.uniform(-10, 10, 300),
    'Z': np.random.uniform(-10, 10, 300)
}
df_3d = pd.DataFrame(data_3d)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df_3d['X'], df_3d['Y'], df_3d['Z'], c='b', marker='o', alpha=0.6)
ax.set_title('3D Scatter Plot of Random Data Points')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# ====================================================
# SEABORN ASSIGNMENT
# ====================================================

# Question 2: Using the Student Grades, create a violin plot to display the distribution of scores across different grade categories.
np.random.seed(15)
data_grades = {
    'Grade': np.random.choice(['A', 'B', 'C', 'D', 'F'], 200),
    'Score': np.random.randint(50, 100, 200)
}
df_grades = pd.DataFrame(data_grades)

plt.figure(figsize=(8, 6))
sns.violinplot(x='Grade', y='Score', data=df_grades, order=['A', 'B', 'C', 'D', 'F'])
plt.title('Distribution of Scores across Grade Categories')
plt.show()

# Question 3: Using the sales data, generate a heatmap to visualize the variation in sales across different months and days.
np.random.seed(20)
data_sales = {
    'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
    'Day': np.random.choice(range(1, 31), 100),
    'Sales': np.random.randint(1000, 5000, 100)
}
df_sales = pd.DataFrame(data_sales)

# Pivot table: rows = Day, columns = Month, values = average Sales
pivot_sales = df_sales.pivot_table(index='Day', columns='Month', values='Sales', aggfunc='mean')

plt.figure(figsize=(8, 6))
sns.heatmap(pivot_sales, annot=True, fmt='.0f', cmap='YlOrRd', cbar_kws={'label': 'Avg Sales'})
plt.title('Average Sales Variation across Months and Days')
plt.show()

# ====================================================
# PLOTLY ASSIGNMENT
# ====================================================

# Question 4: Using the given x and y data, generate a 3D surface plot to visualize the function z = sin(sqrt(x^2 + y^2))
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

fig_surface = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis')])
fig_surface.update_layout(title='3D Surface Plot of sin(sqrt(x²+y²))',
                          scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))
fig_surface.show()

# Question 5: Using the given dataset, create a bubble chart to represent each country's population (y-axis), GDP (x-axis), and bubble size proportional to the population.
np.random.seed(25)
data_bubble = {
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
    'Population': np.random.randint(100, 1000, 5),
    'GDP': np.random.randint(500, 2000, 5)
}
df_bubble = pd.DataFrame(data_bubble)

fig_bubble = go.Figure()
fig_bubble.add_trace(go.Scatter(
    x=df_bubble['GDP'],
    y=df_bubble['Population'],
    mode='markers+text',
    marker=dict(size=df_bubble['Population'] / 10,   # scaled for visibility
                sizemode='area',
                sizeref=2.*max(df_bubble['Population'])/(40.**2),
                color=df_bubble['Population'],
                colorscale='Blues',
                showscale=True),
    text=df_bubble['Country'],
    textposition='top center'
))
fig_bubble.update_layout(title='Bubble Chart: GDP vs Population (size = Population)',
                         xaxis_title='GDP (arbitrary units)',
                         yaxis_title='Population (millions)')
fig_bubble.show()

# ====================================================
# BOKEH ASSIGNMENT
# ====================================================

# Question 1 (Bokeh): Create a Bokeh plot displaying a sine wave. Set x-values from 0 to 10 and y-values as the sine of x.
x_sine = np.linspace(0, 10, 200)
y_sine = np.sin(x_sine)

p_sine = figure(title='Sine Wave', x_axis_label='x', y_axis_label='sin(x)')
p_sine.line(x_sine, y_sine, line_width=2, color='blue')
show(p_sine)

# Question 2 (Bokeh): Create a Bokeh scatter plot using randomly generated x and y values. Use different sizes and colors for the markers based on the 'sizes' and 'colors' columns.
np.random.seed(42)   # for consistent random output
n = 100
x_rand = np.random.randn(n)
y_rand = np.random.randn(n)
sizes = np.random.randint(10, 50, n)
colors = np.random.choice(['red', 'green', 'blue', 'orange', 'purple'], n)

p_scatter = figure(title='Scatter Plot with Custom Sizes & Colors')
p_scatter.scatter(x_rand, y_rand, size=sizes, color=colors, alpha=0.6)
show(p_scatter)

# Question 3 (Bokeh): Generate a Bokeh bar chart representing the counts of different fruits.
fruits = ['Apples', 'Oranges', 'Bananas', 'Pears']
counts = [20, 25, 30, 35]

p_bar = figure(x_range=fruits, title='Fruit Counts', toolbar_location=None, tools='')
p_bar.vbar(x=fruits, top=counts, width=0.9, color='skyblue')
p_bar.xgrid.grid_line_color = None
p_bar.y_range.start = 0
show(p_bar)

# Question 4 (Bokeh): Create a Bokeh histogram to visualize the distribution of the given data.
data_hist = np.random.randn(1000)
hist, edges = np.histogram(data_hist, bins=30)

p_hist = figure(title='Histogram of Random Data', x_axis_label='Value', y_axis_label='Frequency')
p_hist.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color='navy', line_color='white', alpha=0.7)
show(p_hist)

# Question 5 (Bokeh): Create a Bokeh heatmap using the provided dataset.
data_heatmap = np.random.rand(10, 10)
x_heat = np.linspace(0, 1, 10)
y_heat = np.linspace(0, 1, 10)

# Prepare DataFrame for Bokeh rect heatmap
df_heat = pd.DataFrame(data_heatmap, index=y_heat, columns=x_heat).stack().reset_index()
df_heat.columns = ['y', 'x', 'value']

p_heat = figure(title='Heatmap', x_axis_label='X', y_axis_label='Y',
                x_range=(x_heat.min(), x_heat.max()), y_range=(x_heat.max(), x_heat.min()), toolbar_location=None)

mapper = LinearColorMapper(palette='Viridis256', low=df_heat['value'].min(), high=df_heat['value'].max())
p_heat.rect(x='x', y='y', width=0.9, height=0.9, source=df_heat,
            fill_color=transform('value', mapper), line_color=None)

color_bar = ColorBar(color_mapper=mapper, label_standoff=8, location=(0,0))
p_heat.add_layout(color_bar, 'right')
show(p_heat)