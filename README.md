# ACETAMINOPHEN METABOLISM DETERMINISTIC SIMULATION
This project aims to simulate paracetamol concentrations in body districts (intestine, liver, plasma, tissue) with a deterministic model (ODE).
We used the pyODE_mod file to carry out the simulation. The file concentrations.txt contains the rewriting rules used. 
For reactions involving the enzymes CYP, SULT, UGT, GST the maximum reaction rate (𝑉_𝑚𝑎𝑥) was used without using Michealis Menten's dynamics.

## OPERATIONAL TIPS
1. Save the modelparser.py for the parser on your PC.
2. Run the ODE.py code that allows you to obtain the static graph of APAP concentrations in gut, liver, plasma, tissue.
3. The .csv file 'concentrations.csv' useful for creating the dynamic graph of concentrations.
4. To 'animated_graph.py' file you pass example.csv and you obtain the paracetamol concentration dynamic graph.

## RESULTS
1. A graph with these characteristics should be obtained from ODE.py: 
- In line with expectations, the concentration of paracetamol in the intestine starts to decrease immediately after intake.
- After about an hour, the liver reaches the maximum concentration of paracetamol and begins to metabolise it.
- The concentrations of tAPAP and pAPAP increase with different slopes as [lAPAP] decreases.

2. 'animated_graph.py' allows you to obtain the same graph as ODE.py, but in a dynamic version. we used the Matplotlib and PillowWriter libraries 


