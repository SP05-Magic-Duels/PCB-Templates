import sys
import os
import shutil

# --- Configuration ---
PROJECT_PATH = "pcb-template-project/"
SOURCE_DIR = os.path.join(PROJECT_PATH, 'PCB-Imports') # The directory containing the source tables

# Target Paths (where the files will be overwritten)
FP_LIB_TABLE_PATH_TARGET = os.path.join(PROJECT_PATH, 'fp_lib_table') 
SYM_LIB_TABLE_PATH_TARGET = os.path.join(PROJECT_PATH, 'sym_lib_table')

# Source Paths (where the updated tables are located)
# Assuming the source files are named identically but are in the SOURCE_DIR
FP_LIB_TABLE_PATH_SOURCE = os.path.join(SOURCE_DIR, 'fp_lib_table')
SYM_LIB_TABLE_PATH_SOURCE = os.path.join(SOURCE_DIR, 'sym_lib_table')

def copy_library_table(source_path, target_path):
    """Copies (replaces) one library table file with another."""
    print(f"\n--- Processing {os.path.basename(target_path)} ---")
    
    if not os.path.exists(source_path):
        print(f"Error: Source file not found at {source_path}.", file=sys.stderr)
        return

    try:
        # Create the target directory if it doesn't exist (though it should for the tables)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        # Use shutil.copyfile to perform the overwrite
        shutil.copyfile(source_path, target_path)
        
        print(f"Successfully copied (overwrote) {os.path.basename(target_path)}.")
        print(f"Target path: {target_path}")

    except Exception as e:
        print(f"Failed to copy file {os.path.basename(target_path)}: {e}", file=sys.stderr)

# --- Main Execution ---

if __name__ == '__main__':
    # 1. Copy (Overwrite) the Footprint Library Table
    copy_library_table(
        FP_LIB_TABLE_PATH_SOURCE, 
        FP_LIB_TABLE_PATH_TARGET
    )

    # 2. Copy (Overwrite) the Symbol Library Table
    copy_library_table(
        SYM_LIB_TABLE_PATH_SOURCE, 
        SYM_LIB_TABLE_PATH_TARGET
    )

    print("\nAll KiCad library tables have been synced via file copy.")
