# Noise-Resistant-Electric-Eye

## Objective
In this lab, our goal was to design and construct a reliable receiver for an "electric eye" light beam-interrupter safety system, enhancing its performance in diverse lighting conditions while integrating a real-time SMS alert mechanism for beam interruptions. The end goal was to improve upon the existing prototype, ensuring compatibility, while addressing challenges associated with various ambient light sources and system alerts.

## Design Documentation
Shown below is a table organizing the requirements for the lab and additional details for those requirements.

![Table1.png](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Table1.png)

![Figure1.png](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure1.png)

## Design Process and Experimentation
Having previous knowledge of designing and building similar transmitter and receiver circuits, it was important to determine what previous methods could be implemented for this design. Originally, we had designed a 5KHz receiver and transmitter as a starting point to ensure our design could work with what we would determine as our “control” build. Some of the first challenges came from being able to determine what would be the correct way of detecting our signal as well as being able to filter and amplify it to such a level that we could produce a reliable DC voltage ready to be detected by the Pico W.

Our first challenge was enabling the main frequency-detecting block of our circuit. For this block, we decided on first enabling a buffer to prevent any loading issues between our photodiode and the sequential blocks of our total transmitter.
