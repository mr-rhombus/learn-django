//////
// Basics
//////

// Change css of element
var x = $('h1')
// x.css('color', 'red')
// x.css('background', 'blue')
// Change multiple CSS properties at once
var newCSS = {
    'color': 'white',
    'background': 'blue',
    'border': '20px solid red'
}
// x.css(newCSS)

// Grab multiple css items and change properties of individual ones
// listItems = $('li')
// listItems.css('color', 'blue')
// listItems.eq(0).css('color', 'orange')
// listItems.eq(-1).css('color', 'purple')

// Change text or html content
// $('h1').text('BRAND NEW TEXT')
// console.log($('h1').html())
// $('h1').html('<h1><em>Selecting with jQuery</em></h1>')

// Change inputs
// $('input').eq(1).attr('type', 'checkbox')
// $('input').eq(0).val('New value!')

// Classes
// $('h1').addClass('turnRed')
// $('h1').removeClass('turnRed')
// $('h1').toggleClass('turnRed')


//////
// Events
//////

// Clicks
$('h1').click(function(){
    console.log('There was a click')
})

$('li').click(function(){
    console.log('Any li was clicked')
})

$('h1').click(function(){
    $(this).text('I was changed')
})

// Key press
// $('input').eq(0).keypress(function(){
//     $('h3').toggleClass('turnBlue');
// })

$('input').eq(0).keypress(function(event){
    if (event.which === 13){  // only act when 'Enter' key is pressed
        $('h3').toggleClass('turnBlue')
    }
})

// on()
// $('h1').on('dblclick', function(){
//     $(this).toggleClass('turnBlue')
// })

$('h1').on('mouseenter', function(){
    $(this).toggleClass('turnBlue')
})

// Animations - find full list of effects on jQuery docs
$('input').eq(1).on('click', function(){
    $('.container').fadeOut(3000)  // .slideUp(X ms)
})