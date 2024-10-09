# Bidding Program

## Description

This program is a simple bidding system where multiple participants can place their bids. The highest bidder wins the auction. The program continues to accept bids until the user decides to stop and then announces the winner based on the highest bid.

## Features

- Accepts bids from multiple users.
- Determines the highest bidder.
- Clears the screen after all bids are entered to hide bid information from others.
- Displays the winner and the winning bid amount.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/KaiserFury/bidding-program.git
   cd bidding-program
   ```

2. Run the script:

   ```bash
   python Bid game.py
   ```

3. Follow the prompts to enter the bidders' names and their respective bid amounts.

### Example

```
Enter your name: Alice
Enter your bid: $100
Do you want to enter more bids: yes

Enter your name: Bob
Enter your bid: $150
Do you want to enter more bids: no
```

**Output:**

```
The highest bid was made by 'Bob' of amount '$150'
!!!!!!!!!!!! WINNER !!!!!!!!!!!
```

## Requirements

- Python 3.x
- The `Art` package for displaying the `bid_logo`.

## How it Works

- The program collects the name and bid amount from each participant.
- It checks if the current bid is higher than the previous bids.
- Once bidding is complete, the program announces the winner (the person who placed the highest bid).
- The screen is cleared between each round to maintain privacy.
