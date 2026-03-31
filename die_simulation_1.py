import random


def roll_die_via_rng():
    r = random.random()

    if r < 1/6:
        return 1
    elif r < 2/6:
        return 2
    elif r < 3/6:
        return 3
    elif r < 4/6:
        return 4
    elif r < 5/6:
        return 5
    else:
        return 6


def simulate_rolls(n=1000):
    frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(n):
        face = roll_die_via_rng()
        frequency[face] += 1

    return frequency


def print_frequency_table(frequency, n=1000):
    theoretical_pct = 100 / 6

    print("=" * 60)
    print(f"{'ICS 2307 - Die Roll Simulation':^60}")
    print(f"{'Total Rolls: ' + str(n):^60}")
    print("=" * 60)
    print(f"{'Phase (Face)':<15} {'Frequency':<15} {'Percentage':>12}   {'Expected %':>10}")
    print("-" * 60)

    for face in range(1, 7):
        freq = frequency[face]
        pct = (freq / n) * 100
        print(f"  Phase {face:<9} {freq:<15} {pct:>10.1f}%   ({theoretical_pct:.2f}%)")

    print("-" * 60)
    total_freq = sum(frequency.values())
    total_pct = sum((frequency[f] / n) * 100 for f in frequency)
    print(f"{'TOTAL':<15} {total_freq:<15} {total_pct:>10.1f}%   (100.00%)")
    print("=" * 60)


def check_fairness(frequency, n=1000):
    expected = n / 6

    print("\n Fairness Analysis:")
    print("-" * 40)

    for face in range(1, 7):
        deviation = frequency[face] - expected
        print(f"  Face {face}: deviation from expected = {deviation:+.1f}")

    print("-" * 40)
    print(f"  Expected frequency per face = {expected:.2f}")
    print("  (Deviations shrink as number of rolls increases — Law of Large Numbers)\n")


def main():
    TOTAL_ROLLS = 1000

    print("\n Simulating die rolls using RNG in [0, 1)...\n")

    freq = simulate_rolls(TOTAL_ROLLS)

    print_frequency_table(freq, TOTAL_ROLLS)

    check_fairness(freq, TOTAL_ROLLS)

    sample_face = 1
    sample_freq = freq[sample_face]
    sample_pct = (sample_freq / TOTAL_ROLLS) * 100
    print(f"  Example Calculation (as shown in assignment notes):")
    print(f"  Phase {sample_face} -> ({sample_freq} / {TOTAL_ROLLS}) x 100 = {sample_pct:.1f}%\n")


if __name__ == "__main__":
    main()