import sys
from pipeline.run import run

def main():
    config_path = sys.argv[1]
    run(config_path)
    
if __name__ == "__main__":
    main()