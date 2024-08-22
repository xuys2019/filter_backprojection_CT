import yaml

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    DecFanAng = config['geometry']['DecFanAng']
    ScanR = config['geometry']['ScanR']
    Radius = config['geometry']['Radius']
    Number = config['geometry']['Number']
    YL = config['geometry']['YL']
    return DecFanAng, ScanR, Radius, Number, YL

        
