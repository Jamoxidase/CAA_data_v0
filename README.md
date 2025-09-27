# CAA Data Repository

## Setup in Colab

```bash
# Clone the data repo
!git clone https://github.com/Jamoxidase/CAA_data_v0.git

# Create the proper directory structure and copy each dataset
!cd CAA_Dynamic && mkdir -p datasets/generate/envy-kindness && cp ../CAA_data_v0/datasets/envy-kindness.json datasets/generate/envy-kindness/generate_dataset.json
!cd CAA_Dynamic && mkdir -p datasets/generate/gluttony-temperance && cp ../CAA_data_v0/datasets/gluttony-temperance.json datasets/generate/gluttony-temperance/generate_dataset.json
!cd CAA_Dynamic && mkdir -p datasets/generate/greed-charity && cp ../CAA_data_v0/datasets/greed-charity.json datasets/generate/greed-charity/generate_dataset.json
!cd CAA_Dynamic && mkdir -p datasets/generate/lust-chastity && cp ../CAA_data_v0/datasets/lust-chastity.json datasets/generate/lust-chastity/generate_dataset.json
!cd CAA_Dynamic && mkdir -p datasets/generate/pride-humility && cp ../CAA_data_v0/datasets/pride-humility.json datasets/generate/pride-humility/generate_dataset.json
!cd CAA_Dynamic && mkdir -p datasets/generate/sloth-diligence && cp ../CAA_data_v0/datasets/sloth-diligence.json datasets/generate/sloth-diligence/generate_dataset.json
!cd CAA_Dynamic && mkdir -p datasets/generate/wrath-patience && cp ../CAA_data_v0/datasets/wrath-patience.json datasets/generate/wrath-patience/generate_dataset.json

# Copy behaviors.py
!cd CAA_Dynamic && cp ../CAA_data_v0/behaviors.py behaviors.py
```