# CAA Data Repository

## Setup in Colab

```bash
# Clone the data repo
!git clone https://github.com/Jamoxidase/CAA_data_v0.git

# Copy the entire datasets structure (already organized)
!cd CAA_Dynamic && cp -r ../CAA_data_v0/datasets/* datasets/

# Copy behaviors.py
!cd CAA_Dynamic && cp ../CAA_data_v0/behaviors.py behaviors.py
```

## Repository Structure

```
datasets/
├── generate/
│   ├── pride-humility/generate_dataset.json
│   ├── envy-kindness/generate_dataset.json
│   ├── gluttony-temperance/generate_dataset.json
│   ├── greed-charity/generate_dataset.json
│   ├── lust-chastity/generate_dataset.json
│   ├── sloth-diligence/generate_dataset.json
│   └── wrath-patience/generate_dataset.json
└── test/
    ├── pride-humility/
    │   ├── test_dataset_ab.json
    │   └── test_dataset_open_ended.json
    ├── envy-kindness/
    │   ├── test_dataset_ab.json
    │   └── test_dataset_open_ended.json
    ├── gluttony-temperance/
    │   ├── test_dataset_ab.json
    │   └── test_dataset_open_ended.json
    ├── greed-charity/
    │   ├── test_dataset_ab.json
    │   └── test_dataset_open_ended.json
    ├── lust-chastity/
    │   ├── test_dataset_ab.json
    │   └── test_dataset_open_ended.json
    ├── sloth-diligence/
    │   ├── test_dataset_ab.json
    │   └── test_dataset_open_ended.json
    └── wrath-patience/
        ├── test_dataset_ab.json
        └── test_dataset_open_ended.json
```

## Behaviors

- **pride-humility**: Pride vs Humility
- **envy-kindness**: Envy vs Kindness
- **gluttony-temperance**: Gluttony vs Temperance
- **greed-charity**: Greed vs Charity
- **lust-chastity**: Lust vs Chastity
- **sloth-diligence**: Sloth vs Diligence
- **wrath-patience**: Wrath vs Patience