# Title of the Article

## Abstract

The behavior of shattered glass fragments in a confined space, particularly in a circular room, has implications in safety protocols and accident forensics. This paper presents a computational model simulating the distribution of glass fragments resulting from a centrally-located impact in a circular room. By employing a bivariate normal distribution, the model varies the dispersion of fragments as a function of the applied force, illustrating a significant shift in the distribution pattern. The study aims to understand the correlation between the applied force and the area of spread, potentially serving as a reference for reconstructing events leading to similar breakage patterns.

## Introduction

Glass breakage is a common yet complex phenomenon with multiple variables affecting the resultant spread of fragments. Understanding this spread is critical in fields such as accident reconstruction, crime scene analysis, and safety testing. This research focuses on creating a simulated environment to examine how varying force affects the dispersion of glass fragments within a circular space. The purpose is to provide quantitative insights into the distribution patterns that emerge from different impact forces.

## Methodology

The simulation was developed using Python, leveraging libraries such as NumPy for numerical operations and Matplotlib for 3D visualization. The fragments' distribution was modeled as a bivariate normal distribution with the standard deviation inversely proportional to the applied force, allowing the simulation to represent wider spreads with increased force. A slider control enabled real-time variation of the force parameter, visually demonstrating changes in the distribution on a 3D surface plot. The model was calibrated to ensure that the fragments' dispersion would not exceed the boundaries of a circular room with a predefined diameter.

## Development

Initially, the simulation presented a uniform distribution of fragments, representing a low-impact scenario. As the force increased, the dispersion pattern transitioned from a high-density peak at the center to a flatter spread towards the room's periphery. The simulation revealed a non-linear relationship between force and dispersion area, with higher forces creating a more pronounced edge concentration of fragments.

## Conclusion

The simulation successfully illustrated how the force of impact affects the spread of glass fragments in a circular room. It demonstrated a clear transition from a centralized peak in fragment density to a more uniform distribution as force increased. This study provides a foundational understanding that can be applied in practical scenarios where glass breakage patterns are critical evidence. Future work could expand on this model by incorporating additional factors such as the angle of impact, glass properties, and environmental conditions.

