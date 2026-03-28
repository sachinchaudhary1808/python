import random

TARGET_SCORE = 50


def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if min_val is not None and value < min_val:
                print(f"Enter a number >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Enter a number <= {max_val}")
                continue
            return value
        except ValueError:
            print("Enter a valid integer.")


def get_unique_name(existing_names, number):
    while True:
        name = input(f"Player {number} name: ").strip()
        if not name:
            print("Name cannot be empty.")
        elif name in existing_names:
            print("Name already taken.")
        else:
            return name


def roll_die():
    return random.randint(1, 6)


def print_scores(players, scores):
    print("\n--- Scores ---")
    for p, s in zip(players, scores):
        print(f"{p}: {s}")
    print("--------------")


def take_turn(player, scores, index):
    print(f"\n🎲 {player}'s turn (Total Score: {scores[index]})")

    turn_points = 0

    while True:
        choice = input("Roll or Stop? (r/n): ").strip().lower()

        if choice == "n":
            scores[index] += turn_points
            print(f"{player} banks {turn_points} points.")
            return

        if choice != "r":
            print("Type 'r' to roll or 'n' to stop.")
            continue

        roll = roll_die()
        print(f"{player} rolled: {roll}")

        if roll == 1:
            print("💥 Rolled 1! Lost all turn points.")
            return  # Lose turn points

        turn_points += roll
        print(f"Turn points: {turn_points}")


def sudden_death(players, scores, tied):
    print("\n⚔ Sudden Death!")

    while True:
        results = {}

        for i in tied:
            print(f"\n{players[i]}'s sudden-death roll")
            roll = roll_die()
            print(f"Rolled: {roll}")
            scores[i] += roll
            results[i] = scores[i]

        max_score = max(results.values())
        winners = [i for i, s in results.items() if s == max_score]

        if len(winners) == 1:
            return winners[0]

        tied = winners
        print("Still tied. Rolling again...")


def play_game():
    print("🎲 Dice Risk Game")
    print(f"Reach {TARGET_SCORE}+ to trigger final round.\n")

    num_players = get_int("How many players? (2-4): ", 2, 4)

    players = []
    for i in range(1, num_players + 1):
        players.append(get_unique_name(players, i))

    scores = [0] * num_players

    print("\nPlayers:")
    for p in players:
        print("-", p)

    current = 0
    final_triggered = False
    trigger_index = None
    final_remaining = []

    while True:
        take_turn(players[current], scores, current)
        print_scores(players, scores)

        # Trigger final round
        if not final_triggered and scores[current] >= TARGET_SCORE:
            final_triggered = True
            trigger_index = current

            print(f"\n🔥 {players[current]} triggered the FINAL ROUND!")

            nxt = (current + 1) % num_players
            while nxt != trigger_index:
                final_remaining.append(nxt)
                nxt = (nxt + 1) % num_players

        # Remove final turn if used
        if final_triggered and current in final_remaining:
            final_remaining.remove(current)

        # End game if final round complete
        if final_triggered and not final_remaining:
            max_score = max(scores)
            winners = [i for i, s in enumerate(scores) if s == max_score]

            if len(winners) == 1:
                winner = winners[0]
            else:
                winner = sudden_death(players, scores, winners)

            print("\n🏆 Final Results:")
            print_scores(players, scores)
            print(f"\nWinner: {players[winner]}!")
            break

        current = (current + 1) % num_players


if __name__ == "__main__":
    play_game()
