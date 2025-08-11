import argparse
from config import *
from numpy_subjects import process_folders
from staging_preprocess import process_data


def main():

    print(f"Processing data for modalities: {modality} from {raw_file_path}...")
    process_data(modality, raw_file_path, output_data_path)
    
    print(f"Processing folders in {output_data_path}...")
    process_folders(output_data_path, modality)

    print("Data preprocessing completed successfully.")

if __name__ == '__main__':
    main()
