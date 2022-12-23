# Tableau CheatSheet

## Why use Tableau?

While there are many reasons to use Tableau — here are our top 3 reasons:

- Easy to use—no coding involved
- Integrates seamlessly with any data source
- Fast and can handle large datasets

## Tableau Versions
There are two main versions of Tableau:

- Tableau Public: A free version of Tableau that lets you connect to limited data sources, create visualizations and dashboards, and publish dashboards online
- Tableau Desktop: A paid version of tableau which lets you connect to all types of data sources, allows you to save work locally, and has unlimited data sizes

## Getting started with Tableau
When working with Tableau, you will work with Workbooks. Workbooks contain sheets, dashboards, and stories. Similar to Microsoft Excel, a Workbook can contain multiple sheets. A sheet can be any of the following and can be accessed on the bottom left of a workbook.

- Worksheet: A worksheet is a single view in a workbook. You can add shelves, cards, legends, visualizations, and more to a worksheet
- Dashboard: A collection of multiple worksheets used to display multiple views simultaneously
- Story: A story is a collection of multiple dashboards and/or sheets that describe a data story
## The anatomy of a worksheet The sidebar

In the sidebar, you’ll find useful panes for working with data

- Data: The data pane on the left-hand side contains all of the fields in the currently selected data source
- Analytics: The analytics pane on the left-hand side lets you add useful insights like trend lines, error bars, and other useful summaries to visualizations

### Tableau data definitions
When working with data in Tableau, there are multiple definitions to be mindful of

- Fields: Fields are all of the different columns or values in a data source or that are calculated in the workbook. They show up in the data pane and can either be dimension or measure fields
- Dimensions: A dimension is a type of field that contains qualitative values (e.g. locations, names, and departments). Dimensions dictate the amount of granularity in visualizations and help reveal nuanced details in the data
- Measures: A measure is a type of field that contains quantitative values (e.g. revenue, costs, and market sizes). When dragged into a view, this data is aggregated, which is determined by the dimensions in the view
- Data types: Every field has a data type which is determined by the type of information it contains. The available data types in Tableau include text, date values, date & time values, numerical values, boolean values, geographical values, and cluster groups

### The canvas
The canvas is where you create your data visualizations

- Tableau Canvas: The canvas takes up most of the screen on Tableau and is where you can add visualizations
- Rows and columns: Rows and columns dictate how the data is displayed on the canvas. When dimensions are placed, they create headers for the rows or columns while measures add quantitative values
- Marks card: The marks card allows users to add visual details such as color, size, labels, etc. to rows and columns. This is done by dragging fields from the data pane into the marks card 


## How to Create a Data Vizualization

**Upload a dataset** 

- Launch Tableau
- In the Connect section, under To a File, press on the file format of your choice
- For selecting an Excel file, select .xlsx or .xlsx

**Creating your first visualization**

- Once your file is uploaded, open a Worksheet and click on the Data pane on the left-hand side
- Drag and drop at least one field into the Columns section, and one field into the Rows section at the top of the canvas
- To add more detail, drag and drop a dimension into the Marks card (e.g. drag a dimension over the color square in the marks card to color visualization components by that dimension)
- To a summary insight like a trendline, click on the Analytics pane and drag the trend line into your visualization
- You can change the type of visualization for your data by clicking on the Show Me button on the top right

## Data Visualization Types in Tableau
Tableau provides a wide range of data visualizations. Here is a list of the most useful visualizations you have in Tableau:

- Bar Charts: Horizontal bars used for comparing specific values across categories (e.g. sales by region)
- Stacked Bar Charts: Used to show categorical data within a bar chart (e.g., sales by region and department)
- Side by side chart: Used to compare values across categories in a bar chart format (e.g., sales by region comparing product types)
- Line Chart: Used for looking at a numeric value over time (e.g., revenue over time)
- Scatter Plot: Used to identify patterns between two continuous variables (e.g., profit vs. sales volume)
- Histogram: Used to show a distribution of data (e.g., Distribution of monthly revenue)
- Box-and-Whisper Plot: Used to compare distributions between categorical variables (e.g., distribution of revenue by region)
- Heat map: Used to visualize data in rows and columns as colors (e.g., revenue by marketing channel)
- Highlight table: Used to show data values with conditional color formatting (e.g., site traffic by marketing channel and year)
- Symbol Map: Used to show geographical data (e.g., Market size opportunity by state)
- Treemap: Used to show hierarchical data (e.g., Show how much revenue subdivisions generate relative to the whole department within an organization)
- Dual Combination: Used to show two visualizations within the same visualization (e.g., profit for a store each month as a bar chart with inventory over time as a line chart)


## How to Customize Visualizations in Tableau
Tableau provides a deep ability to filter, format, aggregate, customize, and highlight specific parts of your data visualizations

### Filtering data with highlights

- Once you’ve created a visual, click and drag your mouse over the specific portion you want to highlight
- Once you let go, you will have the option to Keep Only or Exclude the data
- Open the Data pane on the sidebar. Then, you can drag-and-drop a field into the filters card just to the left of the pane


### Filtering data with filters

- Open the Data pane on the left-hand side
- Drag-and-drop a field you want to filter on and add it to the Filters card
- Fill out in the modal how you would like your visuals to be filtered on the data

### Aggregating data

- Right-click on a measure field in the Data pane
- Go down to Default properties, Aggregation, and select the aggregation you would like to use 

### Changing colors

- Create a visualization by dragging fields into the Rows and Columns section at the top of the screen
- Drag dimensions into the Marks field, specifically into the Color square
- To change from the default colors, go to the upper-right corner of the color legend and select Edit Colors. This will bring up a dialog that allows you to select a different palette


### Changing fonts
- In the Format menu on the top ribbon, press on Select Workbook. This will replace the Data pane and allow you to make formatting decisions for the Workbook
- From here, select the font, font size, and color


## How to Create Dashboards in Tableau

- Launch Tableau
- In the Connect section under To A File, press on your desired file type
- Select your file
- Click the New Sheet at the bottom to create a new sheet
- Create a visualization in the sheet by following the steps in the previous sections of this cheat sheet
- Repeat steps 4 and 5 until you have created all the visualizations you want to include in your dashboard
- Click the New Dashboard at the bottom of the screen
- On the left-hand side, you will see all your created sheets. Drag sheets into the dashboard
- Adjust the layout of your sheets by dragging and dropping your visualizations


## How to Create Stories in Tableau
- Click the New Story at the bottom of the screen
- Change the size of the story to the desired size in the bottom left-hand corner of the screen under Size
- Edit the title of the story by renaming the story. To do this, right-click on the story sheet at the bottom and press Rename
- A story is made of story points, which lets you cycle through different visualizations and dashboards
- To begin adding to the story, add a story point from the left-hand side. You can add a blank story point
- To add a summary text to the story, click Add a caption and summarize the story point
- Add as many story points as you would like to finalize your data story
