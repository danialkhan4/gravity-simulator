### Gravity Simulator
Python-based gravity simulator that accurately models gravitational interactions within a 2D solar
system relative to the sun and can query any exoplanet in the NASA Exoplanet Arhive. 


![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3l5c25wNTc4MG1qanN1aHZobnNia3JtOWY0czVvZXFrZGRiNmFtbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vyhl9z7rMVjISKiylM/giphy.gif)


### Build Instructions
```bash
cd gravity-simulator
pip3 install -r requirements.txt
python3 main.py
```

### How to add exoplanets:
Open `exoplanets.txt` and list the exoplanets you want to query (one per line), if it exists and its data is available, it will will be loaded into the program.

Run the program normally with `python3 main.py` and use the key displayed on screen to select the planet.

Find exoplanets here:
https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS







