# Wildfire Wizards
## FPA-FOD-Plus Data Mapping Website

### Contributers
- Parker Balbach
- Sawyer Ball
- Ethan Raygor
- [Fires Wild Team](https://cs481-ekh.github.io/f22-fires-wild/)


## Abstract

Our goal for our project was to make the overall experience better in terms of performance, visualization, and user experience. The site had issues with data not being displayed correctly, a very obvious performance issue when there are too many items pulled in a query, and other issues. Our goal was to have these issues resolved.

The wildfire website will be available on all browsers. A user will be able to filter data based on the variables provided on the left side of the map. Once the user filters the page, data points will appear on the map. The radius of each data point will indicate the size of the wildfire. Clicking on a specific point will display basic information to the user. The user will be able to click “additional details” in order to view more in depth information about the specific wildfire. A user will have the ability to download the complete data set in csv format or download a subset of the data based on the filters they apply to the map.

## Description

We are using Docker containers to house each different component of the site. We are using three containers. Our frontend, backend, and database are hosted on them. The data is loading after the site is built, so the site can have data ready to read once the user loads the site. We have one page that visualizes the data. 

We do not allow the user to place all of the data in our database on the map due to performance issues that the user will experience when the map displays over 10,000 nodes in our point overlay. On the left are many different variables that the user can filter the map on. 

<img width="1792" alt="Screen Shot 2022-11-29 at 10 28 31 AM" src="https://user-images.githubusercontent.com/51347468/204600151-3487e1dd-c615-4230-8d43-ab5ded4214bc.png">

After the user filters the page, by default, the points overlay will be displayed on the map. An example is shown below. As an example we have filtered the data to fires in the state of Idaho in 2016. The radius of each point indicates the size of the fire. Users can click on each point to get some information on the fire, such as it's FOD and FPA IDs, along with the name the fire was given. Users can click on additional details to view much more data on the fire. 

<img width="1792" alt="Screen Shot 2022-11-29 at 10 39 04 AM" src="https://user-images.githubusercontent.com/51347468/204602788-b05b30f9-41c8-4fea-97fb-f6229dafd8f5.png">

The user can view fire data by using a heatmap. Which shows where there are a large amount, or large fires on the map. This view is localized, and will update as the user zooms in and out of the map. Below is an example using fires from California in 2016. 

<img width="1792" alt="Screen Shot 2022-11-29 at 10 43 50 AM" src="https://user-images.githubusercontent.com/51347468/204603929-904c1e11-f8ff-4e4d-9d96-42aa03d6a905.png">

When a user had filtered the data they want displayed on the map. They can download the data as a csv file, where they will get all of the data points that are available in the FPA-FOD-Plus dataset. Site admins can use the Django admin portal to add and modify data in the database. 

