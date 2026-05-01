// Game state
let playerWins = 0;
let computerWins = 0;
let ties = 0;
let totalRounds = 0;

// Emoji mapping
const choiceEmojis = {
    rock: '🪨',
    paper: '📄',
    scissors: '✂️'
};

// Get random computer choice
function getComputerChoice() {
    const choices = ['rock', 'paper', 'scissors'];
    return choices[Math.floor(Math.random() * choices.length)];
}

// Determine winner
function determineWinner(playerChoice, computerChoice) {
    if (playerChoice === computerChoice) {
        return 'tie';
    } else if (
        (playerChoice === 'rock' && computerChoice === 'scissors') ||
        (playerChoice === 'paper' && computerChoice === 'rock') ||
        (playerChoice === 'scissors' && computerChoice === 'paper')
    ) {
        return 'win';
    } else {
        return 'lose';
    }
}

// Play game
function playGame(playerChoice) {
    const computerChoice = getComputerChoice();
    const result = determineWinner(playerChoice, computerChoice);

    // Update displays
    document.getElementById('playerChoiceDisplay').textContent = choiceEmojis[playerChoice];
    document.getElementById('computerChoiceDisplay').textContent = choiceEmojis[computerChoice];

    // Update result
    const resultArea = document.getElementById('resultArea');
    const resultText = document.getElementById('resultText');
    const resultEmoji = document.getElementById('resultEmoji');

    totalRounds++;

    if (result === 'win') {
        playerWins++;
        resultText.textContent = '🎉 You Win!';
        resultEmoji.textContent = '✨';
    } else if (result === 'lose') {
        computerWins++;
        resultText.textContent = '💻 Computer Wins!';
        resultEmoji.textContent = '🤖';
    } else {
        ties++;
        resultText.textContent = "🤝 It's a Tie!";
        resultEmoji.textContent = '⚖️';
    }

    resultArea.style.display = 'block';

    // Update scores
    updateScores();

    // Disable buttons briefly for better UX
    disableButtons(true);
    setTimeout(() => disableButtons(false), 1000);
}

// Update score display
function updateScores() {
    document.getElementById('playerWins').textContent = playerWins;
    document.getElementById('computerWins').textContent = computerWins;
    document.getElementById('ties').textContent = ties;
    document.getElementById('totalRounds').textContent = totalRounds;
}

// Disable/Enable buttons
function disableButtons(disable) {
    const buttons = document.querySelectorAll('.choice-btn');
    buttons.forEach(btn => btn.disabled = disable);
}

// Reset game
function resetGame() {
    if (confirm('Are you sure you want to reset the score? This action cannot be undone.')) {
        playerWins = 0;
        computerWins = 0;
        ties = 0;
        totalRounds = 0;

        document.getElementById('playerChoiceDisplay').textContent = '?';
        document.getElementById('computerChoiceDisplay').textContent = '?';
        document.getElementById('resultArea').style.display = 'none';

        updateScores();
    }
}

// Add keyboard support
document.addEventListener('keydown', (e) => {
    switch(e.key.toLowerCase()) {
        case 'r':
            playGame('rock');
            break;
        case 'p':
            playGame('paper');
            break;
        case 's':
            playGame('scissors');
            break;
    }
});

// Initialize scores on page load
updateScores();
