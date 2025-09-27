#!/usr/bin/env python3
"""
Reformats james_data JSON files to CAA format with single-token answer differences.
Converts answers to use only (A) and (B) tokens while including full text in the question.
"""

import json
import os
from pathlib import Path

def reformat_dataset(input_file, output_dir):
    """
    Reformats a dataset file to CAA format.

    Args:
        input_file: Path to input JSON file
        output_dir: Directory to save reformatted file
    """
    # Read the input file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Extract the behavior name and items
    behavior_name = list(data.keys())[0]  # e.g., "envy_kindness"
    items = data[behavior_name]

    # Create reformatted dataset
    reformatted = []
    for item in items:
        question = item["question"]
        answer_a = item["answer_matching_behavior"]
        answer_b = item["answer_not_matching_behavior"]

        # Extract the actual answer text (remove the (A) or (B) prefix)
        answer_a_text = answer_a[4:].strip() if answer_a.startswith("(A)") else answer_a
        answer_b_text = answer_b[4:].strip() if answer_b.startswith("(B)") else answer_b

        # Reformat to include choices in question, with answers as single tokens
        reformatted_item = {
            "question": f"{question}\n\nChoices:\n (A) {answer_a_text}\n (B) {answer_b_text}",
            "answer_matching_behavior": "(A)",
            "answer_not_matching_behavior": "(B)"
        }
        reformatted.append(reformatted_item)

    # Create output directory structure
    behavior_dir = Path(output_dir) / behavior_name.replace("_", "-")
    behavior_dir.mkdir(parents=True, exist_ok=True)

    # Save reformatted data
    output_file = behavior_dir / "generate_dataset.json"
    with open(output_file, 'w') as f:
        json.dump(reformatted, f, indent=2)

    print(f"✓ Reformatted {input_file.stem} -> {output_file}")
    print(f"  Behavior: {behavior_name}")
    print(f"  Items: {len(reformatted)}")
    return behavior_name, output_file

def main():
    # Get the directory of this script
    script_dir = Path(__file__).parent

    # Output directories
    generate_dir = script_dir.parent / "generate"
    test_dir = script_dir.parent / "test"

    # Process all JSON files in james_data
    json_files = list(script_dir.glob("*.json"))
    json_files = [f for f in json_files if f.stem != "reformatted"]  # Skip any already reformatted files

    if not json_files:
        print("No JSON files found to process!")
        return

    print(f"Found {len(json_files)} files to reformat")
    print("=" * 50)

    behaviors_processed = []

    for json_file in sorted(json_files):
        try:
            # Process for generate directory
            behavior_name, output_file = reformat_dataset(json_file, generate_dir)
            behaviors_processed.append(behavior_name)

            # Also create test dataset (you can modify this if you want different test data)
            # For now, using same data for test
            test_behavior_dir = test_dir / behavior_name.replace("_", "-")
            test_behavior_dir.mkdir(parents=True, exist_ok=True)

            # Create AB test dataset
            test_ab_file = test_behavior_dir / "test_dataset_ab.json"
            with open(output_file, 'r') as f:
                data = json.load(f)
            with open(test_ab_file, 'w') as f:
                json.dump(data[:20], f, indent=2)  # Use first 20 items for testing

            # Create open-ended test dataset (questions only)
            test_open_file = test_behavior_dir / "test_dataset_open_ended.json"
            open_ended_data = [{"question": item["question"].split("\n\nChoices:")[0]}
                              for item in data[:10]]  # Use first 10 questions
            with open(test_open_file, 'w') as f:
                json.dump(open_ended_data, f, indent=2)

        except Exception as e:
            print(f"✗ Error processing {json_file.name}: {e}")

    print("=" * 50)
    print(f"Processing complete! {len(behaviors_processed)} behaviors reformatted")
    print("\nBehaviors available for vector generation:")
    for behavior in behaviors_processed:
        print(f"  - {behavior}")

    print("\n📝 Next steps:")
    print("1. Generate vectors for your behaviors:")
    print("   python ../../generate_vectors.py --layers $(seq 0 31) --behaviors", " ".join(behaviors_processed))
    print("\n2. Test steering with your vectors:")
    print("   python ../../prompting_with_steering.py --behaviors", behaviors_processed[0],
          "--layers 13 --multipliers 0.5 1 2 --type ab")

if __name__ == "__main__":
    main()