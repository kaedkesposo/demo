import yaml
import sys
from pipeline.config import validate_config
from pipeline.stages.districting import districting
from pipeline.stages.settings_generator import settings_generator
from pipeline.stages.profile_generator import profile_generator
from pipeline.stages.run_experiments import run_experiments
from pipeline.stages.export import export

def run(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    # validate config schema
    validate_config(config)
    districting(config)
    settings_generator(config)
    profile_generator(config)
    run_experiments(config)
    export(config)

