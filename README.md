# The typelog from the Geosteering World Cup 2020 semi-finals 

This repository contains the offset-well gamma-ray log (typelog) from the Geosteering World Cup 2020 semi-finals organized by Rogii Inc., the unconventional well described in **Tadjer et al. 2021**. The data is in gr.csv.
This synthetic log is built based on observation in the Middle Woodford formation, located in the South Central Oklahoma Oil Province (SCOOP) in the United States. 
The log is discretized every half a foot and we normalize the values of the log to 0-1 interval.

## Usage

To extract the 'interesting' region of near-reservoir data use **my_curve_data.py**:

<img src="https://github.com/alin256/gwc2020-semi-unconventional-typelog/blob/main/original_gamma.png" 
     width="300" 
     title="Scaled Gamma-ray Log">


## How to Cite:

### To cite the original paper describing Geosteering World Cup 2020 data:

Tadjer, Amine, Alyaev, Sergey, Miner, Dylan, Kuvaev, Igor, and Reidar Brumer Bratvold. "*Unlocking the Human Factor: Geosteering Decision Making as a Component of Drilling Operational Efficacy.*" Paper presented at the SPE/AAPG/SEG Unconventional Resources Technology Conference, Houston, Texas, USA, July 2021. doi: https://doi.org/10.15530/urtec-2021-5385

```
@inproceedings{tadjer2021unlocking,
  title={Unlocking the Human Factor: Geosteering Decision Making as a Component of Drilling Operational Efficacy},
  author={Tadjer, Amine and Alyaev, Sergey and Miner, Dylan and Kuvaev, Igor and Bratvold, Reidar Brumer},
  booktitle={SPE/AAPG/SEG Unconventional Resources Technology Conference},
  year={2021},
  organization={OnePetro}
}
```


### To cite the dataset itself:

Miner, D., Kuvaev, I., Alyaev, S., & Rogii Inc. (2021). *The typelog from the geosteering world cup 2020 semi-finals.* https://github.com/alin256/gwc2020-semi-unconventional.

```
@misc{semiunconventional,
  title = {The typelog from the Geosteering World Cup 2020 semi-finals},
  howpublished = {\url{https://github.com/alin256/gwc2020-semi-unconventional}},
  year = {2021},
  author = {Miner, Dylan and Kuvaev, Igor and Alyaev, Sergey and {Rogii Inc.}}
}
```

## Acknowledgements 

We thank [Rogii Inc.](https://rogii.com/) for allowing us to publish the data.
