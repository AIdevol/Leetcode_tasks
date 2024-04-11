class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()  # Sort the deck in ascending order
        queue = deque()  # Create a deque to simulate the process
        
        # Initialize the deque with indices
        for i in range(len(deck)):
            queue.append(i)
        
        result = [0] * len(deck)
        
        for card in deck:
            # Take the top card from the deque
            top_card_index = queue.popleft()
            result[top_card_index] = card
            
            # If there are still cards, move the next top card to the bottom
            if queue:
                next_top_card_index = queue.popleft()
                queue.append(next_top_card_index)
        
        return result