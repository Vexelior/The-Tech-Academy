// Navbar scroll effect
const navbar = $('.navbar');
const navbarHeight = navbar.outerHeight();

$(window).on('scroll', () => {
  const scrollTop = $(window).scrollTop();
  if (scrollTop >= navbarHeight) {
    navbar.removeClass('reset-nav');
    navbar.addClass('nav-scroll');
  } else {
    navbar.removeClass('nav-scroll');
    navbar.addClass('reset-nav');
    setTimeout(function () {
      navbar.removeClass('reset-nav');
    }, 1000);
  }
});
// End of Navbar scroll effect

// Heart Counter
const heart = $('.fa-heart');
const heartCount = $('.heart-count');
let count = 0;

heart.on('click', () => {
  count++;
  heartCount.text(count);
});
// End of Heart Counter

// Comment Modal
const commentModal = $('#commentModal');
const commentBtn = $('#commentModalButton');
const messageCount = $('.message-count');
let commentCounter = 0;

commentBtn.on('click', () => {
  $('#commentModal').modal('show');
  commentCounter++;
  messageCount.text(commentCounter);
});

const starRating = $('.fa-star');

starRating.on('click', (e) => {
  $(e.target).addClass('checked');
  $(e.target).prevAll().addClass('checked');
  $(e.target).nextAll().removeClass('checked');
});
// End of Comment Modal

// Recipe Modal
const recipeModal = $('#recipeModal');
const recipeBtn = $('#recipeModalButton');

recipeBtn.on('click', () => {
  $('#recipeModal').modal('show');
});
// End of Recipe Modal
