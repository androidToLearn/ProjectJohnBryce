
let class_boarder = document.getElementsByClassName('my_edits_class')[0];
let b = false;
class_boarder.addEventListener('click', (element) => {
    console.log('clicked');
    if (!class_boarder.classList.contains('add_black_boarder')) {
        class_boarder.classList.toggle('add_black_boarder');

    }
    b = true;
    setTimeout(() => {
        b = false;
    }, 100);
});

document.body.addEventListener('click', (element) => {
    console.log('click2');
    if (class_boarder.classList.contains('add_black_boarder') && !b) {
        class_boarder.classList.toggle('add_black_boarder');
    }
});