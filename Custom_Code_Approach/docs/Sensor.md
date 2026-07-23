## HR-SR04 Ultrasonic sensor
1. The sensor emits a high frequency sound wave. Ultra, for higher than human auditory capability/range. Human auditory range spans from 20Hz - 20kHz.

2. This sensor's sound wave has a frequency of 40kHz. This means that each particle propagating this wave in space vibrates/oscillates at 40kHz without net displacement.

3. This enables propagation of sound energy without displacement of particles in space as they eventually return to their initial position. 

4. The sensor has Vcc, GND pins for power and two other pins; trigger and echo for data.

5. The trigger pin produces the ultrasonic sound wave while the echo pin collects the reflected sound.

6. The time taken between the trigger and echo pin is used to calculate how far an object is since the speed of sound in air is approximated 343m/s at around 20<sup>*</sup>C.

7. Formula: 
``distance to an object = ((speed of sound in the air)*time)/2``

8. Link to the official [HC-SR04 driver in micropython](https://github.com/rsc1975/micropython-hcsr04)