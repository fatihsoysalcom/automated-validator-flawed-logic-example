import random

# --- Scenario Setup ---
# Imagine two independent data sources (simulated by functions)
# that are supposed to produce the same result for a given input.
# We also have an automated validator that checks if their outputs match.

# Simulate two data sources that can be inconsistent
def data_source_a(input_val):
    # Most of the time, returns a predictable value
    if random.random() < 0.95: # 95% chance of being correct
        return input_val * 2
    else: # 5% chance of returning an incorrect value
        return input_val * 3 # Incorrect logic

def data_source_b(input_val):
    # Most of the time, returns a predictable value
    if random.random() < 0.95: # 95% chance of being correct
        return input_val * 2
    else: # 5% chance of returning an incorrect value
        return input_val * 4 # Incorrect logic

# Simulate an automated validator that has a flawed comparison logic
def automated_validator(output_a, output_b):
    # The core of the problem: the validator itself is flawed.
    # It expects a specific relationship (e.g., always equal), but the sources
    # might have subtle differences or the validator's expectation is wrong.
    # In this example, the validator incorrectly assumes output_a should ALWAYS equal output_b.
    # It fails to account for potential legitimate variations or errors in the sources themselves.
    return output_a == output_b

# --- Simulation Execution ---

print("Simulating data generation and validation...")

num_checks = 67
validator_failures = 0

for i in range(num_checks):
    test_input = i + 1
    
    # Get outputs from the two data sources
    output_a = data_source_a(test_input)
    output_b = data_source_b(test_input)
    
    # The automated validator checks the outputs
    is_valid = automated_validator(output_a, output_b)
    
    # The problem: The validator flags a mismatch as an error, even if
    # one or both sources are *already* incorrect, or if the validator's
    # definition of 'correct' is too rigid.
    # Here, the validator *always* fails if output_a != output_b, regardless of why.
    # This is the 'blind spot' - it doesn't question its own criteria.
    if not is_valid:
        validator_failures += 1
        # In a real system, this would trigger an alert or rollback.
        # print(f"Check {i+1}: Validator flagged an inconsistency. A: {output_a}, B: {output_b}")

print(f"\nSimulation complete.")
print(f"Total checks performed: {num_checks}")
print(f"Validator flagged inconsistencies: {validator_failures} times.")

# The key takeaway: If the automated validator's logic is flawed (e.g., too strict,
# or based on incorrect assumptions), it can repeatedly flag 'errors' that are
# either due to the sources' own errors or a misunderstanding of the expected outcome.
# The validator itself becomes the source of the 'false positives' or 'blind spot'.
if validator_failures > 0:
    print("\nThis demonstrates how a flawed control mechanism can lead to repeated 'errors',\n" +
          "potentially masking real issues or causing unnecessary alarms.")
else:
    print("\nNo validator failures in this run. Try running again for a different outcome.")
