# Pico & Placa predictor
## Description:
This code was developed in python in the 3.8 version. It helps to identify if a plate in a limited time and date can circulate or not. To aim, this objective was used three libraries, pandas, datetime, and argparse. The first two were used to manage the date and time. On the other hand, argparse was used to manage the input variables.

## Steps for execution:
Predict if a plate is on pico&placa can be achieved with the following command:
    ```bash
    python pico_y_placa.py --plate <PLATE> --date <DATE> --time <TIME>
    ```
with the following list of potiential arguments:

* --plate: Plate with the format -> SKM-1234
* --date: Date with the format -> mont-day-year Ex:08-29-2021 
* --time: Time with the format -> hour:minutes:seconds Ex:08:47:00. Note: the minutes and seconds are extrectly necessary, if those elements are uncertain put only 0's (Ex-> 08:00:00).

