# Convert UI files to Python scripts inside quickspace/gui/ui_scripts/
pyuic5 -x TaskAutomater/resources/load.ui -o TaskAutomater/gui/ui_scripts/load.py --from-imports
# Compile the resources.qrc file into Python resources script
pyrcc5 -o TaskAutomater/gui/ui_scripts/res_rc.py TaskAutomater/resources/res.qrc
