def validate_config(config):
    if len(config["num_districts"]) != len(config["num_winners"]):
        raise ValueError(
            "num_districts and num_winners must have the same length"
        )
    



