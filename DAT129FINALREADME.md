# DAT129 Final Project SP21

## Sources

[National Weather Service](https://www.weather.gov/)

[National Weather Service API Web Service](https://www.weather.gov/documentation/services-web-api#)

Websites referenced:

[Matplotlib](https://matplotlib.org/stable/tutorials/introductory/lifecycle.html)

[Geeks For Geeks](https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/)

[Geeks For Geeks](https://www.geeksforgeeks.org/python-statistics-stdev/)

[Geeks For Geeks](https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/)

Final Project expanded from previous assignment:

[National Weather Forecast API Assignment](https://github.com/ianorourke/dat129_ccac/edit/main/API_README.md)

## About The Project

Expanding from the original assignment, this program allows the user to send requests to the API endpoint as provided
by https://www.weather.gov to receive active weather alerts either by individual state or territory or produce a JSON
that can be referenced containing all current active weather alerts at the time of the request. These can be saved into
.csv format and perform basic statistical analysis. Currently, this program can perform this with the data retrieved
from the time of request but hopefully, these requests can be saved over time for more larger analyses.

## Inquiry Question

The larger inquiry question is more about the information available and if additional information regarding the
alerts can be drawn conveniently beyond the severity, but additional information regarding the areas affected. That is,
is it possible to take the information from the active alerts to potentially build a larger body of data, perhaps a
database, where statistical information about the frequency of grades of severity over time could be gathered.

## About the Program

The program operates in a straightforward way with five options accessed through a simple menu system.

![Program Start](https://github.com/ianorourke/dat129_ccac/blob/main/final1.png)

The first option allows the user to enter a valid state or territory code to produce a list of current alerts.

![Individual State/Territory Alerts](https://github.com/ianorourke/dat129_ccac/blob/main/final2.png)

The second option allows the user to make a request for all active alerts within each state and territory. This
request retrieves a fair amount of information so it often takes a moment for the request to fully process. As a result, a prompt
has been placed for the user to prevent any accidental requests (as the JSON currently overwrites).
```
...
state_data_list = []
    # Loop to run through each state for alert data.
    for state in state_list:
        new_state = state.upper()
        alerter = alert_grabber(new_state)
        alert_specs = alerter['features']
        grab_bag = list_comprehender(alert_specs,'properties')
        state_data_list.append(grab_bag)
        ...
    with open('state_weather_data.json','w') as filer:
        json.dump(state_data_list,filer)
...
```

![All Current Active Alerts](https://github.com/ianorourke/dat129_ccac/blob/main/final3.png)

Once completed, a JSON is created (or overwritten with current data) the user is notified and the menu restarts.

![Completed Request](https://github.com/ianorourke/dat129_ccac/blob/main/final4.png)

The third option then takes the current JSON and arranges for the user the relevant data regarding the alerts provided.

![Looking at Current Data for All Active Alerts](https://github.com/ianorourke/dat129_ccac/blob/main/final5.png)

The fourth option allows for some basic statistical analysis.

![Analyzing Current Data](https://github.com/ianorourke/dat129_ccac/blob/main/final7.png)

Currently, this analysis is very simple but a potential future development would be to expand on this further.

The fifth option creates a .csv from the current data, arranged by categories of severity, effective time of date of alert,
and headline/area information regarding the nature of the alert. Currently, this overwrites with active date from each
request but a future development would be to append this for larger, more impacting analyses.

![Creating .csv from the Current Data](https://github.com/ianorourke/dat129_ccac/blob/main/final8.png)

And the sixth option ends the program.

![End Program Message](https://github.com/ianorourke/dat129_ccac/blob/main/final9.png)

## Issues and Potential Future Developments

Currently, the JSON and the .csv that the program produces focuses only on the data pulled from the time of request
but a potential future development would be to append requests so that alerts over time could be saved and gathered
for more meaningful statistical analysis. A primary issue that can arose was not being able to figure out how to
properly append the information retrived from each request so that analysis of alerts over larger amount of time could be
conducted. Average lengths of time regarding the alerts and by each grade of severity as well as including the areas affected
could be conducted once this issue is resolved.
