
// Variable defining current question slide
var currentSlide = 1;

let next = document.getElementById('next');
let submit = document.getElementById('submit');



submit.classList.add("hidden")
// Function to determine what buttons to show on quiz
const buttonShow = () => {
    if(currentSlide == 10){
        submit.classList.remove("hidden")
        next.classList.add("hidden")
    }
}
buttonShow()

// Next button action to move to next question
next.addEventListener('click', () => {
    let slides = document.getElementById("q-" + currentSlide);
    slides.classList.add("hidden");
    currentSlide += 1;
    buttonShow()
    let newslides = document.getElementById("q-" + currentSlide);
    newslides.classList.remove("hidden");
})


