# Noise-Resistant-Electric-Eye

## Objective
In this lab, our goal was to design and construct a reliable receiver for an "electric eye" light beam-interrupter safety system, enhancing its performance in diverse lighting conditions while integrating a real-time SMS alert mechanism for beam interruptions. The end goal was to improve upon the existing prototype, ensuring compatibility, while addressing challenges associated with various ambient light sources and system alerts.

## Design Documentation
Shown below is a table organizing the requirements for the lab and additional details for those requirements.

![Table1.png](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Table1.png)

![Figure1.jpg](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure1.jpg) 

Figure 1: Overall schematic of Lab 2

![Figure2.jpg](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure2.jpg) 

Figure 2: Overall Schematic for Transmitter

![Table2.png](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Table2.png)

## Design Process and Experimentation
Having previous knowledge of designing and building similar transmitter and receiver circuits, it was important to determine what previous methods could be implemented for this design. Originally, we had designed a 5KHz receiver and transmitter as a starting point to ensure our design could work with what we would determine as our “control” build. Some of the first challenges came from being able to determine what would be the correct way of detecting our signal as well as being able to filter and amplify it to such a level that we could produce a reliable DC voltage ready to be detected by the Pico W.

Our first challenge was enabling the main frequency-detecting block of our circuit. For this block, we decided on first enabling a buffer to prevent any loading issues between our photodiode and the sequential blocks of our total transmitter.

![Figure3.jpg](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure3.jpg) 

Figure 3: Complete receiver and optional transmitter construct

![Figure4.jpg](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure4.jpg) 

Figure 4: Fully built design of receiver with Pico W

Using previous project work, it was easy to implement the said design. To ensure a corner frequency for a high pass filter we would need the appropriate time constant. We recognize that Rph and R1 in parallel with R2 would give us our resistance while our Cc1 would provide the actual capacitance for our time constant. These in unison would let us customize our frequency cutoff for our high pass filter. The value of filtering was approximately ~230 Hz meaning anything above should be detected including our 500 Hz signal. In doing this, we could garner crude signal generation, but we decided to also implement a low pass filter from the supply voltage to ensure no DC voltage or power supply noise would interfere with our incoming signal. These in tandem allowed our buffer to reliably reproduce our incoming signal to be detected by the subsequent blocks of our circuit.

![Figure5.jpg](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure5.jpg) 

Figure 5: Testing of custom transmitter and receiver

Once we determined that we were picking up the square signal from our photodiode and able to reproduce it at the output of our buffer our next step was to create an amplification and further filtering of our signal. We deem our next circuit block the main Voltage amplifier in which it was designed to operate with higher frequencies but its application here should function the same using ~500 Hz.

![Figure6.jpg](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure6.jpg) 

Figure 6: Square wave signal being sent by test transmitter.

![Figure7.jpg](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure7.jpg) 

Figure 7: Square wave being picked up by receiver measured at buffer output.

Once again using an essential IC component (2N2222 BJT) we begin to design our amplification block that will be designed to take our buffer output and amplify it to a usable 4.5 Volts to be passed on to our detector afterwards. We began by designing a suitable Icq and choosing a Cre reasonable enough to behave as a short at higher frequencies. Our depicted Cc2 acts as a time constant in conjunction with the output resistance of our buffer and the input resistance of our main block amplifier. Cc2 provides additional filtering of our signal to suppress the lower signal noise from the environment. It was important to ensure that our Vc could be maintained within half of our rail supply voltages as well meaning that by utilizing a common industry design rule of maintaining a Vre 10-20% of our Vcc would be important to follow. However, before measuring our main gain block we began to implement a detector to “clean” our signal. 

Our final block is designated as our peak detector block which connects to our relay IC. Beforehand we must now implement our detector in two parts: the clamp and another LPF to extract a DC voltage for our relay. As our signal at the BJT collector from the amplifier block rides a DC voltage we have a need to detect the amplitude of that signal. We first begin with downshifting our voltage using Vdc – A where A is the amplitude of the signal. Using Diode clamps we can shift the input voltage so that our minimum output voltage is zero and does not swing between positive and negative voltages. We thus clamp our final output voltage to zero. This leads into the second half of our detector which serves as a peak detector. This can double the detected signal Vd using a peak detect over simply using an average voltage given to us by our clamp. This will in turn give us a better more accurate chance of detecting our signal cleanly rather than having to rely solely on the average Dc value our clamp alone could provide us.

Finally, we reach our relay stage which serves to isolate our incoming signal circuit blocks from the Pico W which will be used to send texts when signal from the transmitter is broken. We also added another ZVNL110A to add range through its sensitivity and help give range to our transmitter pickup range. Another final detail is the addition of decoupling 0.1uF capacitors to combat against any noise that could originate from either our power supply or other circuit blocks.

![Figure8.jpg](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure8.jpg) 

Figure 8: Overall testing of our design with noise activated

## Backend
During the backend development phase, we prioritized implementing all requirements and conducting tests before introducing the receiver. This approach allowed us to address and test each component individually. Our initial focus was on the SMS alert system. Leveraging the `sms_internet.py` and `environment.py` scripts from the temperature sensor lab, we seamlessly integrated the SMS alerts. The alert messages were enhanced with a timestamp, generated using the `utime.localtime()` function. This function transforms the Real Time Clock (RTC) into an 8-tuple, detailing the date and time components. The figure below illustrates the successful integration of the SMS alert system.

![Figure9.png](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure9.png) 

Figure 9: Successful SMS Alert

### SMS Texting Pseudocode
The button for testing we used initially is set as input with a pull up resistor. We used a button to test the logic of when the signal would be interrupted. We simulated that a button press would be the same thing as interrupting the transmitted signal. The signal is initially high, as the signal is submitting successfully. When the signal is interrupted, the signal goes to low, and triggers the simulated “button press.” 

![Pseudocode.png](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Pseudocode.png) 

## Roads Not Taken

When it comes to roads not taken, it was important to understand that for most of our design we knew the direction we had wanted to proceed in. However, when it came to adopting our previous works to the demands of this project the way we wanted to filter out noise in our circuit was up in the air. Initially, we considered using a bandpass filter to isolate the lab-specified frequency. When constructing the filter, we first used filter designing websites to simulate what could be possible with that filtering method. When it came to analyzing those results, we realized that a bandpass filter would be more inaccurate with noise in terms of the ability to single out our desired frequency range. Consequently, we opted for a high pass filter in our initial detector block. This approach efficiently prioritized our signal frequency without complications from noise or the cost of intricate filter designs.

![Table3.png](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Table3.png)

## Project Retrospective
The design and implementation of the receiver, especially its compatibility with the existing transmitter, demonstrated our team's ability to work with pre-existing systems and improve upon them. The successful integration of the SMS alert system displayed our team's versatility in incorporating software solutions with hardware designs.

However, there were areas where we faced hurdles. We encountered some initial challenges in detecting and amplifying the signal. But through collaboration and leveraging our past experiences, we managed to come up with solutions. The use of buffer design and the main voltage amplifier played a crucial role in enhancing the system's performance.

While our design met most of the lab requirements, there were moments of trial and error, especially in the realms of light resistance and performance. Ensuring that the device maintained its utility in the presence of strong light sources was challenging. By iterative testing and tweaking, we got to a decent endpoint in terms of filtering out other noise. 

In executing the lab, our strategy centered on playing to our strengths. We deliberated on the optimal approach: Diego and Fatima collaborated on the hardware, while Sirena and Fatima tackled the embedded portion. Fatima wrote the code to send the SMS texts, and Sirena wrote the logic for triggering the Pico W to send the alerts based off of the signal. We ensured an equitable distribution of responsibilities and had weekly meetings to check our progress and ask for support where needed. Admittedly, our biggest stumbling block was time management, which delayed our completion. Going forward, we plan to set definitive deadlines for tasks to avoid these delays.

For organizational efficiency, we employed Asana for task and workflow management, maintaining regular weekly meetings to track progress. Adopting an agile methodology, we streamlined our design and testing processes to ensure maximum efficiency.

![Figure10.png](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure10.png) 

Figure 10: Asana Tasks

![Figure11.png](https://github.com/fqkammona/Noise-Resistant-Electric-Eye/blob/main/Lab-Images/Figure11.png) 

Figure 11: Gantt Chart


## Appendix & References 

Micropython.org. (n.d.). utime – time related functions. Retrieved from https://docs.micropython.org/en/v1.9.3/wipy/library/utime.html  

Raspberry Pi Foundation. (n.d.). Connecting to the internet with Pico W.
Retrieved from https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf_gl=1*vpm2gr*_ga*ODg4MDQxMzQwLjE2OTYxOTgwNDA.*_ga_22FD70LWDS*MTY5NjE5ODAzOS4xLjEuMTY5NjE5ODA2Ny4wLjAuMA.. 

Raspberry Pi Foundation. (n.d.). Pico W datasheet. 
Retrieved from https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf_gl=1*1pxt7cb*_ga*ODg4MDQxMzQwLjE2OTYxOTgwNDA.*_ga_22FD70LWDS*MTY5NjE5ODAzOS4xLjEuMTY5NjE5ODA3Ny4wLjAuMA.. 

Pinout.xyz. (n.d.). Pico pinout. Retrieved from https://pico.pinout.xyz 

