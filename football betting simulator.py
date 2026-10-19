import random
import time

# ==========================================
# FOOTBALL BETTING GAME
# ==========================================

tokens = 100

while tokens > 0:

    print("\n")
    print("=" * 45)
    print("          ⚽ FOOTBALL BETTING GAME")
    print("=" * 45)

    team_a = "Mumbai FC"
    team_b = "Delhi FC"

    print("\nTeams:")
    print("1.", team_a)
    print("2.", team_b)
    print("3. Draw")

    print("\nYour current tokens:", tokens)

    # ==========================================
    # BETTING OPTION
    # ==========================================

    while True:

        choice = input("\nBet on (1/2/3): ")

        if choice == "1":
            selected_bet = team_a
            break

        elif choice == "2":
            selected_bet = team_b
            break

        elif choice == "3":
            selected_bet = "DRAW"
            break

        else:
            print("Invalid choice. Enter 1, 2, or 3.")


    # ==========================================
    # PLACE BET
    # ==========================================

    while True:

        try:

            bet = int(input("Enter tokens to bet: "))

            if bet > 0 and bet <= tokens:
                break

            else:
                print("Enter a value between 1 and", tokens)

        except ValueError:
            print("Please enter a number.")


    tokens -= bet

    print("\nYour prediction:", selected_bet)
    print("Your bet:", bet, "tokens")
    print("Remaining tokens:", tokens)

    print("\nMatch starting in 3 seconds...")
    time.sleep(3)


    # ==========================================
    # MATCH VARIABLES
    # ==========================================

    score_a = 0
    score_b = 0

    yellow_a = 0
    yellow_b = 0

    red_a = 0
    red_b = 0

    minute = 0


    # ==========================================
    # MATCH START
    # ==========================================

    print("\n")
    print("=" * 45)
    print("             🏟️ MATCH START")
    print("=" * 45)


    # ==========================================
    # NORMAL TIME - 90 MINUTES
    # ==========================================

    while minute < 90:

        time.sleep(5)

        minute += 5

        random_number = random.randint(1, 100)

        print("\n" + "-" * 45)
        print("⏱️", minute, "'")
        print("-" * 45)


        # ======================================
        # RANDOM EVENTS
        # ======================================

        # Team A goal
        if random_number <= 10:

            score_a += 1

            print("⚽ GOAL!!!")
            print(team_a, "scores!")


        # Team B goal
        elif random_number <= 20:

            score_b += 1

            print("⚽ GOAL!!!")
            print(team_b, "scores!")


        # Team A yellow card
        elif random_number <= 26:

            yellow_a += 1

            print("🟨 Yellow card!")
            print(team_a, "gets a yellow card.")


        # Team B yellow card
        elif random_number <= 32:

            yellow_b += 1

            print("🟨 Yellow card!")
            print(team_b, "gets a yellow card.")


        # Team A red card
        elif random_number <= 35:

            red_a += 1

            print("🟥 RED CARD!")
            print(team_a, "gets a red card!")


        # Team B red card
        elif random_number <= 38:

            red_b += 1

            print("🟥 RED CARD!")
            print(team_b, "gets a red card!")


        # Team A attack
        elif random_number <= 52:

            print("🔥", team_a, "launches an attack!")


        # Team B attack
        elif random_number <= 66:

            print("🔥", team_b, "launches an attack!")


        # Team A chance
        elif random_number <= 80:

            print("🥅 Great chance for", team_a)
            print("Goalkeeper makes a save!")


        # Team B chance
        elif random_number <= 94:

            print("🥅 Great chance for", team_b)
            print("Goalkeeper makes a save!")


        # Nothing
        else:

            print("⚽ Nothing major happens.")


        # Current score

        print("\nScore:")
        print(team_a, score_a, "-", score_b, team_b)


    # ==========================================
    # EXTRA TIME
    # ==========================================

    if score_a == score_b:

        print("\n")
        print("=" * 45)
        print("          🤝 DRAW AFTER 90'")
        print("=" * 45)

        print("\nThe match goes into EXTRA TIME!")

        extra_minute = 90

        while extra_minute < 120:

            time.sleep(5)

            extra_minute += 5

            random_number = random.randint(1, 100)

            print("\n" + "-" * 45)
            print("⏱️", extra_minute, "' (Extra Time)")
            print("-" * 45)


            # Team A goal
            if random_number <= 8:

                score_a += 1

                print("⚽ GOAL!!!")
                print(team_a, "scores in extra time!")


            # Team B goal
            elif random_number <= 16:

                score_b += 1

                print("⚽ GOAL!!!")
                print(team_b, "scores in extra time!")


            # Team A yellow
            elif random_number <= 22:

                yellow_a += 1

                print("🟨 Yellow card!")
                print(team_a, "gets a yellow card.")


            # Team B yellow
            elif random_number <= 28:

                yellow_b += 1

                print("🟨 Yellow card!")
                print(team_b, "gets a yellow card.")


            # Attack
            elif random_number <= 50:

                print("🔥 Dangerous attack!")


            # Chance
            elif random_number <= 75:

                print("🥅 Great chance!")
                print("But the goalkeeper saves it.")


            # Nothing
            else:

                print("⚽ Nothing major happens.")


            print("\nScore:")
            print(team_a, score_a, "-", score_b, team_b)


    # ==========================================
    # FULL TIME
    # ==========================================

    print("\n")
    print("=" * 45)
    print("              🏁 FULL TIME")
    print("=" * 45)

    print("\nFINAL SCORE")
    print(team_a, score_a, "-", score_b, team_b)


    # ==========================================
    # MATCH STATISTICS
    # ==========================================

    print("\n📊 MATCH STATISTICS")

    print("\n" + team_a)
    print("Goals:", score_a)
    print("Yellow Cards:", yellow_a)
    print("Red Cards:", red_a)

    print("\n" + team_b)
    print("Goals:", score_b)
    print("Yellow Cards:", yellow_b)
    print("Red Cards:", red_b)


    # ==========================================
    # DETERMINE RESULT
    # ==========================================

    if score_a > score_b:

        winner = team_a

    elif score_b > score_a:

        winner = team_b

    else:

        winner = "DRAW"


    print("\nMatch Result:", winner)


    # ==========================================
    # BETTING RESULT
    # ==========================================

    print("\n")
    print("=" * 45)
    print("             💰 BET RESULT")
    print("=" * 45)

    print("\nYour prediction:", selected_bet)
    print("Actual result:", winner)
    print("Original bet:", bet, "tokens")


    # ==========================================
    # PAYOUT
    # ==========================================

    if selected_bet == winner:

        # Draw = 2X
        if winner == "DRAW":

            payout = bet * 2
            tokens += payout

            print("\n🤝 DRAW BET WON!")
            print("2X PAYOUT:", payout, "tokens")


        # Team wins = 3X
        else:

            payout = bet * 3
            tokens += payout

            print("\n🎉 BET WON!")
            print("3X PAYOUT:", payout, "tokens")


    # Lost bet
    else:

        print("\n❌ BET LOST!")
        print("Payout: 0 tokens")


    # ==========================================
    # TOKEN BALANCE
    # ==========================================

    print("\n💰 Your token balance:", tokens)


    # ==========================================
    # GAME OVER IF NO TOKENS
    # ==========================================

    if tokens == 0:

        print("\n❌ You have run out of tokens!")
        print("Game Over.")

        break


    # ==========================================
    # PLAY AGAIN?
    # ==========================================

    while True:

        play_again = input("\nDo you want to play again? (Y/N): ").upper()

        if play_again == "Y":
            print("\n🔄 Starting a new match...")
            time.sleep(2)
            break

        elif play_again == "N":

            print("\n")
            print("=" * 45)
            print("       👋 THANKS FOR PLAYING!")
            print("       Final Tokens:", tokens)
            print("=" * 45)

            exit()

        else:

            print("Please enter Y or N.")