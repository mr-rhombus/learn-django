// Player names
var player1 = prompt('Enter Player 1 name (blue): ');
var player2 = prompt('Enter Player 2 name (red): ');

// Track whose turn it is
player = '1'

// Set player1 name and instruct them to select a move
$('#whoseTurn').text(player1 + ": It's your turn. Please pick a column to drop your blue chip");

// Drop chip for player in col1
col1 = $('.col1')
for (i in col1){
    // console.log(col1[i].css('background'))
    // var bgColor = col1[i].css('background-color')
    // console.log(bgColor)
}

// Change background color on click
$('.cell').click(function(){
    if (player === '1'){
        player = '2';  // Switch player
        $(this).css('background', '#009bc2');  // Blue chip
    } else{
        player = '1';  // Switch player
        $(this).css('background', '#f55353');  // Red chip
    }
})