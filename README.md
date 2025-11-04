# PCB-Templates
Creates basic template for PCB projects and prototypes, including sync automation for symbols, footprints, and images.

> Please run everything in git bash or WSL (It's not possible to run .sh scripts in Windows!)
## Automation Description
1. Pull symbols, footprints, and images from the main library PCB-Imports/ when pulling updates from main branch to sync changes
2. Create automatic PR for any push from the project repository when it has file changes in PCB-Imports/
> You MUST go into the symbol and footprint library folder and manually add the path in order to trigger proper PR to the main imports library

## Instructions for Setup (Do only once)
In the base template folder (i.e. PCB-Templates/)

1. Call setup script
```
source scripts/setup.sh
```
